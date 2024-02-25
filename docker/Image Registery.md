#docker/commands 
#docker/direcotries 
its a registery used to store docker images to store and share docker images, they can either be public or private images.

Dockerhub is a public registery, that anyone can use. it's the default location docker looks for images.

you can even create your own registry using docker trusted registry service.

most cloud services provide you with container registeries of their own.

each image can be named and tagged. so each version can have multiple tags each can be used to pull the image.
tags such as
- latest: is reserved for latest version of the software, it is also the default tag of a built image
image naming convention:
image_registry/acount_name/image_name
example:
- image_registry: docker.io
if the account name is not given, docker assumes that both the account and image name are the same.

authenticating into registeries is only needed when dealing with private registries.
this can be done through
`docker login image_registry`
this saves the commands into `$HOME/.docker/config.json`