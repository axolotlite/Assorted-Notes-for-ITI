They are declared under the commands yml key of the `config.yml` they allow you to write reusable code across multiple jobs.
they're usually placed after excutors.
they have their own steps and condition, so a command can be placed inside another command.
it could be treated as a "sub-job" that runs inside bigger jobs
## template command exerpts: 
### Template
```
commands:
	command_name:
		description: optional command description
		parameters:
			parameter_name:
				type: string/whatever
				default: optional default value
			steps:
				-	run:	shell command to run
				-	run: another shell command
					when: on_fail/on_success
```
## example commands i've used:
### parameterized command
```
commands:
  sayhello:
    description: "Are these manditory?"
    parameters:
      to:
        type: string
        default: "Hello World"
    steps:
      - run: echo <<parameters.to>>
```
### Prints Circle variable
```
commands:
  print_pipeline_id:
    description: "Prints the pipeline id for this process"
    steps:
      - run: echo $CIRCLE_WORKFLOW_ID
```
### this command returns a specified exit code
```
commands:
  return_code:
    description: "returns exit code"
    parameters:
      code:
        type: integer
    steps:
      - run: exit <<parameters.code>>
```
### this installs ansible
```
commands:
  install_ansible:
    description: updates the system and install ansible
    steps:
      - run: apk add --update ansible
```
### this destroys a cloud formation stack when a deployment fails
```
commands:
  destroy_infrastructure:
    description:  destroys cloudformation on failure
    parameters:
      stackName:
        type: string
    steps:
      - run:
          name: destroy infrastructure
          command: aws cloudformation delete-stack --stack-name <<parameters.stackName>>
          when: on_fail
```
### this installs tar and gzip for aws-cli container to enable workspace persistence.
```
commands:
  install_workspace_utils:
    description: installs tar and gzip
    steps:
      - run:
          name: Install tar utility
          command: |
            yum install -y tar gzip
```
