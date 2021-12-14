# Jupyter
![Jupyter](https://jupyter.org/assets/nav_logo.svg)

## 演示截图
![JupyterLab](https://jupyter.org/assets/labpreview.png)

## 文档推荐
* 官网 [Jupyter](https://jupyter.org/)
* 镜像 [DockerHub](https://hub.docker.com/u/jupyter)
* 快速入门 [QuickStart](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)
* 官方文档 [Document](https://jupyter.org/documentation)
* GitHub [Issues](https://github.com/jupyter/docker-stacks/issues)

## 镜像选择
![images](https://jupyter-docker-stacks.readthedocs.io/en/latest/_images/inherit.svg)

## 镜像拉取
``` bash
docker pull jupyter/minimal-notebook:notebook-6.4.0
```

## 镜像运行

### 准备工作
``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/jupyter
```

### 拉起镜像
``` bash
docker run -d \
    -p 8888:8888 \
    -e JUPYTER_ENABLE_LAB=yes \
    -e GRANT_SUDO=yes \
    -v ${HOME}/docker/jupyter:/home/jovyan/work \
    --restart=always \
    --name=workspace-jupyter \
    jupyter/minimal-notebook:notebook-6.4.0 start-notebook.sh \
    --NotebookApp.password='sha1:a7c0702d28e9:8a8868c5d4ea33af70e04c634487402b3997f40c' \
    --NotebookApp.base_url=/jupyter/
```

## 测试验证

* 打开网站 http://your-ip:8888/jupyter/
* 在命令行窗口输入"docker ps"查找刚刚创建的容器实例
* 通过命令行"docker logs [容器id]"查看日志, 找到token用于登陆
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
