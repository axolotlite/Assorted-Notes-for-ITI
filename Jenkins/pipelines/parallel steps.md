

we can run several parallel steps using:
```jenkinsfile
steps{
	parallel{
		"step 1":{
			sh "echo first parallel step"
		},
		"step 2":{
			sh "echo second parallel step"
		}
	}
}
```