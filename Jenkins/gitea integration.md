
follow [this](https://stackoverflow.com/questions/48316346/gitea-and-jenkins-webhook)
Same as github but there are a few differences:
the target url will be:
jenkins-url/gitea-webhook/post
![[gitea options add webhook.png]]

and on the jenkins part we'll have to enable `Poll SCM`

![[Pasted image 20230425185219.png]]