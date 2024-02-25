#docker/commands 
#docker/direcotries 
docker supports different logging mechanisms using logging drivers.
the default logging driver can be found through the `docker system info` which is usually json-file.
these logs can found inside the `/var/lib/docker/container_id` directory stored as a json object.
you coud disable logging drivers.
you can access the logs of the container by running:
`docker logs container_id/name`
you can listen for any upcomming logs by using:
`docker logs -f container_id/name`

these logs is stored according to the logging driver,  which can be changed using the `/etc/docker/daemon.json` refer to [[dockerd daemon]]

you can determine the specific logging driver for a newly run container using the optinos are available in [[dockerd daemon]]
`docker run -d --log-driver option image-name/id`

