Interview questions you may get asked:

What is the boot process from pressing the power button to the moment the machine starts?
The BIOS, depending on the generation it'll go either through the legacy boot or UEFI boot sequence.
first, it goes through POST (Power On Self Test) to check in order:
1) CPU: writes its data to the ROM
2) RAM: 
3) VGA
4) BOOT: finds the storage mediums, checking its partitioning style to find whether its MBR (for legacy and UEFI boot) or GPT (for UEFI Boot only)
MBR: once boot sequence finishes it finds the partition containing the boot loader to start the boot sequence
GPT/UEFI: has a specific partition that is called the EFI partition on which the bootloader and other specific variables exist
after the boot loader is selected, if it's the grub bootloader it'll start the kernel as process 0 then start the "init" service(from redhat 1-6) or systemd (redhat 7 til now) as process 1, starting the run level (there are multiple run levels that you can configure, the default is run-level 5)
There is a chip called ROM that contains the BIOS data.

MBR allows for only 4 primary partitions, meaning if we have 4 drives: C, D, E, F.
we cannot increase or reduce sizes of each partition unless they're sequentially related, for example: C can move its empty space to D but can't to E, because D is in between them.
unlike GPT which create logical partitions which allow us to transfer empty spaces.
MBR Partitioninig

| ppo  | pp1 | pp2 | pp3 |
| ---- | --- | --- | --- |
| data | data    | data    | data    |
MBR with extended partition

| ppo  | pp1  | pp2  | Extended                                                                                                                                |
| ---- | ---- | ---- | --------------------------------------------------------------------------------------------------------------------------------------- |
| data | data | data | This saves a piece of the space to record the data of the internally created parition table inside this extended partition<br>\|ep0 \|ep1  \|<br>\|data\|data\| | 
what's the difference between firmware and software?
firmware is hardware specific code designed for the device, it's hardware specific.
software is multi-function and can be used on difference devices.

what are the network protocols used by the DNS?
first of all, it uses port 53 (by default) or 6513 (over ssl/tls)
it's designed to use both UDP and TCP.
UDP: is used during querying for a URL
TCP: is used when we need replicate from the Primary DNS to a secondary DNS.
for example when searching for a URL, you'd prefer to get the IP of the url, so UDP is used to ensure speedy resolution.
but when two DNS, want to replicate data, they use TCP to ensure no record loss or corruption.
DNS is separated into zones:
- forward:
	Contains 1 record type (PTR) which is responsible for returning a URL when given an IP address
- reverse:
	There are several types of records here:
		- AAA -> IPV4  (used for search indexing)
		- AAAA -> IPV6 (used for search indexing)
		- ns -> DNS
		- MX -> mail exchange
		- Srv -> Service
		- cName -> Cannonical Name (main name of the host DNS responsible for reaching that specific domain, like yaho.com instead of its actual name which is far longer)
		- Alias -> alternative name for a host

What are the steps to getting an ip address of a URL?
Recursive DNS Query: it's called that because each resolution will return another domain to ask about the URL until the URL itself is return.
first it looks for the ip address in the cache 
then it goes through the hosts file, to find the ip
third, the resolver of the PC will contact the root dns to ask for the TLD (top level domain) responsible for the domain (.com, .org, .net) which will return the address of the Authoritative DNS which is responsible for all the servers within the specified domain, after contacting it, itll return to the resolver the main DNS responsible for it, or the ip address of the URL.
finally after the ip is found it's cached.

What is DHCP?
it's a protocol responsible for transferring the network configuration to any newly connected device in a network.
first, the newly connected device will send a **Layer 2** Broadcast containing it's mac address to **Discover** if there is a DHCP server in the network.
then, the DHCP Server will return a **Layer 3** broadcast and a **Layer 2** unicast message offering the DHCP server info, to prevent any other DHCP server from contacting the device to offer another IP address
then, the device will send both a **Layer 2 & 3** broadcast for the ip address the device wants to acquire, to prevent any other device from taking that IP address and causing a conflict.
finally an acknowledgement is sent from the DHCP server, which can either be unicast to the requesting device, or multi-cast to both the requesting device and any other DHCP server in the network.

Routers don't allow broadcast messages, then how does DHCP work through it?
Through something called DHCP relay agent, which allows any DHCP broadcast requests to just reach the DHCP server without causing an issue through broadcasting.

What are the TCP handshake stages?
1) Syn (Synchronization):
	This is sent when we establish a connection
2) ACK (Acknowledgement)
	This is sent when we want to acknowledge / confirm that the previous package was received correctly.
	If no ack is received that means that the previous packet failed, so resend the package.
3) FIN (Finish)
	This is sent once the connection ends correctly, no errors occur in transmission.
4) RST (RESET)
	This occurs if an error occurs during communication, it either terminated incorrectly or abruptly before finishing transmission (data lost or discarded).
	This is a request to restart / re-establish communication.
5) PUSH 
	Sends data in sequence in the buffer.
6) URGENT
	Special request that bypasses the buffer, causing the data to be sent directly without waiting for the sequence.
what are the Firewall DROP / DENY Policy effects on a TCP packet?
Drop policy returns a RST / ACK packet
Deny doesn't return anything.

What is the difference between the OSI and TCP/IP models of network visualization?
OSI is the reference model used to explain networking as a framework
TCP is the standard reference model that is an actual practically implemented model in networking.

What is the application layer responsible for?
it's the interface between the user and the application and it provides the data given to the presentation layer.
What is the presentation layer responsible for?
it's responsible for finding the specific format of the data to display it for the user. 
for example data comes, presentation finds the data type, for example a PNG image, then displays the PNG image.

what is the transport layer responsible for?
it's responsible for determining the protocol type, receiving the segment 

Which layer is responsible for encryption?
There is no dedicated layer for encryption, depending on the protocol, the layer responsible for encryption changes.
#### Layer 7,6,5 is called data
#### Datalink: frames
#### Physical: stream of bits
What are the components of a packet?
the headers that identify the packet, like it's state.
the payload which is the actual data contained in the packet.

what is meant by an active directory domain?
its a logical boundary 
what is meant by a forest in active directory?
it's a security boundary, which is also the root of all domains contained within it.
what is meant by active directoy?
it's a type of database containing all objects inside a domain?

which port does ping use?
ping has no port, since it uses ICMP which is based on layer 3 and ports are layer 4.

how does ping work?
it operates on ICMP through an `echo 9` request, which is replied to by an `echo 0` reply.

What is the NTDS in active directory?
it's the database inside the active directory.
Why are the group policies saved inside sysvol ?
because anytime a new policy is applied, the `sysvol` is flushed to apply the new policies without having to reload the entire NTDS database.

can windows home edition enter a domain?
no, it cannot. 
this feature is available in enterprise editions like professional and ultimate.

what is meant by domain controller?
the centralized machine managing the active directory services.

what is meant by LDAP?
Light weight directory protocol, it's responsible for querying user information within an active directory.

what is kerberos?
it works on 3 different things: client, KDC, 