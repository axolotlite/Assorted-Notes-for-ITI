this jenkins pipeline checks the version of both jenkins and docker

```jenkinsfile
pipeline {
    agent any
    stages {
        stage('check docker version') {
            steps {
               sh "docker --version"
            }
        }

        stage('check jenkins version') {
            steps {
               sh "jenkins --version"
            }
        }
    }
}
```
