tfstate files are created only `terraform apply` are used once.

it is a json file matching the infrastructure created by terraform, it details the resources, their attributes and all their details.

it is a bad idea to store the statefile in a source control software.

we can specify the usage of a remote statefile on aws s3 by using:
```terraform.tf
terraform {
	backend "s3" {
		key = "terraform.tfstate"
		region = "us-east-1"
		bucket = "remote-state"
	}
}
```