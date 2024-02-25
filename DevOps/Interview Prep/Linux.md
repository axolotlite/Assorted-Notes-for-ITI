1) EC2 instance is running out of disk space, what actions will you take to mitigate the issue:
	This means that:
	- EBS volume is affeted
	- we will have to check root volumes
	- if root, we'll check the logs and try to clear space
	- if application, we'll take snapshots then increase disk space
2) What is the bastion host or gateway server? what role does it play?
	bastion server is used to manage acess to internal/private networks, sometimes they're called gateway servers or jump boxes or jumb servers
3) Multiple EC2 instances in ASG are getting terminated and this is causing downtime on the application. EC2 pricing and quota all look good. How would you start debugging this issue?
	if an ec2 is being terminated it, it maybe because it's unhealthy.
	some factors affecting the "health" of the OS:
	- disk space full
	- high cpu 100%
	- no memory left
	so the first debugging step would be running top comman