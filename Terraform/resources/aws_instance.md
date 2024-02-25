
modifyign the aws_instance resource will trigger a reboot.

these variables:
```
variable "ami" {
  default = "ami-06178cf087598769c"
}

variable "instance_type" {
  default = "m5.large"
}

variable "region" {
  default = "eu-west-2"
}
```

the resource:
```tf
resource "aws_instance" "cerberus" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name = keyname
  user_data = file("./install-nginx.sh")
}
```

user_data only runs at first boot, 