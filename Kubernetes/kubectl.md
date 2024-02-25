#kubernetes/commands 
list all pods in the default namespace:
`kubectl get pods -n default`
alternatively we can get services in a specific namespace using:
`-n namespace`

we can delete a pod through:
`kubectl delete pod_name`
we can delete a pod using its defintion file through:
`kubectl delete -f pod-definition.yml`

we can create a pod using:
`kubectl apply -f pod-defintion.yaml`
`kubectl create -f pod-defintion.yaml`

we can see all running replication controllers using:
`kubectl get replicationcontroller`

we can rollback anything using:
`kubectl rollout undo object_type/object_name`

we can check the history of a command using:
`kubectl rollout history object.something/name`

this can tell us about the object.
`kubectl describe object_name`

this can edit the object using kubernetes:
`kubectl edit object_name`

we can expose a port for a pod using:
`kubectl expose po pod_name --port port_number --type NodePort`
this port should now be accessible using a browser.

we can create a new kubernetes namespace using:
`kubectl create namespace <your-namespace-name>`

we can add a label to any object using
`kubectl label object object_name label_key=label_value`

parameters:
`--record` records the command in the rollout history.
