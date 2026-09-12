
# Namespaces

```sh
k create namespace xpto

k get namespaces

k get pods -n xpto

# get pods with all namespaces
k get pods -A

k describe namespace xpto

k delete ns xpto

# run a pod in a specific namespace
k run nginx --image=nginx -n xpto
```
