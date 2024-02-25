to see routing:  `sh ip route`
it'll show you the available routes and their ports.

to create a route to a router in conf t mode:
`ip route 192.168.20.0 255.255.255.0 192.168.1.1`
now we test ping.

we will need to setup up the same route on the other side.
`ip route 192.168.10.0 255.255.255.0 192.168.1.2`

we can specify the exit interface through:
`ip route 192.168.40.0 255.255.255.0 s 0/1/0`

we can use loopback interface as the equivalent of 127.0.0.1

now to create a loopback interface
`interface loopback 1`
then give it an ip address.
`ip address 192.168.2.1 255.255.255.0`
we can give the loopback any ip address we want
then route everything through it, by default.

`change cdp entry protocol`
we can specify the routing protocol through:
`router protocol`
there is a pcl called `rip`
to stop the protocon we can use no
`no router protocol`
then in the configuration table, we specify the router-connected networks that will use this protocol
`network 192.168.1.0`
`network 192.168.2.0`
you can change the `rip` version through:
`version n` there are two versions 1 and 2.

configs:
```
int g 0/0/0
no shutdown
ip address 192.168.10.1 255.255.255.0
int s 0/1/0
no shutdown
ip address 192.168.1.1 255.255.255.0
router rip
network 192.168.1.10 (network belonging to the router)
version 2

```

we can use tracert to find the hops.