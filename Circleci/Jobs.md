[What are CIrcleci Jobs?](https://circleci.com/docs/jobs-steps)
A CircleCI job is a collection of steps. All of the steps in the job are executed in a single unit, either within a fresh container, or a virtual machine. Jobs are orchestrated using workflows.
`-checkout` downloads data from git and puts it in working directory.

## Template job
```
job_name:
	executor: executor_name
	steps:
		-	run: 
				name: whatever you name this command
				command: shell code
		-	run: another shell code
```
### Job that saves output to cache in a file called output.txt
```
  save_hello_world_output:
    executor: my-executor
    steps:
      - run: echo "hello world" > ~/output.txt
      - persist_to_workspace:
          root: ~/
          paths:
            - output.txt
```
### job that attaches a workspace and reads from a file called output
```
  print_output_file:
    executor: my-executor
    steps:
      - attach_workspace:
          at: ~/
      - run: cat ~/output.txt
```
### A job that uses a command called sayhello
```
  hello_world_command:
    executor: my-executor
    steps:
      - sayhello
```
### A job that calls a command to print a workflow related variable
```
  print_pipe_id:
    executor: my-executor
    steps:
      - print_pipeline_id:
          to: "$CIRCLE_WORKFLOW_ID" 
```
### a job that fails then reports its failure
```
  fail_on_purpose:
    executor: my-executor
    steps:
      - run: "echo this code fails on purpose"
      - return_code:
          code: 1
      - run:
          name: "Failure Report"
          command: echo "Mission Failed Successfully"
          when: on_fail
```
### a job that echoes once  it fails
```
  succeed_on_purpose:
    executor: my-executor
    steps:
      - run: "echo this code succeeds on purpose"
      - return_code:
          code: 0
      - run:
          name: "Success Report"
          command: echo "Mission Successfully Failed"
          when: on_fail
```
### a job that deploys a stack, then stores its ip in cache 
```
  create_infrastructure:
    executor: my-aws-executor
    steps:
      - checkout
      - run:
          name: create Cloudformation Stack
          command:  |
            aws cloudformation create-stack \
              --template-body file://template.yml \
              --stack-name myStack-${CIRCLE_WORKFLOW_ID:0:5} \
              --region us-east-1
      - run:
          name: await stack completion
          command:
            aws cloudformation wait stack-create-complete --stack-name=myStack-${CIRCLE_WORKFLOW_ID:0:5} --region=us-east-1
      - run: echo "[all]" > ~/inventory
      - run: aws ec2 describe-instances --query 'Reservations[*].Instances[*].PublicIpAddress' --output text > ~/smoke_test_inventory
      - run: cat ~/smoke_test_inventory >> ~/inventory
      - install_workspace_utils
      - persist_to_workspace:
          root: ~/
          paths: 
            - inventory
            - smoke_test_inventory
```
### a job that uses a predefined ssh key, to configure a group of EC2 instances using ansible
```
  configure_infrastructure: 
    docker:
      - image: python:3.7-alpine3.11
    steps:
      - checkout
      - attach_workspace:
          at: ~/
      - add_ssh_keys:
          fingerprints: ["bf:ec:ad:0d:27:83:8c:48:f0:c3:5e:21:32:c4:42:46"]
      - run:
          name: Install dependencies
          command: |
            # install the dependencies needed for your playbook
            apk add --update ansible openssh
      - run:
          name: Configure server
          command: |
            ansible-playbook -i ~/inventory main.yml
```
### A smoke test runs on a single host that is in cache, destroys resource on failure.
can be modified to loop through several hosts
```
  smoke_test:
    executor: my-aws-executor
    # parameters:
    #   website:
    #     type: string
    steps:
      - checkout
      - install_workspace_utils
      - run:
          name: install curl
          command: yum install -y curl
      - attach_workspace:
          at: ~/
      - run:
          name: Availability test
          command: |
            if curl -s --head $(cat ~/smoke_test_inventory):3000
            then
              exit 0
            else
              exit 1
            fi
      - run:
          name: smoke_test successful
          command: echo "The smoke test was a Success"
          when: on_success
      - run:
          name: smoke_test failure
          command: echo "The smoke test was a failure"
          when: on_fail
      - destroy_infrastructure:
          stackName: myStack-${CIRCLE_WORKFLOW_ID:0:5}
```
### deploys an s3 using cloudformatoin, then uploades relevant data to it for static hosting
```
  create_and_deploy_front_end:
    executor: my-aws-executor
    steps:
      - checkout
      - run:
          name: Execute bucket.yml
          command: |
            aws cloudformation deploy --template-file bucket.yml --stack-name stack-create-bucket-${CIRCLE_WORKFLOW_ID:0:7} --parameter-overrides MyBucketName="mybucket-${CIRCLE_WORKFLOW_ID:0:7}"
      - run:
          name: upload git repo content to s3 bucket
          command: aws s3 sync pages/ s3://mybucket-${CIRCLE_WORKFLOW_ID:0:7} --delete
      - destroy_infrastructure:
          stackName: stack-create-bucket-${CIRCLE_WORKFLOW_ID:0:7}
  # Fetch and save the pipeline ID (bucket ID) responsible for the last release.
```
### gets the old pipeline and saves it to cache for green migration.
```
  get_last_deployment_id:
    executor: my-aws-executor
    steps:
      - checkout
      - run: yum install -y tar gzip
      - run:
          name: Fetch and save the old pipeline ID (bucket name) responsible for the last release.
          command: |
            aws cloudformation list-exports --query "Exports[?Name==\`PipelineID\`].Value" --no-paginate --output text > ~/textfile.txt
      - persist_to_workspace:
          root: ~/
          paths: 
            - textfile.txt 
```
### changes cloudfront target using cache
```
  promote_to_production:
    executor: my-aws-executor
    steps:
      - checkout
      - run:
          name: Execute cloudfront.yml
          command: aws cloudformation deploy --template-file cloudfront.yml --stack-name production-distro --parameter-overrides PipelineID="mybucket-${CIRCLE_WORKFLOW_ID:0:7}"
```
### deletes the old unused bucket data
```
  clean_up_old_front_end:
    executor: my-aws-executor
    steps:
      - checkout
      - run: yum install -y tar gzip
      - attach_workspace:
          at: ~/
      - run:
          name: Destroy the previous S3 bucket and CloudFormation stack. 
          command: aws s3 rm "s3://$(cat ~/textfile.txt )" --recursive

```
