
```tf
resource "aws_key_pair" "cerberus-key" {
	key_name = "cerberus"
	public_key = file(".ssh/cerberus.pub")
}
```