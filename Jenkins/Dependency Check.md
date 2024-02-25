it's a software that checks the dependencies of a project to see if any of them are vulnrable.
it's made by OWASP.

after installing the plugin in jenkins we can add the following stage to test for dependencies:
```jenkinsfile
stage('Vulnerability Scan - Docker ') {
      steps {
        sh "mvn dependency-check:check"
      }
      post {
        always {
          dependencyCheckPublisher pattern: 'target/dependency-check-report.xml'
        }
      }
    }
```
