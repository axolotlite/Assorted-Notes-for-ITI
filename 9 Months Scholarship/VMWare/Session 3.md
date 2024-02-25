t#### MTU(maximum transfer unit):
The largest TCP/IP packet size allowed to be transferred through the network, this limitation is applied on layer 2 in the network.

We're allowed to create a VMK without configuring any server on it.

vmNICs are not given ip addresses.

##### Standard Switch
managing it requires us to:
1) select esxi host from vCenter
2) configure 
3) configure networking
4) add networking
	1) vm kernel adaptor
	2) virtual switch / port group
	3) physical adaptor

Adding a new physical adapter:
1) select esxi host from vCenter
2) configure 
3) configure networking
4) Select Standard Switch
5) Manage physical adapter
6) unclaimed -> (active/standby/unused)

#### Distributed Switch:
Managed:
1) Select Networking tab from vCenter
2) Select Data Center
3) configure new / existing Distributed Switches
4) Select Distributed Switch
5) Add / Manage hosts
###### Interview questions:
- What is a snapshot?
- what are the types of a snapshot?
- Which is better, a snapshot or a clone?
- What are the drawbacks of a snapshot?
### VM Snapshots:
it's a way to save the VM's state at a certain point, allowing us to return to that specific point whenever we want.
The snapshot is concerned with the disk state, once a snapshot it taken a new file called `delta` is created, the VM will then begin writing on this delta file instead of the VMDK file.
This means that the delta file, has the any changes from the VMDK written to it and the base VMDK file is now read-only.
#### How snapshots work:
##### write request:
it follows the concept of `copy-on-write`, the VMDK file is turned read-only and an empty delta file is created, any new write at the block-level are redirected (copied) towards the delta, any writes meant for the VMDK is written on the delta instead, the location of the newly written delta data is then mapped to where it was supposed to be on the read-only VMDK file.
##### read request:
if a file is being read, the hypervisor checks if the file has been modified, if it's been modified, it checks where it's mapped in the delta and reads from there.
otherwise, if it has not been modified, it'll just read from the read-only VMDK file.

##### Multiple snapshots / deltas:
creating a new snapshot will create a new delta that will receive all upcoming writes, this will turn any previous delta into read-only, and any new writes will be compared with each previous delta to map the new block to the changes blocks in all the previous deltas.
##### rewriting on the same block:
this will cause the block to be rewritten on the delta file.
##### Deleting a snapshot:
This causes the delta file to be merged / committed into the VMDK file and or previous delta file, this returns it to a read/write state. allowing the hypervisor to continue writing on it.
This happens by overwriting the changes from the delta to either the previous deltas if they exist or to the VMDK file directly if no deltas exist.
##### Delete all snapshots:
Like normal delete, it merges all existing deltas into the VMDK file, allowing the last modified blocks to overwrite all previous versions.
##### Revert:
returns to the save state, this deletes the delta file, and returns the VMDK file into a read/write state, allowing us to continue working on it as normal, as if was at the same state before the snapshot.
##### performance impact:
performance degrades due to the need to check the block-file changes every time you start writing, this only increases as you increase snapshots, this is because you'll have to check the new write across each and every snapshot block.
##### Snapshot size:
###### Thick Provisioning:
first we assume the base VMDK is a 50GB thick provision, the created snapshot delta will first be created at a size of 0.
The VM, when writing, will assume it's writing on the same drive, which has 50GB while in reality it will be writing on the delta, increasing the size of the delta until it reaches the maximum size of 50GB.
This means a 50GB thick provisioned disk, will require storage in the range of 50 -> 100GB, this range will increase by previous delta size (in range of 0 to 50 GBs) + possible 50 GB of the newest delta.
Deleting it, will of course produce a merged VMDK file of size 50 GBs.
###### Thin provisioning:
we assume the base VMDK is a 50GB thin provision, there is 20/50 GBs written on the VMDK, we create a new snapshot delta, and write 20 more GBs on deleting this delta the merge will over write any existing blocks in the VMDK file, however any blocks not written to( these blocks are not occupying any space) will be written to, meaning the merge will produce a VMDK in range of 20GB (original VMDK) -> 40 GB (original + write over the unwritten blocks)
#### Memory Snapshot:
we have a VM with several running applications (browser, openssh, servers), normally if we revert this VM to a previous snapshot, the VM will return in a shutdown state, terminating all the running applications.
however, a memory snapshot will take a copy of the running memory during the backup, so when you revert into it, the running applications are restarted in the same state they were.

## VMotion:
This is a software solution that allows transfer of VMs between esxi hosts.
there are two types of migration:
Cold Migration: occurs while the VM is shutdown
Hot Migration: occurs while the VM is operational
once the migration is done, the target esxi sends a `Gracious ARP` which notifies all the hosts on the network that this VM (it broadcasts the MAC Address) now resides on a new host.
##### Requirements of vMotion:
The network on which vmotion operates has specifications, one of which is having a faster transfer rate than the file modification rate in a VM.
- both hosts on the same network (to allow transfer of VM memory) the transfer occurs through the esxi hosts VMK.
- enough memory in the target host to allow the launch of a VM after its transferred
- having a share datastore to allow the VMDK file to either migrate or be read by the target host
vMotion allows us to move VMs between esxi hosts.
##### TCP/IP Stacks:
This is the protocol implementation of the network layers, a part of this stack is the routing table, any OS has a routing table.
any running service on your device will have to find its destination through the routing table.
vSphere gives us the option to use any of several TCP/IP stacks inside the virtual network, there is the default TCP/IP stack that it uses, which is the same as any physical traffic.
we can create another stack that operates separately and serves a specific service, this basically creates a new separate routing table inside the vSphere for a specific set of applications. this of course will require the configuration of VMK to connect the esxi hosts.
#### scenario:
The default gateway is `192.168.1.1` which allows communication between subnets, all traffic is routed through it before finding its destination.
we create the management VMK_1 with ip `192.168.1.2/24`.
another VMK_2 with ip `10.1.1.2/24` which doesn't have the same default gateway.
By using the default TCP/IP Stack for communication: if VMK_2 tries to communicate with VMK_1 it will face the issue of both having different default gateway because we cannot have more than one default gateway.

Through VMotion we can create another TCP/IP stack which creates a new routing table, this routing table will have a default gateway that allows connection to the other subnet, which can then route the traffic through it.
Now, we have two different gateways which allows both subnets to connect and communicate.
#### Planned outage / maintenance:
i slept through it