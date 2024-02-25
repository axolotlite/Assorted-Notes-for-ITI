we can promote /demote workers in managers using:
`docker node promote node_name`
`docker node demote node_name`
we should have multiple manager nodes in case one fails.
however there will be only one leader node.
docker uses RAFT algo, to find out who will be the leader among the managers.

we can inspect it using
`docker node inspect node_name`

there can only be one leader for the manager nodes.

we can update availability of a node using

`docker node update --availability STATUS node_name`
STATUS can be: available, pause, drain
we can use the drain to update each node in a cluster individually to prevent application downtime.
if we want to delete a node, we must first drain it. then run this command:
`docker swarm leave`

running an app on a cluster if replicas are not specified it starts only 1.
`docker service create --replicas=3 httpd`

we can see the info of a service using this command.
`docker service inspect service_name `

we can delete a service using:
`docker service rm service_name`

we can change the number of replicas of a serive using
`docker service update --replicas=new_number <parameters> image_name`

## rolling update
the following command can do a rolling update
`docker service update <parameters> --image=new_image:tag image_name`
we can change the delay between updating instances using `--update-delay time` parameter
`docker service update <parameters> --update-delay --image=new_image:tag image_name`
there is also a parameter that controlls how many containers are updated at a single time it's called `--update-parallelism number`
`docker service update <parameters> --update-parallelism number --image=new_image:tag image_name`
if an replica update fails, you can specify what happens. but by default it pauses the update:
`--update-failure-action pause|continue|rollback`

## rollback
if we want to go back to an older version.
`docker service update --rollback service_name`

global services don't need replica count, because it always deploys a single instance of an app on all clusters.
`docker service create --mode=global agent`
this service is usually used for deploying monitoring and deploying agents.

## Placement strategies using labels and constraints
we can label nodes using key value format in parameter `--label` on nodes:
key: type, value: cpu/mem-optimized/gp
`docker node update --label-add type=cpu-optimized node_name`
`docker node update --label-add type=memory-optimized node_name`
`docker node update --label-add type=gp node_name`

we can put contraints on an app using  `--constraint=JSONPATH`
`docker service --constraint=node.labels.type==cpu-optimized app_name`
we can specify that it shouldn't be put on a specific node using:
`docker service --constraint=node.labels.type!=cpu-optimized app_name`


### mounting files using swarm
we cannot bind files/directories using the same way as base docker, we must ensure that the file is available on all dockerhosts or on the nodes where this is to run.
`docker service create --replicas=4 -v src_file:/dst_location image_name`
this fails on any device where `src_file` doesn't exist.

so we'll use docker configs
`docker config create config_name config_location`
this object can then be called with swarm
`docker service create --replicas=4 --config config_name image_name`
we can specify the path in the command using
`docker service create --replicas=4 --config src=file_name,target="/dst/on/container" image_name`
we can remove the config using parameter `--config-rm config_name`:
`docker service update --config-rm config_name image_name`

then we can delete the config entirely:
`docker config rm config_name`

we can rotate configs by creating a new config then updating the service:
`docker service update --config-rm old_config_name --config-add new_config_name image_name`

### stacks
we can deploy docker-compose files using
`docker stack deploy --compose-file docker-compose.yml`
however, we must note that there are swarm specific compose parameters like replicas and constraints.
