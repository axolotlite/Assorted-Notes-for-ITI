[docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_user)
to create an IAM user in terraform we can use this template:

```tf
resource "aws_iam_user" "users" {
     name = "mary"
}
```

