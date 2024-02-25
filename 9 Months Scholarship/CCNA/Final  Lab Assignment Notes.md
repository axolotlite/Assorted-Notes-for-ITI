first, we count the vlans and the switches.
Vlans:

| Left side   | right side |
| ----------- | ---------- |
| 10,20,30,40 | 50,60,70,80,90,100           |

Vlan Assignment:

| Vlan Number    | network address  | Devices                        |
| -------------- | ---------------- | ------------------------------ |
| 10             | 192.168.10.0/24  | PCA                            |
| 20             | 192.168.20.0/24  | PCB,PCE                        |
| 30             | 192.168.30.0/24  | PCD,PCH                        |
| 40             | 192.168.40.0/24  | PCX                            |
| 50,60,70,80,90 | 192.168.50.0/24  | Laptop0->2,PC-vlan80,PC-vlan90 |
| 100            | 192.168.100.0/24 | internal-server                               |

we start with layer 2 configs (switches) before configuring the routers.
- creation of vlans on all switches (use vtp if possible)
	using VTP, we'll use two main vlans: S1 and S4, enable telnet / ssh for ease of configuration using an added admin PC.
	Then S5 will have its own configuration.
- vlan port assignment
- create an stp to prevent looping
	This will be applied on S1,S2,S3
- configure the ether channel
	This will be between S1 and S3
- assign ips for the devices from subnets

| PCs     | ip address |
| ---------- | ---------- |
| PCA-Vlan10 |            |
| PCB-Vlan20 |            |
| PCD-Vlan30 |            |
| PCE-Vlan20 |            |
| PCH-Vlan30 |            |
| PCX-Vlan40 |            |
| PC-vlan80 |            |
| PC-vlan90           |            |

| server        | ip address |
| ------------- | ---------- |
| Public Server |            |
| Internal Server             |            |

| laptop         | ip address |
| -------------- | ---------- |
| laptop0-vlan70 |            |
| laptop1-vlan50 |            |
| laptop2-vlan60               |            |
### R1
 | interface | ip address |
 | --------- | ---------- |
 | G 0/0/1    |            |
 | G 0/0/0    |            |
 | S 0/1/0          |            |

### R2
 | interface | ip address |
 | --------- | ---------- |
 | S 0/1/1    |            |
 | G 0/0/0    |            |
 | S 0/1/0          |            |

### R3
 | interface | ip address |
 | --------- | ---------- |
 | G 0/0/0    |            |
 | S 0/1/0          |            |

### R4
 | interface | ip address |
 | --------- | ---------- |
 | G 0/0/1    |            |
 | G 0/0/0    |            |
 
| Switch | ip address |
| ------ | ---------- |
| S1     |            |
| S2     |            |
| S3     |            |
| S4     |            |
| S5     |            |
| S6       |            |

we'll do the subnets and their configs on our own
this will apply for both left and right sides of the lab.

next step we enter the routers
- set the default root
- set ospf where its located
- configure acls
- dhcp server configuration
- nat addressing configuration

you can check if it works if you ping all devices in accordance to the acl configuration.
