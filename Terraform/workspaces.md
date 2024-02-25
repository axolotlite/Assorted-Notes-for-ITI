#terraform/directories 
using workspaces creates a directory for tfstate files, allowing for workspace related tfstate.
this directory is called: `terraform.tfstate.d`

to create a workspace we must use:
`terraform workspace new workspace-name`
this will automatically switch into it.

we can see all available workspaces:
`terraform worksapce list`
we can switch to a workspace using:
`terraform workspace select workspace_name`
the current worksapce will be marked with a '\*'

we can get the name of the workspace using this inside a .tf:
`terraform.workspace`

example for workspace application in a project:
```main.tf
module "payroll_app" {
  source = "/root/terraform-projects/modules/payroll-app"
  app_region = lookup(var.region, terraform.workspace)
  ami        = lookup(var.ami, terraform.workspace)
}
```
which will call these variables, depending on the workspace
```variable.tf
variable "region" {
    type = map
    default = {
        "us-payroll" = "us-east-1"
        "uk-payroll" = "eu-west-2"
        "india-payroll" = "ap-south-1"
    }

}
variable "ami" {
    type = map
    default = {
        "us-payroll" = "ami-24e140119877avm"
        "uk-payroll" = "ami-35e140119877avm"
        "india-payroll" = "ami-55140119877avm"
    }
}
```