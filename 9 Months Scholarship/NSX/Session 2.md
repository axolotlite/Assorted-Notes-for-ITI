### Logical Switching / Segments'
manager views segments as logical switching and policies view logical switching as segments.
they are one and the same, and they extend functionality on the network.
Each segment has its own VNI which works as an identifier such as VLAN id in cisco, and each host in a segment can communicate with other hosts within a segment as long as their within the same host, otherwise the two hosts will require using *TEP* to allow communication.
 
we can install a segment on a VDS this "segment" has a VNI (Virtual Network Identifier) which allows us to distinguish between vlans in the network.
each segment will have several segment ports (which allows hosts such as VMs, routers, switches or containers to connect to the network through it) that allows it is similar to a "port group" of a VDS.
###### Difference between a Segment and Port Group
a segment has VNI that's used to identify it inside the NSX network.

##### Advanced operations through Segment Profile (part of micro-segmentation)
- traffic sourced through a specific IP on a specific port on the segment
- quality of service (increase bandwidth to a specific port on the segment)

### Geneve(Generic Network Virtualization Encapsulation)
allows us to tunnel layer 2 (mac address) over layer 3 (ip addresses), meaning that we can connect two different devices as if they're sharing the same layer 2 space, with access to their mac address.

its header will contain the target VNI (segment identifier) in its data alongside its options.
### Tunneling between two hosts:
TEP(Tunnel End Point) in NSX uses geneve encapsulation (a standard encapsulation method unrelated to vmware) to allow encrypted communication across a vDS regardless of host (since the same vDS can be installed on multiple esxi hosts), it uses tunneling to avoid the need for physical switches to find the destination outside this host, since the tunnel will directly route to the destination across it's tunnel with no switching.

#### Creating a Segment:
creating a segment in NSX will create a policy rule that will be passed to the manager to apply it to the central control plane, which sends commands to the local control planes through their NSX-proxy agent, which will execute these switching policies.

#### Network Topology feature in NSX
there is a feature that allows you to visualize your network topology in NSX, you can see the VMS, their segments and the routers connecting them.

### Segment Profile:
this allows us to create more advanced configuration not available in normal segments, it basically allows us to apply these configuration on multiple segments or segment ports.
these features are:
- IP & MAC discovery: allows discovery of mac and ip address of included VMs in all host in a segment even if they change. 
- Spoof Guard: prevents fishing
- Segment Security: accepts specific traffic for an approved source on an approved port.
- QOS(quality of Service): give specific hosts preferential treatment when provisioning or using specific services, in this case network bandwidth.
#### Applying a segment profile vs a segment port profile
as their names specify, segment profiles are applied on a segment, segment port profiles are applied on segment ports.
if you apply a segment profile on a segment, all its configuration will apply to its ports, except on ports where you apply a segment port profile.
segment port profile takes precedence over segment profiles.

### Logical Switching Packet Forwarding
This is similar to normal packet forwarding, it uses the same basics such as needing an IP and other stuff but it's mechanism is different

##### Scenario:
we have 3 esxi hosts, each with the same distributed switch and segment installed on each of them.
let the segment **VNI = 6500**
since vms are assigned to segments,
if each host has a single VM installed in it, with each VM connected to a segment port, if we want these packets to exit a host through the physical network to reach another host, we'll require them to go through a TEP, which will Geneve encapsulate it as it exists the host and goes through the physical network on its way to another host.
let host A,B,C have a corresponding VM 1,2,3 and their own TEP.
TEP(A) = 850, TEP(B) = 900, TEP(C) = 1000
IP(VM 1) = 10.10.10.1, IP(VM 2) = 10.10.10.2, IP(VM 3) = 10.10.10.3
if VM 1 wants to send data to VM 2 while only knowing its ip address, then the packet from VM 1 -> 2 on the same vDS:

| src ip | src mac | dst ip | dst mac | VNI |
| ---- | ---- | ---- | ---- | ---- |
| 10.10.10.1 | A:1 | 10.10.10.2 | ?? | 6500 |
since the destination mac is unknown, we'll flood the network to acquire the mac address, this means the traffic will go from host 1, to each segment port in the same vlan (excluding itself), this packet will include the VNI, but to exit the network, it'll need to know the TEPs for each host to reach them.
this means each TEP needs to be recorded inside a table such as the following:

| VNI | TEP |
| --- | --- |
| 6500   | 850 |
| 6500   | 900 |
| 6500   | 1000    |
now the packet will go through the physical switches through Geneve encapsulated because of TEP which allows for layer 2 traffic, it'll be able to find the mac address.
once it reaches the other side of the TEP, it'll be decapsulated and sent to the hosts until it reaches its target host (any other host will drop the packet)
after the flood is done, the packet will become

| src ip | src mac | dst ip | dst mac | VNI |
| ---- | ---- | ---- | ---- | ---- |
| 10.10.10.1 | A:1 | 10.10.10.2 | B:1 | 6500 |
now, anytime VM 1, tries to send packets to VM 2, the source iP an destination IP will be known alongside source and destination mac addresses.
So, it sends the packet, which passes though the TEP.
vDS has a mac address table which maps the mac address with the corresponding TEP that allows the packet to reach its target, this also means that the physical switch which will be able to identify the host where VM 2 is through the mac address.
vDS mac address-TEP table:

| Mac | TEP  |
| --- | ---- |
| A:1 | 850  |
| B:1 | 900  |
| C:1 | 1000 |
##### NSX Flooding vs Normal Flooding
normal flooding sends a broadcast to all hosts across the network, this creates a load on the network, another flood will increase the load, and only the host requesting the mac address of the target will record the results of the flood.
Unlike NSX which records the results of the flood alongside the host who flooded. so, if another VM on the host asks for the mac address of the same ip, it'll not need to flood since the results of the previous flood were recorded.
##### Scenario Continued: 
so, if we create VM 4 on host A, and it wants to contact VM 2, which was already found by **VM 1** during the previous flood.
VM 4 will not need to flood to find the mac address, because the results of the first flood were recorded by NSX, so VM 4 will get the mac address **without flooding**. so the packet will be:

| src ip     | dst ip     | src mac | dst mac | VNI |
| ---------- | ---------- | ------- | ------- | --- |
| 10.10.10.4 | 10.10.10.2 | A:2     | B:1     | 6500    |
As you can see, it's not missing the destination mac address.

all this data is sent back to the Central Control Plane to create a centralized TEP Table, Mac Table and IP Table, that it will distribute to its local control planes.
##### Building a TEP Table:
once an ESXi host is attached to a segment, it notifies the central control plane of its existence in a segment, and its TEP.
now, any VM connected to the esxi host on the same segment will register its mac address to the TEP ip inside the same table.
now the **TEP Table** will save the `VNI, VM Mac, VM IP, TEP IP.` but the most important two attributes in the TEP Table will always be the VNI and TEP IP / subnet.

**NOTE** the main reason the esxi host or vDS may not know the VM ip address is because the VMware tools that we're supposed to install are not installed or not working properly.
#### Important TERMS:
**flooding** is a type of bum traffic
**Bum Traffic**: its any traffic with an unknown destination whether it is flooding broadcast or unknown unicast.
Replication mode: once a TEP receives bum traffic it goes into **replication mode**, to replicate this traffic to all other TEPs in the segment VNI, 
there are two types of replication mode:
- head: 
	source TEP does everything it replicates the packet, encapsulates it and sends it to all over TEPS in the segment
- hierarchical(default of replication mode): 
	given servers within the same TEP subnet, we replicate and encapsulate the packet to it, otherwise if the TEP is in another subnet, we send it the encapsulated replicated packet and inform it that it has to do the same process in its own TEP subnet, this will make it a **proxy TEP**.
	This means a unicast to TEPs in other subnets and multi-cast to TEPs in the same subnet.

This whole process allows the decoupling of switching from the actual hardware switching.