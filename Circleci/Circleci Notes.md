CIrcleCI is a continues integration and delivery platform that can implement Devops.
It is used for DevOps, it's free and allows you to spin up a vm or a container to do something and then depending on its success or failure, do something else.
It is as they note on their website  "aggressive" because it runs on each and every commit to its relevant repository.
it has many features which i will disect here.
this is their "Hello World"
```
version: 2.1
jobs:
  job_name:
    docker:
      - image: docker:image_version
    steps:
      - checkout
      - run: shell code to run
workflows:
	workflow_name:
		jobs:
			-	job_name
			-	other_job:
					requires:
						job_name
```

first, `jobs` definition, it's where you'll need to specify the runner of this job, preferably a docker container.
then the steps the job takes.
these jobs usually run in parallel, but you can make it sequential depending on what you need.