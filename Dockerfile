# comments in a Dockerfile?

FROM yobasystems/alpine-nginx:latest
ADD index.html /etc/nginx/html/index.html
RUN apk add --no-cache bash