
# Pods

get pods

```sh
k get pods
```

create nginx pod

```sh
k run nginx --image=nginx
```

delete pod

```sh
k delete pod nginx
```

port forward pod

```sh
k port-forward nginx 8000:80
```
