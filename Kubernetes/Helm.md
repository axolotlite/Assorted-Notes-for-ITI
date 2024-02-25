[github repo](https://github.com/helm/helm)

is a package manager for kubernetes
we can install it using:
```sh
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

we can install falco to a k8s namespace dedicated for falco using:
`helm install falco ./falco/ --namespace falco --create-namespace --set falcosidekick.enabled=true --set falcosidekick.webui.enabled=true
helm install vault hashicorp/vault --version version_number`