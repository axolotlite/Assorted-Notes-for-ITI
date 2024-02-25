a small revision in virtualization

type 1 hypervisor:
the hypervisor is installed on the hardware, for example installing esxi on a server
type 2 hypervisor
the hypervisor is installed on the OS.

Hyper-V:
hyper V is a feature in windows, enabling it, will activate Hyper V which will turn your machine into a type 1 hypervisor.

VMWare has vCenter, which is a VM installed to manage your esxi hosts.
Hyper-v allows any component to become a controller (Hyper-V Manager), allowing us to control it through it.
there are two levels of features:
vm level:
	snapshot
	cloning
	migration
	templating
	fault tolerance
cluster level:
	high availability
	DRS
	EVC

Hypervisors are the main component of any virtualization technology that allows for hardware abstraction through software components.