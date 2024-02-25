## Overview of Storage types:
- DAS(directly attached storage)
- SAN(Storage Area Network): it's a type of block level storage, it's provisioned without any filesystem, leaving formatting and partitioning to the host, they can transfer data through the following protocols.
	- FC (explained in session 2): 
		- lossless
		- expensive
		- complex
		- initiator hardware (HBA)
		- traffic transferred through: SAN Switches / Directors
	- IP-SAN: further divided into two protocols / network layers
		- iSCSI
			- lossy
			- cheap
			- simple
			- initiator hardware (NIC, NBA, ToE)
			- traffic transferred through: Network switches
		- FC-IP: transfers SAN Traffic between two sites
			- Merged fabric
			- traffic transferred through: FC-IP Switches
	- FCoE: uses mixed layers from the previous methods
		- mixed between FC & iSCSI
		- initiator hardware (CNA)
		- traffic transferred through: FCoE Switches
- NAS (Network Attached Storage): a file sharing protocol that allows directories to be attached through TCP. the following protocols are:
	- NFS: for \*nix
	- SMB: for windows
	- HDFS: for hadoob systems
- Object: uses flat-address space to store data
- Unified: is a type of storage box that understands the previous types and is capable of provisioning each of them.

## IP SAN:
### iSCSI:
unlike FC, this protocol uses the TCP/IP stack to deliver block level storage.
#### advantages:
- low cost
- simple (not complex like other protocols)
#### disadvantage
- lossy layers and packet loss
- increased traffic through the shared network
#### Initiator hardware:
in this protocol the initiator(device requesting block storage) can use the following hardware components to communicate with the ISCSI servers:
- iSCSI HBA (host bus adaptor): this hardware card will be responsible for both transferring data and encapsulating it with tcp/ip to transfer it through the network.
- ToE (tcp offloading engine): this piece of hardware lets the cpu handle the SCSI protocol while the ToE offloads the en/decapsulation process onto the network controller, instead of the host.
- NIC (network interface card): the card uses the CPU to en/decapsulate the ip/tcp data, while transfering the block storage, which is a wasted utilization.
The initiator here will need to work through two protocols, the SCSI's storage commands and transferring/receiving them through the ip/tcp protocol.

#### Target Hardware:
the target(block storage provider) has it';'s own HBA with iSCSI functionality.
### FC-IP:
This protocol uses both fiber channel and ip protocols, it's used to connect two data centers / sites together.
basically, connecting two different SANs through the ip protocol across two different geographical location while having each of them use FC inside their own respective networks.
#### FC-IP Gateway: 
this is a device placed in each site, which allows the internal SANs to use FC while it en/decapsulates any cross site traffic with the IP protocol.
This merge of protocols occurs due to a limitation of fiber channels (10km max distance which you should not mistake with fiber cables which have a range of 100km), because they do not support long distance connectivity.

### iSNS Discovery Domain:
this is the iSCSI equivalent of zoning, it has you to add an initiator to the same domain as the target device, allowing both of them to communicate and transfer data.
This will be configured through the network switches.
then you can configure the vlans alongside it, with all the features of a vlan.

#### vlan stretching:
you can extend a vlan into another site / network through a tunnel between both sites.
this makes the vlan available in both sites

### FCoE (Fiber Channel over Ethernet):
This protocol uses FC-layers for transmission with the physical layer of the network. This will require specialized hardware:
#### FCoE Switch:
This special switch is capable of transferring both FC and Network protocols, allowing us to use either or both (FCoE).
#### CNA(Convergent Network Adaptor):
a piece of hardware connected to the initiator which is capable of handling both FC and Network protocols.

This doesn't actually solve the core issues of the previous protocols, as it requires specialized hardware for both the initiator, switching and targets.
the switch will route the normal network traffic to the target devices and the SAN traffic to their storage boxes.

## NAS
the main difference between the SAN and NAS is that SAN doesn't have a filesystem, it's up to you to format it, unlike NAS which comes with a pre-installed file system on the shared directory.
#### NAS Components:
- Controller / NAS head: all the functionality is implemented here.
- Storage : the place where data is stored
#### Scaling up NAS:
- scale up: we can increase the number of disks for storage or the number of nas disks
- scale out: we add another nas device which includes disks and nas heads

most commonly used file systems for NAS:
##### CIFS / SMB: 
commonly used in windows, it's a stateful(it sends a request for file change and waits for acknowledgement before write while keeping info about the responsible channel) file system.
##### NFS:
used in \*nix systems.
##### HDFS (Hadoob distributed filesystem):
used in hadoob, for big data applications.

both NFS and SMB work as client / server.

### Object Based Storage
it's used when there is a lot of data files, too many for blockfile storage to handle, another use case for real-time data like monitoring data from IOT.
It saves data in a flat address space, alongside the meta data and additional access info, any edited object is saved as a new object.

Unified Storage: a storage box capable of all the previous methods of data sharing, it has all the specialized controllers and software needed to launch them.

## SDN(Software Defined Network):
this add a virtual layer on top of a physical switch, allowing us to exponentially increase the number of vlans.
given a switch, we want to have each customer on a specific vlan, each switch has a limit or 4096 vlans, by adding a virtual layer on top of the switch, we can create over 16 million vxlan, this virtual layer will also separate the data and control planes.
this also adds more services like NATing, firewalls and more control over this virtual layer.

