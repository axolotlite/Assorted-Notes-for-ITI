#docker/networking 
after initializing docker swarm, a new network of type overlay.
it's an internal private network spanning across all notes participating in the cluster.
it allows every container in the cluster to communite with eachother

### Ingress network:
when a swarm is created it automatically creates an ingress network with a load balancer.
it redirects traffic from the published ports on the host.

### bridge network:
this network connects the individual docker daemons in the swarm.

we can create an overlay network:
`docker network create --driver overlay network_overlay_name`
adding these flags:
`--subnet xxx.xxx.xxx.xxx/x` :specify subnet
`--attachable` :allows standalone containers to be run inside this overlay network
`--opt encrypted` :encrypt application data alongside swarm communication

we can then attach to a custom overlay network using
`docker service create --network overlay_network_name service_name`

do delete a network
`docker networm rm overlay_network_name`