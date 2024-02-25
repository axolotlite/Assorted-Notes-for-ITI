
Why would we need a NAT Gateway?
to translate the ip of the instances inside the VPC into an external ip address when transferring data through an internet gateway.

Why can private instances access the internet but devices out of its subnet cannot access it?
due to NAT-ing, which allows traffic to exit through a public ip address and drops any external traffic towards the private instance that isn't part of the session it started.

What is the difference between a public and private subnet?
the public subnet has a direct route to the internet gateway
the private subnet has a route to a net-gateway that translates traffic.

what is the NAT Gateway?
this is an AWS gateway that allows private subnets to communicate with the internet, while preventing inbound traffic from reaching the devices.

What is the difference between a NAT Gateway and a NAT Instance?
They're both NAT tables that translates outbound traffic , but the NAT Gateway is managed by the user unlike the NAT Instance which is managed by AWS.

What is VPC Sharing?
a recently added feature that allows an AWS Account within an AWS Organization to share his VPC with other Accounts as participants (they can create resources and add them to the subnets)

What is VPC Peering?
This is a method to connect two VPC's within the same account, which allows for traffic between the two VPCs.
This is managed by AWS.
One of the requirements of VPC Peering is not having any overlapping subnets (no two subnets should have the same address range)

What is AWS Site to Site VPN?
This is a site to site VPN service presented by amazon to allow connecting a VPC to the customers Data Center.
This is done by creating a `Virtual gateway` in the VPC and creating a customer gateway on premise then using `AWS Direct Connect` before finally configuring the route table between them.

#### VPC Endpoints:
This is a service provided by AWS that allows you to privately route AWS data through the Amazon backbone.
for example, an EC2 instance wants to access a file through an S3 Bucket, usually this is done through a publicly accessible API.
through VPC Endpoints, we can make this API accessible through a VPC Endpoint, making it private.

#### AWS Transit Gateway:
This is a hub that centralizes all external networking configuration(VPNs, Direct Connect & customer gateways, VPCs & VPC Peering)
