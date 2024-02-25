information is extracted from data for use in business, it's an enhancement of data.
data is unsorted knowledge.

data can be:
- structured: like databases.
- semi-structured: has a non uniform pattern like xml files, structured language with unique query.
- quasi-structured: info can be queried by patterns but it's even less uniform than semi-structured data, like logs, most unstructured data but with enough patterns to allow a person with enough knowledge to handle it.
- 

### volatile vs non-volatile storage:
ram vs hard disk, one loses data once it loses power, the other keeps the data regardless of power.

### To build a data centers:
depending on the budget, it would be better to build your datacenter in already established datacenter or just use the cloud.

### Data Integrity:
checking the data to ensure it wasn't damaged, corrupted or changed without permission.
this can be done through checksums
### Availability:
your ability to access the data anytime you need, without anything stopping you or preventing rightful access.

### Security:
physical: by having secrity personnel prevent unlawful or unrestricted access to the datacenter premise
software: prevent any access to the data through the internet without authorized access, this can be done through WAF firewalls, which work on layer 7.

### Performance:
ensuring the best performance of the data center components through the equipment or buying high end hardware.

### Scalability:
The ability to accommodate any newly bought racks or servers to expand the data center components, basically having enough place to buy and place new racks.
### Capacity:
How many servers are needed to run an application, and then how much compute will the app require or what kind of hardware will it require.
capacity is having the availability to run an app, while scalability is the ability to expand the hardware to meet the increasing demand of the apps.

## The Cloud
It's the ability to provision the infrastructure or resources of another company through the internet.

### What are the charactaristic of a cloud service:
- measured service: the metering of used resources / components.
- resource pooling: the ability to share a single resource across multiple devices / data centers with multiple clients.
- rapid elasticity: the ability to accommodate the customers need through increased provisioning / releasing of reserved resources / components.
- on demand self-service: the ability of the customer to provision resources through automated portals, without any human approval for resource provisioning.
- broad network access: the accessibility of the data through the internet, basically the cloud is online.

### As a service:
The physical components are managed by the provider, they're responsible for keeping it up and working without any issue while maintaining its operability.
- PAAS(platform as a service): the provider gives you a machine specifically configured to run an application, it has most of the required services pre-installed and you'll deploy your app on top of the machine with minimal configuration to the platform. You're responsible for your app and its integration with the platform.
- IAAS(infrastructure as a Service): you provision the network components, vms, storage devices and you're responsible for managing them and their accessibility, you're given free reign over your provisioned resources.
- SAAS(Software as a service): the provider will configure underlying infrastructure and software integration with it, you'll only use the service and the data produced from the service is yours. the app and infrastructure are owned by the provider.

### Deployment models:
- public cloud: these are privately owned infrastructure that allow for any third party provisioning of resources.
- private cloud: your own infrastructure with your own provisioning portal for your own use and (you) can be multiple owners!
- community cloud: a group of entities owning infrastructure, sharing access to it and its resources for people within this group.
- hybrid: a mixture of both public and private clouds, you have a could accessible only for specific owners and a subset of it accessible for everyone.
### multi-cloud:
the usage of multiple public cloud provider resources to host your infrastructure

## Traditional VS Modern DataCenters
### traditional data centers:
rely on baremetal installation of operating systems, which lock the resources on the server, this resources cannot be utilized, thus causing sub-optimal utilization of resources.
This means if an application requires more resources, you won't be able to scale the baremetal quickly and easily without downtime.

### modern data centers:
on the other hand uses virtualization to run resources ontop of VMs, this means a server can run several applications on a single server on different VMs, if the resource requirement increases, we can easily reduce the resources of other VMs on the machine while increasing the resources of the app VM.

### Clouds on the other hand:
may share the use of virtual machines for resource distribution but it needs the ability to provision resources without manual approval or intervention.

## The difference between rack mounting and blade system:
rack servers allow a pc to work as a single entity, each rack server is a PC working on its own to provide a service or for virtualization.
blade enclosures are placed inside a rack, it's usually larger than 8U and  are connected within a single NIC and SAN cables.
they have a single centralized ip for management, through it you can interact with the blade units inside.

### Filesystems
it's responsible fore defining the block size, which is responsible for maximum file size handling(copying)
Disk based:
ext, fat, ntfs

network based:
smb for windows
nfs for linux

virtual:
VMFS:it's a filesystem used in vsphere disks

## Hypervisors
there are two types:
- type 0: installed on baremetal, virtualizes hardware directly
- type 1: installed on an OS, competes for resources with the OS
a hypervisor has a virtual machine manager responsible for running the vm.

The two most famous desktop virtualization solutions are:
vmware horizon and Citrix, there is also Xen Desktop

## SAN
you consolidate all storage devices into dedicated storage boxes, these boxes can be scaled up(increasing the storage arrays in a box) or scale out (buying more boxes)
the storage disks are then placed in a pool that allows us to provision storage from them.
the transfer of block filesystems between a server / VM and a SAN(storage) server.
this occurs through an FC Switch, it encapsulates and decapsulates SAN traffic.

## Traditional Vs Modern Application
traditional application were monoliths, each application contains all the needed services to run it.
modern uses microservice architecture, seperating components in layers, to ensure that a failure in a layer doesn't affect another layer, allowing us to fix or replace components.

## SDDC (Software Defined Data Center)
it's equivalent to the virtualization layer, its basically a pre-configured layer that allows you to launch an app.
this layer is of course configured by you.
- SDC(software defined compute): This is responsible for virtualizing compute, for example VSphere.
- SDS(Software defined storage): this is as the name says responsible for storage
- SDN(Software defined network): yeah, network. virtualized networking.

### DIY Data center
there are two types:
- Green field: you don't have any infrastructure nor components, so you're starting from scratch
- Brown field: you already have some infrastructure, for example traditional data center and you want to update it to modern standard, so you start adding virtualization layers and components.

### Convergent vs Hyper Convergent
- convergent collects several components into a single component, basically has a drive installed.
- hyper convergent doesn't have a storage box, it has a single device with several disks that consolidates storage through SAN
