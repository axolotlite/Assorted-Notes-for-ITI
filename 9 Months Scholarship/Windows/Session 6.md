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