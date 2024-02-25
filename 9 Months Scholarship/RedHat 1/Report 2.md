# newgrp

log in to a new group

The `newgrp` command is used to change the current group ID during a login session. If the optional - flag is given, the user's environment will be reinitialized as though the user had logged in, otherwise the current environment, including current working directory, remains unchanged.

## **Uses:**

**Group Switching:**
This allows users to switch their effective group ID, enabling them to access files and resources associated with a different group.

**Access Control:**
Allows you to control access to files and directories that for specific group.

**Resource Sharing:**
Allows the sharing of resources between groups by allowing users to temporarily adopt the group's identity.

## **Conclusion:**
I've only used it to avoid logging out and back into a Desktop Environment, but I can see how it can be used in conjunction with groups to quickly log users in and out.

---

# Group Passwords
They are located in a file called gshadow
like normal shadow file, it's distributed into the following fields:
`group_name:encrypted_password:administrators:members`

/etc/gshadow contains the shadowed information for group accounts.
This file must not be readable by regular users if password security is to be maintained.

These passwords are used as an added layer of security and group managements.
They provide us the following benefits:
**Access Control:**
You can choose who can access what resources based on his group/s, without explicitly placing him into a group.
Since he can join the group using their password.

**Selective Group Membership:**
This allows an admin to select members of a group and allow them access to said group whether they're already a part of it or not.

**Restriction of Shared Resources:**
Users within a group may require more permissions to access a more restricted location in a group shared resource

**Temporary Group Access:**
A group password can be locked, preventing access to a resource.
## **Conclusion**
Group passwords allow access control, security, and compliance, they're valuable tools in managing user groups within Linux.

---
# groupmems vs gpasswd

| Name      | Description from its man page|
| --------- | ----------- |
| groupmems |       allows a user to administer their own group membership list without the requirement of superuser privileges. The groupmems utility is for systems that configure its users to be in their own name sake primary group(i.e., guest / guest).      |
| gpasswd          |        The gpasswd command is used to administer /etc/group, and /etc/gshadow. Every group can have administrators, members and a password.     |

From their man page descriptions we can easily surmise that `groupmems` are for single group administration, it allows us to manage individual users within a group, adding or removing them.

mean while `gpasswd` is used to configure groups, not their users, it allows us to add and remove users as well as setting a group password and administrator, which in turn will allow said admin to user `groupmems` to moderate the group.

## **Conclusion**
`gpasswd` is a more powerful administrative tools, it manages the groups and its users unlike `groupmems` which only deals with users.
