#docker/commands
#docker/flags
`docker version`
shows version of docker and its data
`docker system info`
shows you runtime related data

`dockerd` , `dockerd --debug` , `dockerd --host=tcp://ip-address:port`
runs docker as a front command, it prints its logs onscreen.
debug flag adds more info to output.
adding a host flag allows you to access the socket through the network
the default port is 2375
you'll have to set the env variable `DOCKER_HOST="tcp://ip-address:port"` to access it from the client.
you can encrypt it through:
`dockerd --tls==true --tlscert==/var/docker/server.pem --tlskey==/var/docker/serverkey.pem`