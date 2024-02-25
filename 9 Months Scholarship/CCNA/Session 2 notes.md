commands:
to config the switch we need to be in config mode through admin mode
enable -> configure terminal

to change the hostname in config mode we use `hostname new_name`
to configure the console we use `line console 0` to change the tty for 0.
to change the password we use `password` each tty can have their own password.
after doing that we need to append `login` command.

`line vty` is for remote connections, we can configure from 0-15 connections.
`line vty 0 n` to specify which connections to configure
to specify the protocol to accept taking we use `transport input protocol`
for telnet:
`transport input telnet`
as usual we use `login` command after configuring a password.

we can configure an ip through terminal by using:
`interface vlan 1` to select the first vlan interface
then use ip address with the ip and subnet.
`ip address 192.168.1.100 255.255.255.0`
finally we open it by removing the shutdown for that specific interface through:
`no shutdown`
now we can connect through telnet from any other device.
but through telnet you won't be able to login into privilege mode without configuring a password.
which can be done through the main console by entering privilege mode and create a password through:
`enable secret password`
in the config mode, this will be encrypted.

we can disable translating wrong commands in a domain server through:
`no ip domain-lookup`

we can give the switch the domain name it belongs to through:
`ip domain-name iti.local`
we can even create a username for ssh through:
`username your_name secert your_password`
next we create the encryption key through crypto:
`crypto key generate rsa`
this creates a key named (hostname).(domain)
then we enable ssh through `line vty n m` and specify the lines.
`transport input ssh` then `login domain_name` in this case `login local`

vlan related commands:

we enter privilege mode, do the usual cofiguration.
then specify an interface, specifically the port
`interface fastEthernet 0/1`
then we go into an access mode
`switchport mode access`
before assigning it to a vlan we create a vlan
`vlan 10`
then, we can name said vlan
`name ITI`
we can check the vlan info using `show vlan`
now, to assign it ports through `interface f 0/1`
then we assign it to the specific vlan
`switchport access vlan 10`

to assign a range instead of a single port we can do this
`interface range f 0/2-5` this configures ass ports from 2 to 5
then `switchport mode access` after that `switchport access blan 10`

we can automatically create a vlan using switchport.
`switchport access vlan n` this creates a vlan with the id n, with the selected ports.
then we can name it using `vlan n` and `name new_name`

separating ports by vlans will make them inaccessible to each other.

we can trunk switches in configuration, to connect vlans together
we can use a high throughput port like
`interface gigaEthernet 0/1`
this can be achieved by switching port mode into trunk
`switch port mode trunk`
then put this port in the native vlan (we specify the native vlan here)
`switch trunk vlan native vlan 99`
then specify which vlans are allowed to route their traffic in the native vlan
`switchport trunk allowed vlan 10,20,30,n`
this will allow vlans to be connected across blans
