# Nginx
![Nginx](https://www.nginx.com/wp-content/uploads/2020/06/NGINX-Logo-White-Endorsement-RGB.svg)

## 解决方案
![Solution](https://www.nginx.com/wp-content/uploads/2018/07/solutions-diagram.jpg)

## 文档推荐
* 官网 [Nginx](https://www.nginx.com/)
* 镜像 [DockerHub](https://hub.docker.com/_/nginx)
* 快速入门 [QuickStart](http://nginx.org/en/docs/beginners_guide.html)
* 官方文档 [Document](http://nginx.org/en/docs/)
* GitHub [Issues](https://github.com/nginxinc/docker-nginx/issues)

## 镜像拉取
``` bash
docker pull nginx:latest
```

## 镜像运行

### 准备工作
``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/nginx
```

### 拉起镜像
``` bash
docker run -d \
  -p 80:80 \
  -v ${HOME}/docker/nginx/nginx.conf:/etc/nginx/nginx.conf:ro \
  --restart=always \
  --name=workspace-nginx \
  nginx:latest
```

docker run -d \
  -p 80:80 \
  --restart=always \
  --name=workspace-nginx \
  nginx:latest




``` bash
version: '3'

services:

  nginx:
    container_name: nginx
    image: nginx:latest
    restart: always
    ports:
      - 80:80
    volumes:
      - ${HOME}/docker/nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    environment:
      - TZ=Asia/Shanghai
    networks:
      - nginx-stack

networks:
  nginx-stack:
    driver: bridge
```

## 测试验证
* 打开网站 http://your-ip:port/
* enjoy >_<

## 常用配置

### 反向代理

``` bash
http {
...

    server {
        listen 80;
        server_name xxx.com;
        
        # http://xxx.com/jupyter/... -> http://yyy.com:8888/jupyter/...
        location /jupyter/ {
            proxy_pass       http://yyy.com:8888;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_redirect off;
        }
    }

...
}
```

### 负载均衡

``` bash
stream {
    upstream mysql {
       server 192.168.100.xxx:3306 weight=5 max_fails=3 fail_timeout=30s;
    }
    server {
       listen 3306;
       proxy_connect_timeout 30s;
       proxy_timeout 600s;
       proxy_pass mysql;
    }
}
```

## 问题反馈
* 邮件 (liukunwlb#163.com, 把#换成@)
* 微信 liukun250596945

## 关于作者

``` javascript
var liukunup = {
  nickname  : "我的代码温柔如风",
  site : "http://liukunup.com"
}
```







docker cp nginx workspace-nginx:/etc/










































user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}










user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;

events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;

    server {
        listen 80;
        server_name liukunup.oicp.io;
        location /portainer/ {
            proxy_pass http://aio.liukun.com:9000;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            rewrite "^/portainer/(.*)$" /$1 break;
        }
        location /phpmyadmin/ {
            proxy_pass http://aio.liukun.com:9080;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            rewrite "^/phpmyadmin/(.*)$" /$1 break;
        }
        location /grafana/ {
            proxy_pass http://aio.liukun.com:3000;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
        }
        location /jupyter/ {
            proxy_pass       http://aio.liukun.com:8888;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_redirect off;
        }
        location / {
            proxy_pass http://bastion.liukun.com:10000;
            proxy_http_version 1.1;
            proxy_buffering off;
            proxy_request_buffering off;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $remote_addr;
        }
    }
}
