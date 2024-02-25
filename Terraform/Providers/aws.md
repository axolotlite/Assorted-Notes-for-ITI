
using this block in any aws tf file will mitigate errors:

```
provider "aws" {
     region = "ca-central-1"

}
```

using a custom endpoint:
```
provider "aws" {
  region                      = "us-east-1"
  skip_credentials_validation = true
  skip_requesting_account_id  = true

  endpoints {
    iam                       = "http://aws:4566"
  }
}
```