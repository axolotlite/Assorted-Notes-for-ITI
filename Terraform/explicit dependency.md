we can specify which resource depends on which one.
this will make terraform, deploy resources in order of dependencies.

example:
```tf
resource local_file file_filename {
	filename = var.filename
	content = "text content of a file"
	depends_on = [
		resource_type.resource_name
	]
}
```

unlike implicit dependency which can be inferred by terraform through referencing variables available in other resources.