microsoft has an equivalent to ether channel called NIC teaming.
it groups multiple NICs and virtualizes them into a single new interface.

NIC teaming works up to 8 NICs in physical interfaces.

Switch Independent Mode: works without configuring the switch, it allows the server to select which interface as input / output

Static Teaming: selects which interfaces for input / output. this has to be configured between the device and the switch.

LACP: link aggregation control protocol, allows communication between the server and the switch to configure Input / output interface automatically.

standby-adaptor allows you to keep one as a backup in case any of the other adaptors fail.

RDP (Remote Desktop Protocol) uses port 3389 to access a windows machine with a GUI. there is a group called Remote Desktop Users Group, if we want a user to allow RDP into it, we add him to said group.

you can add users, groups and users to groups in Computer management.
adding a user to a group occurs through the user properties in the advanced tab.

Firewall:
can exist as either software or hardware.
both will manage the incoming / outgoing traffic.
most firewalls disable ping by default to prevent DDOS attack.
DDOS(distributed denial of server): 