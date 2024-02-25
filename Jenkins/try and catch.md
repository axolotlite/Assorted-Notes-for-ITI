
we can catch errors in jenkinsfiles
using try and catch

example:
```yaml
    stage('Integration Tests - DEV') {
      steps {
        script {
          try {
            sh "bash integration-test.sh"
            }
          catch (e) {
            sh "kubectl -n default rollout undo deploy ${deploymentName}"
          throw e
          }
        }
      }
    }
```

