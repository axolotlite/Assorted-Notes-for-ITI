# Session 1
we can't create user specific permissions in a workgroup.
sam file is saved in `C:/windows/system32/config/SAM` it's the windows equivalent to `shadow`

# Session 2
making a webserver.
we'll need to install IIS(Internet I service)

we'll need a dns server to make it work.

the first 1024 ports(well-known ports) are reserved, as regulated by ICAN.
ports of note:

| protocol | port  |
| -------- | ----- |
| http     | 80    |
| https    | 443   |
| fpt      | 20,21 |
| telnet   | 23    |
| ssh      | 22      |

the next range between 1024 -> 49151 are reserved for user.
ICAN decided to create something called NTLD (New Top Level Domains) domains such as
.movie, .team, .fyi, .shop, .work
each with a yearly registration fee.

turns out linux doesn't keep a local cache.

the steps of DNS resolving:
given a site name, the PC looks inside its cache for the IP address of the site.
a hit, returns the IP.
if it misses, 

logs are saved in `C:/inetpub/logs/`

we can create an ftp server through adding an ftp role, then specifying a folder where files are stored, then we can access it through the same menu as IIS, for installation and configuration

we can create a user through computer management -> local users and computers -> users

now we can connect through the browser, file explorer or cmd (ftp command).

`ftp> open 10.10.10.2`
any other command can be seen through `?`

# Session 3

microsoft has an equivalent to ether channel called NIC teaming.
it groups multiple NICs and virtualizes them into a single new interface.

NIC teaming works up to 8 NICs in physical interfaces.

Switch Independent Mode: works without configuring the switch, it allows the server to select which interface as input / output

Static Teaming: selects which interfaces for input / output. this has to be configured between the device and the switch.

LACP: link aggregation control protocol, allows communication between the server and the switch to configure Input / output interface automatically.

standby-adaptor allows you to keep one as a backup in case any of the other adaptors fail.

RDP (Remote Desktop Protocol) uses port 3389 to access a windows machine with a GUI. there is a group called Remote Desktop Users Group, if we want a user to allow RDP into it, we add him to said group.

you can add users, groups and users to groups in Computer management.
adding a user to a group occurs through the user properties in the advanced tab.

Firewall:
can exist as either software or hardware.
both will manage the incoming / outgoing traffic.
most firewalls disable ping by default to prevent DDOS attack.
DDOS(distributed denial of server):  a group of PCs target a single server, flooding it with requests.

# Session 4
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

# Session 5

global catalog: it is an index that allows searching for all objects available in the forest. 
you can install one on both the main DC or one of its replicas.
RODC: Read only Domain Controller
this is a copy of the database that's on the main domain controller, and as the name implied, it's read only.
allowing reading of user data without writing.
RODC server cache the login passwords, saving them whenever a new user logins into a device in its domain.
however, caching opens us to a vulnerability as it may save the admin password, leaving the device unsafe for use.
this was solved by preventing the caching of the admin password, instead it authenticates the password from them main server to allow logging into the device.

there is also a choice to select a group of users to save their passwords in a local cache on the RODC server.

you can also delegate control, allowing for some permissions from administrative control without giving them total admin access.

we can disable this account from the users -> properties -> account -> `account is disabled`

In a subdomain, the child database is different from the root controller.
enterprise admin (The admin of the root controller in the forest) can access and work on any subdomain.

Tasks:
- offline join NTDS
We can offline join a NTDS server, this of occurs happens without being connected with the forest domain.
and once connectivity is established, the data is transferred between them.
steps:
first, disable the NIC of the Device you want to offline join with.
this is a task we're supposed to do.

- child domain controller
create a child domain, disjoin PC 1 from the root domain, then proceed to enter it onto the child domain then try to login to a PC in the main domain using a child domain account.

# Session 6
### DNS (Domain Name Server):
in a website owning the domain of zaki.com.
`zaki.com` is the main root domain of the organization.
it may have other subdomain, such as app.zaki.com
each subdomain will provide a unique service, accessible by its ip or port number within the organization.

now, lets assume an organization wants to buy that domain, they will contact a seller such as godaddy.com, who were given these domains by ICAN.

now, from the user perspective, in order to find zaki.com
your pc will look in this order to find it:
1) cache
2) hosts
3) dns
the whole purpose of a DNS is, when given a query to find the app of a url, the DNS finds it. whether locally if the zone exists inside its domain or externally by looking at the root hint at the end of the domain zaki.com[.].

ICAN has 13 root servers containing all information about every domain made.
these servers are queried by your DNS, it asks it where to find it, they return the query of the `.com` and where you can find it, then it goes to the server containing its location, giving you where to look for the identifier `zaki` in turn pointing you to the server containing the name, which should containing the ip address or the location of another DNS to help you find it.
then, the ip address is cached in the DNS for a period of time, in case any other device wants to find it.

this lookup process can be made efficient by having the DNS forward any external(internet domain) request to an external DNS such as google(8.8.8.8) or cloudfare(1.1.1.1), having them do all the work to find the ip of the given url.

### conditional forwarding
when the DNS is asked about a specific zone by a specific device, the request of the query will cause the DNS to return the static ip of the DNS containing the relevant domains.
however, if the DNS address changes, we'll no longer be able to access the content of this dns.
### stub zone
the DNS creates a shortcut between itself and a Zone DNS, this means if a device asks the DNS to resolve a URL it'll give it the shortcut to the Zone DNS which will return the updated IP address.

### DNS Secondary Zone 
you can replicate the zone of another domains dns, but you'll need explicit permission from the secondary zone to take a direct copy into your DNS, this'll return any resolving requests almost instantly.

### Authoritative vs Non-Authoritative answers
any query asked of a DNS that does not manage the domain is considered non-authoritative, but if the domain is managed by said DNS the answer is authoritative, since the DNS itself is the upmost authority on the specific url / domain and its content.

## DNS inside DC1
since we've worked with domains such as iti.local, we understand why DNS was installed alongside it.
we can find its manager in tools->dns.
inside forward lookup zones we can find our forest root domain, within it all the devices belonging to it alongside the domains.
these data are saved in records.
we can manually add records by right click new host.

we can query the DNS server through `dnslookup` from the cmd, for example any newly created host:
`dnslookup pc6.iti.local`
to further test the resolution of the url, you can use ping which will return the up address.

we can create an alias for any CName(Canonical name) within the domain using create new alias.
this alias will redirect any traffic to the address without having you write the long canonical name.

you can have several addresses for the same ip or several ips belonging to the same url. this'll allow us to host a single website across multiple servers.

## Zone creation
we can create it either by forwarding or reverse lookup

we go into the manager, `forward lookup zone` and specify that we want a new lookup zone of the types (primary, seconday or stub)
there is an option to allow the zone to be within the active directory, allowing for replication between each Directory Controller and its children.
alternatively, we can create an independent DNS.
## Setting up:
### Dynamic Updates
this allows a device to update the DNS with its new acquired ip address.
this could be configured to allow only devices in the domain to update (secure dynamic update)
or any device can update (non-seure and secure dynamic update) this could lead to dns poisoning, where a malicious device changes its ip address, causing other devices to be redirected to it.
we can also turn it off completely.
### Reverse lookup Zone
to create a reverse lookup zone, we go to reverse loopup zone and creat a new zone.
we finish the configuration wizard.
this newly created zone will return the url given the ip address within the specified range.
we can create a new pointer to an ip address from within this zone or during creation of a new url in the `forward zone`
### Root Hints & Forwarders
on DC1 in the dns manager we select dc1 and open its properties, we'll find a tab for root hints in there, from it we can specify the root hints server.
another tab is for forwarding, from there we can specify to whom we want to forward.

### Conditional Forwarding
inside teh DNS manager we can add another dns zone, in the `Conditional Forwards` by specifying the zone through its ip and we specify the domain name.
now any url within this DNS should be accessible within our original DNS.

### Stub Zone
its created through Zone creation, after specifying it. we refresh the forward looking zone.