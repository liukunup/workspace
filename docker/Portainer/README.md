# Portainer
![Portainer](https://www.portainer.io/hubfs/Brand%20Assets/Logos/Portainer%20Logo%20Solid%20All%20-%20Blue%20no%20padding.svg)

## 架构框图
![Diagram](https://www.portainer.io/hubfs/Portainer-Diagram-jpg.jpeg)

## 文档推荐
* 官网 [Portainer](https://www.portainer.io/)
* 镜像 [DockerHub](https://registry.hub.docker.com/r/portainer/portainer-ce)
* 快速入门 [QuickStart](https://documentation.portainer.io/quickstart/)
* 官方文档 [Document](https://documentation.portainer.io/)
* GitHub [Issues](https://github.com/portainer/portainer/issues)
* Slack [Slack](https://join.slack.com/t/portainer/shared_invite/zt-txh3ljab-52QHTyjCqbe5RibC2lcjKA)

## 镜像拉取
``` bash
docker pull portainer/portainer-ce:2.6.2
```

## 镜像运行

### 准备工作
``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/portainer
```

### 拉起镜像
``` bash
docker run -d \
    -p 8000:8000 \
    -p 9000:9000 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ${HOME}/docker/portainer:/data \
    --restart=always \
    --name=workspace-portainer \
    portainer/portainer-ce:2.6.2
```

## 测试验证
* 打开网站 http://your-ip:9000
* 输入创建管理员账号密码, 点击"Create"按钮
* 选择"Docker", 点击"Connect"按钮
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
