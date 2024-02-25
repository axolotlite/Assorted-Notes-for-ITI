what's the point of virtualization?
optimizing the usage of resources while reducing deployment time and cost.

what's the main difference between hyper v and vmware storage?
vmware uses .VMDK extension for storage, and .delta for snapshots 
while Hyper V uses .vhdx(virtual hard drive) extension, and .avndx for snapshots
thin provisioning vs thick
vmware thin provisioning of 1 TB uses 0 bits of actual storage once created
hyper V thin provisioning of 1 TB is called dynamic and uses by default 4MBs of real storage once created
vmware thick provisioning of 1TB will actually use 1 TB on creation.
hyper V thick provisioning is called Fixed provisioning and uses 1TB on creation.

what's the difference between vmware and hyper v in snapshots?
vmware calls it snapshot and hyper v calls it checkpoint.

| POC | VMWare Snapshots | Hyper-V Checkpoint |
| ---- | ---- | ---- |
| max num | 32 | 50 |
| automatic snapshoting/checkpointing | not available | can be automated |
| memory + storage | default snapshot | standard checkpoint |
| storage only | ??? | production checkpoint |
production snapshots are the norm.

what's the difference between hyper v and vmware switches?
there are three types of switches in hyper V:
- private
	we can connect one and more VMs, allowing only them to communicate through this private network, no one else can access them through it.
- internal:
	Connects the VMs together, while allowing communication between them and the host.
- external
	Everything is connected in the network; VMs, host, physical switches and the internet.

#### NUMA(Non-unified memory access):
google it or go see the vmware pdfs, it should be there somewhere.

### Replication:
this is a feature in hyper-v that allows us to duplicate any updates or modifications of a running VM onto another one, working as a replica / duplicate of the VM, until the original VM fails causing the duplicate to take the originals place.
its microsoft attempt at fault tolerance.

### Migration:
we have two hosts, and we want to transfer a VM from one to another.
we can do:
- live which is basically vmwares hot migration
- dead migration which is cold
### High Availability:
we install a High Availability agent on the hosts to monitor it and notify when to transfer VMs.

### DRS & EVC:
there is no equivalent in hyper v.

### Nested Virtualization
we can install several hypervisors on top of each other, virtually an infinite amount of nested hypervisors as long as the resources allow for it.
for example, installing esxi as a host OS on a baremetal server, then install another esxi as a guest VM on the host, on top of which another esxi guest is installed on the guest.
each new guest will have performance degradation but it is possible, as long as we have enough resources.


Scenario:
given two hosts, each one having 16 gigs of RAM, 
host A has 15VMs, it's resources are almost depleted.
Host B has 8 VMs, it has a lot of spare resources,
now given that High Availability is active on the cluster, if host A crashes which will start a migration of all of the 15VMs to Host B, if protection or usage limits are set, the VMs will migrate til the limit is reached, protecting host B from crashing like host A.

