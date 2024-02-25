a normal build process could meet a lot of errors, mostly package mismatch, loss, etc..

first stage could be build
`npm run build`
second stage in containerization
docker build -t my-app .
```dockerfile
FROM nginx
COPY dist /usr/share/nginx/html
CMD ["nginx", '-g', "daemon off;"]
```

alternatively we can build it using docker itself.
first stage:
`docker build -t builder .`
```dockerfile
FROM node
copy . .
RUN npm install
RUN npm run build
```
stage 2: 
extract build from first image
```bash
docker container create --name builder builder
docker container cp builder:dist ./dist
docker container rm -f builder
```
third stage is containerization
docker build -t my-app .
```dockerfile
FROM nginx
COPY dist /usr/share/nginx/html
CMD ["nginx", '-g', "daemon off;"]
```


now, if we use multi-stage building in docker, we can do all of this in a single dockerfile.
we use a node container to build the data, then copy it to the nginx container.
using this dockerfile:
```dockerfile
FROM node AS builder
COPY . .
RUN npm install
RUN npm run build

FROM nginx 
COPY --from=builder dist /usr/share/nginx/html
# alternatively we could use the number of the container starting from 0 index
# COPY --from=0 dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
```
if we want to build a specific stage in a dockerfile, we can use the `--target stage_name/number -t image_name build_context` 