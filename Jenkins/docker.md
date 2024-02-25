we must first install the docker pipeling plugin.
this plugin can also be used with podman api
then we must setup credentials if we want to push to dockerhub

we must go to:
Dashboard -> Credentials -> system -> global credentials 
then add credentials:
we specify the username and its password, then give it an id:`docker_id`.

then if we ever want to use this credentials we'll add this to the stage:
`withDockerRegister([credentialsId: "docker_id", url: ""])`

we can build an image using this stage
```jenkinsfile
stage('Build Docker Image') {
      steps {
        sh 'docker build -t "image_name" .'
      }
    }
```