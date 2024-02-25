#kubernetes/directories
#kubernetes/yaml 
they're used to store secritive information like password and credentials, unlike configmaps they are encrypted.

you can create them inperatively using
`kubectl create secret generic --from-literal=key=value`
you can use the parameter `--from-literal` as many times as you like.

using a yaml file, you can put as much data as you want through the data array
you should specify the data into a hashed format inside the file.
you can secure it using
`echo -n 'password' | base64` which i assume is retarded, then put the output in the yaml file.
but remember, this leaves a trace in your bash_history
```yml
apiVersion: v1
kind: Secret 
metadata:
	name: app-secret
data:
	DB_Host: mysql
	DB_Password: someretardedhash==
```

you can refernce a secret in a pod defintion using `spec.containers.envFrom.secretRef[name]` 
example:
```yml
apiVersion: v1
kind: Pod
metadata:
	name: app-name
	labels:
		name: app-name
spec:
	containers:
	- name: app-name
	  image: appp-image
	  ports:
	    - containerPort: 8080
	  envFrom:
	    - secretRef:
		    name: app-secret-name
```
you can inject a single env variable from a secret or the whole secret.
environment secret injection:
```yml
envFrom:
  - secretRef:
	    name: secret_name
```
single secret:
```yml
env:
  - name: env_var_name
	valueFrom:
		secretKeyRef:
			name: app-secret
			key: app_value
```
you can even mount a secret as a volume:
```yml
volumes:
  - name: app-secret-volume-name
	secret:
		secretName: app-secret
```
you can access these files at `/opt/app-secret-volume-name` inside the pod.