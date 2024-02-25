
the format of hcl syntax consists of blocks and arguments
```hcl
<block> <parameter> {
	key1 = value1
	key2 = value2
}
```
a block contains info about the infrastructure platform and a set of resources within the platform on which we want to create it.

if w want to creae a file in `home/test` on a local system we'll do the this:
```hcl
resource "local_file" "pet" {
	filename = "$HOME/pets.txt"
	content = "We love pets!"
}
```
the type is "resource", then we declare the new resource type which is a fixed value "local_file".
the resource type "local_file" tells us who is the provider we'll be using, in this case it's local provider
finally we specify the resource name "pet", it is used to identify the resource and it can be anything.
now, inside the curly praces we define the arguemts which are specific to the type of resource we're creating.

example ec2 instance:
```tf
resource "aws_instance" "webserver" {
	ami = "ami_id"
	instance_type = "t2.micro"
}
```
example s3 bucket:
```tf
resource "aws_s3_bucket" "data" {
	bucket = "webserver-bucket-org-2207"
	acl = "private"
}
```
you can identify the resource provider from before the first underscore:
in the previous two cases, we can see that the provider for both "aws_instance" and "aws_s3_bucket" are a resource type of "aws"

these could be deployed by:
- `terraform init` : this will check the config file, then initialize the working directory. this will download any plugins needed to deploy the resources.
- `terraform plan`: this will show the actions carried by terraform to create the resources. this is similar to the diff command in git.
- `terraform apply`: this will ask us to confim the plan, then it will create the resources.

ofcourse after this we can destroy the object if it is no longer in use.
`terraform destroy` inside the directory.