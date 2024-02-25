### Secondary Zone
to create a secondary zone from a different DC, you need to create a `seconday zone` from the new zone wizard.
after creating it you return to the host server (DC2) enter the zone properties to configure the `zone transfer` this will allow you to send data to the specified server.

Forward lookupzone -> secondary_zone_directory -> right click -> properties -> Zone Transfer -> enter DC1 ip

Now DC1 will have read only access to the secondary zone from DC2, it can read but it can't create nor delete.

if the allowed server ip changes, you'll have to manually update it, however having a name will allow it to look for the machine.
### Time To Live (TTL)
this is the time your PCs cache keeps a website cached within its local dns cache.
### Start of Authority
the serial number is incremented on any change to the zone.
changes include:
- adding a record
- deleting it
- modifying
this will help the secondary realize that any change occurred on the primary server.

the refresh interval specifies how long to wait before they check for any updates in the server.
Expires after: in case DC2 is unreachable, DC1 will resolve domains using the saved data within the time of the expiry date. once the time exceeds it, it no longer resolves domains.
finally TTL: we specify how long a PC should cache the received address resolution.

### Clear DNS Cache
you can clear the cache in DNS Manager by pressing the Directory Controllers name, then right clicking it and selecting `Clear Cache`

### DNS Scavenging
If you allow a device to update their own ips, sometime a machine will connect, but it'll never reconnect again, at least not at the same device name.
this will take another record with a different ip, causing some records to be permanently left.
we can make it so any record not refreshed within a `time period` it'll be marked as `unusable` so, after 7 more days it'll be scavenged.

### Domain Authentication 
When a machine tries to authenticate from a Domain Controller to join its domain, it updates itself in the DNS records of the Domain.
now, when a user logins on his machine, it authenticates through Kerberos protocol.

### DHCP
A protocol responsible for distributing network configurations to devices in a network.
if it fails, the PC will rely on acquiring the configuration from APIPA.
which takes a random ip address from a set range.
warning: two devices may randomly select an IP, causing conflict.
#### DORA
- Discover Message: A broadcast message is sent through the network
- Offer: is presented by the DHCP server to the device who sent the discovery.
- Request: The device then requests an IP address from the DHCP server.
- Acknowledgement: is sent by the DHCP server of the ip address, reserving it to the requesting device and binding its mac address in the ARP table.
The ARP table records the lease time for each IP address and the device its bound to, this lease increases everytime the device connects to the network.
once the lease expires, the reserved IP address is returned to the IP Pool of the DHCP server.
#### Microsoft Vs Cisco handling of Request & Acknowledgement
Cisco dhcp servers send unicast requests and ack messages
Microsoft sends broadcast requests and ack messages in case there exists several DHCP servers, letting them know that the ip address has been leased by a device.
#### Lease period:
if all ips in a pool were leased, no more devices will be able to connect.
There is an attack targeting this called DHCP Starvation, where an attack leases all ips and redistributes them according to his device.
### Setting up
to add a dhcp server to a domain, you must be within a domain.
so DC2 should be joined to iti.local domain.
then DHCP role should be added and completed, you'll have to use the credentials of DC1 admin to complete it.
#### Specifying ip range
this could be done through creating a new scope from the DHCP server manager
right click ipv4 -> create new scope
and follow the wizard along.
Subnet Delay: if there is another DHCP server, we can set a delay that would affect who replies to the DORA process first. allowing us to priorities servers.
0ms delay makes this server the top priority and first pick

### Scenario
We have DHCP server in our organization, to control it.
we installed an Active directory Domain Controller in DC1, so whenever a PC connects, we can control it and add policies for it.
once this device joins a domain with a location containing a DHCP server that would allow it an IP address.
this DHCP server should be approved/authorized by the Domain Controller to do so, securely.
otherwise anyone could sniff the DORA Process on the network, and distribute non-authentic addresses.
the device will have to distinguish between the real and fake dns through finding which one is authorized within this domain.

another device tries to connect to the network, although it does not belong to the domain, the DHCP will give it an ip regardless of its affeliation, however, the safest thing to do is give it an ip from an isolated network / ip pool.

### Filtering
we can allow specific devices into the network by specifying their Mac address.

#### Failover Clustering in DHCP
in a cluster, they use a `heartbeat` signal to notify other nodes of the fact that they're active.
if this heartbeat message stops, it means the server has failed and is no longer reachable.
having 2 dhcp servers working together to distribute addresses.
### Superscope
like NIC teaming, it's a virtual scope created by combining several scopes together.
#### Hot standby
one device works the DHCP server and once it shuts down or becomes unaccessible, the other device will take its place.
we can configure the percentage of servers allowed in standby while the main DHCP returns. this is because the main server maybe in standby because of a reboot.
we 
#### state-switch
this switches the main DHCP server within the specified time.

### Backing up and Restoring DHCP
you have the option to backup the DHCP database through DHCP Manager, by rightclicking the server name then backup.
we can migrate it to a newer device by pressing restore.

task:
- dhcp server
- scope and pc take from it
- create superscope
- delete superscope
- create a filter
- backup and restore
- failover
- secondary dns server