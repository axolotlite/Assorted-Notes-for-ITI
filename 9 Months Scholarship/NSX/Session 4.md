### Zero Trust Security:
trust no one and verify everything in the network.
basically, place firewalls within each layer to prevent any unknown packet or data from entering or exiting the network without being explicitly accepted.

### NSX Distributed Firewall
This is part of micro-segmentation, it distributes the task of firewalling into smaller segments.
there are two types of firewalls
- perimeter
- distributed:
	This is a kernel module installed on all the transport nodes, specifically working on the vNIC of the VM, it checks the input / output traffic.
	the gateway firewall does the same but on both tier-0 and 1 uplinks and interfaces.
### Distributed Firewall policies:
we can specify policies for group to apply specific firewall rules to a specific group of devices / hosts.
#### Time based policies
you can specify a time interval to apply or annul specific firewall policies. 
##### Tags
we can assign tags to specific resources, to specify where or who it belongs to, as a concept tagging is used as an additional general identifier.
Then we can apply tag based rules, which can make it easier to add policies by tagging any newly creating resource which in turn will apply the policies related to the tag on creation.
### NSX Gateway Firewall:
This is a firewall applied between each gateway, whether between the Physical router leading to the internet & the tier-0 gateway
or
between tier-0 and tier-1 firewalls.
This is most commonly used, unlike the distributed firewall.

### NSX Services

#### NAT:
This allows us to allow all devices within a host to interact with the external network through a shared IP address / pool.

| NAT Type                          | device      | descriptions                      |
| --------------------------------- | ----------- | --------------------------------- |
| SNAT                              | tier-0 & 1  | allows stateful nat communication |
| Reflexive NAT                     | tier 0 only | stateless nat                     |
| Stateful Active-Active SNAT /DNAT | tier 0 & 1  | allows for stateful active-active which according to our instructor is a revolutionary feature only available in NSX 4                                  |
##### SNAT:
you change the source IP address exiting the router to interact with the external network.
for example there are two vms inside the vSphere, with external internet connectivity.
both vms will have their own private ips, that they can only use internally.
to interact with the internet, the tier-1 gateway will give them a public ip to allow them to access the internet.
#### MPLS:
its basically no-NAT, it allows you to use your private ip address through the public internet, this is a service provided by your internet provider
##### DNAT
This is the opposite of SNAT, instead of converting internal traffic using external ip address, it turns external traffic in, using a private ip from inside the network.
#### Reflexive NAT:
Stateless NAT, this means that its traffic can enter and exit from different sources.
#### DHCP
we have a dedicated server with an ip pool, that distributes ips from that pool to any newly connected device in the network.
this leasing of IP addresses is recorded in a table for reserving that ip for a while.
We specify a profile before selceting the type of DHCP to apply it to, finally we can configure it further.
##### Types of DHCP Server:
- Segment DHCP:
	Segment Specific DHCP server, can only answer dhcp calls inside its segment and only that.
	This works only in its own segment, giving up within the same IP.
- Gateway DHCP:
	This DHCP is made for tier-1 routers, giving ip addresses for devices within the network.
- DHCP Relay:
	this sends any dhcp requests to and from the DHCP Server, it acts like a middle man, transfering any request between clients before sending them to the server.
#### IPSec VPN (Internet Protocol Security)
The goal is to send secure trusted traffic through an untrusted network such as the internet.
we do this through putting a tunnel between both end points (your network and the target network)
This can be done through encryption, authentication and preshared keys.
pre-shared keys: we agree on two keys, one at the source and another public at the target, we agree to encrypt the data to which the end user can decrypt with their key.

Types of IPSec VPN:
- Policy Based:
	This works on tier-1 routers, so vodaphone only allows policy based to avoid configuring tier-0 routers.
- Route Based:
	This works on tier-0 routers
##### IPSec VPN High Availability:
using failover and traffic distribution to avoid over working a single tunnel.
##### Layer 2 VPN:
unlike normal VPN, we do this to extend the broadcast domain across two different sites, so we transfer the entire layer 2 alongside its broadcast domain, through a layer 3 tunnel.
making two different locations across an entire different network act as if they're in the same site, securely sharing the layer 2 network.
This works on both overlay and vlan segments.
This is done through something called GRE (Generic Routing Encapsulation) that is encapsulated in IPSec on top of it, allowing both layer 2 and layer 3 tunneling.
##### L2 Tunneling through Autonomous Edge:
This an OVF edge VM that can run without having anything control or manage it, it comes with its own control and data planes implemented.
it contains all the needed VMs to run itself, creating a tunnel between the site and the place containing the autonomous edge.
##### Setting it up
we can get an L2 config from the server that would allow us to set up a connection with its keys.

### Advanced Load Balancer
This is a product similar to NSX, VMWare have been pushing to remove any load balancing from NSX onto this project.
#### Load Balancing Algorithms:
- Round robin:
	equal sequantial distribution of data
- Least connections:
	host with the least amount of active connection
- Least Time
	distribute the fastest ending connections to the host to finish quickly
- ip hash:
	depending on the ip, you hash it and distribute according to the result of the hash
#### AVI Architecture
similar to the NSX, we have several planes:
- Advanced Load Balancer Controllers (Management and Control plane)
	This is a replicated cluster that manages the rest, it has the configuration and manages the service engines
- Service Engine (Data plane):
	This is a vm carrying the load balancer, it's a small vm with small capabilities.
	it can be active-active or active-standby.
	whenever a load balancer in created, a corresponding service engine VM is created to handle the load balancing while collecting real time analytics from operation.
#### Service Engine Group
we create a group of service engines, giving them names to identify them and give them specific configurations to apply whenver we add or remove service engines.
this configuration will be customer specific.
##### Deploying a service Engine GRoup
we connect the service engine group to the NSX server, gateway and the application to allow its operation.
#### Components needed in load balancing
- vIP that goes to a service engine pool
- application profile
- health monitor