
```
pipeline {
  agent any

  environment {
    deploymentName = "devsecops"
    containerName = "devsecops-container"
    serviceName = "devsecops-svc"
    imageName = "docker-registry:5000/java-app:latest"
    applicationURL = "http://controlplane"
    applicationURI = "/increment/99"
  }

  stages {

    stage('Build Artifact - Maven') {
      steps {
        sh "mvn clean package -DskipTests=true"
        archive 'target/*.jar'
      }
    }

    stage('Unit Tests - JUnit and JaCoCo') {
      steps {
        sh "mvn test"
      }
    }

    stage('Docker Build and Push') {
      steps {
          sh 'sudo docker build -t docker-registry:5000/java-app:latest .'
          sh 'docker push docker-registry:5000/java-app:latest'
      }
    }

    stage('Vulnerability Scan - Kubernetes') {
      steps {
        sh '/usr/local/bin/conftest test --policy opa-k8s-security.rego k8s_deployment_service.yaml'
      }
    }

    stage('K8S Deployment - DEV') {
      steps {
        parallel(
          "Deployment": {
              sh "bash k8s-deployment.sh"
          },
          "Rollout Status": {
              sh "bash k8s-deployment-rollout-status.sh"
          }
        )
      }
    }
    stage('Integration Tests - DEV') {
      steps {
        script {
          try {
            sh "bash integration-test.sh"
            }
          catch (e) {
            sh "kubectl -n default rollout undo deploy ${deploymentName}"
          throw e
          }
        }
      }
    }
    stage('OWASP ZAP - DAST') {
      steps {
        sh 'bash zap.sh'
      }
    }

  }

  post {
    always {
      junit 'target/surefire-reports/*.xml'
      jacoco execPattern: 'target/jacoco.exec'
      publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'owasp-zap-report', reportFiles: 'zap_report.html', reportName: 'HTML Report', reportTitles: 'OWASP ZAP HTML', useWrapperFileDirectly: true])
    }

  }

}

```

integration-test.sh
```sh
#!/bin/bash

#integration-test.sh

sleep 5s

PORT=$(kubectl -n default get svc ${serviceName} -o json | jq .spec.ports[].nodePort)

echo $PORT
echo $applicationURL:$PORT$applicationURI

if [[ ! -z "$PORT" ]];
then

    response=$(curl -s $applicationURL:$PORT$applicationURI)
    http_code=$(curl -s -o /dev/null -w "%{http_code}" $applicationURL:$PORT$applicationURI)

    if [[ "$response" == 100 ]];
        then
            echo "Increment Test Passed"
        else
            echo "Increment Test Failed"
            exit 1;
    fi;

    if [[ "$http_code" == 200 ]];
        then
            echo "HTTP Status Code Test Passed"
        else
            echo "HTTP Status code is not 200"
            exit 1;
    fi;

else
        echo "The Service does not have a NodePort"
        exit 1;
fi;
```
Dockerfile
```dockerfile
FROM adoptopenjdk/openjdk8:alpine-slim
EXPOSE 8080
ARG JAR_FILE=target/*.jar
RUN addgroup -S devops-security && adduser -S devsecops -G devops-security
COPY ${JAR_FILE} /home/devsecops/app.jar
USER devsecops
ENTRYPOINT ["java","-jar","/home/devsecops/app.jar"]

```
k8s_deployment_service.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: devsecops
  name: devsecops
spec:
  replicas: 2
  selector:
    matchLabels:
      app: devsecops
  strategy: {}
  template:
    metadata:
      labels:
        app: devsecops
    spec:
      containers:
      - image: REPLACE_ME
        imagePullPolicy: Always
        name: devsecops-container
        securityContext:
          runAsNonRoot: true
          runAsUser: 100
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: devsecops
  name: devsecops-svc
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
    nodePort: 30010
  selector:
    app: devsecops
  type: NodePort

```

k8s-deployment-rollout-status.sh
```sh
#!/bin/bash

#k8s-deployment-rollout-status.sh

sleep 60s

if [[ $(kubectl -n default rollout status deploy ${deploymentName} --timeout 5s) != *"successfully rolled out"* ]]; 
then     
	echo "Deployment ${deploymentName} Rollout has Failed"
    kubectl -n default rollout undo deploy ${deploymentName}
    exit 1;
else
	echo "Deployment ${deploymentName} Rollout is Success"
fi

```

k8s-deployment.sh
```sh
#!/bin/bash

#k8s-deployment.sh

sed -i "s#REPLACE_ME#${imageName}#g" k8s_deployment_service.yaml
kubectl -n default get deployment ${deploymentName} > /dev/null

if [[ $? -ne 0 ]]; then
    echo "deployment ${deploymentName} doesnt exist"
    kubectl -n default apply -f k8s_deployment_service.yaml
else
    echo "deployment ${deploymentName} exist"
    echo "image name - ${imageName}"
    kubectl -n default set image deploy ${deploymentName} ${containerName}=${imageName} --record=true
fi
```

kube-scan.yaml
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: kube-scan
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-scan
  namespace: kube-scan
  labels:
    app: kube-scan
data:
    risk-config.yaml: |
      expConst: 9
      impactConst: 4
      attackVector:
        remote: 0.85
        local: 0.55
      exploitability:
        high: 0.54
        moderate: 0.4
        low: 0.1
        veryLow: 0.05
      scopeFactor:
        none: 0.25
        host: 1
        cluster: 1
      ciaScore:
        high: 0.56
        low: 0.22
        none: 0
      riskCategory:
        min: 0
        low: 3
        medium: 6
        max: 10
      individualRiskCategory:
        min: 0
        low: 3
        medium: 5
        max: 10
      basic:
        - name: "privileged"
          title: "Workload is privileged"
          shortDescription: "Processes inside a privileged containers get full access to the host"
          description: "Processes inside a privileged container will have full access to the host, which means any third-party library or malicious program can compromise the host. As a result,  the compromised host could be used to compromise the entire cluster"
          confidentiality: "High"
          confidentialityDescription: "Privileged containers may have the option to read and modify any application, such as Docker, Kubernetes, etc"
          integrity: "Low"
          integrityDescription: "Processes inside a privileged container get full access to the host. This means a malicious program or third-party library can compromise the host and the entire cluster"
          availability: "Low"
          availabilityDescription: "Processes inside a privileged container may have the ability to modify or stop Kubernetes, Docker and other applications"
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "Host"
          handler: "IsPrivileged"
        - name: "runningAsRoot"
          title: "Workload may have containers running as root"
          shortDescription: "Processes in container running as root may be able to escape their container"
          description: "Workload does not specify a non-root user for its containers to run as and does not specify runAsNonRoot. Processes inside a container running as root may be able to escape that container and perform malicious actions on the host - basically giving them complete control over the host and the ability to compromise the entire cluster"
          confidentiality: "High"
          confidentialityDescription: "Root processes that can escape the container have the ability to read secrets from Kubernetes, Docker and other applications"
          integrity: "Low"
          integrityDescription: "Processes in a container running as root may be able to escape their container and perform malicious actions on the host"
          availability: "Low"
          availabilityDescription: "Root processes that can escape the container have the ability to modify or stop Kubernetes, Docker and other applications"
          exploitability: "Low"
          attackVector: "Local"
          scope: "Host"
          handler: "IsRunningAsRoot"
        - name: "AllowPrivilegeEscalation"
          shortDescription: "Privilege escalation allows programs inside the container to run as root"
          description: "Privilege escalation allows programs inside the container to run as root, even if the main process is not root, which can give those programs control over that container, host and even cluster"
          title: "Workload allows privilege escalation"
          confidentiality: "Low"
          confidentialityDescription: "Root processes that can escape the containers have the ability to read secrets from Kubernetes, Docker and other applications"
          integrity: "Low"
          integrityDescription: "Processes in a container running as root may be able to escape their container and perform malicious actions on the host"
          availability: "Low"
          availabilityDescription: "Root processes that can escape the containers have the ability to modify or stop Kubernetes, Docker and other applications"
          exploitability: "VeryLow"
          attackVector: "Local"
          scope: "Host"
          handler: "IsPrivilegedEscalation"
        # - name: "CapNetRaw"
        #   title: "Workload has a container(s) with NET_RAW capability"
        #   shortDescription: "NET_RAW capability enables ARP spoofing from the container\nNET_RAW capability enables the container to craft malicious raw packet"
        #   description: "The capability NET_RAW allows the container to craft any packet, including malformed or malicious packets"
        #   confidentiality: "High"
        #   confidentialityDescription: "This capability enables ARP spoofing from the container, which means UDP packets can be sent with a forged source IP, etc. This enables the container to perform Man-in-the-Middle (MitM) attacks on the host network"
        #   integrity: "None"
        #   integrityDescription: ""
        #   availability: "Low"
        #   availabilityDescription: "This capability enables the container to craft malicious raw packet, such as Ping of Death"
        #   exploitability: "Low"
        #   attackVector: "Local"
        #   scope: "Cluster"
        #   handler: "IsCapNetRaw"
        - name: "WritableFileSystem"
          title: "Workload has a container(s) with writable file system"
          shortDescription: "Writable File System allows the persistence of threats"
          description: "A writable file system allows files within the  container to be changed.  This means a malicious process inside the container can use a writable file system to store or manipulate data inside the container"
          confidentiality: "None"
          confidentialityDescription: ""
          integrity: "Low"
          integrityDescription: "This allows malicious processes to write data to disk, making it easier to drop and execute external malicious code"
          availability: "None"
          availabilityDescription: ""
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "None"
          handler: "IsWritableFileSystem"
        - name: "UnmaskedProcMount"
          title: "Workload exposes unsafe parts of /proc"
          shortDescription: "Full access to /proc can reveal information about the host and other containers\n/proc/sys allows a privileged user to change the kernel parameters are runtime"
          description: "A container with full access (unmasked) to the host’s /proc command is able to retrieve information about all the activities and users on that host. /proc/sys allows a privileged user to change the runtime kernel parameters and impact how resources are shared amongst containers"
          confidentiality: "Low"
          confidentialityDescription: "/proc contains information about all network connections on the host, the file systems and permissions, running processes, etc"
          integrity: "None"
          integrityDescription: ""
          availability: "High"
          availabilityDescription: "/proc/sys allows a privileged user to change the runtime kernel parameters, which may impact how resources are shared amongst containers"
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "Host"
          handler: "IsUnmaskedProcMount"
        - name: "AllowedUnsafeSysctls"
          title: "Workload allows unsafe allocation of CPU resources"
          shortDescription: "Sysctl allows users to modify the kernel settings at run time: networking, memory, etc. Some sysctl interfaces can affect other containers, the host or bypass the CPU quota attributed to the container"
          description: "Sysctl is an interface that enables the container’s parameters to be changed, which could allow the container to grab more CPU resources than it’s allowed by its quota. This may starve other containers from CPU cycles, compromising the operations of the container, host and even the entire cluster"
          confidentiality: "None"
          confidentialityDescription: ""
          integrity: "Low"
          integrityDescription: "Some of the sysctl interfaces allow the container to affect the performance of other containers and/or the host"
          availability: "High"
          availabilityDescription: "Some of the sysctl interfaces allow the container to grab more CPU resources than allowed by their quota. This may starve other containers from CPU cycles"
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "Host"
          handler: "IsAllowedUnsafeSysctls"
        - name: "notConfiguredCpuOrMemoryLimit"
          title: "Workload has a container which its CPU or Memory limit was not configured"
          shortDescription: "CPU and Memory quotas prevent container from grabbing too many resources from the node, and allow a better scheduling of resources across the cluster"
          description: "CPU and Memory quotas prevent container from grabbing too many resources from the node, and allow a better scheduling of resources across the cluster"
          confidentiality: "None"
          confidentialityDescription: ""
          integrity: "None"
          integrityDescription: ""
          availability: "High"
          availabilityDescription: "Workloads with no CPU or memory quota may starve off other workloads on the node, resulting in pod ejections and cascading reschedule of pods on other nodes"
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "Host"
          handler: "IsNotConfiguredCpuOrMemoryLimit"
        - name: "mountingOSDirectoryRW"
          title: "Workload is mounting a volume with OS Directory write permissions"
          shortDescription: "Containers can mount sensitive folders from the hosts, giving them potential dangerous access critical host configurations and binaries"
          description: "Containers can mount sensitive folders from the hosts, giving them potentially dangerous access to critical host configurations and binaries"
          confidentiality: "High"
          confidentialityDescription: "Sharing sensitive folders and files such as / (root), /var/run/, etc., can allow the container to communicate with other host applications, such as a database, which could expose sensitive information"
          integrity: "High"
          integrityDescription: "Sharing sensitive folders and files, such as / (root),  /var/run/, docker.sock, etc. can allow the container to reconfigure the Kubernetes clusters, run new container images, etc"
          availability: "Low"
          availabilityDescription: "Sharing sensitive folders and files, such as / (root),  /var/run/, docker.sock, etc. can allow the container to reconfigure the container quotas, run new container images, etc"
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "Host"
          handler: "IsMountingOSDirectoryRW"
        - name: "mountingOSDirectoryRO"
          title: "Workload is mounting a volume with OS Directory read-only permissions"
          shortDescription: "Containers can mount sensitive folders from the hosts, giving them potential dangerous access critical host configurations"
          description: "Containers can mount sensitive folders from the hosts, giving them potential dangerous knowledge of critical host configurations"
          confidentiality: "Low"
          confidentialityDescription: "Sharing sensitive folders and files, such as /etc, /var/run/, etc., can allow the container to read secrets"
          integrity: "None"
          integrityDescription: ""
          availability: "None"
          availabilityDescription: ""
          exploitability: "Low"
          attackVector: "Local"
          scope: "Host"
          handler: "IsMountingOSDirectoryRO"
        - name: "capSysAdmin"
          title: "Workload has container/s with CAP_SYS_ADMIN capability"
          shortDescription: "CAP_SYS_ADMIN is the most privileged capability with over 150 privileged system calls allowed"
          description: "CAP_SYS_ADMIN is the most privileged capability allowed, out of more than 150 privileged system calls available"
          confidentiality: "High"
          confidentialityDescription: "CAP_SYS_ADMIN gives processes privileges equivalent to running as root. Processes in a container running as root may be able to escape their container and perform malicious actions on the host"
          integrity: "None"
          integrityDescription: ""
          availability: "None"
          availabilityDescription: ""
          exploitability: "Moderate"
          attackVector: "Local"
          scope: "Host"
          handler: "IsCapSysAdmin"
        - name: "ExposedByLoadBalancer"
          title: "Workload is exposed through a load balancer"
          shortDescription: "The service is accessible from other networks and/or from the Internet"
          description: "A load balancer is exposing the workload, making it accessible from other networks and the Internet"
          confidentiality: "High"
          confidentialityDescription: "Accidental exposure of sensitive services may lead to the exfiltration of confidential data through remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          integrity: "Low"
          integrityDescription: "Services open to the Internet may be used to access unprotected services (move laterally) by leveraging remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          availability: "High"
          availabilityDescription: "Accidental exposure to the Internet can make the workload susceptible to DoS attacks from random attackers"
          exploitability: "Moderate"
          attackVector: "Remote"
          scope: "None"
          handler: "IsExposedByLoadBalancer"
        - name: "ExposedByNodePort"
          title: "Workload is exposed through a node port"
          shortDescription: "The service is accessible from other networks and/or from the Internet"
          description: "A node port is exposing the workload, making it accessible from other networks and the Internet"
          confidentiality: "High"
          confidentialityDescription: "Accidental exposure of sensitive services may lead to the exfiltration of confidential data through remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          integrity: "Low"
          integrityDescription: "Services open to the Internet may be used to access unprotected services (move laterally) by leveraging remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          availability: "High"
          availabilityDescription: "Accidental exposure to the Internet can make the workload susceptible to DoS attacks from random attackers"
          exploitability: "Moderate"
          attackVector: "Remote"
          scope: "None"
          handler: "IsExposedByNodePort"
        - name: "ExposedByIngress"
          title: "Workload is exposed through an ingress policy"
          shortDescription: "The service is accessible from other networks and/or from the Internet"
          description: "An ingress policy is exposing the workload, making it accessible from other networks and the Internet"
          confidentiality: "High"
          confidentialityDescription: "Accidental exposure of sensitive services may lead to the exfiltration of confidential data through remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          integrity: "Low"
          integrityDescription: "Services open to the Internet may be used to access unprotected services (move laterally) by leveraging remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          availability: "Low"
          availabilityDescription: "Accidental exposure to the Internet can make the workload susceptible to DoS attacks from random attackers"
          exploitability: "Moderate"
          attackVector: "Remote"
          scope: "None"
          handler: "IsExposedByIngress"
        - name: "HostPort"
          title: "Workload is exposed through a shared host port"
          shortDescription: "The service is accessible from other networks and/or from the Internet"
          description: "This container setting binds the container listening port to the IP address of the host. This exposes the pod to adjacent networks and/or to the Internet.\nA host port is exposing the workload, making it accessible from other networks and the Internet"
          confidentiality: "High"
          confidentialityDescription: "This setting binds the workload listening IP address to the host IP, making the service accessible from other networks and/or from the Internet"
          integrity: "Low"
          integrityDescription: "Services open to the Internet may be used to access unprotected services (move laterally) by leveraging remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          availability: "High"
          availabilityDescription: "Accidental exposure to the Internet can make the workload susceptible to DoS attacks from random attackers"
          exploitability: "Moderate"
          attackVector: "Remote"
          scope: "None"
          handler: "IsHostPort"
        - name: "ShareHostNetwork"
          title: "Workload is exposed through a shared host network"
          shortDescription: "The service is accessible from other networks and/or from the Internet\nShare Host Network allows containers to sniff traffic from host and other containers"
          description: "This Security Context setting allows the workload to share the same network namespace as the host"
          confidentiality: "High"
          confidentialityDescription: "This allows the network to listen to the loopback interface and sniff the traffic to and from other pods. This setting also allows workloads to bind their listening IP address to the host IP, making the service accessible from other networks and/or from the Internet"
          integrity: "Low"
          integrityDescription: "Services open to the Internet may be used to access unprotected services (move laterally) by leveraging remote code vulnerabilities, vulnerable third-party libraries or vulnerable OS services"
          availability: "High"
          availabilityDescription: "Accidental exposure to the Internet can make the workload susceptible to DoS attacks from random attackers"
          exploitability: "Low"
          attackVector: "Remote"
          scope: "Host"
          handler: "IsShareHostNetwork"
        - name: "ShareHostPID"
          title: "Workload shares the host PID"
          shortDescription: "Share Host Pid allow  containers to manipulate other container processes"
          description: "Shared host PIDs enable the sharing of processes with the host and other containers"
          confidentiality: "Low"
          confidentialityDescription: "Each container has access to password, secrets, certificates, etc. read by other containers"
          integrity: "Low"
          integrityDescription: "Each container can manipulate other container processes, inject malicious code, modify /proc, etc. A malicious container can move laterally by infecting other containers on the same host"
          availability: "Low"
          availabilityDescription: "Each container can crash another container’s processes"
          exploitability: "Low"
          attackVector: "Local"
          scope: "Host"
          handler: "IsShareHostPID"
        - name: "ShareHostIPC"
          title: "Workload shares the host IPC"
          shortDescription: "Shared Host IPC can leak confidential data sent from trusted applications"
          description: "IPC allows containers to communicate directly through shared memory - a shared IPC means that anyone in that namespace can access that memory"
          confidentiality: "High"
          confidentialityDescription: "Communication between trusted applications and untrusted applications (malicious third-party libraries, rogue containers) can leak confidential data"
          integrity: "Low"
          integrityDescription: "Untrusted applications can change the behavior of trusted applications through shared memory namespaces by tampering with the memory"
          availability: "Low"
          availabilityDescription: "An untrusted application can use improper Inter-Process Communications to crash the destination process"
          exploitability: "Low"
          attackVector: "Local"
          scope: "Host"
          handler: "IsShareHostIPC"
      remediation:
        - name: "seccomp"
          title: "Workload containers have a seccomp policy"
          shortDescription: "A seccomp policy specify which system class can be called by the application. It is a sandboxing technique that reduces the chance that a kernel vulnerability will be successfully exploited"
          description: "seccomp stands for Secure Computing mode - a seccomp policy can specify which system class can be called by the application. It is a sandboxing technique that reduces the chance that a kernel vulnerability will be successfully exploited"
          confidentiality: "High"
          confidentialityDescription: "A seccomp policy can prevent malicious programs from reading files not used by the container"
          integrity: "High"
          integrityDescription: "A seccomp policy can prevent malicious programs to use kernel exploits to break out of the container"
          availability: "High"
          availabilityDescription: "A seccomp policy can be used to restrict the system calls and prevent processes from grabbing additional CPU or memory resources"
          exploitability: "None"
          attackVector: "Local"
          scope: "Host"
          handler: "IsSecComp"
        - name: "selinux"
          title: "Workload containers have SELlinux or AppArmor enabled"
          shortDescription: "SELinux (RedHat-based distributions) and AppArmor(Debian-based distributions) provides access control policies. They can be used to restrict how processes can communicate"
          description: "SELinux (RedHat-based distributions) and AppArmor (Debian-based distributions) provides access control policies that can be used to restrict how processes can communicate to improve the overall security posture of the container and host"
          confidentiality: "High"
          confidentialityDescription: "The SELinux or AppArmor policy can be used to restrict what processes can read in each folder"
          integrity: "High"
          integrityDescription: "The SELinux or AppArmor policy can be used to restrict what processes can write to disk and in what folders"
          availability: "High"
          availabilityDescription: "The SELinux or AppArmor policy can be used to restrict the system calls and prevent processes from grabbing additional CPU or memory resources"
          exploitability: "None"
          attackVector: "Local"
          scope: "Host"
          handler: "IsSelinux"
        - name: "IngressPolicy"
          title: "Workload has ingress policy configured"
          shortDescription: "The Kubernetes network policy allows specific workloads or specific external IP addresses (such as an external Load Balancer) to access the application running"
          description: "An ingress network policy can prevent a workload from being leveraged to perform lateral movement and data ex-filtration"
          confidentiality: "Low"
          confidentialityDescription: "An ingress policy cuts down on accidental exposure to the Internet, which can lead to confidential data being leaked. (Accidental exposure can be caused when a Load Balancer, Node Port or Ingress Controller is added or misconfigured"
          integrity: "Low"
          integrityDescription: "An ingress policy cuts down on accidental exposure to the Internet, which can make vulnerable code or third-party processes available to be exploited by external attackers"
          availability: "High"
          availabilityDescription: "An ingress policy helps limit accidental exposure to the Internet, which can make workloads susceptible to DoS attacks from random attackers"
          exploitability: "None"
          attackVector: "Remote"
          scope: "None"
          handler: "IsIngressPolicy"
        - name: "EgressPolicy"
          title: "Workload has egress policy configured"
          shortDescription: "The Kubernetes network policy allows workloads to communicate with specific workloads or specific external IP addresses"
          description: "The Kubernetes egress network policy only allows workloads to communicate with specific workloads or specific external IP addresses, which reduces the attack surface"
          confidentiality: "High"
          confidentialityDescription: "A Kubernetes egress policy makes it harder for an attacker to exploit a vulnerable application or OS, or compromised third-party library, etc. to move laterally inside the cluster or exfiltrate confidential data"
          integrity: "Low"
          integrityDescription: "An egress policy makes it harder to leverage a compromised workload to attack other services in the cluster"
          availability: "Low"
          availabilityDescription: "An egress policy makes it more difficult for a workload to be leveraged to mount a DoS attack on other internal services in the cluster"
          exploitability: "None"
          attackVector: "Remote"
          scope: "Cluster"
          handler: "IsEgressPolicy"
        - name: "notListeningToContainerPorts"
          title: "A listening port isn’t configured"
          shortDescription: "A workload with no listening service is not susceptible to remote networking attacks"
          description: "A workload with no listening service is not susceptible to remote networking attacks"
          confidentiality: "High"
          confidentialityDescription: "When there is no listening port configured, workloads are not accessible remotely and are less likely to be leveraged for lateral movement and data exfiltration"
          integrity: "High"
          integrityDescription: "When there is no listening port, workloads with local vulnerabilities are less likely to be exploited"
          availability: "High"
          availabilityDescription: "When there is no listening port, workloads not accessible remotely are less likely to be overloaded by external users"
          exploitability: "None"
          attackVector: "Remote"
          scope: "None"
          handler: "IsNotListeningToContainerPorts"
        - name: "instrumentedByOctarine"
          title: "Workload is instrumented by Octarine"
          shortDescription: "Service meshes such as Istio and Octarine provide encryption of network traffic as well as strong identity, preventing network sniffing or Man-in-the-Middle (MiTM) attacks"
          description: "The Istio and Octarine service mesh encrypts all internal network activities with a mutual TLS connection and uses certificates to provide strong identity to all workloads, which greatly reduces the potential attack surface"
          confidentiality: "High"
          confidentialityDescription: "Service meshes, such as Istio and Octarine, provide encryption of network traffic, as well as strong identity, which prevents network sniffing and Man-in-the-Middle (MiTM) attacks"
          integrity: "Low"
          integrityDescription: "The strong identity provided by an Octarine and/or Istio service mesh prevents rogue containers from impersonating trusted workloads"
          availability: "Low"
          availabilityDescription: "Service meshes, such as Istio and Octarine, can detect and stop abnormal increases in network activities and network errors"
          exploitability: "None"
          attackVector: "Remote"
          scope: "None"
          handler: "IsInstrumentedByOctarine"
        - name: "instrumentedByIstio"
          title: "Workload is instrumented by Istio"
          shortDescription: "The Istio and Octarine service mesh encrypts all internal network activities with a mutual TLS connection and uses certificates to provide strong identity to all workloads, which greatly reduces the potential attack surface"
          description: "Service meshes such as Istio and Octarine provide encryption of network traffic as well as strong identity, preventing network sniffing or Man-in-the-Middle (MiTM) attacks"
          confidentiality: "High"
          confidentialityDescription: "Service meshes, such as Istio and Octarine, provide encryption of network traffic, as well as strong identity, which prevents network sniffing and Man-in-the-Middle (MiTM) attacks"
          integrity: "Low"
          integrityDescription: "The strong identity provided by an Octarine and/or Istio service mesh prevents rogue containers from impersonating trusted workloads"
          availability: "Low"
          availabilityDescription: "Service meshes, such as Istio and Octarine, can detect and stop abnormal increases in network activities and network errors"
          exploitability: "None"
          attackVector: "Remote"
          scope: "None"
          handler: "IsInstrumentedByIstio"
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kube-scan
  namespace: kube-scan
  labels:
    app: kube-scan
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kube-scan
  labels:
    app: kube-scan
rules:
  - apiGroups:
      - ''
      - 'rbac.authorization.k8s.io'
      - 'extensions'
      - 'apps'
      - 'batch'
      - 'networking.k8s.io'
    resources: 
      - '*'
    verbs:
      - 'get'
      - 'list'
      - 'watch'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kube-scan
  labels:
    app: kube-scan
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kube-scan
subjects:
  - kind: ServiceAccount
    name: kube-scan
    namespace: kube-scan

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: kube-scan
  namespace: kube-scan
  labels:
    app: kube-scan
spec:
  selector:
    matchLabels:
      app: kube-scan
  template:
    metadata:
      labels:
        app: kube-scan
    spec:
      containers:
        - name: kube-scan-ui
          image: siddharth67/kubescan-scanner-ui
          imagePullPolicy: Always
          env:
            - name: API_SERVER_PORT
              value: "80"
            - name: CONTACT_LINK
              value: "mailto:info@octarinesec.com?subject=Octarine%20Contact%20Request"
            - name: WEBSITE_LINK
              value: "https://www.octarinesec.com"
        - name: kube-scan
          image: siddharth67/kubescan-scanner
          env:
            - name: KUBESCAN_PORT
              value: "80"
            - name: KUBESCAN_RISK_CONFIG_FILE_PATH
              value: "/etc/kubescan/risk-config.yaml"
            - name: KUBESCAN_REFRESH_STATE_INTERVAL_MINUTES
              value: "1440"
          imagePullPolicy: Always
          volumeMounts:
            - name: config
              mountPath: /etc/kubescan
      volumes:
        - name: config
          configMap:
            name: kube-scan
            defaultMode: 420
      serviceAccountName: kube-scan
---
apiVersion: v1
kind: Service
metadata:
  name: kube-scan-ui
  namespace: kube-scan
  labels:
    app: kube-scan
spec:
  ports:
    - name: kube-scan-ui
      port: 80
      protocol: TCP
      targetPort: 8080
  selector:
    app: kube-scan
  type: ClusterIP

```

opa-docker-security.rego
```rego
package main

# Do Not store secrets in ENV variables
secrets_env = [
    "passwd",
    "password",
    "pass",
    "secret",
    "key",
    "access",
    "api_key",
    "apikey",
    "token",
    "tkn"
]

deny[msg] {    
    input[i].Cmd == "env"
    val := input[i].Value
    contains(lower(val[_]), secrets_env[_])
    msg = sprintf("Line %d: Potential secret in ENV key found: %s", [i, val])
}

# Only use trusted base images
#deny[msg] {
#    input[i].Cmd == "from"
#    val := split(input[i].Value[0], "/")
#    count(val) > 1
#    msg = sprintf("Line %d: use a trusted base image", [i])
#}

# Do not use 'latest' tag for base imagedeny[msg] {
deny[msg] {
    input[i].Cmd == "from"
    val := split(input[i].Value[0], ":")
    contains(lower(val[1]), "latest")
    msg = sprintf("Line %d: do not use 'latest' tag for base images", [i])
}

# Avoid curl bashing
deny[msg] {
    input[i].Cmd == "run"
    val := concat(" ", input[i].Value)
    matches := regex.find_n("(curl|wget)[^|^>]*[|>]", lower(val), -1)
    count(matches) > 0
    msg = sprintf("Line %d: Avoid curl bashing", [i])
}

# Do not upgrade your system packages
warn[msg] {
    input[i].Cmd == "run"
    val := concat(" ", input[i].Value)
    matches := regex.match(".*?(apk|yum|dnf|apt|pip).+?(install|[dist-|check-|group]?up[grade|date]).*", lower(val))
    matches == true
    msg = sprintf("Line: %d: Do not upgrade your system packages: %s", [i, val])
}

# Do not use ADD if possible
deny[msg] {
    input[i].Cmd == "add"
    msg = sprintf("Line %d: Use COPY instead of ADD", [i])
}

# Any user...
any_user {
    input[i].Cmd == "user"
 }

deny[msg] {
    not any_user
    msg = "Do not run as root, use USER instead"
}

# ... but do not root
forbidden_users = [
    "root",
    "toor",
    "0"
]

#deny[msg] {
#    command := "user"
#    users := [name | input[i].Cmd == "user"; name := input[i].Value]
#    lastuser := users[count(users)-1]
#    contains(lower(lastuser[_]), forbidden_users[_])
#    msg = sprintf("Line %d: Last USER directive (USER %s) is forbidden", [i, lastuser])
#}

# Do not sudo
deny[msg] {
    input[i].Cmd == "run"
    val := concat(" ", input[i].Value)
    contains(lower(val), "sudo")
    msg = sprintf("Line %d: Do not use 'sudo' command", [i])
}

# Use multi-stage builds
default multi_stage = true
multi_stage = true {
    input[i].Cmd == "copy"
    val := concat(" ", input[i].Flags)
    contains(lower(val), "--from=")
}
deny[msg] {
    multi_stage == false
    msg = sprintf("You COPY, but do not appear to use multi-stage builds...", [])
}
```

opa-k8s-security.rego
```rego
package main

deny[msg] {
  input.kind = "Service"
  not input.spec.type = "NodePort"
  msg = "Service type should be NodePort"
}

deny[msg] {
  input.kind = "Deployment"
  not input.spec.template.spec.containers[0].securityContext.runAsNonRoot = true
  msg = "Containers must not run as root - use runAsNonRoot wihin container security context"
}
```

pom.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.12.RELEASE</version>
		<relativePath /> <!-- lookup parent from repository -->
	</parent>

	<groupId>com.devsecops</groupId>
	<artifactId>numeric</artifactId>
	<version>0.0.1</version>
	<name>numeric</name>
	<description>Demo for DevSecOps</description>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

	    <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
		<dependency>
			<groupId>org.springdoc</groupId>
			<artifactId>springdoc-openapi-ui</artifactId>
			<version>1.6.9</version>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
                			  <!--                   Jacoco Plugin                   -->
                <plugin>
                   <groupId>org.jacoco</groupId>
                   <artifactId>jacoco-maven-plugin</artifactId>
                   <version>0.8.5</version>
                   <executions>
                      <execution>
                         <goals>
                            <goal>prepare-agent</goal>
                         </goals>
                      </execution>
                      <execution>
                         <id>report</id>
                         <phase>test</phase>
                         <goals>
                            <goal>report</goal>
                         </goals>
                      </execution>
                   </executions>
                </plugin>
                <!--                   PITest Mutation Plugin                   -->
				<plugin>
                   <groupId>org.pitest</groupId>
                   <artifactId>pitest-maven</artifactId>
                   <version>1.5.0</version>
                   <dependencies>
                      <dependency>
                         <groupId>org.pitest</groupId>
                         <artifactId>pitest-junit5-plugin</artifactId>
                         <version>0.12</version>
                      </dependency>
                   </dependencies>
                   <configuration>
                      <mutationThreshold>75</mutationThreshold>
                      <outputFormats>
                         <outputFormat>XML</outputFormat>
                         <outputFormat>HTML</outputFormat>
                      </outputFormats>
                   </configuration>
                </plugin>
				<!--                   Dependency Check Plugin                   -->
                <plugin>
                   <groupId>org.owasp</groupId>
                   <artifactId>dependency-check-maven</artifactId>
                   <version>6.1.6</version>
                   <configuration>
                      <format>ALL</format>
                      <failBuildOnCVSS>12</failBuildOnCVSS>
                      <!-- fail the build for CVSS greater than or equal to 5 -->
                      <!-- 
			                                  use internal mirroring of CVE contents 
			                                  Suppress files 
			                                  E.g. a company-wide suppression file and local project file 
			                                 -->
                      <!-- 
			                                 <cveUrlModified>http://internal-mirror.mycorp.com/nvdcve-1.1-modified.json.gz</cveUrlModified>  
			                                                <cveUrlBase>http://internal-mirror.mycorp.com/nvdcve-1.1-%d.json.gz</cveUrlBase>
			                                 <suppressionFiles>               
			                                                    <suppressionFile>http://example.org/suppression.xml</suppressionFile>
			                                                    <suppressionFile>project-suppression.xml</suppressionFile> 
			                                                </suppressionFiles> 
			                                             -->
                   </configuration>
                </plugin>
		</plugins>
	</build>

</project>
```

triby-docker-image-scan.sh
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

zap-rules.txt
```txt
100000	IGNORE	http://controlplane:30010
100001  IGNORE  http://controlplane:30011
```

zap.sh
```sh
#!/bin/bash

PORT=$(kubectl -n default get svc ${serviceName} -o json | jq .spec.ports[].nodePort)

# first run this
chmod 777 $(pwd)
echo $(id -u):$(id -g)
docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-weekly zap-api-scan.py -t $applicationURL:$PORT/v3/api-docs -f openapi -c zap-rules.txt -r zap_report.html

exit_code=$?

# HTML Report
 mkdir -p owasp-zap-report
 mv zap_report.html owasp-zap-report


echo "Exit Code : $exit_code"

 if [[ ${exit_code} -ne 0 ]];  then
    echo "OWASP ZAP Report has either Low/Medium/High Risk. Please check the HTML Report"
    exit 1;
   else
    echo "OWASP ZAP did not report any Risk"
 fi;
```