Run the command `ps -aux | grep kubelet` and identify the config file - `--config=/var/lib/kubelet/config.yaml`.
the config file contains the path for the static pods
Then check in the config file for staticPodPath.