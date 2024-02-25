[source](https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key)

Resource tls_private_key generates a secure private key and encodes it as PEM. It is a logical resource that lives only in the terraform state.

You can see the details of the resource, including the private key by running the terraform show command.
```tf
resource "tls_private_key" "pvtkey" {
    algorithm = "RSA"
    rsa_bits = 4096
}
```