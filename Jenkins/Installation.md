#jenkins/directories
on centOS 8:

first we'll have to install java:
`dnf install java-1.8.0-openjdk-devel -y`

then add jenkins to the repos through:
`wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo`
to verify security key:
`rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key`

updating the yum packages to ensure that we can find it:
`yum update`

finally, we install jenkins:
`yum install jenkins -y`

we reload the available daemons to find it:
`systemctl daemon-reload`
then run its daemon:
`systemctl start jenkins`

to allow it to become publicly accessible we can open the firewall:
`firewall-cmd --permanent --zone=public --add-port=8080/tcp`
then restart the firewall:
`firewall-cmd --reload`


we can modify the port used in jenkins by creating the file:
`/etc/default/jenkins`
and adding command lines arguments to it, however this wont work for jenkins versions greater than 2.332.1.
```
HTTP_PORT=8090
```

alternatively we can use `systemctl edit jenkins` which will bring an empty file where we can add environmental variables and other data to jenkins:
```service
[Service]
Environment="JENKINS_PORT=8888"
```
