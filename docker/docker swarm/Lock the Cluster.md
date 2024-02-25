
we first run this command during intializing a cluster
`docker swam init --autolock=true`
or on an existing cluster
`docker swarm update --autolock=true`
this returns a key that we can use to lock the cluster.

if a node restarts or leaves the cluster, you'll need to provide the key you got through
`docker swarm unlock`

