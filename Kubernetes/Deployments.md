#kubernetes/yaml 
You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

it allows us to upgrade the underlying instances using rolling updates.
the yaml file looks exactly like a replica set, but the only difference is in the Kind

if we do not specify a strategy in the deployment file it'll use rolling update
we can run it using:
`kubectl create -f deployment-definition.yml`
```yml
apiVersion: apps/v1
kind: Deployment
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

we can check the currently running deployments using:
`kubectl get deployments`

if we modify the deployment-definition.yml, it'll trigger a deployment. by default it'll use rolling update
`kubectl apply -f deployment-definition.yml`

we can rollback this deployment using:
`kubectl rollout undo deployment/deplyment_name`