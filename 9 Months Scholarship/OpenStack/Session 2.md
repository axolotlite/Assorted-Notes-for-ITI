
Networking inside OpenStack
neutron is responsible for managing the network, it creates networks, switches and routers.
now, we create an internal network using the subnet `192.168.10.0/24` then another network `10.10.10.0/24` which is not connected to the internal router / switch.
now any vm in either of those won't be able to communicate without having their subnets connected.

there is also another method of connection called `external network` that is accessible from outside of the network.
this is why we create two NICs, so that one works for the host itself and another is used as a gateway for the internal networks.

neutron uses agents for layer 2 and layer 3 emulation, this happens on linux native networks through namespacing.
The admin is responsible for creating the External Network gateway (Public Network Provider External).

floating ip (public ip):
this is an ip given to a VM from the external network, which allows it to communicate with external networks and anyone on the internet to reach it.
answerfile:
this file contains all the configuration of openstack for use in packstack installation.
we can create it using:
`packstack --gen-answer-file=answer.txt`
there are many parameters we can use

and then apply the created answerfile:
`openstack --answer-file=answer.txt`

#### after installation completion
##### Keystonerc_admin
in the home directory of the root / user that installed openstack. 
a new file `keystonerc_admin` belonging to keystone should've been created.
this file is a bash source file that contains the credentials, we use `source keystonerc_admin` to load those variables into the current shell to allow us to use `openstack-cli`

#### Creating a Public Network Provider
to allow access to the external network / internet, we as the cloud providers we must create a Public Network Gateway to allow the internal networks to reach the internet.
This cannot be done through the GUI. however, we can do this through the `openstack-cli`
##### Creating a Virtual Cloud
for a customer to create his own vms in his private cloud, they must first prepare a private network (through GUI), create a route between this network and the external gateway / net, the specify the flavor of their VM.

### commands of interest:
`openstack server list` : lists all running virtual machines.
##### creating an external network through the cli
`neutron net-create network_name --provider:network_type flat --prodiver:physical_network extnet --router:external`
- `--provider:network_type`: 
- `--provider:physical_network`:
- `--router:external`:
##### Creating a subnet
`neutron subnet-create subnet_name --enable_dhcp=False --allocation-pool start=first_address,end=last_address --gateway=gateway_ip external_network_name your_network_cidr`
- `--enable_dhcp=False`:
- `--allocation-pool start=first_address,end=last_address`:
- `--gateway=gateway_ip`:

### Affinity vs Anti-Affinity Policies
when creating a collection of vms having affinity to a host means these vms will all be created on the same host.
anti-affinity will make those vms be created on different hosts with no specific attachment to a single host.
Nova is responsible for this.
