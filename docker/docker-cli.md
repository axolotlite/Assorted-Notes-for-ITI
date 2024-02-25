\#docker/commands
#docker/direcotries
#docker/flags
its the cli commands used to control docker
it craetes a directory in `/var/lib/docker`
commands should be run before the image name.
`docker container run "commands" image_name`

inside it you'll find object related directory, for each object.
inside each you'll find its corresponding data.
basic commands
`docker image ls`
`docker container ls` ,  `-a` , `-l`  
list relevant data to the containers. 
`-a` flags list all info. 
`-l` gets the last created container
`-q` gets the container id of all running containers
`-qa` gets all containers wether started, stopped or not running
`docker networks ls`
`docker volumes ls`
This grouping is relatively new. (container, image, container ) the old commands didn't add this grouping.
`docker container run -it image`
`docker image build .`
`docker container attach container_name`
`docker container kill container_name`

`docker container create container_name`
this creates a container based on the specified image without running it, if it doesn't exist it'll be pulled from dockerhub, it'll give it a unique id and and will display the shortform of the container id.

`docker container start container_name/id`
this can start a container or creates then starts it.

we can provide a teriminal to a started container by using `-t` flag to the run, the `-i` flag makes it interactive.
`docker container run -it ubuntu`
this will start an interactive terminal into ubuntu container.
`--name` flag allows us to create a custom name for the container.
`docker container rename original_container_name new_name` allows us to rename existin containers.

adding `-d` flag allows us to detach the container from the terminal.
you can reattach by running `docker container attach container_name/id`


we can execute commands inside a running container using the `exec` command
`docker container exec container_name/id "command"`

to get an active shell inside the container without attaching we can run
`docker container exec -it container_name/id /bin/shell`


inspecting running containers cna be done through:
`docker container inspect container_name/id`
this returns all data related to docker container

alternatively you can use container stats
`docker container stats`
this will show the container stats and their configs.
to list a single container stats we could use:
`docker container top container_name/id`

to show the logs of a container we can use:
`docker container logs container_name/id`
adding the `-f` flag allows us to stream the logs live.

`docker system events --since time`
this shows all the system events related to docker.

docker allows similar signals to the OS.
we can pause containers by
`docker container pause container_name`
continue the container by
`docker container unpause container_name`
and we can stop a container through
`docker container stop container_name`
which will forcably kill the container if it refuses to stop.

pausing / unpausing using "freezer cgroup" to pause and unpause container without notifying the containers that they've been paused.

we can remove a container using the `rm` command, as long as it's stopped.
`docker container rm container_name/id`
removing the container deletes its corresponding location from docker directory.

we can stop all container through:
`docker container stop $(docker container ls -q)`
using the same approach we can delete them
`docker container rm $(docker container ls -q)`

another option that can delete all stopped containers is:
`docker container prune`

we can make containers automatically remvoe themselves once they finish their execution
`docker container run --rm container_name "command"`

`docker container run --hostname=name image`
allows us to set the hostname of the container for use in docker networking.

restarting container on different modes, options can be found in [[exit codes]]
`docker container run --restart=option image`

we can map port from host to container using:
`docker container run -p internal_port:external_host_port image_name/id`
we can limit who can access it by specifying an ip or an ip range
`docker container run -p ip_address:internal_port:external_host_port image_name/id`

we can automatically make all used ports on the container available to the host using `-P` flag
`docker run -P image_name/id`
this publishes all ports exposed in the dockerfile used to create the image.

we can search for images using
`docker search image_name`
this prints the first 25 results by limit, we can change the limit between 1 and 100
`docker search image_name --limit n`
we can set the lower limit of stars on a repo using `--filter starts=n` and even select only official sources.
`docker search --filter stars=n is-official=true image_name --limit n`

we can then pull an image using 
`docker image pull image_name/id`

we can add a tag to a downloaded image:
`dockeri mage tag old_image_name:old_image-tag old_image_name:new_image_tag`

we can convert images to tar files, for easier transfer.
`docker iamge save image_name:tag -o image_name.tar`
then we can import it on the next terminal using
`docker image load -i image_name.tar`

we can do the same to containers:
`docker export container_name > container_name.tar`
we can import it as an image through:
`docker image import container_name.tar image_name:tags`

running a container on a specific network:
`docker run image_name --network=network_name`

