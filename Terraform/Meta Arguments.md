they can be used in any resources block to change its behaviour.
example of meta arguments are:
- [[lifecycle rules]]
- depends_on
- count
- for_each

count can query a number of resources:
```tf
resource local_file pet {
	filename = var.filename
	count = 3
}
```
```tf
resource "local_file" "name" {
    filename = var.users[count.index]
    sensitive_content = var.content
    count = length(var.users)
}
```
this will create the same file 3 times, if we want each to be unique:
```tf
variable "filename" {
	default = [
		"/root/pets.txt"
		"/root/dogs.txt"
		"/root/cats.txt"
	]
}
```

count can also use built-in functions to fit a list:
`count = length(var.filename)`

```tf
resource "local_file" "name" {
    filename = each.value
    for_each = toset(var.users)
    sensitive_content = var.content

}
variable "users" {
    type = list(string)
    default = [ "/root/user10", "/root/user11", "/root/user12", "/root/user10"]
}
variable "content" {
    default = "password: S3cr3tP@ssw0rd"
  
}

```