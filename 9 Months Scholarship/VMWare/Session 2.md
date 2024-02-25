## VSphere Networking:
#### Important topics (will come in interviews):
- vNic
- Port groups
- vSwitches (standard vs distributed)
- UPLinks (VMnic connections)
- VMKernel interfaces
##### less important topics: (neglected in interviews, except teaming and failover)
- teaming and failover
- traffic shaping
- routing policies and rules

### vNIC:
virtual Network interface card, does whatever a real interface network card but through the virtual network created in vmware.
we mirror the physical environments network in the vmware virtual network, to do this we'll need other virtual components such as virtaul switches, since we can't connect the vNIC to physical switches.
these vSwitches will do the same function of real ones inside the vmware network, in the esxi host.
### vSwitch:
VMWare implemented **layer 2 switching** inside the esxi host, through virtualization, this means we can have virtually unlimited virtual ports.
we can connect VMs on a host, through this vSwitch to allow it's traffic to be routed through the network.
this is the first step towards virtualizing the data center, virtual hosts connected to virtual networks through virtual switches.

now, if we get anther virtual machine and connect it to the host's vSwitch, they'll be able to directly communicate.
##### Quick Notes:
- We can create multiple vSwitches in an esxi host.
- There is a default vSwitch `vSwitch 0` created alongside the esxi host.
- a Single vSwitch can have multiple vmNIC (Physical NICs for uplink ports) but vmNICs can't pair with more than one vSwitch.
- each vmNIC is connected to a unique uplink port.
- Port Groups are allowed to use any vmNIC as long as it belongs to the vSwitch
### Port Groups:
now, in physical switches we can create VLans to isolate members inside it from other VLans, this feature is also implemented in vSwitches and it's called Port Groups.
`NoVLAN` is the default port group created with the vSwitch, it acts as the default `VLan 1`
they allow us to select parts of the vSwitch network to assign it a VLan id, emulating the physical ports and physical VLan.
we enter the switch and assign `acess vlan 10(id)`
first, we tell the vSwitch the virtual ports we want to create a port group for with its assigned VLan, next we assign the vNIC to the desired port group.
this means that the VM is now part of the desired VLan.
There is no option in vsphere to allow routing within an esxi, meaning if we have two vms connected to different port groups within a vSwitch, they won't be able to connect to each other without NSX.
##### hair pinning (distributed routing):
routing the traffic through a single point in the network, where traffic is forced to pass through it before returning to its destination within an esxi host.
NSX distributes the same router across all the esxi hosts, this allows distributed routing to avoid hair pinning, since each router has it's own `routing point` that allows traffic to be routed inside it while being capable of sending external traffic.
### Uplink Port:
a special virtual port in a vSwitch whose purpose is to connect two vSwitches through a phsyical NIC.
it transfers the virtual packets from the VMs through the phsycal NIC to the network, then another vSwitch.
#### Connecting VLans in different vSwitches:
given two esxi hosts, with two similar VLans within two different vSwitches.
first we'll need to physically connect both hosts through a network, in this case the physical network card will be called vmNIC, which will be connected to a physical switch.
next we use the Uplink Port to connect both switches through the vmNIC and physical infrastructure (routers & switches between them) of the two esxi hosts.
We'll have to specify the `trunking` configuration of the uplink port, for transmission through the distribution layer of the physical network.

#### ARP in vSwitches:
an arp request is sent from an esxi through the port group, this arp request will flood the vswitch, which will be sent to all the connected devices / ports, even the uplink port, which will pass through the vmNIC and even continue through the physical switch, through the trunking configs until it reaches the other vSwitch situated inside the other esxi host.
this vSwitch will continue broadcasting the ARP request to all the connected devices and the requested host will reply if found within the network.
this virtual host will send an ARP reply to the requesting host, now this VM has the mac and ip addresses of that host.
##### The difference between host mac discovery in vSwitches and physical Switches:
physical switches discover host mac addresses through traffic passing through them.
vSwitches already know all the macs belonging to their esxi host, so any internal traffic within an esxi host will be directly routed within it, no discovery occurs and any unknown mac addresses are automatically routed through the uplink port.

##### Data Transfer through virtual Network:
Normally the NIC is responsible for packet encapuslation, but in a virtualized environment, the VM is responsible for for creating the target data in these layers 2,3,4 and 7. then the uplink port and vSwitch tag layer 2 with the relevant VLan info.
now on the other vSwitch, the target vSwitch receives the data through it's uplink port, removing the tag and sending the data to the desired port group containing the mac address which the vSwitch uses to send the data frame to the target VM.
the VM then checks the ip, port and sends the data to the desired application.

### VMKernel interfaces:
after pairing the vmNIC (a physical NIC) to a vSwitch, we'll need to find another way to connect the esxi host to the network, this will happen through a special virtual interface.
The `VMKernel virtual interface` allows the esxi host to connect to an internal vSwitch to route the esxi host traffic through it.
we can add several VMK virtual interfaces to an esxi, to categorize and isolate traffic through each of them.
for example, a specific VMK for ISCi traffic, another for management and any VMK for any specific traffic.

### Standard vs Distributed Switch:
##### Standard Switch
the default created switch in an esxi host is called a standard switch, we will have to manually configure it on each and every single host which is not feasible on a large scale and makes scaling up harder.

instead, we could configure a single switch and share this configuration with all other esxi hosts with similar vSwitches.
##### Distributed Switch
The switch configuration is saved on vCenter, allowing us to select which esxi hosts to implement this vSwitch configuration.
This eases managing vSwitches and removes any room for error, since the configuration is the same across all hosts.

### Control vs Data planes
##### Control plane
The devices / hosts / software where configurations are, where you can **control** the rest of the devices.
example: vCenter & single esxi instance
##### Data plane
the actual physical links where data travels between hosts

#### further examples:
###### in distributed switching
the control plane of the distributed switches is the vCenter and the data plane is the vSwitches on the esxi host
###### in standard switching:
the control plane of the standard switch is the esxi host responsible for configuring the vSwitch
and the data plane is the vSwitch sending traffic.
###### interview related example:
we have an environment with vCenter and several esxi's with distributed switches, what happens to the distributed switches once the vCenter is down?
the data plane will remain functional, any vswitch connected with any VMs will still be able to transfer data between them regardless of whether the vCenter is operational or not.
however, you will not be able to update the distributed switches or change their configuration without the vCenter being operational.
for example, you won't be able to add or remove hosts, change routes or uplinks.

### vSwitch port group configs:

#### Properties
not explained this
#### Security:
these are the following available configurations, their default is reject.
- Promiscuos mode: turn switch into a hub, broadcast every packet through the network 
- MAC Address changes: allow traffic from virtual machines using mac address that's not their vNIC (since the vSwitch knows the mac address of each device connected to the esxi host without any arp discovery). The most famous case of this is nested esxi (installing esxi on a VM inside an esxi host)
- forged transmits:
#### Traffic shaping
the vmNIC has a physical bandwidth, we cannot exceed it due to hardware limitation so, we limit the VM bandwidth to prioritize traffic and VMs.
these are the available configurations
- average bandwidth: the average allowed bandwidth a virtual machine can use in a time frame, once this average is exceeded the bandwidth is throttled.
- peak bandwidth: the maximum speed allowed during a burst.
- burst size: We set a data limit for the VM, it's allowed to use lower speeds, for example 100MBs of data at a specific time and if it doesn't transfer this data at it's average speed, it's allowed to reach the peak speed until the saved percentage of the data remaining ends.
example:
vm1(average bandwidth) wants to send 400MB using average bandwidth of 100 Mbps, this'll take 4 seconds.
vm2(burst speed and peak bandwidth) waited for 10 seconds, transferring at a speed of 50 Mbps(half the average bandwidth allocated to it) even though it could transfer at 100 Mbps(average bandwidth), it transferred data equivalent to 500Mbs although it was supposed to transfer 1000Mbs of data, so now it's saved 400 Mbs of data as burst size, so it's allowed to transfer at 200Mbps (peak bandwidth) until it exhausts the 400 Mbs burst.
#### Teaming and Failover
This is applied in case where the vSwitch has more than one single physical vmNIC, this vSwitch consists of several port groups, `Teaming and Failover` handles how the vSwitch handles traffic in a **port group**.
a port group configured by the following 3 options tells which port group to use which available vmNIC:
- Active uplink: 
	we assign which vmNICs to be used by this port group.
- Standby uplink:
	we specify which vmNICs are selected to start working once the `Active uplinks` fail or stop responding.
- Unused uplink:
	it won't work or be used by this selected port group in any case (vmNICs fail / start)
##### Important:
a vmNIC paired with a vSwitch can be used in any number of port groups belonging to the that same vSwitch in any configuration (Active/Standby/Unused).
for example: vmNIC_1 is Active in both port group 1 & 2, but is in Standby in port group 3, and is Unused in port group 4.
a reason for making a vmNIC unused is to reserve it for critical port groups, saving it's bandwidth for them.
#### Load Balancing(important):
deals with how we distribute traffic across the `Active Uplinks` , according to these rules we can specify which traffic goes through which vmNIC.
##### This is routed based on :
- originating virtual port:
	pair a vmNIC with a specific virtual port, where all its traffic is routed through it, this is not the best load balancing method but it keeps the mac address table stable.
- source MAC Address
	this one pairs the mac address with a vmNIC, basically the previous one but with the mac address of the VM.
- IP Hash:
	hashes the source and destination ip of the packet, pairing the results with one of the physical vmNICs. this means any packet containing the same source and destination ip are routed through the same vmNIC, so if the same VM changes either the source / destination ip it'll change the target vmNIC.
	however, this causes mac address table instability
##### not allowing randomization of frame distribution across vmNICs:
physical switches receiving disorganized frames from different virtual mac addresses, routed through different switches with through different ports. so it saves the port with different mac address every time in its table.
this is `mac address table instability`. 
#### Solving Mac Address Table Instability 
it can be solved through NIC teaming since all the traffic will share the same mac address through NIC teaming the physical switch ports.
#### Failback:
once a port group fails the failback port group takes its responsibility to route data through it's vmNICs, this is detected through Network Failure Detection.
#### Network Failure Detection
The ability to know if a physical vmNIC fails or stops working, this happens through the following:
- link status:
	if the **physical** NIC shuts down (due to switch shutting down or ethernet cable cuts) it counts it as a failure and reports it.
	however, this doesn't detect route failure, meaning the link may still be up but the host / target is unreachable due to cable failure along the way.
- beacon probing:
	we send a heart beat(repeating packet that waits for it to return) to a target, this target is supposed to return the packet through a different vmNIC every time, if a heart beat doesn't return it assumes the target vmNIC for the packet return trip is down.

## Vsphere Storage
esxi can write to both file or block based storage, it uses them to write both the vm configuration and its data.
#### block-based
Through DAS and SAN, formatting it as VMFS.
esxi supports these SAN protocols:
- FC: 
	this requires a special hardware device called VMHBA, this allows the esxi device to handle fiber channel connections and outside the host, the network between the esxi and the storage box is handled by the admin. 
	once they're configured in the same Zone, the esxi host sends a discovery request (SCSI command) to know it's allocated LUNs.
- FCoE:
	is mostly connected to blade servers, since it's chassis(container box) uses an FCoE switch it to connect them together, then transmit their data through FC.
	same logic as FC applies here.
- iSCSI:
	the storage box and esxi host are connected through a normal TCP/IP network, the esxi host will have the ethernet cable connected through its physical interface, but to allow traffic through it, we'll have to configure the VMK virtual interface to allow traffic between the esxi host and the iSCSI storage box.
	This VMK will be connected to a port group with a corresponding vlan to the storage box, this allows them both to exist on the same network.
	the iSCSI port will be layer 4, the ip will be layer 3, the iSCSI commands themselves are layer 7, so we'll need a specialized hardware, in this case an iSCSI HBA, the most prominent one being Software iSCSI adapter.
	This option exists within vCenter or esxi, where you tell it to add a virtual HBA to handle the iSCSI adapter.
	this is all done virtually, without any actual hardware iSCSI adapters installed into the esxi host, then its translated through the normal ethernet port.
#### file-based
the share host is the one responsible for partitioning his own block, but VMware only allows the use of NFS.
we'll need to install a VMK virutal interface in a port group and connect it to the same network as the NFS Server, and since esxi has an NFS Client working by default, we'll just go to Data Store and configure the following options:
- NFS:
	first, we'll need to tell it the `IP` of the NFS Host
	next the exported directory, that the NFS Host allows you to use.
- VMFS
- vSAN:
	this is an object storage solution made by VMWare, each object is stored in a flat file store with its own metadata recorded with it.
	vSAN Allows us to connect the local disks from several esxi hosts and view their total size as a data store called "vSAN Data store"
- Virtual Volumes:
	this is an object storage that uses an external storage box and uses it as an object storage through a special protocol VASA (gffffw which I slept through its explanation.
	alternatively there is SPBM (Storage policy based management) which has the storage box specify the available features like encryption, deduplication, etc... then allow the esxi host to ask the storage box to automatically apply these features onto the object within the storage box without any interference form the esxi host or its VM.
##### Data store:
this refers to any device ready to store a VMs data, wether it is file or block based.
for example: we create a LUN on a storage box, configure it, map it to esxi. This allows esxi to format it accordingly.
This occurs by specifying that you want to create a data store, then specify the LUN and the format, in this case it'll be VMFS.
if it was NFS, you'll be asked for the target ip, and the export name (exported directory location on the target ip host)
in both cases, they will appear as data stores.


### RDM (Raw Device Mapping):
we pass through an entire disk device for use as storage, instead of creating a virtual device.
this can be applied to a LUN from a storage box, or a disk from the host.
