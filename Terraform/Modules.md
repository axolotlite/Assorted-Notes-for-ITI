any directory containing .tf files is called a module.
it has tf config files that can create resources.

we can reference another module through this block
this means the current module is the root module, and it is calling a child module
```tf
module "module_name"{
	source = "relative_location_to_root_module"
}
```
we can call this module, then use the variables defined inside of it:
```tf
module "payroll"{
	source = "../location"
	app_region = "us-east-1"
	ami = "ami-xxxxx"
}
```
app_region, ami are variables in the referenced module.

this is an example module [referencing](https://registry.terraform.io/modules/terraform-aws-modules/iam/aws/latest/submodules/iam-user)
```
module "iam_iam-user" {
  source  = "terraform-aws-modules/iam/aws//modules/iam-user"
  version = "3.4.0"
  # insert the 1 required variable here
  name = username
}
```