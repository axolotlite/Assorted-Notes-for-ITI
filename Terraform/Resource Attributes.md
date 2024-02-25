
Resource attributes can link two resources together.
it allows us to references attributes from other resources, like their ids and name.

for example:
creating a resource, we can refernce it through:
resource_type.resource_name.attribute
```tf
resource "random_pet" "my-pet" {
	prefix = "Mrs"
	separator = "."
	length = 1
}
resource "local_file" "pet" {
	filename = var.filename
	content = "My favorite pet is ${random_pet.my-pet.id}"
}
```
the curly braces allow for insertion.

