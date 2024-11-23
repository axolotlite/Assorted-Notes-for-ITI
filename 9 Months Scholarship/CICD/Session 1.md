### Continuous Integration
example:
we have an app that delivers online banking, (like instapay)
it has a basic feature, send money between two accounts.
let's assume the developers want to add a new feature, this change create a delta (difference between the source repo and a user repo)
the steps to integrate this change into the existing codebase /app will be:
- committing the change to the repo
- checking that the code doesn't conflict or cause errors
- building the new codebase to create an artifact (build binary / directory)
in a critical application you may have variations of this environment before reaching the final codebase, for example:
testing -> staging -> production
the code will go through these environmnets one by one to ensure that it's completely tested and safe before deploying it to production.

outward steps of a pipeline:
developer commits code to external repo -> github triggers pipeline start -> C.I Server starts the pipeline and notifies the team of the result
common steps in a CI pipeline:
- testing for security vulnerabilities
- unit tests for each code component
- static code analysis (example: sonar cube)
- code coverage
- artifact production
- push artifact into artifactory
for example they use trivy for security analysis.
the unit tests are written by the developers for the QA team to integrate into their part of the pipeline.

most CI pipelines are triggered on pull requests, to allow review of both the code in its feature branch and the pipeline results after it's run.
so, the branch settings are configured to prevent directly pushing onto the branch, instead they can only create pull requests.
once the pull request in created a pipeline is triggered to check if the code is up to standards, on successfully completing the pipeline without any issue the merge button becomes available, the tech lead will review the pipeline, the code and approve the merge.

the produced artifact is then sent to an `artifactory` for later use.

#### Branch protection rule:
this are the rules applied to branches, for example juniors are only allowed to create pull requests and are forbidden from directly pushing into the repo.
alternatively only the tech lead can push directly or even the tech lead in unable to push without a pull request.

#### Continuous Delivery Vs Deployment
Delivery is made on the production environment, Deployment is on any environment.
example of a CD pipeline:
- Download the artifact
- Integration testing: checks if all previous services work well
- User acceptance testing
- Performance testing
- Smoke testing: added to production pipeline
This pipeline requires approval so it can be manually triggered, this approval comes from the "release manager."
this release has it's own version which will be deployed.

### Jenkins
jenkins has a "master agent" this is the agent responsible for running the pipeline.
we can configure each agent to have the needed dependencies, and specific packages. 
This means we can delegate specific projects / repos to specific agents that have specific packages and dependencies needed.
#### Master agent:
the agent that's installed on the jenkins node itself, this is the default agent and the agent that's most likely to be used if you specify "any", it's not preferred to use it to prevent overloading the node or crashing it.
#### slave agents:
these are the agents responsible for running a pipeline, they can be anything from vms, containers, bare-metal or any combination of those.
### Devops
there are three components in a devops repo:
- app code
- IaC / CaC
- Author tests
these three are saved in version control for use in building the artifact after passing all tests.
this artifact is then deployed on provisioned infrastructure for further testing on each environment(testing, staging, production) with each having their own unique tests and deployment methedologies.
for example:
- test env: has a lot of code analysis and profiling with tests to ensure security, etc...
- staging acts as the middleman between testing and production
- production: deployment with preparation to rollback, A/B testing, and user feedback integration
#### speeding up the pipeline
there are steps in the pipeline that we can modify to increase the pipelines speed, one of those are caching the dependencies on the artifcatory.

### Branching strategies
there are two strategies:
- feature based strategy(git flow): preferable for medium / large projects
- trunk based strategy: preferable for small projects with speedy delivery goals without care for quality

#### Feature Based Strategy / git flow
this produces the best quality, it creates a set of protected main branches (only pull requests, no direct pushing)
usually ( develop, release, master).
with each team having role-specific privileges, for example:
back-end team can push / pull request their own branch / repos, but can only read front-end team repos / branches.
another protection method is `peer review` meaning even if a tech-lead creates a pull request, he'll need someone else to review his code before it's merged.
each branch will have it's special pipeline, but the `master` branch will almost always need manual approval to run the pipeline.
this allows us to isolate features within a branch, each with its own control and management, it increases the time between each stage but it allows high quality code.
###### versioning in Feature based strategy
version: X.Y.Z-N
- X: major release version
- Y: minor release version
- Z: hotfixes / patches
- N: development snapshots
these are the types used
- snapshots:
	this repo is a fork/clone of major release, used for feature implementation.
	we take snapshots of each version, for example: X.(N+1)-snapshot.
	this is basically a patch
- rc (release candidate): 
	used in minor releases, if we use the previous package as base, once the next version it'll be named: rc-X.(Y+1).0
	this version is used in pre-production environment to test before being deployed into the production environment
- major version release: 
	this is a major release (X+1).0.0, it's feature is complete for its version and may break compatibility, it's applied to the master repo but not used in production as the difference between each major release is a lot of features that should've been deployed to production upon completion(agile methodology).
	so, major version often have CI pipelines only.
	**of course, it's deployment depends on the release manager.**
- hotfixes:
	this is a branch that is used to fix any bugs that appear in the major versions, it's applied at the release X.Y.(Z+1)
#### Trunk Based Strategy
This project uses only one main repo on which the same software versioning method is used.
X.Y.Z -> X.Y+1.Z -> X.Y+2.Z -> X.Y+2.Z+1 -> X+1.0.0
This method is fast, it allows a simple release pipeline built on incremental commits with no complications, however the lack of stages in code commit often leads to low quality code and the larger the team the harder it is to maintain.
#### concepts:
static code analysis: checks for hard coding of data, such as password, sees how much lines are replicated if its secure.
quality gates: these are thresholds for specific parts of the pipeline, you can add security gates through plugins. for example apigee plugin (used to quality check apis.)
- default: it can check mave, java, gradle and python code, without user interference.
- replication: set a threshold for how repeated the codebase is
- security: percentage of security issues allowed to pass the pipeline
trivy: a tool used to check the security of a container image.
jacoco: a tool used for code coverage
code coverage: checks if the packages used are depricated, if so, notifies the developer that he needs to update the package to a more recent version. 
artifactory: a storage for produced artifacts, it's used for rollback and history management.
Semantic versioning: is a plugin applied to repositories which manages the versioning of packages in the package control file.
security scanning: 
LTS(Long term support): a special version of software that has long term development and support.
AWX / Ansible Tower: an ansible tool that runs the playbooks in stages, it's used 