this creates a simple nginx pod.
we can run it using 
`kubectl apply`
```yml
apiVersion: v1
kind: Pod
metadata:
	name: nginx
	labels:
		app: nginx
		tier: frontend
spec:
	containers:
	- name: nginx
	  image: nginx
	- name: busybox
	  image: busybox
```