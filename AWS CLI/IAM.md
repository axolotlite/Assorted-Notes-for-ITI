
`aws iam` is the base command for use with identity and access management.

we can list all the users through:
`aws iam list-users`

to create a new user we need to pass:
`aws iam create-user`
with this manditory parameter:
`--user-name name`

we can give a user admin using this policy:
`aws iam attach-user-policy --user-name name --policy-arn arn:aws:iam::aws:policy/AdministratorAccess`

we can create a new group using:
`aws iam create-group --group-name name`

then we can add users to the group:
`aws iam add-user-to-group --user-name username --group-name groupname`

we can list group attached policies through:
`aws iam list-attached-group-policies --group-name name`

we can attach ec2 access to a group through:
`aws iam attach-group-policy --group-name groupname --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess`