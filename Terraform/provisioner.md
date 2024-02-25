or create time provisoners.
they run after the resources are created.
if a provisioner fails, it results in an error. this can allow us to do on-failure argument

terraform recommends providers as a last resource.

they can also be run post destruction

example:
```
provisioner local-exec {
	command = "echo ${resource_type.resource_name.data}"
	on_failure = fail | continue
}
```

to run it after destruction:
```
provisioner local-exec {
	command = "rm filename"
	when = destroy
}
```

