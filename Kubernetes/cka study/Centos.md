kubelet on centos will require systemd-resolved.service to be installed.
otherwise, it'll look for the resolve.conf file in `/run/systemd/resolve/resolv.conf` instead of `/etc/resolv.conf`  like in ubuntu.

i've debugged this error through looking at `kubectl describe node nodename`, which described the given error for not Ready as:
`container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized`
then another error which said:
`Warning CheckLimitsForResolvConf 4m55s kubelet open /run/systemd/resolve/resolv.conf: no such file or directory
`
upon using `journalctl -u kubelet` i noted that it was unable to find resolve.conf, after a quick google search i found two ways to fix this.
through `/var/lib/kubelet/config.yaml` by changing the location of the `resolv.conf` or by installing `systemd-resolved` service.
