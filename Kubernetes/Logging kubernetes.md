k8s doesn't have a built in logging solution.

so, we'll have to download and install one manually.

one such as cmetric(container metric)
`git clone https://github.com/kodekloudhub/kubernetes-metrics-server.git`
then go into the directory and run the following
`kubectl -f create .`

you now have access to `kubectl top` a kubernetes equivalent to top