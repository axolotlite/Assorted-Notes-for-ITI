
using random resource

```tf
resource "random_pet" "my-pet" {
	prefix = "Mrs"
	separator = "."
	length = 1
}
```
this resource uses 3 arguments
- prefix: added to the pet-name
- separator: between name and prefix
- length: length of the pet name generated.

