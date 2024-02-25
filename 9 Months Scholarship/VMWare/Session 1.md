vmware vsphere is dedicated for server virtualization.
SDDC: software defined datacenter

business are now required to implement Digital transformation, which means there are no business that can operate without the use and implementation of technology.

The whole point of Digital transformation is to show the customer the application that allows the customer to digitize their work, the customer won't care about any underlying layers between their data and their application.

the layer we're most concerned with in this course is the infrastructure layer:
#### Infrastructure:
any component your application will need to operate, other than the application itself.
We design our infrastructure to apply these 3 principles:
- reliability: The app doesn't crash everytime it opens
- performance: it needs to operate at a timely manner without wasting the users time
- security: the customers data should not be shared or stolen
Newer technologies are made to accommodate and improve these 3 principles.

of course, the use case determines what tech we use to implement which of these principles to what degree.

### Components of Infrastructure:
Most corporations own a datacenter, this contains resources that fall into the following categories:
- compute:
- Storage:
- Network:
- Security:

### Traditional VS Modern:
#### traditional data centers:
used each physical server as a host for a single application, given an example of a 3 tier app: a webserver, database and application, we'll get 3 different servers to do each of those.
if we want to isolate these applications, we'll need to buy physical firewalls, routers and switches to isolate these applications.
Basically: each application will be met with a physical requirement.
##### Challenges in traditional Data centers:
- Cost: This gets expensive the more you scale, while wasting resources.
- Time to market: The time between having an idea for an application and deploying int production (for a customer to use), this is affected by the time needed to acquire physical resources to deploy on.
- Management and Automation: How we manage these technical resources on scale, then automate them. This is difficult, since you'll need to connect to physical devices through ports.
To make a developer in the traditional data center, you'll have to give the him access inside the data center to allow him to use any of the resources within, there is no self-provisioning, this problem could easily be solved in the Modern DataCenter
### Modern(Software Defined) Datacenters:
This applies the principle of decoupling -- the process of removing the hardcore component from the production cycle, This can be done through virtualization.
The decoupling of the physical layer and the application layer through virtualization makes a server that can share it's resources to apply our application:
This server will be able to install several virtual operating systems ontop of itself, which can be isolated or shared.
This allows us to be able to run a 3 tier application on 3 different virtual machines, regardless of their underlying hardware. 
This layer of virtualization allows hosting 3 tier applications within their own virtualized host or in any number of different servers hosting them.
#### Over provisioning:
The provisioning of more virtual resources than are available on the server, this can be done due to the virtualization and pooling of hardware.
this can be applied to CPU in the form of time-share, since CPUs are time based, and RAM and storage in the form of data placement.
for example, we have a server with 64 gigs of available ram. we can create several server with over 100 gigs of ram, on the assumption that most servers in the pool won't be using 100% of their RAM at the same time.
if the application is not critical, you are encouraged to over provision.
##### auto-scaling:
The ability to increase or reduce resources of a server according to a user set criteria

unlike traditional data centers:
given a physical servers resources (ex: cpu cores, ram, storage size) these resources are fixed, once you buy them to fit a single purpose, for example an app that needs 64 gigs of ram, it may require more resources that previously specified, the load will change seasonally depending on factors outside the users control.
so, they buy resources according to the peak load, which is wasteful, since it won't be used through out the year.

### Virtualization:
The concept of virtualization depends on abstraction which in virtualization means the process of hiding the details of the device hardware, then give the virtualized device software defined resources, sometimes without even telling it that they're virtualized.

Hypervisor:
a layer between the hardware and the OS (type 1) or the virtual machine (type 2) that allows us to virtualize the vm hardware.
#### Types of hypervisors:
- type 1(baremetal): direct install onto the hardware like vsphere.
- type 2(application): installed ontop of the OS like vmware player.

### Vcenter:
the software solution offered by vmware to manage vsphere installations, they can exist in several subnets as long as they can reach each other through the network.
the tcp/ip requests are sent to the vpx/a (agent), which is responsible for executing the instruction through host.d

we can add hosts into vcenter, and group them by data center through something called a "data center object"

within the datacenter, we can place resources of hosts inside folders for ease of management.

### VCenter server services:
it consists of the following services:
- vsphere client: this is the web interface gui responsible for controlling the vcenter
- vpxd (vcenter server service): this is the service responsible for executing the commands you issue on the server.
- posgres (database): this stores all the data you create and manage.
- sso(Single Sign On):
	users send requests to the VCenter asking for any type of operation(see resources, create vms), but this will require special permissions which is handled by sso.
	This includes authentication and authorization of the users token.
	authentication: identify yourself to the vcenter
	authorization: the permissions you're allowed inside vcenter
	There are two ways to create users in VSphere:
	- local domain (SSO Domain):
	- External Identiy Provider (like Microsoft access directories):
		This is not a part of VSphere but it provides a service that allows you to create users for vsphere.
	login example: x@vsphere.local (this is the local domain), which then checks the user (x) with the given password and once they are checked, it allows you to enter.
	login example: x@DCLab.local (this is an external identity), it starts by contacting the domain controller, that checks for the user and it's given password, then authenticates it before informing the vsphere.
	then depending on your action, the server will check your permissions and allow you to do what you want, or deny you (give permission denied).
	after the first authentication, SSO returns a session token for communication without user / password until the session expires.
	This changes the authorization, the vsphere device will receive the token and authenticate it from the SSO.
- vmca:
	when a user attempts to connect to a server(vxp/a on an esxi host), they will first need to ensure that this server is the actual server it wants to communicate with, to do so, it asks for the servers certificate, this cert should not be self-signed, there are special organizations responsible for signing these certificates, so once the user gets the cert, it checks who signed it by contacting them and verifying the certification authenticity, these organizations are called Certification Authorities or in the case of vmware: VMCA.
	to create a certificate you need to request a CSR(Certificate Signing Request) from a CA.
	Vmware here will act as a CA (Certificate Authority),
	newly created esxi instances self-sign their certs, causing a warning whenever you try to connect another device to it.

### VSphere VMs:
The virtual machines work as a server inside the datacenter, these are its components and what they do:

- VMX: contains the VM data when it's created, the virtualized resources given to the VM(cpu cores, memory, NIC, HDDs etc...)
- VMDK: It is the storage device of the VM and contains all its data.
- delta.VMDK: the difference between the snapshot and the vmdk file, once it's created data is written onto it instead of the original disk, once the vm runs, the data is added on top of the OG.
- NVRAM: BIOS Configuration of the VM, 
- VMWare.log: it's responsible for any logs, for example: error logs from a VM crashing, connection logs from network, etc...
- VSWP:(VSwap):

### VMWare Templates:
These are pre-configured VMWare VM templates, which can easily be deployed with its previous states. this `.VMTX` file contains all the pre-configs and pre-installed software of the VM before you turn it into this template which will be deployed easily.
it copies the VMX, VMDK and delta.VMDK, changes some of the defaults such as the unique addresses in the VMX.
Templates format:
- OVA: Single File template containing all the previous inside it, most commonly used in VSphere
- OVF: Multiple file Template, which seperates the previous data across its several files.

VCSA (VCenter Server Appliance): it's a virtual machine Template (OVA File) that comes with VCenter, containing all the configurations for use install on ESXi hosts to manage them.

VCenter separates the VMs according to function, specifically management VMs and workloads, the internal VMs that are for use in-house are placed in the Management cluster, and any VM used to server external clients or for provisioning are placed in the workload Cluster.

##### Management Cluster:
- DNS
- Active Domain
- VCenter
##### Workload Cluster:
- Business Applications
## Vmware Configuration Information
### CPU configs:
other than the number of vCPU's given to a VM, we can specify the number of sockets in the VM, then the number of Cores per Socket.
#### NUMA(Non Uniform Memory Access) Node:
This is caused by the CPU having different bus lengths between memories (cache, ram) in case of having 2 cpu sockets in a mobo, it'll apply to each CPU trying to access the RAM nearest the other CPU.

This will affect performance, when dealing with wide VMs (vms with multiple CPU Sockets and virtual NUMA nodes) if not configured correctly, it'll experience slow down due to the physical NUMA it depends on, so to configure it correctly: we'll have to configure the vNUMA to mirror the actual NUMA that serves it.

#### Hyperthreading:
we split a single core into two threads, this means only one of them will work at a given moment which will increase performance during scheduling.
this occurs due to the execution engine (thread) no longer having to wait for the data to be fetched from memory because there is another thread that executes during the fetch time of the other, and they each alternate execution when the other fetches.

### Memory Configs:
we specify the amount of memory given to a machine and a dedicated swap file for each machine on the host.

if we've 16gbs of ram on the Host server, with 2 VMs, one of which allocates 8gbs and another 16gbs.
in case any of the two VMs reach their RAM limit, we can specify **priority** to define which of the two uses the available RAM, otherwise it'll be forced to swap.
#### Reservation:
This tells the host that the VM reserves N gbs of ram from the host and are not allowed to be shared with any other VM, this will prevent sharing of resources and swapping to disk, This is a form of thick provisioning.
The total reservation should never exceed the number of RAM of the host, otherwise the VMs will fail to start.
Reserved memory does not have Swap created for it, for example a VM with 8 gigs of reserved ram and 4 gigs shared, will only have an 4 gb swap file for the shared ram.

### Disk Configs:
This is saved as a VMDK file, we can create either as thick (allocate the entire storage on creation) or thin (fill data while in use).
if you don't monitor the thin provisioning of storage, over-provisioning may bring down the storage box as the provisioned data exceeds actual physical storage.
#### Thick provisioning is split into two:
- eager: will create a 50gb file and zero's (formats) the underlying blocks on creation.
- lazy: will create a 50gb file and zero's the files during write operation.
### Network Configs:
we create something called vNIC, it's assigned a unique MAC address, and then route it through a vSwitch.
it can use E1000, a legacy virtual hardware that has fallen to disuse because of vmxNet.

### VMWare tools (guest additions):
This are a set of programs to be installed on the guest machine, to configure and install drivers to related to VMWare virtualized hardware.

