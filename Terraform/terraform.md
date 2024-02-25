these are commands used for terraform

initialize a directory, it must be run whenever a provider is used or added
`terraform init`

this command dry runs the current terraform directory without appplying it.
`terraform plan`

this command applies the current terraform directory.
`terraform apply`
parameters:
`-var "key=value"` allows usage of variables using command line
`-var-file file.tfvars` allows usage of an entire file of variables

this command shows created objects after apply:
`terraform show`

we can check if the .tf file is correct by using:
`terraform validate`
otherwise, it'll show us the line causing the error with possible fixes.

format the files into a canonical format
`terraform fmt`

to see all used providers:
`terraform providers`
we can even already used providers from another directory through:
`terraform provider mirror directory`

seeing all outputs in a directory:
`terraform output`
if we want a specific variable we can do this:
`terraform output variable_name`

put terraform reosurces fromn outside into this current statefile.
`terraform refresh`

generated a graph is dot format
`terraform graph`
we can visualize this using a graphing software such as graphviz
`terraform graph | dot -svg > graph.svg`

we can see the current state of terraform objects through:
`terraform state show resource_type.resource_name`

you can list all resources recorded inside the statefile:
`terraform state list`

you can move items in a terraform state file: it basically renames a resource or moves items into other statefiles
`terraform state mv [option] source destination`
