Domain controller is a physical device responsible for controlling the rest of the devices in the a company network, where all users are registered on it.

first we need to install domain services, to turn a VM to a domain controller, this'll add an NTDS.

each domain has a name: name.organization
example: iti.com
this domain will be available locally, however to allow entrance from the internet, we'll have to use the .local domain, it'll make it accessible from both in and out of the network.
first, you'll need to join the domain.

we can create sub domains by adding alex.iti.local, this new domain is called a child domain.

we can use an additional domain control, this is a copy of the local domain controller, but outside our domain. they're a replica of eachother. this also allows for load balancing.

Policies are only applied on organizational units.

we can create organizations units in a domain, through "active directory computers and users"

The root domain is called a forest, abd any subdomain in the forest is called tree.

global catalog is the indexing of websites in a forest, any forest must have an index, so it's not optional.
NTDS sysvol is responsible for saving the user policies, permissions, and instructions.
whenever a device logins to the NTDS, it goes through SYSVOL to acquire its policies.
a domain user can login to any devices in this domain.
any user within the domain, won't be able to login to it, only the admin can login to the domain controller.
each user in the domain can have up to 10 machines join the domain using his account by modifying the PC settings from workgroup to domain, setting up the domain name and logging in using their credentials

delete protection can be bypassed through advanced features in the "active directory computers and users"
 by enabling it, you'll be able to see the advanced properties.
each user has its own SID, this SID is unique and wont be returned to a user after it is deleted, even if we use the same name.
we can enable a feature called, user recycling that show allow the SID to be reused again, but this feature is available from above 2008 server.
this can be enabled from:
tools -> active directory admin server -> local -> enable recycle bin
restart it from tools and then it should take effect.
you'll find any deleted users in the active dir admin local deleted objects, you can restore it from there.
