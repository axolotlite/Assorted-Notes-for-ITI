we can go to a github page
press the setting:
![[github repo options.png]]

then select webhook:
![[github repo left options pane.png]]

after that you add a new webhook:
which is supposed to be the jenkins-URL/github-webhook
![[github repo add webhook.png]]
finally change the content type into: application/json

then in jenkins we'll have to enable `github hook trigger` when creating a new pipeline:
![[jenkins new pipeline options github hook.png]]

if the github repo contains the jenkinsfile, we have to change the definition into: `pipeline script from SCM` (source code management)
then specify that it's git, then the repo url.
![[jenkins new pipeline options pipeline defintion.png]]
we can even specify the branch.