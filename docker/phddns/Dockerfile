# 基础镜像
FROM ubuntu:focal
# 作者信息
MAINTAINER LiuKun<liukunup@163.com>
# 花生壳版本&架构
ENV HSK_VERSION 5.2.0_amd64
# 时区(可选)
ENV TZ Asia/Shanghai
# 安装花生壳
RUN    apt-get update \
    && apt-get install wget net-tools -y \
    && wget "https://down.oray.com/hsk/linux/phddns_${HSK_VERSION}.deb" -O phddns_${HSK_VERSION}.deb \
    && dpkg -i phddns_${HSK_VERSION}.deb \
    && rm -f phddns_${HSK_VERSION}.deb \
    && apt-get clean
# 拷贝入口程序
COPY entrypoint.sh /
# 执行入口程序
ENTRYPOINT ["/entrypoint.sh"]
