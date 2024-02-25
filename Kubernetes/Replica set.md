#kubernetes/yaml 
It is used to monitor our pods and ensure they're replaced on failure. it is one of the kubernetes controllers.
The difference between replica set and replication controller is a selector, because replica set can manage pods created before the replica set.
if we skip the selecter, it assumes that it is the same as the one in the pod-defintion.yml
we can create it using:
`kubectl create -f replicaset-definition.yml`
```yml
apiVersion: v1
kind: ReplicationController
metadata:
	name: app_name
	labels:
		app: myapp
		type: front-end
spec:
	template:
		metadata:
			name: replicated_pod_name
			labels:
				app: myapp
				type: front-end
		spec:
			containers:
			- name: nginx-container
			  image: nginx
	replicas: number_of_replicas
	selector:
		matchLabels:
			type: front-end
```

we can scale the replica-set by either updating the number of replicas in the definition file, then running:
`kubectl replace -f replicaset-defintion.yml`
or
use this command
`kubectl scale --replicas=6 replicaset-defintion.yml`
or modify the current replica set
`kubectl scale --replicas=6 replicaset replica-set_name`