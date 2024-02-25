#docker/flags
#docker/direcotries 
#docker/env 
once it starts , it listens on an internal unix socket at /var/run/docker.sock
a unix socket is an IPC used for communication between different processes on the same host. meaning it's only accessible within the same host, it allows the docker daemon to communicate through this socket.

if the docker daemon goes down, it'll shut down all containers, you can configure it not to do this. through "live restore" which can be added to the config file

by default you cannot allow external access to this socket, you can add a `--host` flag while running the dockerd to allow external access through the network
this makes the dockerd accessible through the network through the given ip after setting up a environmental variable called `DOCKER_HOST`

there is no encryption or authentication required by default on using the host flag.
you'll need to configure the security on your own, by creating a cert and a key, then adding the following flags:
`--tls==true`
`--tlscert==/var/docker/server.pem`
`--tlskey==/var/docker/serverkey.pem`
note, the port `2376` is used for encrypted traffic. unlike the default port `2375`
alternatively you could use an environmental variable `DOCKER_TLS=true`
alternatively, if you want to use certs to ensure only those with the key can access it, we'll use `DOCKER_TLS_VERIFY=true` env variable or `tlsverify=true` and `tlscacert=cert_location` options in the json configs
these options can be moved to config file in `/etc/docker/daemon.json`
example config file:
```json
{
	"debug": true,
	"host": ["tcp://ip-address:port"],
	"tls": true,
	"tlscert": "/var/docker/server.pem",
	"tlskey":"/var/docker/serverkey.pem",
	"tlsverify": true,
	"tlscacert":"/var/docker/caserver.pem",
	"live-restore": true,
	"log-driver": "json-file"
}
```
available logging drivers, each with their own specific configs
- none
- local
- json-file
- syslog
- journald
- gelf
- fluentd
- awslogs
- splunk
- etwlogs
- gcplogs
- logentries
after creating this you'll meet issues if you run the flags differently.

## podman equivalent
if you're using podman there are several ways to emulate the docker api using podman
https://docs.podman.io/en/latest/markdown/podman-system-service.1.html
### systemd:
`systemctl --user start podman.socket`
where the socket file will be located at:
/run/user/1000/podman/podman.sock
### cli:
`podman system service --time=0 unix://temp/podman.sock`