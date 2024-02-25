docker swarm can combine multiple machines together into a single cluster.
it's responsible for distributing the containers across each host alongside load balancing.

the swarm consists of at least one manager node and multiple worker nodes.
the manager sends instructions to the worker nodes
managers can be configured not to do anything other than management.
they're responisible for managing the structure.

manager creates tasks and assigns them to other workers.

docker has the swarm features embedded inside of it.
each host can be configured as a manager or a worker, you can even modify any of the two to become the other.

we can create them using declaritive language in a service-definition.yml file.

we can scale up or down instances of our application accross all the worker nodes.

we can even roll back to previous verions of our deployment.

if an application crashes a new instance is spun in its place.

the applications are accessible on any other node in the same cluster.

we can use an external load balancer to distribute traffic through the nodes.

the host has a dns server which allows all services to discover eachother.

under the docker-cli commands there are:
API: which sends the commands to the docker daemon
Orchestrator: creates tasks 
Allocator: gives ip addresses to the task
Dispatcher: assigns tasks to node
Scheduler: instructs a worker node to do the task