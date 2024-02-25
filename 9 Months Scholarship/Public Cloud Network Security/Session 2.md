What is openstack?
it's an open source cloud layer.

what is firewalld?
it's a systemd service responsible for firewall.
what is iptables?
same as firewalld.

what's the difference between firewalld and iptables when handling newly configured rules?
iptables new rules are applied on time, unlike firewalld which will require a rule reload.

what are selinux contexts?
they're used to contain processes within their own limits.

what is .bashrc?
it's a file that is sourced whenever a shell is started.

what are the steps to updating a cluster?
first we determine operation type: active-active or active-passive
then check if the hardware is compatible.
you will have to enter a CAP meeting to plan an update.

then we update it following the n-1 principle, we turn off one node to upgrade it before returning it to the cluster and moving onto the next.
this brings the problem if the newer version component may have issues returning to the cluster and working on it.

What is the point of NTP?
to synchronize the time between connected devices, another reason is to keep the time of logs.

what is the search domain?
the domain that the device in the network belongs to.
for example the device of hostname "user" exists in the domain of "lab.local"
so the whole device name will be "user.lab.local"

what is RDO (Redhat Distributed Openstack)?
it's a tool developed by Redhat that automatically installs openstack on a redhat distribution.

what is the difference between scale up and scale out?
scale up: increase the resources given to a vm to increase its capabilities
scale out: increase the number of VMs providing the same service.

what is amazons hypervisor?
Amazon developed their own hypervisor called: Nitro

what is meant by code packing entropy in reverse engineering?
it's the decay or damage to the code when packing source code, this occurs the more times you pack it.

what is the difference between curl and wget?
wget is mainly used for downloading through http, but it has support for other http functionalities.
but curl is a tool capable of handling many more protocols, and has a larger set of commands.

keystone acts as a service catalogue: it facilitates communication between components through authentication and authorization.

what's the difference between object and block storage?
as the name implies object storage saves data in the form of objects with their metadata.
block storage uses file systems to save data as files in their storage medium.

what are the abstract steps of openstack nova creating a VM?
1) authenticate with keystone
2) nova then receives a request
3) nova then checks the user authorization from keystone
4) after keystone confirms the user permissions and identity it sends the confirmation to nova
5) nova then creates the requested resources.

what's the point of AMQP(Advanced Messaging Queue Protocol) services like RabbitMQ or Qbit in openstack?
These services are responsible for acting as a middle man between the users/services sending the requests and the actual API of the components to control the amount of requests sent and prevent overloading the api endpoint.

what is the purpose of the named api endpoint types in openstack?
- Public: used for business traffic between the clients and the components / services
- Internal: used for communication between the services inside the opens stack cluster
- Admin: used for internal management of openstack cluster components.
How do openstack endpoints communicate when using horizon to login?
you can see three of those in any created component in openstack.
for example loging into horizon:
firs the user opens the web-gui to login:
user -> login to horizon: this uses the `public API` to authenticate with keystone to acquire a token
horizon -> checks user token: uses the `Internal API` to authorize that the given token can login to horizon
what is the role of AMQP in the previous question?
they create a Queue that holds the requests sent to the API, before sending them to their respective services.
in this case, a queue is made for the keystone and horizon APIs to handle sent requests and when they are sent to their API's for use.

what layer does RabbitMQ work on?
it works on the application layer.

the kernel is split into two:
- user mode: the processes running on the kernel in the user space
- kernel mode: the processes running on the kernel that belong to it.

what is the point of external network in Openstack?
it acts as a source for floating ips, neutron network ips and as a gateway from any internal customer networks to access the external network.
what's PAT (Port Address Translation)?
it's a method that transfers traffic through a single ip using available ports on it.
What's NAT (Network Address Translation)?
it's a method that transfers traffic through a single ip address.

what's the difference between hashing, encryption and encoding?
hashing: one way algorithm that converts any text into a hashed string. you're not supposed to be able to return it to the original string.
encryption: a two way algorithm that can be decrypted. 
encoding: changes the format of the string into another one, like base64.

what is app blocker?
it's a windows service that runs powershell scripts to ensure that illegal application don't run on the device.
what are the extensions of powershell scripts?
file.ps1: used to import modules of extensions (psm1 module files, psd1 manifest file)
file.bsd1
file.bat

what is CVE (Common Vulnerability exposure)?
This is the format used for exploit documentation, it is as follows:
(exploit name)-year-number

what are the most known threat intelligence platforms for ips?
https://www.virustotal.com/gui/home/upload
https://talosintelligence.com/
https://www.abuseipdb.com/

what network component can protect you against log4j attacks?
WAF (web application firewall) should be able to detect the false or unacceptable signatures from the payload and prevent its access to the server.
alternatively you could disable logging in apache or disable resolving to prevent the exploit from working.

what's the difference between NAT, Bridge, Host-only networking in vmware?
NAT: translates all internal ip addresses into the host ip
Bridge: takes an ip address from the host subnet and uses it to send packets
Host-Only: it's a private network where only the vms inside the network exist.

What is APIPA addresses?
they are non routable ip addresses that are given to devices when DORA fails to find and acquire an address from a dhcp server.

what is meant by loopback?
it's a virtual interface created for local access and debugging.

What is the VPN?
there are several types of VPNs.
for example MPLS VPN works in both layer 2 and 3, but to enable it you'll need to have the central routers to enable this type of VPNs.
it's a type of tunneling through layer 2, this is fast but it's not very secure.
IPSEC: 
what is the protocol of VPN?

what is the difference between WAF and a firewall?
WAF works on layer 7, it can inspect and inject javascript and delete cookies from the coming HTTP Requests.
firewall works on layer 3 & 4 and only works on packets.

What is meant by devops?
Devops is a methodology, created to solve conflicts between the operations and development teams.
where developments teams work in the pre-development environment, once they finish their work they hand-over their code for the operations team to push it to production.
sometimes this generates conflicts which were the main driving force towards the creation of DevOps, a way to automate parts of the process between both teams.

what are microservices?
they're components of a service distributed across devices and communicate through APIs.
what are most modern microservices built on?
they are built on segmenting parts of the project on their own VMs / Containers.

k8s containers are placed inside pods, where the optimal solution is having a single container placed in a single pod.


what is Ansible?
It's a configuration tool that uses ssh, instead of a specialized agent.
it allows you to configure a collection of hosts using scripts called playbooks.

what is jenkins?
it's a testing tool used in CI/CD.

what's the added features in openshift?
they added security features that scans a pulled image for vulnerabilities before pushing it, and if it's safe without any vulnerabilities the image is pushed onto a repo that renames it "image_name"+"golden_image"
it also added ACLs for container and user communication.


What is the inode table?
it's a table written to the partition containing all the inodes and their mapped physical locations on the drives.
it also contains a counter that lists all the hard links to it, once this counter reaches 0, the inode is deleted and the data is no longer accessible.
what is the inode equivalent to windows ?
Field IDs.
what is the similarities between hard and soft links?
Both of them have to be created on the same partition.

what is meant by vlan?
it's a layer 2 isolation method.

what is the difference between hibernate and sleep?
hibernate moves the current memory into swap / paging file before shutting down and reloading the data from swap into memory once it starts.
sleep/suspend keeps the memory powered on and shuts most other components, so it can resume operations once its power on again.

What is the point of DR (Disaster Recovery)?
It's a may to reduce the effects of natural disasters by having a backup data center that resumes operations of the one currently in crises.

Mail protocol transfer:
the user pushes his mail through MUA which uses either SMTP to transfer through the MTA (Mail Transmission Agents) available on the network until it reaches its mailbox destination.
now, the user can access his mail through IMAP/POP3 protocol which contacts the MAA(Mail Access Agent) to acquire the email.
we specify the endpoint for email target in the DMARC to avoid fake domains and authenticate actual domains.

no-reply@domain.com : are emails sent through something called `Pounces?` which are not accessible from out, since this email does not have valid credentials.

what is PKI (public key infrastructure)?

what is the role of certificate authority?
they are organization specialized in authenticating domains.
they have a public key that is used to verify the validity of a websites private key.

###### TLS Handshake:
it starts with the website sending you the encrypted data of the public key of the website, some info such as the address, your domain history and their certificate domain authority.
you get another public key from the domain authority to decrypt the data given to you from the website, this validates that the website is trusted.
next, the public key given to you by the website is used to encrypt a shared key that will be sent to the webserver, which will first be decrypted using the private key of the website.
finally the shared key will be used to encrypt all traffic between host and webserver.
This entire process was devised to prevent anyone listening to http packets from acquiring or stealing the shared key used in https encryption.

what is kerberos?
it's a security service that works on 3 levels:
- user level
- Authentication level
- server level
first users authenticate on the kerbros server which returns an AS_Reply, causing the user to contact kerbros' TGS (Ticket Granting Service) with a request to access a specific service, then the TGS will check the user authorization from Kerbros before returning:
- a refusal if the user is not authorized
- an acceptance if the user is authorized
- a failure if the user is authorized but the service is not actually present
once the user gets his ticket, he can use it to communicate with the service,  which will check the validity of the ticket from kerbros.

what is a kerbros golden ticket?
it's a ticket that grants the user unlimited access to all services available on kerbros.
what is a diamond ticket?
we drop a golden ticket to steal the paramters from the kerbros to create or modify another golden ticket with whatever permissions we want, giving us access to create more tickets.

all active directory attacks are done through kerbros.