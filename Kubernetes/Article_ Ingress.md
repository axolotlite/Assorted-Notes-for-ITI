# Article: Ingress

As we already discussed **Ingress** in our previous lecture. Here is an update.

In this article, we will see what changes have been made in previous and current versions in **Ingress**.

Like in **apiVersion**, **serviceName** and **servicePort** etc.

[<img class="alignnone wp-image-127032" src="../_resources/7bb94aeced4fc8f4eb868fed726de19d" alt="" width="552" height="341" srcset="https://kodekloud.com/wp-content/uploads/2021/08/1200736109541070.InaagGGYE8f31Jm2PTKH_height640-300x185.png 300w, https://kodekloud.com/wp-content/uploads/2021/08/1200736109541070.InaagGGYE8f31Jm2PTKH_height640-400x247.png 400w, https://kodekloud.com/wp-content/uploads/2021/08/1200736109541070.InaagGGYE8f31Jm2PTKH_height640-624x385.png 624w, https://kodekloud.com/wp-content/uploads/2021/08/1200736109541070.InaagGGYE8f31Jm2PTKH_height640-600x370.png 600w, https://kodekloud.com/wp-content/uploads/2021/08/1200736109541070.InaagGGYE8f31Jm2PTKH_height640.png 640w" sizes="(max-width: 552px) 100vw, 552px" style="box-sizing: border-box; height: auto; max-width: 100%; border: 0px; font-style: italic; vertical-align: bottom;">](https://kodekloud.com/wp-content/uploads/2021/08/1200736109541070.InaagGGYE8f31Jm2PTKH_height640.png)

Now, in k8s version **1.20+** we can create an Ingress resource from the imperative way like this:-

`Format - kubectl create ingress <ingress-name> --rule="host/path=service:port"`

`Example - kubectl create ingress ingress-test --rule="wear.my-online-store.com/wear*=wear-service:80"`

Find more information and examples in the below reference link:-

https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-ingress-em-

**References:-**

https://kubernetes.io/docs/concepts/services-networking/ingress

https://kubernetes.io/docs/concepts/services-networking/ingress/#path-types