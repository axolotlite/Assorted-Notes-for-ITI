kubernetes can scale infrastructure up and down based on userload, it can update it in a rolling fashion, if it fails it'll roll back.
it can allow different methods of deployment.
it's open architecture allows many different network and storage plugins, it supports many authentication methods.

it has suppport in every major CSP.

a kubernetes cluster consists of several nodes.

node is a worker machine were containers can be launched.

if a node fails in a cluster, you can have several other nodes take its load.

the nodes in a cluster is controlled by a master node.
the master node is responsible for orchestration of containers on the node

installing kubernetes installs:
- api server: the front end for kubernetes
- etcd: a distributed key value store used to store all data related to the cluster
- kubelet: it's an agent that runs on each node in a cluster
- container runtime: the underlying software used to run containers
- controller: they notice and respond to node failure
- scheduler: it schedules work for containers, it creates containers then assings them to nodes

kubectl: the command line utility for kubernetes. it can deploy and manage application on a k8s cluster.

`kubectl run` to run commands
`kubectl cluster-info` to display k8s info
`kubectl get nodes` gets info of the current node

