They are key value pair files that can be injected into pods

create it through
`kubectl create configmap config_name --from-literal=key=value`
you can use the parameter `--from-literal` as many times as you like.

or declaritvely through a config file
using it through
`kubectl create -f confi-map.yaml`
```yml
apiVersion: v1
kinda: ConfigMap
metadata:
	name: app-config
	data:
		APP_COLOR: blue
		APP_MODE: prod
```

