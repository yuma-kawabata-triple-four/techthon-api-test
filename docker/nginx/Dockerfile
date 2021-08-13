FROM nginx:1.18-alpine

ENV APP_PATH /etc/nginx

COPY ./default.conf /etc/nginx/conf.d/

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
