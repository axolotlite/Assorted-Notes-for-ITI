can be used to do mutation testing on java based apps.

if an app code changes, then it produces a different resault, then the unit test fails.

traditional test coverage measures which code is executed, but it doesn't detect faults in it. meaning it can't test code that doesn't run.

mutation tests changes the behavour of classes, these changes are called mutations. if a test fails after a mutation, then it's caught and killed by JUnit. this means the mutation was not caught and it survived.
the quality can be gauged by how many mutations were killed.
so, if a mutation passes after changing your code. the test failed.

we can add this in a jenkinsfile to use mutations:
```jenkinsfile
stage('Mutation Tests - PIT'){
      steps{
        sh "mvn org.pitest:pitest-maven:mutationCoverage"
      }
      post {
        always {
          pitmutation mutationStatsFile: '**/target/pit-reports/**/mutations.xml'
        }
      }
    }
```
