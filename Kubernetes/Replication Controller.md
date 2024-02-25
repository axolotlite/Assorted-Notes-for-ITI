#kubernetes/yaml 
replication controller is responsible for ensuring that a pod is replaced once it fails in accordance to the number of pods.

template section is used to provide a pod template for replication control to create replicas.
we can specify the number of replicas in the spec.replicas
then we can start it using
`kubectl create -f rc-definition.yml`

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
```

we can see all running replication controllers using:
`kubectl get replicationcontroller`
