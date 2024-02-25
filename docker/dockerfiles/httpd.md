This is a dockerfile for httpd, rename to Dockerfile for use

this assumes that in the same docker build directory exists a file name 'index.html' to copy into the container.
```dockerfile
FROM centos:7
RUN yum -y update
RUN yum -y install httpd
COPY ./index.html /var/www/html/index/html
EXPOSE 80
CMD ["httpd", "-D", "FOREGROUND" ]
```