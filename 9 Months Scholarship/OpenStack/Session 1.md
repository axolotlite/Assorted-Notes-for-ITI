What's the difference between AWS and OpenStack?
AWS is a pre-prepared service set up by amazon that allows users to provision the resources for a fee.
openstack is set up by an organization or a company that allows them or their targets to provision resources.

What is a private cloud?
on premise, we have our own datacenter with our hardware and we setup the services
collocation, we buy hardware off premise, on another organizations datacenter and we setup these services.
###### The answer wanted in an interview:
The resources provided by the cloud are only provisioned by your organization and its people.

What is cloud computing?
it's the ability to self-service and self-provision resources from the pool of resources provided through the internet / network.

what is the difference between cloud computing and virtualization?
cloud computing usually has a web portal that allows you to provision resources, virtualization is a technology that allows you to virtualize resources.
virtualization allowed the creation of the cloud.

What is a hypervisor?
it is a layer existing between the kernel and the host that allows us to virtualize hardware on top of the physical hardware.

what is the difference between scale up and scale out?
scale up (vertical): we increase the resources(vCPU cores, RAM, Storage) allocated to a server, 
scale out(horizontal): we increase the number of servers providing a service, increasing the number of servers.

What is the meaning of open source?
the code is open for review, modification and distribution.

what do you know about API's ?
They are 

What is the difference between authentication and authorization?
authentication allows you to enter a system
authorization specifies what you can do inside the system

What do you imagine about openstack?
it's a software that allows us to build a cloud solution, whether it is public or private.
it is a collection of packages that can be configured into making a cloud.
it first was created in 2010 by two companies (RackSpace and NASA) wanting an open source alternative to AWS cloud.

#### What is open stack?
it's an open source software that allows creation of cloud solutions (private or public).
after it's installed, it manages pools of servers, network devices, storage and allows us to self-serve resources from these pools without any middle-men, through the dashboard and API.
openstack has integration is many open and proprietary technologies, allowing it to be compatible with almost everything.
The goal of openstack is to allow the creation and scaling of a cloud, regardless of the available pool of resources available, as quick and easy as possible.

### Components of OpenStack:
each component is responsible for a specific job, and managed by its own team.
however, there are some basic services that must exist to allow the creation of a cloud.
The components allow the creation of the infrastructure.
#### NOVA (Compute Layer) (main)
it's responsible for self-serving compute
#### KeyStone (identity authenticatoin) (main)
you cannot have self-service and provisioning without having authentication and authorization for who can and can't provision what.
it's also responsible for managing internal services too.
#### Neutron (Networking) (main)
This is the component responsible for managing the network, who can access what and where.
#### Glance (Image Management) (main)
it's responsible for carrying the images from which the virtual machines are spun.
#### Cinder (Block Storage)
Nova has it's own storage provisioning tool, so Cinder is not a main component. however, Nova provisions storage from the same node that creates the VM.
unlike Cinder which allows us to provision block storage from a wide array of storage boxes.
#### Swift (Object storage)
allows us to push files as objects with their own metadata to the cloud object storage.
#### Horizon (Dashboard / UI)
you use this to access and manage the openstack through a web interface.
#### Heat (Orchestration)
this allows for templating of VMs and then application of them at any number with the same specifications across all the specified virtual machines.
this is life cloudformation, and can be substituted by terraform.
#### Ceilometer (telemetry)
this one tracks which users use which resources and for how long.
it keeps track of all these metrics.
#### Trove (Database as a service)
this lets you provision a database and use it.

BMS (Bare metal server): a server that doesnt have a hypervisor, you can use it as it is or install a hypervisor on it.
dedicated host: a bare metal server that comes with a pre-installed hypervisor, allowing you to create virtual machines on it.

Ceph Storage Solution provides the 3 types of storage (block, object and file).

#### Communication between openstack elements
first, when you open the portal to access the UI (horizon), you enter your username and password  to authenticate (keystone).
now, you're authorized to use your openstack services.
now to create a virtual machine(Nova), you'll need an image (Glance), so Nova will ask Glance for an image to install, and an IP (neutron) to give it.
if you want to add a block storage (cinder), you can add it during or after VM creation (Nova)
#### The benefits of OpenStack
opensource means modificatoin and updates, according ot the commmunity
horizontal scale out by adding machines
illusion of finite reasources. you use thin provisioning to tell the gues that they can provision anything, you will have to setup monitoring to prevent it actually using all the real resources.
Rapid Provisioning: quickly create resourcs.
Open Source: you're allowed to modify and customize the code base to suit your needs.
modular: each component has its own API, allowing us to use any of the components without the other.

### Inside every component:
consists of 3 main parts: API, Backend and a System service with the configuration.

#### Common Concepts
##### Messaging queue:
a queue that manages requests sent through the API's, it prioritizes and sends these requests according to an AMQP(Advanced messaging queue Protocol), they use RabbitMQ server to manage the queue and a database server to keep track of all the messages.
##### Token
once you login to your user, keystone will give you a token that will allow you to interact with the environment, this token is given to any component that will check your authorization by asking keystone if the user of this token can do what it asks of it or not, without having to reuse your password.
##### Domain / Tenant
these two means the organization or customer that has access to these resources, you can add a specific amount of of users within this domain according to the cloud provider.
##### Projects
this is the authorization / configuration of a user inside a project, meaning a user can be an admin in one project and a normal user in another.
for example you have ahmed and ali.
there are 3 projects: X, Y, Z
ahmed is an admin on X, user on Y but can't access Z.
ali is an admin on Z but he can't access either X or Y.
##### Role
a role is a credentials template for a user, it specifies which resources / services are accessible, to what degree.

### OpenStack Deployment:
RDO (redhat distribution of Openstack) the one we'll use, it's made for testing and learning.
Packstack this deploys openstack components on pre-installed servers, this is also for testing.
OOO (Openstack on Openstack) it allows you to create a production ready openstack environment.
