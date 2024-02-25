#kubernetes/yaml
#kubernetes/commands
### apiVersion
- v1: supports both PODs and services
- apps/v1 : supports ReplicaSet and Deployment
### kinda:
refers to the type of object we're trying to creata:
- POD
- Replicaset
- Deployment
- Service
### metadata:
as the name says, it's a meta data related to the object, it's only allows name, label and other propreties.
unlike label, which allows any type of key value pair you want.
```yml
metadata:
	name: app_name_pod
	labels:
		app: my_app
		other_label: string 
```
### spec:
specification of an object, each object has its own specifications. it's a dictionary.

we can run a pod defintion using:
`kubectl create -f pod-definition.yml`