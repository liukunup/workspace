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

# 拉取镜像
``` bash
docker pull grafana/grafana:8.3.3
```

# 启动镜像
``` bash
docker run -d \
    -p 3000:3000 \
    -v ${HOME}/docker/grafana:/var/lib/grafana \
    --user=root \
    --restart=always \
    --name=grafana \
    grafana/grafana:8.3.3
```

## 测试验证
* 打开网站 http://your-ip:3000/
* 默认账号密码 admin/admin
* enjoy >_<
