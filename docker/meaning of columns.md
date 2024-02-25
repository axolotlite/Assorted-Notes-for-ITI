$ docker ps -a
CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                      PORTS               NAMES
b1e466176116        python:3.5            "python3"                2 minutes ago       Exited (0) 2 minutes ago                        practical_shtern

* CONTAINER ID: shows the unique ID of each container

* IMAGE: the image from which the container is created

* COMMAND: command executed in the container while starting it

* CREATED: the time the container was created

* STATUS: the current status of the container

* PORTS: if any of the container ports is connected to the host machine, it will be displayed here

* NAMES: this is the name of a container. If it is not provided while creating the container, Docker provides a unique name by default.