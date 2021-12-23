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
docker pull grafana/grafana:latest
```

# 启动镜像
``` bash
docker run -d \
    -p 3000:3000 \
    -v ${HOME}/docker/grafana:/var/lib/grafana \
    --user=root \
    --restart=always \
    --name=workspace-grafana \
    grafana/grafana:latest
```

## 测试验证
* 打开网站 http://your-ip:3000/
* 默认账号密码 admin/admin
* enjoy >_<

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