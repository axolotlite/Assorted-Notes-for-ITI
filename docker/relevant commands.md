`docker run -it <image name> <command to execute>`
To get the shell, we will execute bash as a command. The options i & t are used to provide an interactive mode and a pseudo tty terminal.

`docker commit -m "<commit message>" <container_id/name> <new_image_name>:<version>`
When you commit the container, a new image is created and you can push that image to the registry. Anybody can fetch the image and will have the same code with a consistent environment. This also helps in deployment as well.
the podman equivalent
`podman commit -f=docker -m "<commit message>" <container_id/name> <new_image_name>:<version>`