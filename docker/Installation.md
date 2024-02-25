Centos doesn't have docker in their repos by default
they use podman.
so we must do the following:

first, we must setup the repo:
Install the `yum-utils` package (which provides the yum-config-manager utility) and set up the repository.


 `sudo yum install -y yum-utils`
 `sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo`
then we install it:
`sudo yum update`
`sudo yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

finally we start the dockerd.
`sudo systemctl start docker`