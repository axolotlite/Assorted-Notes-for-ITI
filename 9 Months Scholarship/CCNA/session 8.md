first we create an accces list by selecting a sumber
standard 0->99
extended 100->199
`access-list num deny/permit ip/host wildcard`
`access-list 10 deny 192.168.10.0 0.0.0.255`
then to permit anything
`access-list 10 permit any`
after setting a policy we must apply it to an interface,
before routing = in
after routing = out
so we select an interface
`int g 0/1`
`access-group 10 in`
this'll block anything entering the network from this ip address.
we can remove it by preprending no
`no access-group 10 in`
alternatively we can block anything from going to that ip from the host through
`access-group 10 out`

now to block a protocol using extended access lists
`access-list n permit/deny transfer_protocol source_ip wildcard destination_ip eq/port `
`access-list 110 deny tcp 192.168.10.0 0.0.0.255 host 10.10.10.10 eq www`

then add another rule to permit anything to pass
`access-list 110 permit ip any any`

finally we apply it to an interface
`int g 0/0`
`ip access-group 110 out`
you can view your access lists through
`sh ip access list num`
we can insert between two priorities in an access list using somethibg cakked sequence number which is basically a number indexing at 1 to the numbers of policies in an acl
`15 deny 192.168.10.0 wildcard host host_ip eq port`


lab we've 3 vlans 10,20,30 with 3 sub interfaces on the router.
we need to make an access liust where
10 can browse - bing
20 can  - browse + ping
30 can browse + ping

explicity specifying icmp port didn't work, but using any did.
nat config: we select the interface then specify which one is inside/outside
`ip nat inside/outside`

finally we define the pool of public ips
ip nat pool name start_ip end_ip netmask net_mask 
then we create a list of internal networks through the creation of an access list.
remark is like leaving a comment
`access-list 10 remark internal network`
permit 10.10.10.0 0.0.0.255
ip nat inside source list 10 pool pool_name

ip nat inside source static 10.10.10.200

to use padding.(Everyone in the network using a single ip address)
ip nat inside source list 10 interface g 0/0 overload

## configuring port security.
first, we'll need to disable the dynamic auto port mode.
by selecting a port and switching the mode to access
`switchport mode access`
then select the port-security
`switchport port-security`

we can bind a mac address to the port, forcing any non-bound macs to affect the interface according to violation mode configs.
`switchport port-security mac-address place_your_address_here`
