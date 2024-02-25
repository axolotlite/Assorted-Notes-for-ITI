#docker/commands 
#docker/flags 
#docker/direcotries 
```
Setting up a host to 0.0.0.0 is required if you are running the app inside the container and want to access it outside. If you change it to anything else, you won’t be able to access the app from the host machine
```
the dockerfile is an instruction argument format.
each line instructs docker to do a specific action with arguments explaining this action.
each line of the following instructions creates a new layer. with the applied command.
each layer is cached, in case any step fails, so it'll reproduce the previous layers from cache once a layer fails.
## Building a dockerfile
`docker build -t image_name:version build_context/location`
## . / build_context
the build context can be anywhere, even on different docker daemon hosts.
during the build, the files are temporarily moved inside the docker deamon directory
`/var/lib/docker/tmp/docker-builderxxxxxxxxxxxx`
you can add a dockerignore file to prevent these files from being send to a docker daemon.
you can specify a git repo for docker to clone and build from, you can even specify a directory inside it.
`docker build git_repo_url`
`docker build git_repo_url#branch_name`
`docker build git_repo_url:folder_name`
you can even specify the exact dockerfile needed for the build
`docker build -f Dockerfile.dev git_repo_url`
Example: While building a docker image from code stored in a remote URL, which command will be used to build from a directory called docker in the branch dev?
`docker build https://github.com/kk/dca.git#dev:docker`
## ENV
`ENV <key>=<value> ...`
The ENV instruction sets an environment variable required for the app.
It allows multiple key values
It persists for the image whenever it is run.
Setting the host to 0.0.0.0 means we can access the app using any IP within the container.
you can inspect the environment variables using `docker inspect <id>` and modify them using `docker run --env <key>=<value>`
During builds we can use arg, which doesn't persist after the build stage.

## WORKDIR
The WORKDIR instruction sets a working directory for other Docker instructions such as RUN and CMD.
it basically changes the current directory.
If we do not specify a working directory, we have to provide a full path for running our app file while using the RUN instruction.

## FROM
The FROM keyword tells Docker which parent image to use or what should be the main platform for this image.
each image must be based on another image
unless it uses the keyword 'scartch' which is a reserved image name.
`FROM scratch`
which means that there is no base. it is the top most parent image. 
example of debian parent
```dockerfile
FROM scratch
ADD rootfs.tar.xz /
CMD ["bash"]
```
we can name the image created using the `AS` flag in multi-stage pipelines
`FROM node AS builder`

## ARG
This allows us to create a variable inside the dockerfile context, which we can refer to in other docker instructions by using the $ sign
this var is removed from the image after the build is complete.
it does not exist in the image after the build.
example:
```dockerfile
ARG home=/home/honhon/
RUN ls $home
```
we can change the arg during build runtime through the paramter `--build-arg arg_name`
`docker image build -t user_name/image_name:tag --build-arg home=/home/bonbon/`
## COPY
The COPY instruction literally copies the file from one location to another.
The syntax of the command.
it is recommended for use when you only need to copy.
`COPY SOURCE DESTINATION`
it has the following flags:
`--from=number/name` which can be used to copy from other containers during a multi-stage build pipeline.
## ADD
It acts like copy but it can be an unpacker or a downloader
you can give it a tar file and it'll unarchive it inside the specified directory
`ADD app.tar.xz /location`
give it a url and it'll download it
```dockerfile
ADD http://app.tar.xz /location
RUN tar -xJF /location/app.tar.xz -C /new_location
RUN build_instructions
```
alternatively, making it a single layer for better caching
```dockerfile
RUN curl http://app.tar.xz \
	| tar -xcJ /location/app.tar.xz -C /new_location \
	&& build_instructions
```
## RUN
The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.
### cache busting
is used to prevent package troubles, this can be done by using `\` in the dockerfile
in case we add a package, this allows the docker cache layer to be updated.
preferably, in alphanumeric order.
```dockerfile
RUN apt-get update && apt-get install -y \
	package_1 \
	package_2 \
	package_n
```
alternatively, you can disable the cache using the flag `--no-cache=true`

## ENTRYPOINT
The ENTRYPOINT instruction can be used if you want to configure your container as an executable. If you want to override CMD while running a container, use ENTRYPOINT,
for example, `ENTRYPOINT [“flask”, “run”]`
# USER
this allows us to run the processes inside the container namespace using a different userid that the default root
`USER 1000`
## CMD
CMD runs the command inside the container once a container is forked or created from an image. You can only have one CMD instruction in a Dockerfile. If multiple CMD instructions are used, the last one will be executed.
ex `CMD ["flask", "run"]`
it can even be appended to the entry point.

