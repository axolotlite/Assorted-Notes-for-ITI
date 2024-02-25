ripv2 uses multi-casting while v1 uses broadcasting.

OSPF uses bandwidth instead of hop length to calculate the optimal route.

wild card subnet has all the bits of a network as 0 and all the bits of a host as 1.
it's the opposite of a subnet mask.
its basically the inverse of a subnet mask.

first we enter configuration then specify the routing protocol
`rotuer ospf 10`
10 here being the process id, it's router specific that has nothing to do with routing.
then specify the neworks to use
`network ip-address wilecard-bits area area_id`
`network 192.168.20.0 0.0.0.255 area 0`
another network
`network 192.168.30.0 0.0.0.3 area 0`
another one
`network 192.168.10.0 0.0.0.255 area 0`

you can see your ospf neighbors by using
`sh ip ospf neighbor`

we can manually configure router-id inside the ospf config by using:
`router-id ip-address`

ip ospf priority n(0-255)

interface loopback

passive interfaces.
this will distribute the default root.
`default-information originate`

then we create the default root
`ip route 0.0.0.0 0.0.0.0 loopback 1`
the number n is used for all routers that share the same autonomous system
`router eigrp n`
then we specify the networks
`network 192.168.1.0 wild-card-bits`
auto-summary

router rip
default-information originate

redistribute static

redistribute eigrp 1
network 192.168.4.0
then exit to configure the router
router eigrp 1

this sends eigrp data through another protocol.
redistribute rip metric 1000 something something something

---
router rip
networks
redistribute eigrp 1 metric 1
exit

router egigrp 1
networks
redistribute rip metric bandwitdth delay reliability reload mtu
