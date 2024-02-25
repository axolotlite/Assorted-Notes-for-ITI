[github repo](https://github.com/falcosecurity/falco)

falco is a cloudnative k8s threat detection engine.
it has a config file at `/etc/falco/falco.yaml`

installing falco
```sh
curl -s https://falco.org/repo/falcosecurity-3672BA8F.asc | apt-key add -
echo "deb https://download.falco.org/packages/deb stable main" | tee -a /etc/apt/sources.list.d/falcosecurity.list
apt-get update -y
apt-get install falco -y
```
then we start the service:
`systemctl start falco`