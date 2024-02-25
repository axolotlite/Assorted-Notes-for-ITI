
these are functions available in terraform.

`file("location")` this opens a files content in .tf

`length(var.array)` this returns the length of an array or set

`toset(var.array)` this removes duplicates from an array and returns a set

numberic functions:

`max(1,4,5,7,4,2)` returns max number
`min(1,4,5,7,4,2)` returns min number
we can use them with arrays through the expansion symbol `...`:
`max(var.array...)` returns max number

there are also ciel and floor

string functions:

`split(delimeter, string containing delimeter)` can seperate a string according to a delimeter, this returns an array.

`lower(string)` this returns a lower case string
`upper(string)` this returns a upper case string

`substr(string, start_index, offset)` this returns a substring between the given indecies.

collection functions:

`length(var.list)` return number of elements
`index(var.list, "value")` returns the index of the specific value.
`element(var.list,index)` returns the element specificied by the index
`contains(var.list,"value")` returns true or false, depending on the elements existance in the list, it is case sensitive.

map functions:
`keys(var.map)` this returns a list of keys in a map
`values(var.map)` this returns the values in a map
`lookup(var.ami, key)` this returns the value of the specified key, if the key is unavailable, it'll fail
`lookup(var.map, "key", "default_value")` to mitigate this we specify a default.


