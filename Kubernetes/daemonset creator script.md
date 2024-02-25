`kubectl create deploy nginx --image=nginx --dry-run=client -o yaml | \
    sed '/null\|{}\|replicas/d;/status/,$d;s/Deployment/DaemonSet/g' > nginx-ds.yaml`