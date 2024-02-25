making a webserver.
we'll need to install IIS(Internet I service)

we'll need a dns server to make it work.

the first 1024 ports(well-known ports) are reserved, as regulated by ICAN.
ports of note:

| protocol | port  |
| -------- | ----- |
| http     | 80    |
| https    | 443   |
| fpt      | 20,21 |
| telnet   | 23    |
| ssh      | 22      |

the next range between 1024 -> 49151 are reserved for user.
ICAN decided to create something called NTLD (New Top Level Domains) domains such as
.movie, .team, .fyi, .shop, .work
each with a yearly registration fee.

turns out linux doesn't keep a local cache.

the steps of DNS resolving:
given a site name, the PC looks inside its cache for the IP address of the site.
a hit, returns the IP.
if it misses, 

logs are saved in `C:/inetpub/logs/`

we can create an ftp server through adding an ftp role, then specifying a folder where files are stored, then we can access it through the same menu as IIS, for installation and configuration

we can create a user through computer management -> local users and computers -> users

now we can connect through the browser, file explorer or cmd (ftp command).

`ftp> open 10.10.10.2`
any other command can be seen through `?`
