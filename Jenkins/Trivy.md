it scans application dependencies to find vaulnrabilities in applications.

it can scan:
- container images
- filesystems
- git repos
it's available in binary form and in docker form.
```sh
#Add the trivy-repo
sudo apt-get update
sudo apt-get -y install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list

#Update Repo and Install trivy
sudo apt-get update
sudo apt-get install trivy -y
```
this is a script that leverages trivy to scan a docker image:
this fails the build if vulns are found
```sh
#!/bin/bash

dockerImageName=$(awk 'NR==1 {print $2}' Dockerfile)
echo $dockerImageName

docker run --rm -v $WORKSPACE:/root/.cache/ aquasec/trivy:0.17.2 -q image --exit-code 0 --severity HIGH --light $dockerImageName
docker run --rm -v $WORKSPACE:/root/.cache/ aquasec/trivy:0.17.2 -q image --exit-code 1 --severity CRITICAL --light $dockerImageName

    # Trivy scan result processing
    exit_code=$?
    echo "Exit Code : $exit_code"

    # Check scan results
    if [[ "${exit_code}" == 1 ]]; then
        echo "Image scanning failed. Vulnerabilities found"
        exit 1;
    else
        echo "Image scanning passed. No CRITICAL vulnerabilities found"
    fi;
```
triviy returns exit codes depending on the build, which will be helpful in determining wether jenkins fails the build or not.


```jenkinsfile
stage('Vulnrability Scan - Docker')
```

