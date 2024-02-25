
global catalog: it is an index that allows searching for all objects available in the forest. 
you can install one on both the main DC or one of its replicas.
RODC: Read only Domain Controller
this is a copy of the database that's on the main domain controller, and as the name implied, it's read only.
allowing reading of user data without writing.
RODC server cache the login passwords, saving them whenever a new user logins into a device in its domain.
however, caching opens us to a vulnerability as it may save the admin password, leaving the device unsafe for use.
this was solved by preventing the caching of the admin password, instead it authenticates the password from them main server to allow logging into the device.

there is also a choice to select a group of users to save their passwords in a local cache on the RODC server.

you can also delegate control, allowing for some permissions from administrative control without giving them total admin access.

we can disable this account from the users -> properties -> account -> `account is disabled`

In a subdomain, the child database is different from the root controller.
enterprise admin (The admin of the root controller in the forest) can access and work on any subdomain.

Tasks:
- offline join NTDS
We can offline join a NTDS server, this of occurs happens without being connected with the forest domain.
and once connectivity is established, the data is transferred between them.
steps:
first, disable the NIC of the Device you want to offline join with.
this is a task we're supposed to do.

- child domain controller
create a child domain, disjoin PC 1 from the root domain, then proceed to enter it onto the child domain then try to login to a PC in the main domain using a child domain account.
