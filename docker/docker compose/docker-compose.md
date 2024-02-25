docker-compose can give docker commands in a declaritive way.

common commands used in docker-compose

## docker-compose build
The job of the ‘build’ command is to get the images ready to create containers. If a service is using the prebuilt image, it will skip that service.
## docker-compose images
This command lists images built using the current docker-compose file.
## docker-compose run
Similar to docker run command, this one creates containers from images built for the services mentioned in the compose file. It runs a specific service provided as an argument to the command.
## docker-compose up
This does the job of the `docker-compose build` and `docker-compose run` commands. It initially builds the images if they are not located locally and then starts the containers.
If images are already built, it will fork the container directly. We can force it to rebuild the image by adding a `--build` argument.
## docker-compose stop
This command stops the running containers of the specified services in the docker-compose file.
## docker-compose rm
This command removes the containers of the services or the containers created using the current docker-compose file. It can be containers created using the `docker-compose run` command or the `docker-compose up` command. It will remove all the containers which have services mentioned in the docker-compose file.
## docker-compose start
This command starts any stopped containers of the services.
If all the containers are already up and running, they will just inform that all containers are starting and exit with 0 status.
## docker-compose restart
This command restarts all the containers of the services.
## docker-compose ps
This lists all the containers for services mentioned in the current docker-compose file.
The containers can either be running or stopped.
## docker-compose down
This command is similar to `docker system prune`.
However, there is a small difference. It stops all the services and then cleans up the containers, networks, and images used and created by the compose file services.
## docker-compose logs
This command is similar to `docker logs \<container ID>`.
The little difference is this prints all the logs created by all the services. We can also use the `-f` argument to see real-time logs.