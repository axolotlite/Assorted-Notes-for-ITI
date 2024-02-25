#docker/commands 
#docker/networking
we can copy files from host to container
`docker container cp host_relative_file_location container_name/id:container_relative_location`

we can copy files from container to host
`docker container cp container_name/id:container_relative_location host_relative_file_location`

the same can applied to directories:
`docker container cp container_name/id:container_relative_directory_location host_relative_file_location`

