# MinIO
![MinIO](https://raw.githubusercontent.com/minio/minio/master/.github/logo.svg)

## 演示截图
![Dashboard](https://docs.min.io/minio/baremetal/_images/minio-console-dashboard1.png)
备注: 实际Dashboard面板并没有这么漂亮，不知道为啥!

## 文档推荐
* 官网 [MinIO](https://min.io/)
* 镜像 [DockerHub](https://hub.docker.com/r/minio/minio)
* 快速入门 [QuickStart](https://docs.min.io/docs/minio-docker-quickstart-guide.html)
* 官方文档 [Document](https://docs.min.io/)
* GitHub [Issues](https://github.com/minio/minio/issues)

## 镜像拉取
``` bash
docker pull minio/minio:RELEASE.2022-06-17T02-00-35Z
```

## 镜像运行

### 准备工作
``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/minio
```

### 拉起镜像
``` bash
docker run -d \
    -p 9000:9000 \
    -p 9001:9001 \
    -v ${HOME}/docker/minio:/data \
    -e MINIO_ROOT_USER=LehXBoVThyyDU3vZ \
    -e MINIO_ROOT_PASSWORD=Ggi057AOL8ZRrvxv \
    --restart=always \
    --name=minio \
    minio/minio:RELEASE.2022-06-17T02-00-35Z \
    server /data \
    --address ":9000" \
    --console-address ":9001"
```

## 测试验证
* 打开网站 http://your-ip:9001
* 输入上述管理员账号密码, 点击登录按钮
* enjoy >_<
