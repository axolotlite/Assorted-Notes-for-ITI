#kubernetes/yaml 
first we create the pod definition:
voting-app-pod.yaml

```yml
apiVersion: v1
kind: Pod
metadata:
	name: voting-app-pod
	labels:
		name: voting-app-pod
		app: demo-voting-app
spec:
	containers:
	- name: voting-app
	  image: kodekloud/examplevotingapp_vote:v1
	  ports:
		  - containerPort: 80
```

then we create a result-app-pod:
```yml
apiVersion: v1
kind: Pod
metadata:
	name: result-app-pod
	labels:
		name: result-app-pod
		app: demo-voting-app
spec:
	containers:
	- name: result-app
	  image: kodekloud/examplevotingapp_result:v1
	  ports:
		  - containerPort: 80
```

then the redis: redis-pod.yaml
```yml
apiVersion: v1
kind: Pod
metadata:
	name: redis-pod
	labels:
		name: redis-pod
		app: demo-voting-app
spec:
	containers:
	- name: redis
	  image: redis
	  ports:
		  - containerPort: 6379
```
next postgres-pod.yaml

```yml
apiVersion: v1
kind: Pod
metadata:
	name: postgres-pod
	labels:
		name: postgres-pod
		app: demo-voting-app
spec:
	containers:
	- name: postgres
	  image: postgres
	  ports:
		  - containerPort: 5432
	  env:
		  - name: POSTGRES_USER
		    value: "postgres"
		  - name: POSTGRES_PASSWORD
		    value: "postgres"
```

then the worker pod, which doesn't have any ports listening to it.

```yml
apiVersion: v1
kind: Pod
metadata:
	name: worker-app-pod
	labels:
		name: worker-app-pod
		app: demo-voting-app
spec:
	containers:
	- name: worker-app
	  image: kodekloud/examplevotingapp_worker:v1
```

now we create the services:
redis-service.yaml
```yml
apiVersion: v1
kind: Service
metadata:
	name: redis
	label:
		name: redis-service
		app: demo-voting-app
spec:
	ports:
		- port: 6379
		  targetPort: 6379
	selector:
		name: redis-pod
		app: demo-voting-app
```

postgres-service.yaml
```yml
apiVersion: v1
kind: Service
metadata:
	name: db
	label:
		name: postgres-service
		app: demo-voting-app
spec:
	ports:
		- port: 5432
		  targetPort: 5432
	selector:
		name: postgres-pod
		app: demo-voting-app
```

voting-service.yaml
```yml
apiVersion: v1
kind: Service
metadata:
	name: voting-service
	label:
		name: voting-service
		app: voting-voting-app
spec:
	ports:
		- port: 80
		  targetPort: 80
	selector:
		name: voting-app-pod
		app: demo-voting-app
```

result-service.yaml
```yml
apiVersion: v1
kind: Service
metadata:
	name: result-service
	label:
		name: result-service
		app: voting-voting-app
spec:
	ports:
		- port: 80
		  targetPort: 80
		  nodePort:30005
	selector:
		name: result-app-pod
		app: demo-voting-app
```

