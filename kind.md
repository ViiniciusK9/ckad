
# Kind

```sh

kind create cluster --name ckad --config kind-config.yaml

kind get clusters

kind delete clusters ckad


# install metrics server
k apply -f 05-deployments-replicasets/metric-server.yaml
```
