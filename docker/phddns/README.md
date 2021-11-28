# 花生壳(内网穿透) Docker版本

## 官方信息

花生壳[官网](https://hsk.oray.com/)

花生壳[客户端下载](https://hsk.oray.com/download/)

花生壳[Linux使用教程](https://service.oray.com/question/11630.html)

## 使用方法

1、拉取镜像

``` shell
docker pull liukunup/phddns:latest
```

2、拉起容器

``` shell
docker run -d --net=host --name=phddns liukunup/phddns:latest
```

3、重置SN（由于镜像构建时安装花生壳已生成SN, 避免大家使用一样的SN号可以在使用前重置）

``` shell
# 进入容器/bin/bash执行命令
docker exec -it phddns /bin/bash
# 重置
phddns reset
# 启动
phddns start
# 查看
phddns status
```

4、设置&使用

1.浏览器输入远程管理地址[b.oray.com](b.oray.com)进入花生壳远程管理页面, 输入重置花生壳时生成的SN码及默认密码admin进入;

2.首次登录, 请按照提示选择扫码激活或者密码激活, 以完成激活和授权操作。


## 构建镜像

### Dockerfile
``` Dockerfile
# 基础镜像
FROM ubuntu:18.04
# 作者信息
MAINTAINER LiuKun<liukunup@163.com>
# 花生壳版本&架构
ENV HSK_VERSION 5_1_amd64
# 时区(可选)
ENV TZ Asia/Shanghai
# 无交互前端(可选)
ENV DEBIAN_FRONTEND noninteractive
# 工作目录
WORKDIR /usr/phddns
# 安装花生壳
RUN apt-get update \
    && apt-get install wget net-tools -y \
    && wget "https://down.oray.com/hsk/linux/phddns_${HSK_VERSION}.deb" -O phddns_${HSK_VERSION}.deb \
    && dpkg -i phddns_${HSK_VERSION}.deb && rm -f phddns_${HSK_VERSION}.deb \
    && apt-get clean
# 容器入口 "top -b"占住容器使其不会因空闲而退出
ENTRYPOINT ["top", "-b"]
CMD ["-c"]
```

### 构建->打标签->推送
``` shell
# 如未登陆, 需要先登陆DockerHub账号
docker login
# 镜像构建
docker build -t liukunup/phddns:latest .
# 镜像推送
docker push liukunup/phddns:latest

# 查看当前镜像的IMAGE ID
docker images
# 搭上新版本标签
docker tag <IMAGE ID> liukunup/phddns:<版本号>
# 镜像推送
docker push liukunup/phddns:<版本号>
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
