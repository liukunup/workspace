# Grafana

![Grafana](https://grafana.com/static/assets/internal/grafana_logo-web-dark.svg)

## 演示截图

![Grafana](https://grafana.com/products/assets/homepage_visual_2.png)

## 文档推荐
* 官网 [Grafana](https://grafana.com/)
* 面板 [Dashboard](https://grafana.com/grafana/dashboards/)
* 镜像 [DockerHub](https://hub.docker.com/u/grafana)
* 快速入门 [QuickStart](https://grafana.com/docs/grafana/latest/getting-started/)
* 官方文档 [Document](https://grafana.com/docs/)
* GitHub [Issues](https://github.com/grafana/grafana/issues)

## 拉取镜像

```bash
docker pull grafana/grafana:latest
```

## 镜像运行

### 准备工作

```bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/grafana
```

### 启动镜像

```bash
docker run -d \
    -p 3000:3000 \
    --restart=always \
    --name=grafana \
    grafana/grafana:latest
```

### 反向代理

1. 拉起容器

```bash
docker run -d \
    -p 3000:3000 \
    -v ${HOME}/docker/grafana:/var/lib/grafana \
    -e GF_SERVER_ROOT_URL='%(protocol)s://%(domain)s:%(http_port)s/grafana' \
    -e GF_SERVER_SERVE_FROM_SUB_PATH=true \
    -e GF_SECURITY_ADMIN_USER=liukunup \
    -e GF_SECURITY_ADMIN_PASSWORD=123456 \
    --user=root \
    --restart=always \
    --name=grafana \
    grafana/grafana:latest
```

2. 配置反向代理

核心配置

```text
location /grafana/ {
    proxy_pass http://prod.liukun.com:3000;
    include nginxconfig.io/proxy.conf;
}
```
