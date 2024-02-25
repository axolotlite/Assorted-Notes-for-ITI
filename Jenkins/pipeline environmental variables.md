we can add a section at the start of the pipeline containing any pipeline specific env variables we want using `environment`.
ex:
```
environment{
	anyVar = "value"
	deploymentName = "devops dep"
	containerName = "containerer"
}
```