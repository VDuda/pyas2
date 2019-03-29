# Docker Instructions

Running
```
docker run --rm -d --mount type=bind,source="$(pwd)"/data,target=/app/django_pyas2/data -p 8080:8080 pyas2
```

Production
```
docker run -d --mount type=bind,source=/data/as2,target=/app/django_pyas2/data  -p 80:8080 registry.gitlab.com/thelightwalk/pyas
```