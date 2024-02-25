#docker/networking 
first step:
install docker on several machines.
`docker system info`
can see if swarm is active or not
we open these ports:
| port         | Description                       |
| ------------ | --------------------------------- |
| TCP 2377     | Cluster Management Communications |
| TCP/UDP 7946 | Communications among nodes        |
| UDP 4789     | Overlay network traffic                                  |
now we initialize the docker swarm on the master node using:
`docker swarm init`

we can find the command to run on the worker nodes through 
`docker system info`
`docker swam join-token worker`

we run the given commands on the worker nodes.

we can see all availabe worker nodes using, it'll specify the current node using '\*'
`docker node ls`

AVAILABILITY:
- Active: assign tasks to node
- Pause: do not assign new task to node, but leave existing task
- Drain: do not assign new task to node, and reassign existing task
