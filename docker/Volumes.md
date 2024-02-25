We can create docker volumes to share date either from the host to the container
or from container to container
They can be created using
`docker volume create volume_name`
You can list all available volumes using
`docker volume ls`
You can inspect them using
`docker volume inspect volume_name`
then delete them using 
`docker volume rm volume_name`

remove unused volumes:
`docker volume prune`

Volume mounting can be done using
`docker run -it -v volume_name:mount_location image_name:version`

we can mount read-only volumes using:
docker container run --mount source=source_location,destination=destination_location,readonly