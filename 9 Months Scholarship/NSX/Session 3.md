### Routing
any vm that can have its traffic routed, will have a segment connected to a router.
when a packet wants to exit its local network, the segment will identify that its not in the network and will send the packet to the router to figure out the route / path the packet should take.
##### East-West Routing
this means that the virtual router will route packets inside the NSX Network, this is part of tier 1 routing.
##### North South Routing
this means that the virtual router will route packets outside the NSX Domain, to the internet.

##### Static Route
user manually define routes, any changes will have to be manually configured.
failover is also manually set
##### Dynamic Route
routes discovered and modified through route table exchange between the routers. each router will have a neighbor and route stuff according to their protocols.
###### Examples of each routing:
- The external router (tier 0):
	responsible for routing to the internet which requires it use both static and dynamic routing, since the internet is dynamic with addresses and urls changing periodically
- The internal router (tier 1):
	responsible for traffic inside the NSX domain, since it'll belong to the NSX and most resources can be statically allocated.
#### Services provided by an NSX Router
it can be a firewall, nat host, load balancer, vpn host, dns server, etc...
#### Comparison between Tier 0 and 1:
| POC                          | Tier 0 Router                                                              | Tier 1 Router                                                 |
| ---------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Owner / Configurer           | the NSX host because it is responsible for egress traffic                  | tenant, since its their responsibility to route to their apps |
| static / dynamic routing     | uses both                                                                  | only static routing within the NSX Environment                |
| ECMP (Equal Cost Multi-path) | supports it for physical gateways                                          | doesn't support it                                            |
| reaching other networks              | acts as the gateway between the internal networks and the external internet | can only reach the other networks through tier 0 router (including other tier 1 networks)             |
| Clustering                   | Needs to run inside a Cluster to ensure high availability                  | not required but could be done                                                              |
#### ECMP (Equal Cost Multi-path):
given multiple paths reaching the tier-0 routing, we're able to keep the link running even if one of the paths fails.
#### Routing Architecture:
are split into single or multi tier architectures.
##### Single Tier Arch
This is the least used architecture.
tier 0 gateways are the most used type of routing architecture will several segments connected directly to it.
##### Multi-tier Architecture
This is the most commonly used architecture.
the use of both tier 1 and 0 gateways, where tier 0 gateway is connected to the physical routers and the internet.
then any tier 1 routers are isolated within their network, connected to their segments and can access the external network through the tier 0 gateway.

##### Edge Nodes in an Edge Cluster
this is the VM that hosts the router, in this case it's a tier-0 gateway router that has an uplink connected to the physical router responsible for reaching the internet.
It's required to be clustered.
This edge VM must be mapped to a direct physical connection the router acting as a gateway to the external network.
long explaination:
the VM inside the esxi host, will be connected to a vDS where the port group hosting it has an uplinked physical NIC port connected to the external physical router that allows traffic outside of the data center into the internet. 
This traffic should be routed through two vLANs as a redundancy to prevent failure if one of the two vLANs fails.
This edge node must join an **Edge Cluster** to ensure high availability
#### Edge Cluster:
a single cluster contains a domain, this domain has several Edge nodes to ensure high availability and failure tolerance.
NSX supports up to 10 edge nodes per cluster with a max of 160 clusters.
we can overcome this limit by using VRF(Virtual Router) as a tier-0 router connected to a Physical Router which we use to increase the number of tier-0 routers without informing it of its neighboring tier-0 routers.
##### Failure Domains:
if we have several domains in an Edge Cluster, we can configure a Failure domain, that is automatically used in case another domain fails.
all the routing is then trafficked through the failure domain until the original domain returns.
### Gateway split
our gateway is split into two parts:
- DR(Distributed Router)
	This is made to avoid hair pinning (the process of having to go through an external router to reach an internal ip within the same host)
	the DR is distributed across all our transport nodes(any host capable to sending NSX traffic), its job is to do first hop routing by having the vDS segment consult the DR before sending the packet either through the router or a connected device without going through an actual router.
- SR (Service Routing):
	The allowance for the service traffic to return after the initial communication from the inside of the network.
	services like NAT, DNS, Firewall, etc...
	This is installed on the **Edge Node** because it is responsible for killing or keeping the connections initiated by the services.
	Stateful networking example:
	The connection between a VM and the internet goies like this:
	vm -> switch -> router -> tier 0 gateway -> target
	the returned traffic is:
	target -> tier 0 gateway -> router -> switch -> vm
	if a vm tries to reach the internet, it must be allowed for tier 0 gateway to pass its traffic to a target, we do not need to explicitly allow the firewall to return traffic from the target.
	this is because the vm inside the network initiated the communication and thus the returned communications are not dropped.

#### Intratier Transit Link:
This is an automatically created interface between the SR and DR, all traffic sent between those two passes through the Intratier Transit Link
#### Router Link Port:
this is an automatically created Interface between tier-0 and tier-1 gateways, it allows communication between them.
#### Uplink Interface:
this is the interface created between any port group and physical NIC
#### Downlink Interface:
This is the interface created between the vDS and the VM
#### Transit Link:
a logical link between the DRs and the edge node's SR.
#### Logical Interface:
is created between the vDS and the DR(distributed Router)
#### N-VDS (NSX Virtual Distributed Switch)
This is a switch made to be managed by NSX and is installed on esxi  host on a VM to control NSX traffic coursing through it, it passes its traffic through the hosts vDS which is then routed normally through the uplinks and physical routers.
and SR traffic wanting to exit the host will pass through N-vDS.
### NSX Traffic through a Physical Router:
given two segments spanning 4 esxi hosts, 3 of the hosts are carrying guest VMs, the fourth carries an Edge Node.
the fourth esxi host with the Edge Node has both an SR and an uplink connected to the Physical Router with direct access to the internet.
each of the VMs, have a TEP belonging to a logical switch.
now a traffic from any of the 3 guest VMs wanting to reach `8.8.8.8` will prompt their DR to send their traffic through the Transit Link to the default gateway of the DR which will route to the SR, allowing it to reach the internet and its target address.
#### Tier 0 gateway creation and connectivity
we specify the clusters through which tier 0 acts as a gateway, then we create an uplink interface between the gateway and each of the vDS segment subnets to allow them access to the internet.
#### Tier 1 gateway creation and 
we specify the tier 0 gateway to connect to, we can choose to deploy tier 1 in high availability mode, 
#### Route Advertisement:
it's an option in NSX for tier-1 gateways that allows your network to inform the routers above (tier-0 routers) it of its routes.

#### Gateway High Availability:
we start the gateway in:
- tier 0 in active-active mode
	the workload is distributed across all nodes to prevent overloading any of them
- tier 1 in active-standby mode:
	two nodes, one is active the other waits for it to become inactive, if one node goes down, another will take its place

