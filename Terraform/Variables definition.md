we can define variables for terraform through the command line

during apply:
`terraform apply -var "key=value" -var "key2=value"`

using a var-file
`terraform apply -var-file file.tfvars`

using environment variable by appending variable name to `TF_VAR_`:
`export TF_VAR_varName=value`
`export TF_VAR_key=value`
which will be used during `terraform apply`

we can even use variable definition files:
file.tfvar
```tfvars
key=value
varName=value
```
which will be automatically loaded during `terraform apply` as long as it ends with
- .tfvars
- .tfvars.json
- .auto.tfvars
- .auto.tfvars.json

There is a variable definition precedence for which values to use:
right most takes more precedence
environment variables -> terraform.tfvars file -> .auto.tfvars (alphabetical order) -> -var/-var-file command line parameter

