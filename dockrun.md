# Docker Instructions

Running
```
docker run -it --mount type=bind,source="$(pwd)"/data,target=/data  -p 8080:8080 pyas2 
```