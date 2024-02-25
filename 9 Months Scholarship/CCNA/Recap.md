## Networks and some Basics
What is a network?
grouping of devices together to server a purpose, like sharing of resources.
we can build a network using end devices, with an intermediate device connecting them through a transmission media.

then on the software side we'll need a communication rule to facilitate rules of communication.

hubs don't understand mac addresses, unlike a switch.
switches can record mac addressing by sending a frame to identify their mac addresses and record them in a mac address table.

routers connects networks together.

mac addresses are the physical device identifier, recorded in 48 bits format.

routed protocol: it's the ip of a device in an internal network.

routing protocol: software present on a router, connecting networks, while deciding the best path(route) to send communication through.

## OSI Model

Sending an email to someone, first we interact with the app layer (gmail through browser) underneath it lies the 
presentation layer, responsible for formatting the data, encoding, encryption and most importantly how it looks to the user on his machine. underneath it the layer connecting the users / servers
session layer: keeps devices connected
transport layer: responsible for delivery protocol either using TCP or UDP. tcp ensuring safe delivery of data without any loss, UDP is best effort, responsible for sending the data to the user as fast as possible.
tcp headers is 20 bytes while udp uses 8 bytes for it.
dns uses both TCP and UDP. tcp between servers while UDP between the server and client.

network layer: recieves packets with layer 4 headers, each containing the source ip and destination ip.
data link layer contains frames with the source and destination mac addresses.

finally the physical layer responsible for the bit transfer and checksum.

this previous process is from a user sending an email, the same process in reverse occurs once the reciever takes the packet, bits are made into frames, frames are decapsulated into packets, packets get their data used by each following layer.

there is two types of routing
Static: manually setting the routes and connected networks.
Dynamic: Software is responsible for finding the optimal routes and discovering connected routes.

Types of Routes:
Direct Route: two routers are directly connected through interface, no hops between them. they have the highest admin distance 0.
Static Route: you specify the interface through which the desired network can be reached where through the main interface or the next hop ip. manually. it has an admin distance of 1.

point to point network: two routers connected through a serial cable. in static routing it prefers direct interface.
broadcast network: a switch connected with several routes. in static routing it prefers next hop ip.

In dynamic networking we'll need to configure:
interier gatewat protocol: used to communicate with devices within the internal network. for example: 
vodafone connecting hunderds of routers using the same routing protocol.
this makes it a single network using a single routing protocol in an autonomous system( a domain controlled by a single admin using a single routing protocol)

exterior gateway protocol:
connection between two autonomous systems, to allow the handling of routing by placing a protocol that translates communication between them.

each protocol has its own metric for defining the best route which will assign a number.
administrative distance for that protocol.

dynamic routing protocols:
RIP: uses distance victors. with admin distance 120
V1: lossful protocol that doesn't support subnetting it only sees a single network, broadcasting everything through a general broadcast 255.255.255.255 (every device)
V2: lossless protocol with subnetting support with broadcasting through 224.0.0.9.
when two routers use rip to connect with each other each router sends its own routing table info to each connected router, cascading its info through the network, increasing the administrative distance with each hop.
once a network connected falls, route poisoning may occur, each router pushing a newer larger route of the disconnected network with increasing admin distance.
this was solved with split horizon / hold down time.
once router a router fails, it'll broadcast a timer to ignore any info about this failing network, alternatively once the 180 timer ends they receive info from this network again.
another method is route poisoning, setting the admin distance to an infinity making the route no longer viable.

when given two routes with similar metrics, rip allows for equal load sharing (distribution of data through two similar routes)
RIP doesn't need a subnet mask because it directly matches interfaces of a given ip, then records the subnet mask by its own self, after we specify `no auto summary` during configuration
IGRP: classful protocol (doesnt support subnetting) and broadcasts 255.255.255.255
with admin dist 100, with a max hop of 255 and bandwidth + delay as a metric using an equation.

OSPF: uses link-state (link means connected, state is either up or down) advertisement across all directly connected routers, which in turn is saved in link-state database.
in a point to point topology each router sends a hello package before a link-state advertisement. once a link-state adv is received it's added to the link state database which is used to build a route tree, finally it starts determining the best route in the tree through djikstras algorithm. this means we rarely get loops, while its multicast uses 224.0.0.5 to broadcast LSA to all connected routers with an admin dist 110 and a billion/bandwidth as a metric.

but once an interface is modified(up'd/downed), the tree is remade, so a solution was made.
divide the network into areas, each area connected with a singular backbone area.
this limits recreation of the tree is limited to each area, reducing the rebuilding of the tree in all connected routers, instead they receive the updated tree from their border router (backbone area connected router).
it has a hello interval and a dead interval calculated as 4x the hello interval, these two intervals should be the same on all devices in the network.

in a broadcast a leader router is assigned, through connecting a group together, the fastest to reply within 40 seconds of connection is designated as a leader, otherwise they'll check the pre-assigned vendor OSPF priority which can be manually modified, and finally if all priorities are the same, a comparison of each devices router ID is made, making the leader the router with the highest router id.

picking a router id:
loopback is a virtual interface used for its always up state, making it perfect for testing, it's configured, given an IP and used as an alternative for a router id.
the highest physical interface which may cause a problem if the connected cable is removed.
the leader (Designated Router) has any newly connected router advertise itself to it on 224.0.0.6 in turn, he will multicast the new tree update through 224.0.0.5 to the rest of the routers, while asking them for their data to send to the new router on the same address, if any new routers are connected they will advertise him into the database, then ask them for their info to send to the new device.

EIGRP: is a proprietary cisco protocol.
each have their own autonomous system  number configuration, they need to match between communicating routers.
this number is bought from IANA.
it is backward compatible with IGRP, provided both belong to the same autonomous system.
wildcard mark, the 0 bit here means don't check for change. making it the inverse of a subnet mask.
the successors are stored in their own tables, their feasible successors are saved in the topology table, which are acquired from there once a successor falls off.
uses dual equation to find the best route and makes it the successor then its feasible successor. 
we can allow automatic transferal of all connected networks in a router by adding the 0.0.0.0 network to the eigrp system id.
## Redistribution
having two routers, one using RIP another using OSPF and we want both of them to communicate despite the conflicting protocols.
in order to do this we redistribute the RIP / OSPF metrics into OSPF / RIP format, alongside everything else.
this'll bring us to dealing with the differing hop count.

## DHCP
statically assigning an ip is done manually, user set.
there is also another static method called alternate.
dynamically setting it is done through dhcp and once it fails, it defaults to apipa (automatic private ip address)
class a 10.0.0.0/8
Class b 172.16.0.0/12
class c 192.168.0.0/16
class d 224.0.0.0/20
class e the rest
there are two more private networks, a device loopback 127.0.0.1 and apipa network.

first a discover message is sent by a client to find the dhcp server in the network, once the server recieves the message it offers it an ip address, while identfying itself, the device then makes a request for the offered ip address, finally receiving an acknowledgement from the server with the ip for assignment.

in case of multiple routers and an external dhcp server, in order to reach said dhcp server, it has to go through the router, which single cast to the dhcp server if it's configured with the helper-address(dhcp server ip).
the helper address can be specified on an interface to allow specific distribution of ip addresses.
configuring dhcp occurs after specifying the routes to the dhcp server, so we can specify the helper-address and allow the routing table to handle the path to it.
APIPA may have ip addressing conflict.

## NAT
Static: acquiring one public ip then binding it to a single private ip address in the internal network.
Dynamic: acquiring a pool of public ips and binding them to an equivalent amount of public ips.
PAT: port address translation, using ports we can send data and receive them through said port, giving each device a collection of ports to use for their session.
for each device we assign a unique source port and destination port, so no conflicts occur between them.

## Switching
connects multiple devices in the same network, we could isolate devices in the same network through vlans.
vlans allows us to isolate networks, reduce broadcast and cost instead of buying a new switch.
it's preferred to change the native vlan in the switch.
trunking mode tells the router that this interface is designed to send vlan data, each tagged with their equivalent number, only the native vlan is untagged.

encapsulation in the router side is tag specific, the router notifies the interface of the tag coming form the switch and how to handle it.

## Spanning tree
given a number of switches in a network, if an interface between then shuts down, we must ensure an alternative path for the network, this may require redundancy which will increase cost and may cause a loop that causes a broadcast storm (the same broadcast echoes through several switches without stopping) and mac address instability, due to multiple mac addresses returning from the broadcast.

this will allow all the vlans to go through the main cable, we can use per vlan spanning tree, a way to divide vlan traffic alongside different routes.

this connection takes 15 seconds listening, 15 learning and then it starts working, using rapid pvst we can skip the listening and learning.
there is also a security feature that disable end points from acting like a switch(sending switch specific packets) called (bpdu guard). this drops any bpdu packets trying to go into or from this interface.


