`int g 0/0/0`
this is in a router after entering conf
this will turn the interface up
`no shutdown`

then we give it an ip address:
`ip address 192.168.1.1 255.255.255.0`
we can see the interface info through
`sh ip interface` and adding brief makes it brief.

```
int g 0/0/2
ip address 192.168.2.1 255.255.255.0
no shutdown
```
this'll give the network the address of `192.168.1.0`
and it'll allow us to use the routers ip as a default gateway `192.168.2.1`.

`sh ip route`
shows you all the routes on this router.

we will have to configure vlans in the switches using preivous methods
`int f 0/n`
`switchport mode access`
`switch access vlan n`
we can disable the vlan through
`no switchport access vlan n`

to connect two routers together we need to us a `serial cable` 
after we nter the physical router table,
we shut it down, then drag the NIM-2T serial interface cable in one of the open slots before utrning it back on.
this will add two serial ports for use.
careful: shutting down the routers will delete the previous running-configs.

then using the serial cable to connect between routers then enter to select the interface and turn it up.
```
int s 0/0/0
no shutdown
```
on both connected routers, then define an ip for the interface in the same network.