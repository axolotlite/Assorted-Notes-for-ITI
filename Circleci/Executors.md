[What are Executors?](https://circleci.com/docs/executor-intro)
CircleCI offers several execution environments: Docker, Linux VM (virtual machine), macOS, Windows, GPU and Arm. Each job defined in your project configuration is run in a separate execution environment, either a Docker container or a virtual machine.
They're often put at the start of the .circleci/config.yml
you can specify multiple executors in a folder
### this is a general template
```
executors:
	executor_name:
		docker/machine:
			-	image: image_name:image_version
```
## these are examples of docker executors i've used before
### for node projects
```
executors:
  my-executor:
    docker:
      - image: circleci/node:13.8.0
```
### for aws-cli
```
executors:
  my-aws-executor:
      docker:
        - image: amazon/aws-cli
```
### a light weight docker image i used for ansible, note you'll have to `apk add ansible openssh`
```
executors:
  my-ansible-executor:
    docker:
      - image:  python:3.9-alpine3.11
```
### another light weight general bash scripts alpine image
```
executors:
  my-alpine-executor:
    docker:
      - image:  alpine:3.15
```