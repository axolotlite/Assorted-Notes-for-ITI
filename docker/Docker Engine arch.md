docker cli -> rest api -> docker daemon
docker daemon is responsible for creating and managing images and containers and everything related to them.
the rest acts as an intermediary between them.

lxc was used in the past to create isolated environments on linux called containers. it was hard for normal users, so they made a wrapper for it called docker.
at version 0.9 docker created their own alternative called lib-container to replace lxc, it's written in golang, like docker itself.

open container initiative in 2015 was formed by docker and coreos alongside other container oriented organizations
they created two specs: runtime and image specs
runtime: defines life cycles (create creates container, start starts, delete deletes container, etc...)
image: 

the docker demon was a single monolithic code base performaing multiple functions, after the OCI standards, docker engine architecture was refactored into fine grained components.
now runc is responsible for running the containers.
it's donated to open compute foundation, it's not dependent on docker.

daemon managing containers is now called containerd, it manages runc to create and run containers.
if the demon goes down, containerd-shim makes it daemonless, it monitors the state of the container even if containrd is shutdown.

