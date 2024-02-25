I've created a set of scripts that simulate the exam environment.
There are 3 hosts:
lab a, b and a classroom serving the repo.
#### First Lab a Problems:
#### 1-Resetting root
first we start by modifying the kernel boot parameters during runtime
![[ITI/9 Months Scholarship/RedHat 1/Untitled/p1.png]]
Then we change the root password
![[ITI/9 Months Scholarship/RedHat 1/Untitled/p2.png]]
#### 2- Create a repository File
since I've setup a classroom server, i'll be using it to download the packages.
![[ITI/9 Months Scholarship/RedHat 1/Untitled/p3.png]]
#### 3-Create a swap partition of 512M
I'll be creating a swapfile
![[ITI/9 Months Scholarship/RedHat 1/Untitled/p6.png]]
then setting a file system and setting it on
![[ITI/9 Months Scholarship/RedHat 1/Untitled/p7.png]]
finally make this swap partition persistent
![[ITI/9 Months Scholarship/RedHat 1/Untitled/p8.png]]
#### 4- Logical Volumes
first we add a virtual disk of 10Gbs to the virtual  then partition it
![[add_disk.png]]
using cfdisk i partitioned it
![[cfdisk_partition_disk.png]]
result
![[partition_disk.png]]
then we create the volume group with an extent size of 8Mbs
![[create_vg.png]]
then, create a volume group of extent size 50
![[create_lv.png]]
finally we mount the logical volume
![[mount_lv.png]]
#### 5- Resize the logical volume by adding 100 extents.
![[resize_lv.png]]
#### 6- Set the recommend tuned profile for your system.
first we install tuned.
![[tuned_1.png]]
then enable it
![[tuned_2.png]]
finally, we check the recommend profile before setting it up
![[tuned_3.png]]
#### Lab B Problems:
#### 1- Configure the network
first we set the hostname `ahmed-said`
![[set_hostname.png]]
next, we use nmcli to set a static ip address alongside the rest of the network data.
note: I added two addresses(exam request and current ip address) to prevent the ssh session from crashing.
![[set_network.png]]
#### 2- create a repo file
since I've already pre-compiled a special httpd package that comes pre-configured to work on port 82, i'm going to use it through the custom repo.
![[set_repos_2.png]]
#### 3- configure selinux
first we install the custom httpd package

![[selinux_httpd_1.png]]
then we verify the configured port
![[selinux_httpd_2.png]]
next we configure selinux and the firewall to allow httpd traffic through this port.
![[selinux_httpd_3.png]]
![[selinux_httpd_4.png]]
finally add an index.html and ensure correct selinux permissions on all files in the directory before starting httpd service.
![[selinux_httpd_5.png]]
#### 4- Create the following users, groups and group memberships:
![[user_groups.png]]
#### 5- Create a collaborative directory /common/admin with the following characteristics:
![[group_dir.png]]
#### 6- Configure autofs to automount the home directories of production5 domain users.
I've set up nfs using the script, but I couldn't get it to work except once before resetting the VM to continue setting up the initialization scripts.
good thing it's not part of the exam.
#### 7- The user harry must configure cron job that runs daily at 12:30
![[crontab.png]]
#### 8- Configure your system so that it is an NTP client of classroom.example.com
![[chrony.png]]
#### 9. Locate the Files created by sarah
since I'm supposed to create the user sarah in the exam, I've configured the script to automatically create another user by the name "farah" and then distribute all her files randomly.
so, i'll be using "farah" instead.
![[find_files.png]]
#### 10. Find the string
the production users are created by the nfs init script.
![[grep_home.png]]
#### 11- Create an user account
![[user_alies.png]]
#### 12-Create a tar archive file
![[tar.png]]
#### 13 & 14 containers.
the script i've written sets up a container registery, but i didn't prepare a container file.
also, it's not part of the exam.
#### 15 MISC
1) set umask
   ![[permissions.png]]
2) expiry date
   ![[expiry_date.png]]
3)  assign sudo privs
   ![[admin_privs.png]]
4) custom login greeting message
   ![[alies_login.png]]
5) create script
setting the suid fails.
![[last_one.png]]
running the script as root works.
![[last_one_2.png]]