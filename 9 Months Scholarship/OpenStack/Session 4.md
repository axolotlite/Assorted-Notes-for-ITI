### components of NOVA
#### Nova api
it is used to control Nova, but first it must authenticate any user with keystone.
#### Nova Scheduler
when a request comes from the api, it determines the best place to place the VM on which compute host, according to its own algorithm.
It used to be responsible for keeping track of the node resources, to make optimal decisions about where to place vms.
Of course, those optimal decisions depend on your configuration files.
however, a new component was put in place to monitor resources across nodes, it's called Placement.
#### Nova Compute
it's a service present on the compute nodes, they receive commands from the `Nova Scheduler` to communicate with virtualization API, in this course it's libvert (kvm hypervisor API)
This is installed on all the virtualization hosts.
#### Nova Conductor:
It is responsible for dealing with the database, recording requests and transactions for Nova.
There is a main Nova DB in the control plane that has the metadata on all cells that belong to the cluster.
each of those cells will contain their own `Nova Conductors` that has the data, resource info and all metadata of all the worker nodes that belong to the cell and their virtualized guests.
#### Nova Cell
This service is responsible for communicating between the scheduler and the placement component, to help determine which cells are optimal for use.
each cell may contain multiple virtualization hosts, a single Nova-scheduler and Nova-Conductor managing those virtualization hosts and each cell will contain its own Cell Database to keep track of everything that happens in the cell.
#### nova-consoleauth & nova-novncproxy
these two allows us to enter the virtual machine's console through a console shell, you open a console session inside the VM to control it through.
this is not ssh.
#### Nova Cell 0
This is a specialized cell that is created to monitor and keep track of failures in the cluster.
its name is a derivative of the main `Nova Conductor` Database name:
- if `Nova Conductor` main DB is called `Nova`, Cell0 DB will be called `Nova_cell0`
- if `Nova Conductor` main DB is called `X`, Cell0 DB will be called `X_cell0`
### Placement component
this component is responsible for monitoring the resources and possible vm count, it distributes hosts into cells, each cell having a possible count of VMs, so that when Nova-Scheduler tries to set a VM on a cell, the placement components tells it of the available resources on a cell to ease its decision making.

