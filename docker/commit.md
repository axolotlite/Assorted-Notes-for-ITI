You enter a docker containers through and interactive shell
`docker -it container_name shell`
Then do whatever you want to do inside of it.
finally, you exit the container, get its ID or name Then commit your changes into a new image
`docker commit -m 'commit message' container_name new_image_name:version`
i need to emphasize the difference between containers and images. because it's important.