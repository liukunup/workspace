# Nextcloud

[官网](https://nextcloud.com/)

![image](https://nextcloud.com/wp-content/uploads/2022/04/Illustration.png)

## 文档推荐

* 镜像 [DockerHub](https://registry.hub.docker.com/_/nextcloud)

## 拉取镜像

```bash
docker pull nextcloud:22.2.9-apache
```

## 镜像运行

### 启动镜像

```bash
docker run -d \
  -p 8086:80 \
  -v nextcloud:/var/www/html \
  -v apps:/var/www/html/custom_apps \
  -v config:/var/www/html/config \
  -v data:/var/www/html/data \
  -v theme:/var/www/html/themes/custom \
  --restart=unless-stopped \
  --name=nextcloud \
  nextcloud:22.2.10-apache
```
