terraform can read attributes from resources, then provision data according to these attributes.

datasources only read info from a regular source,

```tf
data "local_file" "os" {
  filename = "/etc/os-release"
}
```

which can be accessed through:
```tf
output "os-version" {
  value = data.local_file.os.content
}
```

