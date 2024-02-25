Technical interview question:
if you have two esxi hosts, one connected to the default TCP/IP stack and the other is connected to a custom TCP/IP Stack, if vMotion attempts to migrate a VM between them, it'll fail.
you'll need to have both of them at a similar Stack for it to work.

### Storage vMotion:
This is a vMotion feature that allows you to move the VMDK files from one Data Store to another.
This can be done by having the esxi host read from the original data store and write what it reads to the new data store through the storage network. This means that the host should have access to both datastores it wants to read from and write to.
#### Storage load balancing:
the two main reasons to load balance storage are:
- capacity: the storage in the current box is running out and a migration is needed to allow operations to continue
- I/O: is starting to slow down in this box, so a migration is needed to maintain acceptable I/O
#### SCSI Controller: 
is a virtual component added to a VM, to allow it to write/read data it believes to be in local storage(in reality it's writing to a VMDK).
this traffic sent through the SCSI controller is intercepted by the esxi host which then specifies where to forward it in order to write to it's specified VMDK file.
The VM assumes that it's writing on its own local disk through the `SCSI Controller`, unaware of the fact that the hypervisor is actually writing to the data store through its own HBA(which can be physical) whatever the protocol is(FC, FCoE, iSCSI, NFS).

#### Compute + storage vMotion:
This allows us to both transfer the VM Compute and it's storage at the same time.
There is also the option to transfer these to a non-shared storage (the current host doesn't have access to the target storage).
This transfer occurs through the network, the esxi host sends the VM, its memory and the VMDK file through the network itself, not through iSCSI or SAN.
This of course means that the vMotion recommended network bandwidth is 10GB/s.
This is the least used migration option, there are special cases and requirements that use it.
### Availability / Durability during backup:
During a shutdown of a VM we can preserve the VMs because their data exists in two different hosts this makes it `durable` since it's available in multiple places, however. the VM will not be available during shutdown, making it `unavailable`.
### Content Library:
We have 10 different vCenters, each controlling a Data Center of its own, through `Templates` we can have all those vCenters to create a VM having the same configurations.
This can be easily achieved through creating a `content library` on which we add a collection of Templates and Files for reuse and sharing, by **Publishing** the content library across all the connected vCenters.
now all these vCenters can subscribe to the content library to access anything published in the content library including the Templates.

### Resource Allocation:
| device | Applies to                  |
| ------ | --------------------------- |
| CPU    | Reservation, shares, limits |
| Memory | Reservation, shares, limits |

##### Configured Memory
The memory allocated to a VM is called `Configured Memory`, this memory is the only memory the VM can see or have access to.
#### Reservation:
this can apply to both CPU Cores and Memory, this means that a VM is given a specific amount of resources that do not exceed the host capacity(no more cpu cores or ram than the host has).
##### Reserved but unused:
reserved resources must exist on the physical host, even if the VM isn't using 100% of the reserved resources, it will be allocated.
##### used but unreserved :
the resources are allocated to the VM but it's not at 100% use, this means that it only has the resources that it's currently using.
#### Reservation on CPU:
since CPUs are a processing unit which cannot be interrupted, having a CPU reserve doesn't actually stop anyone from using the resources, it will just mean that the CPU will just point towards the recently arriving instructions instead of the previous once, resuming them once the reserved CPU instructions are done.
##### Memory Swap Cost:
Since memory reads / writes data, which will need to be moved from memory to a disk, we have to put the data transfer time between memory and swap.
This issue is not fully solvable, you have to either sacrifice memory which will waste resources or sacrifice speed by not reserving memory which will cause swap once it's full.
#### swapping in case of exceeding the hosts max memory
We have two critical vms called VM1 & VM2, we do not want it to share it's memory with any other VMs, these 2 VMs have 8 gigs of ram each, 4G of which are reserved.
the host will allocated 4 gigs during it's runtime and increase its allocated memory if it needs more than those 4 gigs.
however, lets assume the host has 12 gigs of ram, meaning only 4 gigs will be reserved on each VM taking 8 gigs of ram, leaving 4 left of the 12 gigs.
in the case of the VMs reaching their maximum ram usage of 8 + 8 gigs, requiring 4 more gigs than the host, this will cause the memory to use swap instead.
there are several methods for that, by default it'll split the swap on each VM to not impact performance negatively, so 2 gigs of swap in each VM.
in memory shares, there is a method to specify which VM gets swapped and which remains in memory.
### Shares:
we assign a share number for the VM, which is only invoked when there is a contention on the resources, which will then check the VM priority (share in resources) then specify which of the VM keeps its resources and which VM will have to use swap space.
**This doesn't affect the reserved resources.**
##### Relative Priority in shares (RAM):
we have two VMs with 8 gigs (4 reserved and 4 shared) of ram , on a 14 gigs of Ram host.
VM1 has a share of 2, while VM2 has a share of 1.
in the case that both VMs reach max memory of 16 gigs of RAM, the host will prioritize the VM with the highest relative priority (VM1 with a share of 2) meaning it will not be forced to swap, it'll be given 8 gigs of the host RAM.
the other vm will then have to swap to disk, so VM2 will have 4 gigs of reserved ram (because the reserve is unaffected by shares) 2 more gigs of available memory and the other 2 gigs will then be swapped to disk until VM1 no longer needs 8 gigs.
##### Relative Priority in shares (CPU):
Given 2 vms each with reserved processing time equal to 500MHz and total allocated processing equal to 1.5GHz each on a host with a 2GHz CPU.
the share priority will decide which CPU gets more time to process its data.tarek youns is perfect.

### limits:
we set the maximum usable physical resources for a VM.
this limit should not be exceeded by the VM.
this limit is unrelated to the allocated memory for the VM, this is simply the maximum possible resources it can use.

## Resource Pools:
we consolidate resources into an object with specific configurations(example: reservations, shares, limits). This allows us to control the total resources from which we can create VM.
This object can then have VMs created from it following the specified resource allocations rules without manual intervention.
note:
- resource pools can be placed inside resource pools (not recommended)
example:
creating a VM(resource consumer) and allocating its resources from the esxi host(resource provider).
This is a parent(esxi host) / child(VM) relationship, this relationship becomes difficult to scale and maintain on clusters(large infrastructure), so we create resource pools to start VMs with automatic configuration of its resources within that specific pool.
#### Resource Pool Memory reservation:
the resource pool has a right to take an allocated amount of memory from the cluster for itself (the resource pool reserves memory from the host / cluster for to share with its vms), to use whenever a VM within the pool asks for it, this means it'll allocate this memory once it asks for it, otherwise the pool will allow the host / cluster to use the memory until it's allocated within the pool.
once it's no longer allocated / used it may return to the cluster.
#### Example:
2 vms within a resource pool each with a reserved RAM of 4 gigs, these resources will belong to the host to whatever it wants with it until these VMs start, once the VMs start, their resources are allocated within a pool, which will then return these resources from the host / cluster into the pool for use.
means that the pool should at minimum should have a reserved 8 gigs of ram, reserved to it before allocation, to even allow the vms to reserve within these resources from the pool.
However the pool will only receive this memory from the host / cluster during allocation ( when the vms start / require it).

### Cluster Sevices:
These services are enabled by default once you setup a cluster.
#### HA (High Availability): explain
It is a service that automatically restarts VMs on another host, once they crash and fail.
#### FDM Agent:
it's the software installed on a host, responsible for receiving command to start a VM on the host once it fails on another.
##### FDM Agent Election:
all connected hosts in a cluster will have to **elect** an **FDM Master** to coordinate between them.
the rest of the FDM Agents will become slaves, and they will have to send a `heart beat`(network or data store heartbeat) to the FDM Master, to assure it that it is still operational and haven't crashed yet.
##### Data store heartbeat:
the FDM master and all his slaves share a datastore, this store is continuously written to by all the slaves, the master will check the datastore for the last slave write(their heartbeat).
##### FDM Agent Slave shutdown / Heartbeat failure:
once an FDM Slave shuts down or stops sending heartbeats to the FDM Master, the master is now responsible for restarting all the VMs on the failed slave, on other esxi hosts in the cluster including itself.
##### Isolation Response:
what happens when you can no longer reach the FDM Slave through the network but the VMs are still writing , we configure  the VMs to either continue as they are or shutdown and restart them onto another esxi host.
requirements of HA:
- shared storage between esxi hosts 
#### DRS(Distributed Resource Scheduler):
This is a load balancer that automatically that monitors both the CPU and memory utilization between all the cluster members, if they exceed a certain percentage, it will migrate some VMs from the host with the excessive utilization to another host.
DRS options:
- fully automated:
	Initial placement: once the VM is powered on, the DRS will automatically find the most suitable host for this newly run VM.
	Loadbalancing: if there is an over load on the host resources it will automatically migrate it to another host to reduce the load
- partially automated:
	initial placement: it will automatically place the VM on a suitable host once it starts (just like fully automated)
	Loadbalancing: it will suggest a more suitable host to migrate to, but will wait for the admin approval to migrate.
- manual:
	initial placement: you decide where to put the VM
	Loadbalancing: you decide where to move the VM if there is an overload on the system.
##### INterview question
if vCenter crashes what remains operational and what fails?
operational:
- data plane
- HA
- standard vSwitches
fail:
- control plane
- DRS
- Distributed switch will stop updating

#### EVC(Enhanced vMotion Compatibility):
This is a service that enables cluster wise CPU baseline family, allowing a specific set of CPU features common between all the esxi host CPUs to avoid any migration failures. 
This also means that a host may some times have to mask(hide) some features from any VM residing on it, to keep it compatible with other host CPU's missing these features.
#### VM-Level EVC:
this is a feature that allows us to specify which specific features are given to a VM, different from the normal baseline.
#### Migration failures:
First of all, vMotion won't even initiate if CPU manufacturers are different, for example host is AMD and target is Intel.
vMotions migration transfers the VMs compute from one esxi host to another, we must keep in consideration the fact that the original host, has its own CPU either Intel or AMD and each has their own family, for example intel's sky lake / westmere family.
each CPU family has `unique features` that may not be available in other families.
these features are given to the vCPUs during virtualization, since the physical CPU is the one executing the instructions given by the VM.
these `special features` may not be available to the target esxi host, this may cause <span style="color:red">migration failure</span>.
These features are detected on powering on the VM, and are considered during migration to ensure compatible physical CPU's in the target host.

