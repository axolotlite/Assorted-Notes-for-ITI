# Maximum members per group
This could be defined inside the login.defs.
from the man page:
```
MAX_MEMBERS_PER_GROUP (number)

Maximum members per group entry. When the maximum is reached, a new group entry (line) is started in /etc/group (with
the same name, same password, and same GID).

The default value is 0, meaning that there are no limits in the number of members in a group.

This feature (split group) permits to limit the length of lines in the group file. This is useful to make sure that
lines for NIS groups are not larger than 1024 characters.

If you need to enforce such limit, you can use 25.

Note: split groups may not be supported by all tools (even in the Shadow toolsuite). You should not use this variable
unless you really need it.
```


| action                      | source | target |
| --------------------------- | ------ | ------ |
| copy a directory            | r-x    | -wx    |
| copy a file                 | r-x    | -wx    |
| delete a file               | -wx    |        |
| change a directory          |        | -wx       |
| list directory content      |       |  r     |
| view the contents of a file |       |   r     |
| modify a file content       |       |   w     |


