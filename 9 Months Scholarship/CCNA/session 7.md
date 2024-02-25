setting up 2 vlans accross 2 switchs
```
vlan 10
vlan 20
```
we then select an interacce and specify the switchport mode for both vlans
```
int f 0/1
switchport mode access
switchport access vlan 10
```
after which we enable trunking between the two switchs on both ends
```
int g 0/1
switchport mode trunk
switchport trunk allowed vlan 10,20 
```

then we install a router, connect both of them to it and cofigure the protocols and sub interfaces `0/0.n`
`int g 0/0/0.10`
to configure encapsulation to allow understanding between switch packets, specifically the vlan(10)
`encapsulation dot1Q 10`
this will allow us to configure a sub interface.
then we can give it an ip
`ip address 192.168.10.1 255.255.255.0`

finally we return to the connected switch and enable trunking between it and the router.

now each device connected to its own vlan can only connect to their networked devices and the routers(gateway ips)

## DHCP:
distributes ips to the devices connected to the network.
first, the pc sends a broadcasting discovery while waiting for a reply from anyone.
this anyone is non other than the dhcp server, offering to give the pc an ip address.
then the pc sends a request to take an ip from the available (ip bool) available in the dhcp server.
the server then returns the ip address.

the server has an arp(binding) table containing each used IP address with its owners mac address.

alternatively, if no one replies to the broadcast, the PC will rely on HPIPA, and guess a possible ip address to connect to the network with.
HPIPA exists in rance of 169 -> 252
several devices using HPIPA instead of dhcp, it means there is a problem in the dhcp server, its either down or the client is no longer in the network.

release duration: is the length of time an ip address is bound to a pc.
if said pc is removed from the network and the release duration ends the ip is reassigned to a new device, but as long as the device is connected to the network the release duration is renewed and the device holds the same ip.


we select a pc then from `IP configuration` then choose dhcp, without a DHCP it'll automatically use HPIPA.

then we go to the router to start configuring the dhcp server.
`ip dhcp pool pool_name` this'll allow us to configure dhcp after naming the pool
then we can specify the networks included in this pool
`network 192.168.10.0 255.255.255.0`
then we can add a dns server
`dns-server 8.8.8.8`
finally we'll need to add a deafult gateway
`default-router 192.168.10.1`

to exclude some ip range from the dhcp pool we use
`ip dhcp excluded-address 192.168.10.1 192.168.10.20`

if we're to create a pool for routers only, this will allow asignment of two ips per network
```
ip dhcp pool routers
network 192.168.1.0 255.255.255.252
```

we can specify the interface to specify which pool any new router connects, pulls from by manually specifying the ip address:
```
interface g 0/1
ip address 192.168.1.1 255.255.255.252 
```
then we configure the port interface to use the dhcp table
```
interface g 0/1
ip address dhcp 
```
we can configure a relay through the client:
```
ip hdcp relay information trust-all
```
we set up the default route
`ip route 0.0.0.0 0.0.0.0 192.168.1.2`
we set up the default route on the other router through
`ip route 0.0.0.0 0.0.0.0 192.168.1.1`
then we can specify a helper address to allow the passing of dhcp packets
`ip helper-address ip_of_dhcp_server`
we can see the content of the binding table through:
`sh ip dhcp binding`

in case of multiple routers, we'll have one router act as a dhcp server and the other routers use a relay agent to request ip addresses from the dhcp server.
we can renew ip lease in windows cmd:
`ipconfig /release`
`ipconfig /renew`

```
 r1
int g0/0/0
no sh
ip add 10.10.10.1 255.255.255.0
ex
ip dhcp pool aaa
net 10.10.10.0 255.255.255.0
 r2
int g 0/0/0
ip add 192.168.1.1 255.255.255.0
no sh
ex
ip dhcp pool bbb
netword 192.168.1.0 255.255.255.0

 r3
int g 0/0/0
ip add 172.1.1.1 255.255.255.0
no sh
ex
ip dhcp pool ccc
netword 172.1.1.0 255.255.255.0
```
switch configs to specify which of the previous dhcp servers to allow
```
ip dhcp snooping (do not trust any dhcp server)
int f 0/10
no ip dhcp snooping (trusted)
ip dhcp snooping trust
ex
ip dhcp snooping information option
```

## ACL
```
router
int g 0/0/0
ip addr 192.168.1.1/24
no sh
ex

ip access-list standard 10
deny host 192.168.1.20
permit any
int g 0/1
ip access-group 10 out

```