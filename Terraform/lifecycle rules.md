we can use lifecycle rules to define how terraform deals with files upon creation of a new state.

creating file before destroying it, we append this to a resource:
```
lifecycle {
	create_before_destroy = true
}
```

prevent the destruction from destruction:
```tf
lifecycle {
	prevent_destroy
}
```
for example, you don't want to destroy the database.

we can ignore any specific changes using:
```
lifecycle {
	ignore_changes = [
		tags, ami, all
	]
}
```
this means the specified elemnts will be ignored if they changed.

