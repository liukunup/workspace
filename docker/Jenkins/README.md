# Jenkins

[官网](https://www.jenkins.io/zh/)

## 文档推荐

* 镜像 [DockerHub](https://hub.docker.com/r/jenkins/jenkins)

## 拉取镜像

```bash
docker pull jenkinsci/blueocean:latest
```

## 镜像运行

### 启动镜像

```bash
docker run -d \
  -p 8087:8080 \
  -p 50000:50000 \
  -v jenkins-data:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --user=root \
  --restart=unless-stopped \
  --name=jenkinsci-blueocean \
  jenkinsci/blueocean:latest
```
