[github repo](https://github.com/istio/istio)
istio is an open framwork for connecting, securing, managing and monitoring microservices.
it allows for discovery, load-balancing, failure recovery and monitoring.
all of this without using any change of code.

istio control plane contains:
- pilot: used for traffic management
- citadel: service to service auth using tls
- galley: data configuration, also responsible for interpreting kube yaml into a format usable by istio

[installation guide](https://istio.io/latest/docs/setup/getting-started/#download)
```sh
curl -L https://istio.io/downloadIstio | sh -
cd istio-<version-number>
cp bin/istioctl /usr/local/bin/
```
```sh
cd istio-<version-number>
istioctl install --set profile=demo -y
```

you can use the addons to install monitoring tools:

istio sidecar container injection:
it can be done automatically by adding a label to a namespace, this label is `istio-injection=enable`
`kubectl label namespace ns_name istio-injection=enable`
`kubectl apply -f object.yaml`
or manually:
`kubectl apply -f < istioctl kube-inject -f object.yaml`

most of the additional services provided istio can be view and modified using kiali.

we can verify istio configuration using:
`istioctl analyze`

then we can deploy it using kubectl

we can launch kiali using:
`kubectl apply -f istio-version/samples/addons/kiali.yaml`

lock down workloads in the istio-system namespace to only accept mutual TLS traffic. 
```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: devsecops-auth
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
```

Configure an ingress using an Istio gateway on port 80 for http traffic for a host called "devsecops.com"
```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: devsecops-gateway
  namespace: devsecops-istio
spec:
  selector:
    istio: ingressgateway # use istio default controller
  servers:
    - port:
        number: 80
        name: http
        protocol: HTTP
      hosts:
      - "devsecops.com"
```

finally, adding routes for the api:
```yaml
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: devsecops-numeric
  namespace: devsecops-istio
spec:
  hosts:
  - "devsecops.com"
  gateways:
  - devsecops-gateway
  http:
  - match:
    - uri:
        prefix: /increment
    - uri:
        exact: /
    route:
    - destination:
        host: devsecops-svc
        port:
          number: 8080
```

we can install prometheus and grafana using the same method:
`kubectl apply -f istio-version/samples/addons/prometheus.yaml`
`kubectl apply -f istio-version/samples/addons/grafana.yaml`

