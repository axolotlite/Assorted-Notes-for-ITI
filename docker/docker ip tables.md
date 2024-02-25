#docker/commands 
#docker/networking 
port mapping in docker relies on ip tables of the host kernel.

Docker relies on the kernels IP table to manage network communications.
Ip tables have different chain of rules
input -> forward -> ouput

docker creates its own chain:
docker-user -> docker

this chain contains all rules created by docker, we can see them using

`iptables -t nat -S DOCKER`
this lists all the rules used by docker to map ports.