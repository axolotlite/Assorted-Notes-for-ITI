#docker/flags 
#docker/commands 
containers are meant to run a specific task to process, unlike vms.
once they finish their task, they will exit.

they share the kernel of the host. all their processes is run on the host given their own namespace, this doesn't allow it to see any processes outside the containers namespace. 
but the docker host can see all the processes inside the container namespace.

a container only lives if the process inside is alive.
once it stops of crashes, the contaienr itself dies.

if we download an ubuntu image and run it through
`docker container run ubuntu`
it'll start and exit immediatly, you can use it to create other specialized containers.
creating a container creates a directory inside the docker containers diretory
`/var/lib/docker/containers/`

pausing / unpausing using "freezer cgroup" to pause and unpause container without notifying the containers that they've been paused.

every container gets an internalized ip address only accessible within the docker host.
you can access it using curl within the docker network.
to access it from outside the network we'll need to map the port to the docker host using `-p` parameter

we can limit application network access in containers. to prevent access in unwanted networks.
## namespaces
linux boots with 1 process, called the boot process. it starts all other process after it.
this can be seen by using ps.
each process id is unique. 
if we create a container, we need to give it an illusion of it being an independant system. to do that we have to give it its own namespace.
using namespacing, we can give each process multiple process ids, one for the actual host running it and another inside the container namespace, this id is only visible inside the container. 
this allows the container to think it's independent.
## process scheduler
docker supports Realtime schedule. which is not the deafult for linux.
CFS give every container 1024 share by default.
we can change that by using the parameter `--cpu-shares=512`
ex: `docker container run --cpu-shares=512 app_name`
this defines how the total amount of cpu is shared, this doesn't limit the actual usage of the cpu.
we can do this by selecting which container uses which cpu and cores with the flag `--cpuset-cpus=lower_range-upper_range` both these are between 0 and the maximum number of cores.
ex: `docker container run --cpuset-cpus=0-1 app_name`

another newer way to do so, is using the parameter `--cpus=2.5` this means that the container can use 2.5/n_cores. this is a hard limit that prevents the container from going throug the limit
this can also be applied to running containers through the update command
`docker container update --cpus=0.5`
once these limits are surpassed, the container will be throttled.
unlike
### memory
There is no restriction on container memory use.
we can limit it through `--memory=512m` parameter, which gives a hard limit on the memory usage of a container.
you can also give it swap using `--memory-swap=512m` which gives both memory and swap the size specified in the memory parameter.
we can specify unlimited swap using `--memory-swap=-1`
further explaination:
`--memory=512m` and `--memory-swap=512m`  means swap = mem_swap(512)  - memory(512)= 0
`--memory=512m` and `--memory-swap=768m`  means swap = mem_swap(768) - memory(512) = 256
the paramter `--memory-reservation=100m` adds a range between the define memory - the reservation.

if the container tries to exceed the assigned hardlimit, the container is killed with the OOM exception.
The dockerfile expose parameter allows us to automatically specify which ports to expose on the host using `-P`, of course we can add more mores to expose using the `--expose=port` parameter

each container is  made of layers, we can view these layer commits using
`docker iamge history image_name`
this shows us all the layers creating an image and all the commands used to create each layer, without the dockerfile creating the layer.

alternatively we can use
`docker image inspect image_name`
which returns a json output displaying all info of an image.
we can filter is using json path: `-f {{jsonPath_expr}}`

we can even create a new image from the current existing container:
`docker container commit -a "auther_name" container_name new_image_name`
we can add a `-c 'CMD ["commands"]'` parameter to change the cmd of the container
`docker container commit -a "auther_name" -c 'CMD ["commands"]' container_name new_image_name`