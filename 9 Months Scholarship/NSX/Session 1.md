### Why NSX?
NSX is an SDN (software defined network) like cisco ACI.
This can be installed on a cluster through an OVF Template file (like vCenter) this will deploy an NSX Manager.
#### Deploying NSX
after installing through the OVF we can enter the UI to configure it and register it in the vCenter in the cluster, this will then allow us to configure it. however a DNS, NTP and vCenter should already exist on the cluster.
##### Syncing the environment:
in any enterprise environment, you'll need to sync both the time and network certificates, so a local NTP server will have to installed alongside a DNS server to keep track of time and accessible hosts.
any unsynced hosts may cause errors and prevent resources from becoming accessible.

### why use an SDN:
Traditional networking is hardware dependent which means each hardware device like a router or a switch will contain its own control-plane, this is good but makes it difficult to scale.
so, we decide to split the devices and their configuration into two planes, a centralized control plane and a data plane.
we can change anything in the environment in a centralized control plane and any changes are pushed to all the devices in the data plane, allowing ease of management and scale.
SDN use cases:
- reduce provisioning times by allowing self-service
- vlans
	in traditional networking we can create a max of 4096 vlans, in a public cloud, having a 100 customer than request at least 100 vlans, this will exhaust the number of vlans quickly.
	so, using NSX we can virtualize the vlans allowing us 16 million vlans, and if the vlans are exhausted, we'll create another environment allowing us another 16 million.
- multi-tenancy:
	allows us to share resources between the customers, this means each customer can take a piece of the infrastructure for his own use while its shared across several other customers.
	in a traditional environment, migrating between providers may cause conflict between existing ip schemas, however using multi-tenancy and isolation, we can create a network that handles any conflicts in the ips of the devices 
- micro segmentation:
	this takes each virtual network device and adds a firewall with ingress / egress rules, allowing each virtual NIC to protect itself using virtual firewalls.
- load balancing:
	in traditional networking, physical load balancers require a license, which means any newer load balancers will require configuration alongside their fees.
	in NSX, load balancers are a self-provisioned service that allows for load balancing.
- reduce cost:
	by increasing the efficiency and speed of provisioning, we reduce the work time which reduces cost and allows flexibility.
ip schema: the distribution of ips on specific devices / networks
### NSX Architecture:
like as software defined solutions, it's split into two decoupled components:
- control / management plane
	exists in the NSX management cluster, a cluster of 3 highly available vms that communicate together to manage all the available devices in the data plane
- control plane
	any amount of devices can reside here, it can contain esxi servers, baremetal servers, a special VM called NSX Edge (virtual router).
	these components can exist in either a public or private cloud but NSX will only manage the private cloud with several APIs / gateways to allow communication between devices in the public cloud and the network.
clusters: are a logical collection of vms that do one or more tasks
NSX router: a logical router that allows us to control and configure it through the control plane.
#### Management and Control Plane:
consists of 3 VMS, they provide the rest API responsible for controlling everything and a web UI.
they are 3 manager VMs in a cluster, they are replicated to ensure high availability in case of the components fails, another node continues with the last synced configurations.
each node will contain a persistent database, this database is replicated and synced regularly to prevent any failure.
each VM will contain a software responsible for Management, control and a database that serves them.
##### Management Plane:
which is split into two parts
- Policy Role:
	The desired configurations the customer / user wants to apply to the devices
- Manager Role:
	The device responsible for configuring the wanted policies and turning them into an applicable form for use in the data plane 
##### Central Control Plane:
this is the device responsible for communicating and applying configurations the devices in the data plane. it acts as the middle man between the incoming configurations and the devices in the data plane.
it takes all the decisions while maintaining the runtime states of all connected devices in its network (in case a vm migrates, it'll reroute traffic to its new location, if a vm shutdown, it halts traffic to it).
The database of the control plane will contain all the runtime states of the devices in the data plane.
Components of the CCP (Central Control Plane):
- Local Control Plane
	This is a service that is installed on each ESXi host, allows for the host to update the control plane on anything that happens to any of the VMs present on the ESXi host, any updates, deletion or failures are then sent to the control plane
- Transport Node / NSX-Proxy
	This is a host with nsx-proxy agent installed on it, it allows you to use NSX on the local control plane.
	distributes an agent on each collection of devices(routers / switches) belonging to a local control plane that works under the Central Control Plane and applies the given configuration to the traffic.
##### Control Plane Sharding:
Since we may have thousands of local control planes, sharding allows us to specify which of the 3 controllers manage which local control planes, then sync together the info collected from their managed local planes.
so, even if a controller is not managing a specific local control plane and said control plane fails, all the controllers will be aware of their failure due controllers syncing together.
it allows redistribution of their managed planes if any of the controllers fail.
##### Cluster Virtual IP Address:
this virtual ip is a utility feature inside the NSX, allowing you to access the cluster manger vms through it.
it requires all of the 3VMs to be in the same subnet, so you can access them through th vIP address, this IP address will be assigned to the leader of the controllers, through an election process.
although, this vIP will contact the manager leader, it does not load balance to the other controllers, which means that the leader will inform the other controllers of any decisions and policies applied on it.

##### Management Cluster with Load Balancer:
we can increase the security of the cluster by placing each manager VM in its own subnet, and add a load balancer to allow traffic to be distributed across the the 3 VMs.
we can also, specify traffic use case which allows specific traffic to target a specific VM.

### Data plane:
it carries the work load of the virtual data center, its job is to forward the traffic specified by the management plane.
It contains devices that could be virtualized (vms) or physical.
Since traffic is virtual, any packets transferring between the virtual and physical networks will have to be encapsulated with additional headers to make the traffic compatible with the physical network and are decapsulated once it returns to the virtual network.

##### NVDS:
this is a virtual switch that is automatically installed onto the bare metal host by NSX, to allow traffic to be virtually routed through NSX.
#### The five stages of setting up NSX-T:
##### 1) IP Pool (Tunneling End Points):
Ip Address pooling is a virtual feature that simulates Vlan isolation and allows us to map TEPS (Tunneling End Points) to specific pools which act like VMWare VMK in esxi hosts.
the source TEP encapsulates the NSX traffic, as it exists the host and passes through the environment until it reaches its target TEP which then decapsulates it and sends it to its target.
If a host doesn't have a TEP compatible IP, the TEP redirects it to the ip pool to provision for a compatible ip address that is allowed to transfer data through the TEP.
we can also setup a default gateway, and the TEP traffic can be routed through the router containing the gateway.
##### 2) Transport Zones:
this is the "configuration boundary" that is applied on a VDS(Virtual Distributed Switch) which basically specified which transport nodes are accessible to any other transport nodes.
this is a faster way to configure access, view-ability and traffic for a set of esxi hosts.
any two members of a transport zone are considered in a layer 2 broadcast domain, so any messages between them will be accessible by everyone else in the transport zone.
in a node / host the can exist in multiple Segments with their own transport zone property at the same time.
there are two types:
- Overlay Transport Zone:
	  This applies to NSX Traffic, encapsulates it in the form of "geneve-encapsulation"
- Vlan Transport Zone:
	This changes the encapsulated packages into a vLan compatible form, instead of the special encapsulation typically used by NSX (called geneve-encapsulation)
example:
we've an NSX Edge, 2 ESXi hosts and a bare-metal server on a shared transport zone, these devices are capable of sharing a vLAN inside this transport zone, they can access each other and the internet through it.
however, we wanted to add the NSX edge into two other vLANs, so we create two more transport zones and include the NSX device in it.
##### 3) Uplink Profile:
This is a template responsible for directing how traffic exits the host, it is connected to a vDS and specifies how the traffic exits through the physical NIC of the host.
this allows us to map a vDS to a physical NIC, for traffic to pass through them.
this is the same uplink used in vDS but as a template that can be applied to any switch, it's literally the same.
but it has TEP integration, you can use it in the Overlay Transport Zone instead of using vLAN.
Teaming Policies:
- load balancing:
	you split packets across available active uplinks
- failover:
	specify which backup uplinks are to be used on failure of any of the active uplinks
##### 4) Transport Node Profile:
This is an optional step, that allows us to create a template of the NSX cluster configuration that automatically installs the configuration of the previous 3 steps (IP Pools, Transport Zones & uplink profiles) to the cluster.
This increases cluster deployment speed with consistent re use of the template.
##### 5) Transport Node Preparation:
i slept.
#### Opaque Networks
these are networks created and managed outside the vsphere context, for example vCenter creates an opaque network on an esxi host and once you access it from the host vsphere it will have a special symbol that tells you that it's managed remotely either by vCenter or NSX.