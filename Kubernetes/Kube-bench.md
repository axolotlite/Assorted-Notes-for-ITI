git [repo](https://github.com/aquasecurity/kube-bench)
[installation guide](https://github.com/aquasecurity/kube-bench/blob/main/docs/installation.md)
a go app that checks wether kuberenetes is deployed securely by running checks documented in [[CIS Benchmark]]
we can use a docker container, or run it through a binary.

there are AKS and EKS cluster specific kube-bench.

installation:
Ubuntu/Debian:
```
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.6.2/kube-bench_0.6.2_linux_amd64.deb -o kube-bench_0.6.2_linux_amd64.deb

sudo apt install ./kube-bench_0.6.2_linux_amd64.deb -f
```
RHEL:
```
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.6.2/kube-bench_0.6.2_linux_amd64.rpm -o kube-bench_0.6.2_linux_amd64.rpm

sudo yum install kube-bench_0.6.2_linux_amd64.rpm -y
```
Alternatively, you can manually download and extract the kube-bench binary:

```
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.6.2/kube-bench_0.6.2_linux_amd64.tar.gz -o kube-bench_0.6.2_linux_amd64.tar.gz

tar -xvf kube-bench_0.6.2_linux_amd64.tar.gz
```

default command that displays all compliance:
for nodes:
`kube-bench node`

for the master controller node.
`kube-bench master`

parameters:
`--check section_number,other_section_number` we can check specific CIS documentent sections.
`--json` outputs the result as json
`--targets node_name,other_node_name` selects which nodes to test
`--version kubernetes_version` compares the security to the specified kubernetes version