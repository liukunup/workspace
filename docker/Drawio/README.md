# Draw.io
![Draw.io](https://drawio-app.com/wp-content/uploads/2020/11/drawio_logo_RGB_dark_mini_199x50px.png)

## 演示截图
![Draw.io](https://drawio-app.com/wp-content/uploads/2021/01/drawio_interface_flowchart-1200x680.png)

## 文档推荐
* 官网 [Draw.io](https://draw.io/)
* 镜像 [DockerHub](https://hub.docker.com/r/jgraph/drawio)
* GitHub [Issues](https://github.com/jgraph/drawio/issues)
* 在线应用 [Diagram](https://app.diagrams.net/)

## 镜像拉取
``` bash
docker pull jgraph/drawio:15.0.3
```

## 镜像运行

### 拉起镜像
``` bash
docker run -d \
    -p 8080:8080 \
    -p 8443:8443 \
    --restart=always \
    --name=workspace-drawio \
    jgraph/drawio:15.0.3
```

## 测试验证
* 打开网站 http://your-ip:8080
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
