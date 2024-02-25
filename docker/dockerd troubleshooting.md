#docker/env
#docker/commands 

`docker ps` returns cannot connect when:
if remotely: check the `DOCKER_HOST` env variable to check if you've connected corretly
if not remotly: chec status of dockerd service using `systemctl status dockerd`

then we can check the logs using
`journalctl -u docker.service`

we can check if there is a misconfiguration problem in `/etc/docker/daemon.json`
then we can enable the debug flag to show more info refer to [[dockerd daemon]]

also check if there is still disk space, if it's full. the service will crash. this can be fixed through pruning.

if the service is up, we can check its info through `docker system info`

we can see the actual weight docker images take by using:
`docker system df`
reclaimable column: targets images that are not used by containers.