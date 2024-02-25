[github repo](https://github.com/hashicorp/terraform)
terraform is a popular IAC tool developed by hashicorp, it can be installed using a single binary that allows deployment and destruction of infrastructure on private and public clouds.

it can provision infrastructure on
- physical machines
- vmware
- aws
- gcp
- azure

terraform uses hcl language and uses a main.tf file to run the code inside of a directory.
hcl is decralitive while attempting to be human readable.

terraform works in 3 phases:
- init: initalizes the project while identifying the providers used
- plan: plans how to achieve the target state
- apply: applied the plan to reach the desired state.
each object managed by terraform is called a resource, it manages their lifecycle from its provisioning to configuration to decomissioning.

a .tfstate file is created to keep a blue print of the infrastructure deployed by terraform. this can be later used for configuring other resources.
this also allows it to control other resources not deployed using terraform.

[installation guide](https://developer.hashicorp.com/terraform/downloads)
