# JumpServer 堡垒机
![Jupyter](https://jupyter.org/assets/nav_logo.svg)

## 演示截图
![JupyterLab](https://jupyter.org/assets/labpreview.png)

## 文档推荐
* 官网 [Jupyter](https://jupyter.org/)
* 镜像 [DockerHub](https://hub.docker.com/u/jupyter)
* 快速入门 [QuickStart](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)
* 官方文档 [Document](https://jupyter.org/documentation)
* GitHub [Issues](https://github.com/jumpserver/Dockerfile/tree/master/allinone)

## 镜像选择
![images](https://jupyter-docker-stacks.readthedocs.io/en/latest/_images/inherit.svg)

## 镜像拉取
``` bash
docker pull jumpserver/jms_all:v2.16.3
```

## 镜像运行

### 准备工作
``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/jumpserver
mkdir ${HOME}/docker/jumpserver/core
mkdir ${HOME}/docker/jumpserver/core/data
mkdir ${HOME}/docker/jumpserver/koko
mkdir ${HOME}/docker/jumpserver/koko/data
mkdir ${HOME}/docker/jumpserver/lion
mkdir ${HOME}/docker/jumpserver/lion/data
```

### 拉起镜像

``` bash
docker run --name jms_all -d \
  -v ${HOME}/docker/jumpserver/core/data:/opt/jumpserver/data \
  -v ${HOME}/docker/jumpserver/koko/data:/opt/koko/data \
  -v ${HOME}/docker/jumpserver/lion/data:/opt/lion/data \
  -p 10000:80 \
  -p 2222:2222 \
  -e SECRET_KEY=kWQdmdCQKjaWlHYpPhkNQDkfaRulM6YnHctsHLlSPs8287o2kW \
  -e BOOTSTRAP_TOKEN=KXOeyNgDeTdpeu9q \
  -e LOG_LEVEL=ERROR \
  -e DB_HOST=aio.liukun.com \
  -e DB_PORT=3306 \
  -e DB_USER=jumpserver \
  -e DB_PASSWORD=nu4x599Wq7u0Bn8EABh3J91G \
  -e DB_NAME=jumpserver \
  -e REDIS_HOST=aio.liukun.com \
  -e REDIS_PORT=6379 \
  -e REDIS_PASSWORD=kyUQ9xf7knPbYCQt \
  --privileged=true \
  jumpserver/jms_all:v2.16.3
```

## 测试验证
* 打开网站 http://your-ip:10000/
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
