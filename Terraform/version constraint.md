we can use it to lockdown the version of the providers used
adding this block to main.tf
```tf
terraform {
	required_providers{
		local = {
			source = "hashicorp/local"
			version = "1.4.0"
		}
	}
}
```
to prevent it from using a specific version:
`version = "!= 2.0.0"`
to make use a lesser version than a range
`version = "< 1.4.0"`