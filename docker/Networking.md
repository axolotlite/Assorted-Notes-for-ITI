#docker/networking 
#docker/commands 
when we install docker 3 networks are created by default:
### Bridge: the default network the container is attached to.
it gives an internal ip in the range of 172.17.0.0/16
### Node: no access to any network
they're completely isolated and are incapable of connected or communicating with other containers.
### Host: this is the host network
there is no isolation between the docker container and the host network, meaning we won't need to port map, because the container is accessible from the network.
this means we can map ports, because the ports are now unique on your device.

we can create our own network using
`docker network create <parameters> network_name`
with these parameters:
`--driver bridge` specifying the network driver which determines ho to connect to it and other things
`--subnet xxx.xxx.xxx.xxx/X` which determines the range of ips available for the networks

containers can reach eachother on the same network using their container names, or using the internal ip addresses assigned on container creation which is ill adviced.

in podman the default network is reserved for root.
so, in order to use networking we'll have to create a new network
`podman create network_name`
then whenever we want a container to belong to said network, we append `--network netwod_name` to its run command
podman and docker have different approach to networking.
docker can link created containers with a specific name.
`docker run --link "other_container_name:name_in_hosts" container:version`
but podman has the name reserved in the other container
`podman run --network network_name --network-alias name_in_hosts container:version`

we can connect a container to multiple networks using :
`docker network connect custom_network container_name`
and disconnect it using:
`docker network disconnect custom_network container_name`