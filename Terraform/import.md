terraform import allows us to modify the statefile by importing resources.

`terraform import <resource_type>.<resource_name> attribute`
this will modify the .tfstate file.

to avoid errors, we'll have to create an empty resource block for our resource.
```tf
resource "resource_type" "resource_name"{
	# literally empty
}
```
we can import an ec2 instance using this method:
`terraform import aws_instance.jade-mw id-of-the-resource`
```tf
resource "aws_instance" "jade-mw" {

}
```