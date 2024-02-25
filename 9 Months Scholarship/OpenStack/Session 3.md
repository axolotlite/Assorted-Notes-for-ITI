Before manually installing openstack we must first install some pre-prerequisites, which are:
- DBServer: for all the components
- NTP: we'll use chrony as an NTP server
- MQ (massaging queue): we'll use rabbitMQ
- memcache (caches authentication tokens)
- etcd (json key value store)
These components will have to be installed on a controller or distributed on a group of controllers.

#### Controller Nodes:
the controller nodes should have the management components:
- keystone: for authentication
- glance: for hosting the images for the compute
- neutron: for networking
- horizon: dashboard to control everything else
however, we can create a dedicated server to host neutron to scale out our network.
#### Compute Nodes:
the compute nodes must have a hypervisor

#### All in one Installation
because we don't have enough PCs to install each of these components on their respective host, we'll do an all-in-one installation on a single host.
however, in an actual environment the components are distributed across different hosts with redundancy to allow for high-availability.

#### 