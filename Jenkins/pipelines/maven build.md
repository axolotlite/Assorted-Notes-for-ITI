This will allow you to build an artifact using maven

after the build step, we archive the artifact.

then test the build.
```jenkinsfile
pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            steps {
               sh "mvn clean package -DskipTests=true"
               archive 'target/*.jar'
            }
        }
        stage('Testing'){
            steps{
                sh "mvn test"
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                    jacoco execPattern: 'target/jacoco.exec'
                }
            }

        }
    }
}
```