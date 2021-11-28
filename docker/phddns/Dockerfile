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
