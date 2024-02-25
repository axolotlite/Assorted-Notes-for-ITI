## Team distribution
Team 1: Max, Yasser, Ebtehal, Samuel, Mohanad, farghaly

Team 2: Hamed, Mahmoud, Eman, Mahfouz, Nour, Ashraf

Team 3: Emad, Toka, Shaza, Mohab, Khamis, Mostafa

Team 4: Abdelrahman, Tarek, Arwa, Khaled, Amr, Said

Team 5: Sarah, Hazem, Hussein, Anan, Rowan, Eslam

6 devices, there will probably be switches involved, we can get a hotspot device, creating our own network.

each of our computers will host 2 virtual devices, we'll use bridge networking to connect to the switch.

we'll be given an infrastructure to build, for example
a webserver with 2 sites,
- web1.com
- web2.com
we'll configure the device to host the webservers, a connected user must be able to connect to the webserver through `http.web1.com` or `https.web2.com`.
we'll need to download actual template websites, instead of using simple html.

another example:
several domain controllers, DC1 & DC2 & DC3
DC3: read only, IBI.local(read only), H1(can only login into this machine)
DC2: Child DC, alex.IBI.local
DC1: IBI.local

another example:
PC2 should be able to remote into the DC, there should be a user for example ali, should be able to remote into the DC without being a member of administrator group.
ali should be a user within the DC, we want to be able to remote into the DC after logging into PC1 with ali.

there should be a user named Ahmed@ibi.local, he should be able to login to PC2(who joined the alex.ibi.local domain) 
there should be a user named max@alex.ibi.local, he should be able to login into PC1(who joined the ibi.local)
basically cross rdp into non-affiliated domains.

each two domains will have their own dns
DC1: has web1.com in its domain, have ibi\\PC1(who belonds to DC1) resolve the url.
meanwhile alex\\PC2 should be able to resolve https://web2.com with use of dns.

then we'll deal with PC3: this will be a self-study case.
he wants us to:
- once PC3 is opened it should automatically install windows through WDS(Windows Deployment Server)
then group policies:
we'll create users:
- A1: the group once connected it, it should receive a welcome message "ezayak ya 7oby".
- B1: once he logs in, he'll be asked to change password using complex configuration.
- C2: this guy will need to install winrar on his device, so he requested for us to open his usb, then we told him no, login and logout and the program will be installed on his device. **this will be achieved through a policy.**

group policy, PC1 