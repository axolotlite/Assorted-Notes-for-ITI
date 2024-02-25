## Neutron
This is the networking component of openstack, it deals with managing, controlling and providing networking for the entire system.

it has the following components:
### Neutron API
This is main entry point for neutron and it has the following plugins
#### Core Plugin
This is the plugin responsible for layer 2 networking in neutron and it uses multiple frameworks but we can use only 1 of them at a time.
this is installed on the controller and has its agents placed on the controller and compute machines.
##### ML2 Plugin
the default layer 2 core plugin for neutron, it can use multiple type drivers (networking backends) and each of them has their own agent that will be installed on their worker nodes
###### Drivers, their supported L2 features and agents
| driver | Flat | vLan | vxLan | GRE | Layer 2 Agent | Available Service Plugins Agents |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Open vSwitch | 1 | 1 | 1 | 1 | OVS Agent | L3, DHCP, Metadata, L3 Metering |
| Linux Bridge | 1 | 1 | 1 | 0 | Linux Bridge Agent | L3, DHCP, Metadata, L3 Metering |
| SRIOV | 1 | 1 | 0 | 0 | SRIOV Nic Switch Agent | None |
| MacVTap | 1 | 1 | 0 | 0 | MacVTap agent | None |
| L2 Population | 0 | 0 | 1 | 1 | Open vSwitch Agent / Linux bridge Agent | None |
###### Agent placement on devices
| Node      | Compute Node    | Network Node  | Controller Node      |
| --------- | --------------- | ------------- | -------------------- |
| **Installed Agents** | **OVS Plugin ** | **OVS, L3, DHCP** | **Neutron Server & ML2 Plugin** |
The Controller node will have the Neutron-API, ML2 Plugin and Router.
The Network and Compute Nodes will have the L2 Agents, in this case we'll be using Linux Bridge Agent.
and depending on this L2 Agent support for L3 services it may also install the following agents alongside it (depending on our configuration):
- L3 Agent
- Metadata
- Metering
- DHCP
Neutron API call steps:
1) user makes a request (create a new subnet, security group, etc... )
2) 2)request is sent to the `Neutron API`
3) `Neutron API` contacts the `Keystone API` to check for authorization
4) `Neutron API` sends the request to the Neutron Server to execute it
5) Neutron Server processes the request and starts calculating which of its services / agents to contact
6) for example, Neutron Server sends to the ML2 plugin to fulfill the user request.(create subnet, security group, etc...)
##### Network Protocols Explaination:
- Flat Network: 
	connecting all networks to the same network segment without any vLans or segmentation, everyone and everything is on the same network
- vLan Network:
	The use of vLan protocol on the virtual network to isolate its devices in their own segments.
- vxLan(Virtual Extensible Lan) Network:
	The use of vxLan tunneling protocol on the virtual network to extend the available number of vLans when using them to isolate the network devices in their own segments
- GRE (Generic Routing Encapsulation) Network: 
	The use of GRE tunneling to transfer layer 2 packets of a segment through the layer 3 network to isolate your virtualized network environment.
depending on your layer 2 implementation, you will be able to use service specific plugins from layer 2 agents, both Open vSwitch and Linux Bridge Agents have Layer 2 and 3 agents, DHCP, Metadata and L3 Metering.
##### Cloud-init
This is a tool created to allow the cloud to run specific scripts on VM creation, after the VM is made, `cloud-init` runs these scripts on the VM.
in this case, it takes all the user data /metadata (example: ssh keys) and places them on the VM.
#### Service Plugin
This is the plugin responsible for controlling layer 3, advanced features and providing services for that layer (firewall as a service)
