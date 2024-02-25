[github repo](https://github.com/hashicorp/vault)
it's a secret keeping software that allows securely accessing secrets.
the server always starts in a sealed status. it generates the root tokens during initialization with default 5 key-shares.
there are several ways to install hashicorp vault:
[guide](https://developer.hashicorp.com/vault/docs/install)
helm:
```sh
helm repo add hashicorp https://helm.releases.hashicorp.com
helm install vault hashicorp/vault --version version_number
helm install vault --set='ui.enabled=true'\
	--set='ui.serviceType=NodePort' \
	--set='server.dataStorage.enabled=false' hashicorp/vault --version version_number
```

using k8s we can get the vault status using:
`kubectl exec -it vault_pod_name -- vault status`

to shell into the vault:
`kubectl exec -it vault-name -n namespace -- sh`

creating the unseal keys for the vault:
`vault operator init`
we take the keys and use them to unseal the vault using atleast 3 of the 5 keys:
`vault operator unseal key_1`
`vault operator unseal key_2`
`vault operator unseal key_3`

we can create a secret path in vault through:
`vault secret enable -path=path_location kv-v2`

we can put data in a vault through:
`vault kv put path_location/data_name key=value key2=value2`
and retrieve them through:
`vault kv get crds/mysql`

vault policies can be added at `/home/vault/policy.hcl`
example for a readonly data
```hcl
path "path_location/data_name"{
	capabilities = ["read"]
}
```
then we apply the policy:
`vault policy write policy_name /home/vault/policy.hcl`

we can enable k8s auth method using:
`vault auth enable kubernetes`
then allowing it to talk to k8s cluster with:
```sh
vault write auth/kubernetes/config \
token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)"  \
kubernetes_host=https://${KUBERNETES_PORT_443_TCP_ADDR}:443 \
kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
```
finaly configuring a role for the app:
```sh
vault write auth/kubernetes/role/phpapp \
bound_service_account_names=devsecops-app \
bound_service_account_namespaces=vault-devsecops \
policies=devsecops-app \
ttl=1h
```

vault injections in k8s object template:
```yaml
spec:
  template:
    metadata:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/agent-inject-secret-username: "devsecops/secret-data"
        vault.hashicorp.com/agent-inject-secret-password: "devsecops/secret-data"
        vault.hashicorp.com/agent-inject-secret-apikey: "devsecops/secret-data"
        vault.hashicorp.com/role: "phpapp"
```
then we can patch it through:
`kubectl patch deploy php -p "$(cat patch-annotations.yaml)" -n vault-devsecops
`
