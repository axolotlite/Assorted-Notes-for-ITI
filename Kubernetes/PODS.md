kubernetes encapsulates containers inside and object called "pod"
pod is the smalled object creatable by kubernetes, it is a single instance of an application

the number of pods can scale up and down according to demand on the cluster.

a single pod can encapsilate several containers. like the app itself and its helper containers.

helper containers have a 1 to 1 relationship with their containers.

multi-container pods are a rare usecase.