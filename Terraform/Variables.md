
we can create variables in terraform using:
it has 3 parameters
```
variable "variable_name" {
	default = "variable"
	type = "string | number | boolean | any"
	description = "optional explaination"
}
```
type is enforced only when applied. so if you try to access a number in a place that requires a string, it'll return an error.
the default type is "any"
there are additional types such as:
- list: ["cat", "dog"]
- map: {pet1 = cat, pet2 = dog}
- object: complext data structure
- tuple: also complex data structure
we can then call upon this variable in any other resource using:
```tf
resourse "local_file" "file_something"{
	filename = var.variable_name
	content = var.variable_name
}
```

special variable types:
list type:
```tf
variable "prefix" {
	default = ["Mr", "Mrs", "Sir"]
	type = list
}
```
we can access the list using zero indexing.
```tf
resource random_pet pet-name {
	prefix = vars.prefix[0]
}
```
this will return "Mr"

map type:
```tf
variable file-content{
	type = map
	default = {
		"statement1" = "We love A"
		"statement2" = "We love B"
	}
}
```
which can be accessed through:
matching key.
```tf
reosurce resource_type resource_name {
	argument1 = var.file-content["statement1"]
}
```
both list and map can have types, through using
`type = map(string)` and `type = list(string)`

set type: 
it's like a list with the condition of no duplicates
```tf
variable "fruit" {
	default = ["apple", "banana"]
	type = set(string)
}
```
an example of an unacceptable set due to duplication:
```tf
variable "fruit" {
	default = ["apple", "banana", "banana"]
	type = set(string)
}
```

object type:
we can create object data structure by combining all the variable types we've seen so far
```tf
variable "cat_object" {
	type = object({
		name = string
		color = string
		age = number
		food = list(string)
		favorite_pet = bool
	})
	default = {
		name = "bella"
		color = "brown"
		age = 7
		food = ["fish","chicken", "turkey"]
		favorite_pet = true
	}
}
```

tuple type:
it's a list of list containing different elements, consisting of a sequence of elements that could be anything.
we can specify the types in the tuple using type
```tf
variable tuple {
	type = tuple([string, number, bool])
	default = ["cat", 7, true]
}
```