1-Basic configuration on all Devices
### Switches:
first: we select S1 and S4 and apply the following to them:
```
en
conf t
hostname S1
vtp domain left.side
vtp password left
vtp mode server
vtp version 2
int f 0/6
switchport mode trunk
```

```
en
conf t
hostname S4
vtp domain right.side
vtp password right
vtp mode server
vtp version 2
int g 0/2
switchport mode trunk
```
this will apply to S2 & S3
```
en
conf t
hostname S{2/3}
vtp version 2
vtp mode client
vtp domain left.side
vtp password left
```
as for S6:
```
en
conf t
hostname S6
vtp version 2
vtp mode client
vtp domain right.side
vtp password right
```
finally
S5:
```
en
conf t
hostname S5
```
Routers:
## R1
```
en
conf t
hostname R1
int s 0/1/0
ip address 192.168.1.1 255.255.255.252
no shutdown
int g 0/0/0
no sh

int g 0/0/1
ip add 40.40.40.1 255.255.255.0
no sh

int g 0/0/0.10
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0

int g 0/0/0.20
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0

int g 0/0/0.30
encapsulation dot1Q 30
ip address 192.168.30.1 255.255.255.0

int g 0/0/0.40
encapsulation dot1Q 40
ip address 192.168.40.1 255.255.255.0
```
## R2
```
en
conf t
hostname R2
int s 0/1/0
ip address 192.168.1.2 255.255.255.252
no shutdown
int s 0/1/1
ip address 192.168.2.1 255.255.255.252
no sh
int g 0/0/0
ip add 192.168.50.1 255.255.255.0
no sh
```
## R3
```
en
conf t
hostname R3
int s 0/1/0 
ip address 192.168.2.2 255.255.255.252
no sh
int g 0/0/0
ip address 192.168.100.1 255.255.255.0
no sh
```
## R4
```
en
conf t
hostname R4
int g 0/0/1
ip address 40.40.40.2 255.255.255.0
no shutdown
int g 0/0/0
ip address 100.100.100.1 255.255.255.0
no sh
```
2-create vlans 10,20,30,40,50,60,70,80,90,99,100
first, we head to S1, to create vlan10->vlan40
```
vlan 10
vlan 20
vlan 30
vlan 40
```
then we apply the vlans to each device on the network, starting with:
S1:
```
int f 0/23
switchport access vlan 20
int f 0/24
switchport access vlan 10
```
S2:
```
int f 0/23
switchport access vlan 20
int f 0/24
switchport access vlan 30
```
S3:
```
int f 0/23
switchport access vlan 30
int f 0/24
switchport access vlan 40
```
then, we head to S4, to create vlan50->vlan90
```
vlan 50
vlan 60
vlan 70
vlan 80
vlan 90
```
after which we assign vlans to their corresponding interfaces:
S4:
```
int f 0/1
switchport access vlan 70
int f 0/6
switchport access vlan 50
int f 0/20
switchport access vlan 60
```
S6:
```
int f 0/13
switchport access vlan 90
int f 0/21
switchport access vlan 80
```
finally in S5:
```
int g 0/2
switchport access vlan 100
```
3-vlan 99 is the management vlan 192.168.99.0/24
TODO

4-configure etherchannel between S1,S3
first, we configure both S1 & S3
```
en
conf t
int r f 0/1-4
channel-group 1 mode active
int port-channel 1
switchport mode trunk
```
5-per-vlan stp S1 the primary of vlan 10,30 and  S2 The primary of vlan 20,40  and S3 the secondry of vlan 10,20,30,40
first S1
```
en
conf t
spanning-tree mode pvst
spanning-tree vlan 10,30 root primary
```
then S2
```
en
conf t
spanning-tree mode pvst
spanning-tree vlan 20,40 root primary
```
finally S3
```
en
conf t
spanning-tree mode pvst
spanning-tree vlan 10,20,30,40 root secondary
```
6-perfom subnetting of  192.168.50.0/24 , subnet 0 for vlan 50 , subnet 1 for vlan 60 , subnet 2 for vlan 70 , subnet 3 for vlan 80 
subnet 4 for vlan 90

we need 5 subnets, using approximation 2^3 = 8 subnets.
so we'll have to reserve 3 bits for the subnet and the rest of the 8 bits will go to the ip addresses.
255.255.255.224/27
each network will contain 2^5 = 32 ip addresses

| subnet num | vlan | subnet ip      | first ip | last ip | broadcast |
| ---------- | ---- | -------------- | -------- | ------- | --------- |
| 0          | 50   | 192.168.50.0   | .1       | .30     | .31       |
| 1          | 60   | 192.168.50.32  | .33      | .62     | .63       |
| 2          | 70   | 192.168.50.64  | .65      | .94     | .95       |
| 3          | 80   | 192.168.50.96  | .97      | .126    | .127      |
| 4          | 90   | 192.168.50.128 | .129     | .158    | .159          |
to apply the previous calculations we'll have to configure both the switch and the router.
first S4:
```
en
conf t
int g 0/1
switchport mode trunk
```
then R2:
```
en 
conf t
int g 0/0/0
no sh

int g 0/0/0.50
encapsulation dot1Q 50
ip address 192.168.50.1 255.255.255.224

int g 0/0/0.60
encapsulation dot1Q 60
ip address 192.168.50.33 255.255.255.224

int g 0/0/0.70
encapsulation dot1Q 70
ip address 192.168.50.65 255.255.255.224

int g 0/0/0.80
encapsulation dot1Q 80
ip address 192.168.50.97 255.255.255.224

int g 0/0/0.90
encapsulation dot1Q 90
ip address 192.168.50.129 255.255.255.224
```

7-apply dynamic routing with ospf protocol 
we must configure OSPF on R1,R2,R3,R4.
so, first we start with
R1:
```
en
conf t
router ospf 10
network 192.168.1.0 0.0.0.3 area 0
network 40.40.40.1 0.0.0.255 area 0
network 192.168.10.0 0.0.0.255 area 10
network 192.168.20.0 0.0.0.255 area 10
network 192.168.30.0 0.0.0.255 area 10
network 192.168.40.0 0.0.0.255 area 10
```
R2:
```
en
conf t
router ospf 10
network 192.168.1.0 0.0.0.3 area 0
network 192.168.2.0 0.0.0.3 area 0
network 192.168.50.0 0.0.0.31 area 20
network 192.168.50.32 0.0.0.31 area 20
network 192.168.50.64 0.0.0.31 area 20
network 192.168.50.96 0.0.0.31 area 20
network 192.168.50.128 0.0.0.31 area 20
```
R3:
```
en
conf t
router ospf 10
network 192.168.2.0 0.0.0.3 area 0
network 192.168.100.0 0.0.0.255 area 30
```
R4:
```
en
conf t
router ospf 10
network 40.40.40.0 0.0.0.255 area 0
network 100.100.100.0 0.0.0.255 area 0
```
8-default route loopback 1 on  R2
```
en 
conf t
interface loopback 1
ip add 1.1.1.1 255.255.255.0
ip route 0.0.0.0 0.0.0.0 loopback 1
```
9-R1 IS THE DHCP server
we'll need to configure each vlans pool with its router ip address within R1.
```
en 
conf t

ip dhcp pool vlan10
default-router 192.168.10.1
network 192.168.10.0 255.255.255.0

ip dhcp pool vlan20
default-router 192.168.20.1
network 192.168.20.0 255.255.255.0

ip dhcp pool vlan30
default-router 192.168.30.1
network 192.168.30.0 255.255.255.0

ip dhcp pool vlan40
default-router 192.168.40.1
network 192.168.40.0 255.255.255.0

ip dhcp pool vlan50
default-router 192.168.50.1
network 192.168.50.0 255.255.255.224

ip dhcp pool vlan60
default-router 192.168.50.33
network 192.168.50.32 255.255.255.224

ip dhcp pool vlan70
default-router 192.168.50.65
network 192.168.50.64 255.255.255.224

ip dhcp pool vlan80
default-router 192.168.50.97
network 192.168.50.96 255.255.255.224

ip dhcp pool vlan90
default-router 192.168.50.128
network 192.168.50.127 255.255.255.224
```
then each router will need the ip address of the DHCP server, in this case, R1 in the external network.
R2:
```
en
conf t
int g 0/0/0.50
ip helper-address 192.168.1.1
int g 0/0/0.60
ip helper-address 192.168.1.1
int g 0/0/0.70
ip helper-address 192.168.1.1
int g 0/0/0.80
ip helper-address 192.168.1.1
int g 0/0/0.90
ip helper-address 192.168.1.1
```
10-Vlan 10,30,50 can't ping the Hosted Server but can perform browsing , Vlan 20,40,60 can't browsing the Hosted Server but can perform ping
first, we configure blocking ping (icmp) from vlan 10,30,50
in R1:
```
en
conf t
access-list 110 deny icmp 192.168.10.0 0.0.0.255 host 100.100.100.100
access-list 110 deny icmp 192.168.30.0 0.0.0.255 host 100.100.100.100
access-list 110 deny icmp 192.168.50.0 0.0.0.31 host 100.100.100.100

access-list 110 permit ip any any

int g 0/0/1
ip access-group 110 out
```
then we block the http port from being accessed in R1:
```
en
conf t
access-list 120 deny tcp host 100.100.100.100 eq 80 192.168.20.0 0.0.0.255
access-list 120 deny tcp host 100.100.100.100 eq 80 192.168.40.0 0.0.0.255
access-list 120 deny tcp host 100.100.100.100 eq 80 192.168.50.32 0.0.0.31

access-list 120 permit ip any any

int g 0/0/1
ip access-group 120 in
```
11-static nat g0/0/1 on R1 translate to Internal Server IP 
we will simply give the server the ip 40.40.40.100
in R1:
```
en
conf t
ip nat inside source static 192.168.100.100 40.40.40.100
```
12-Vlan 10,20,30,40,50,60,70,80,90 Pat  configuration

finally in R1:
```
en 
conf t
access-list 10 permit 192.168.10.0 0.0.0.255
access-list 10 permit 192.168.20.0 0.0.0.255
access-list 10 permit 192.168.30.0 0.0.0.255
access-list 10 permit 192.168.40.0 0.0.0.255

ip nat inside source list 10 interface g 0/0/0.10 overload
ip nat inside source list 10 interface g 0/0/0.20 overload
ip nat inside source list 10 interface g 0/0/0.30 overload
ip nat inside source list 10 interface g 0/0/0.40 overload

access-list 20 permit 192.168.50.0 0.0.0.31
access-list 20 permit 192.168.50.32 0.0.0.31
access-list 20 permit 192.168.50.64 0.0.0.31
access-list 20 permit 192.168.50.96 0.0.0.31
access-list 20 permit 192.168.50.128 0.0.0.31

ip nat inside source list 20 interface g 0/0/1 overload

int g 0/0/1
ip nat outside

int g 0/0/0.10
ip nat inside
int g 0/0/0.20
ip nat inside
int g 0/0/0.30
ip nat inside
int g 0/0/0.40
ip nat inside

int s 0/1/0
ip nat inside

int g 0/0/0.10
ip nat inside
int g 0/0/0.20
ip nat inside
int g 0/0/0.30
ip nat inside
int g 0/0/0.40
ip nat inside

```