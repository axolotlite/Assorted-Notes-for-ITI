What is meant by cyber security?
It's a field that focuses on securing anything that uses or works with technology.
what is meant by cloud computing?
X service over intranet or internet.
any computing service provided over the internet.
What does CIA stand for?
Confidentiality: The authentication and authorization, this can be achieved through encryption.
Integrity: ensuring data was not manipulated or changed between the source and destination, for example this can be achieved through hashing.
Availability: 

What's the difference between symmetric and asymmetric keys?
symmetric keys use a single key for both encryption and decryption, asymmetric keys use a key for encryption and another for decryption like gpg keys.

What is non repudiation?
this means that the sender cannot deny sending his encrypted traffic.
This is a feature of asymmetric keys, since each encryption key and decryption key used are unique and the decryption key can only work on data decrypted by it's own encryption key.

What is meant by a heartbeat?
it's a method on which nodes in a cluster are monitored to ensure that they haven't shutdown or failed.

What's the difference between the UPS and a Generator?
UPS is a capable of changing power sources while maintaining the operation of the devices connected to it.
since Generators take time to start, UPS powers the machine until the generator turns on.

Security Devices:
##### IDS (Intrusion Detection System): 
Detects threats and alerts the users, it has the ability to inspect the packets passing through it.
##### IPS (Intrusion Prevention System): 
Like an IDS but is capable of taking action to attempt to stop the threat, and if it detects something in the packet it will stop it.
###### Anomaly Mode:
this lets the IPS/IDS learn the normal traffic and protect against anything that is anomalous from the normal traffic.
##### Types of alerts
|          | True                                                          | False              |
| -------- | ------------------------------------------------------------- | ------------------ |
| **Positive** | Detects: Malware<br>File: Malware<br>Alerts user              | Detects: Malware<br>File: Non-Malware<br>Alerts user |
| **Negative** | Detects: Safe FIle<br>File: Non-Malware<br>Doesn't alert user | Detects: Safe File<br>File: Malware<br>Doesn't Alert user                   |
- False Negative: The most dangerous one, since the malware bypassed the security measure and will start causing problems.
- False Positives: This may cause you to inspect the files manually, wasting your time but is over all safe.

#### Firewall:
cannot inspect packets sent through it, as long as they're allowed in the ACLs.
stateful inspection: firewalls keeps the source and destination of a packet during session to keep track of who sent to whom and terminate traffic if it changes.
early negotiation: detecting an attack early before reaching the firewall
WAF (Web Application Firewall):
a firewall specialized in preventing web attacks on the servers, attacks such as SQL Injection, and others.
WAF works to secure http methods, 
what's the difference between ssl and tls?
tls is the enhancement of ssl, it's upgrade. it fixes several security flaws in the original protocol.
how can WAF work with https, since it can't really inspect it?
it can protect against SSL Overloading.
Firewalls are placed before the IPS/IDS since we have 65k ports, reducing most traffic before passing it to the IPS/IDS for inspections, reducing their load.
#### Status Codes:
10X: information
20X: success
30X: redirection
40X: client side error
50X: server side error
##### proxy: 
it's purpose is to hide the ip address, and categorize who has access to which parts of the network.
- Reverse Proxy:
	This one has the API endpoint behind it, and specifies which external devices access which endpoints behind it.
- Forward Proxy:
	This one has a NAT inside its network and allows translation of traffic through it.
##### HSM (Host Security Module): 

### Defense in Depth:
implementation of multiple layers of security, both physical and cyber.

Types of Attacks:
Passive: all attacks start out as passive, it starts by monitoring and information gathering.
Active: this is where the attack takes action such as applying what they've learned from info gathering, targeting ports, snooping and sniffing for more info.
Types of Security Teams:
Blue: defense 
Red: attack
Purple: does both
Types of Attackers:
White: works for the company to find vulnerabilities
Black: works for himself and will steal what he can
Grey: can either work for a company or steal from them, depends on the person.

#### Cloud Deployment Models
##### Private Cloud:
This infrastructure and its contents are managed in house either by the company or a subsidiary
##### Public Cloud:
This is a cloud that we provision from, we manage the provisioned infrastrcture
##### Hybrid Cloud:
We have data(employee data, government data, etc...) that can't be hosted out of house, so we make our own cloud to manage this data but the non-critical infrastructure is hosted in a public cloud.
##### Community Cloud:

SDN:
it separates the control plane from the data plane.

What is meant by Resource Ballooning?
If a host is not utilizing his entire resource pool, a part of it is transferred to another host until the original one asks for it.

SLA (Service Level Agreement):
This is the agreement between the cloud provider and the provisioner for the agreed upon maintenance and shutdown times in a year.
like amazons 99.99% thing.

Hypervisor hijacking:
the injection of the hypervisor to gain access to the host and all its guest machines.
this attack allows you to control the vms or even transfer them to another host.

what is kubernetes?
it's a container orchestration layer.

