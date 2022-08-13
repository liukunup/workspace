# Code Server

![code-server-banner](https://raw.githubusercontent.com/linuxserver/docker-templates/master/linuxserver.io/img/code-server-banner.png)

## 文档推荐

* 镜像 [DockerHub](https://registry.hub.docker.com/r/linuxserver/code-server)
* GitHub [Issues](https://github.com/coder/code-server/issues)

## 拉取镜像

```bash
docker pull linuxserver/code-server:latest
```

## 镜像运行

### 准备工作

```bash
mkdir ${HOME}/docker/code-server
mkdir ${HOME}/docker/code-server/workspace
mkdir ${HOME}/docker/code-server/config
```

### 启动镜像

```bash
docker run -d \
  -p 8444:8443 \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Asia/Shanghai \
  -e HASHED_PASSWORD='$argon2i$v=19$m=4096,t=3,p=1$kWrzf2c0IKyk8t/LwhEyJg$Ps0yVV637Oy9fv0RxBxhIwhbGweQYNDjOMdy69MGyW4' \
  -e SUDO_PASSWORD_HASH='$argon2i$v=19$m=4096,t=3,p=1$kWrzf2c0IKyk8t/LwhEyJg$Ps0yVV637Oy9fv0RxBxhIwhbGweQYNDjOMdy69MGyW4' \
  -e PROXY_DOMAIN=prod.liukun.com \
  -e DEFAULT_WORKSPACE=/config/workspace \
  -v ${HOME}/code-server/config:/config \
  --restart=unless-stopped \
  --name=code-server \
  lscr.io/linuxserver/code-server:latest
```

怎么创建一个Hash密码

```shell
echo -n "hard-to-guess" | npx argon2-cli -e
$argon2i$v=19$m=4096,t=3,p=1$kWrzf2c0IKyk8t/LwhEyJg$Ps0yVV637Oy9fv0RxBxhIwhbGweQYNDjOMdy69MGyW4
```
