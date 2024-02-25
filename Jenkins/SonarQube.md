it is used for continues inspection of code through static analysis of code.
it can find areas that needs refactoring or simplification early in the code.

it acts as a quality gate on any stage in the CI/CD. it can find code smells, security hotspots, etc... once all conditions succeeds the build continues.

we'll be using a docker image to run this.

we must install the sonarQube plugin in jenkins.

first, we get the URL sonarQube listens on, then go to jenkins:
manage jenkins -> configure system -> sonarQube service
add a sonarqube installations, give it a name that you'll use later. then give it the URL of sonarr.

can generate a token from inside sonarqube admin profile -> security
we shall give the generated token to jenkins.
add the token as a jenkins secret then specify it in configuration.

then we need to configure the jenkins webhook in sonarQube,
we login as admin -> adminstration -> configuration -> webhooks -> add
we'll name the webhook and specify the jenkins-url/sonarqube-webhook/



creating a project:
![[Pasted image 20230426120054.png]]
then select jenkins:
![[Pasted image 20230426120142.png]]
or go to admin profile, security and create a new token:
![[Pasted image 20230426121909.png]]

from jenkins we'll go to:
admin -> configure
to add a new token:
![[Pasted image 20230426122848.png]]
we'll need to save the token name for use in jenkinsfile



relevant jenkinsfile stage:
```jenkinsfile
    stage('SonarQube - SAST') {
      steps {
        sh "mvn sonar:sonar -Dsonar.projectKey=devsecops-numeric-application -Dsonar.host.url=http://controlplane:30012 -Dsonar.login=<use-your-token-here>"
      }
    }
```