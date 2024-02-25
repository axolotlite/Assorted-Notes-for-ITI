github [repo](https://github.com/controlplaneio/kubesec), [docs](https://kubesec.io/)
Open source kubernetes security scanner and analysis tool, it tries to find common exploits in your kube cluster while providing severity scores for each vulnerability.

it takes a single yaml file as input. it can target multiple kubernetes resources.
in can be installed on linux or run through a docker image. it has a REST API.
This REST API allows you to send your yaml file through their website to get a score
`curl -sSX POST --data-binary @"k8s_config_file.yaml" https://v2.kubesec.io/scan`

we can install it using this script:
```sh
wget https://github.com/controlplaneio/kubesec/releases/download/v2.11.2/kubesec_linux_amd64.tar.gz
tar -xvf  kubesec_linux_amd64.tar.gz
mv kubesec /usr/bin/
```

this script uses the online REST API to get score:

```sh
#!/bin/bash
#kubesec-scan.sh
# using kubesec v2 api
scan_result=$(curl -sSX POST --data-binary @"k8s_deployment_service.yaml" https://v2.kubesec.io/scan)

scan_message=$(echo $scan_result| jq .[0].message -r )

scan_score=$(echo $scan_result| jq .[0].score)
# echo $scan_score
echo "Score is $scan_score"
if [[ $scan_score -ge 4 ]] then;
	echo "Kubesec Scan Passed with a score of $scan_score points"
else
	echo "Kubernetes template scanning failed because score is less than 4"
	exit 1;
fi
```