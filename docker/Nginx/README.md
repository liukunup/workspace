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

## 参数配置

参考conf

## 部署实施

1. 镜像构建

```shell
docker build -t liukunup/nginx:latest .
```

2. 镜像推送

```shell
docker push liukunup/nginx:latest
```

3. 构建镜像

```shell
docker run -d -p 80:80 --restart=always --name=nginx liukunup/nginx:latest 
```
