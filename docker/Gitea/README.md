# Gitea

![Gitea](https://www.gitea.com/assets/img/logo.svg)

## 演示截图

![Gitea](https://gitea.io/images/screenshot.png)

## 文档推荐
* 官网 [Gitea](https://gitea.io/zh-cn/)
* 镜像 [DockerHub](https://hub.docker.com/r/gitea/gitea)
* 官方文档 [Document](https://docs.gitea.io/zh-cn/)
* GitHub [Issues](https://github.com/go-gitea/gitea/issues)

## 拉取镜像

``` bash
docker pull gitea/gitea:latest
```

## 镜像运行

### 准备工作

``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/gitea
```

### 启动镜像

``` bash
docker run -d \
    -p 3000:3000 \
    -p 222:22 \
    -v ${HOME}/docker/gitea:/data \
    -v /etc/timezone:/etc/timezone:ro \
    -v /etc/localtime:/etc/localtime:ro \
    -e USER_UID=1000 \
    -e USER_GID=1000 \
    --restart=always \
    --name=gitea \
    gitea/gitea:latest
```

## 测试验证
* 打开网站 http://your-ip-addr:3000/
* enjoy >_<
