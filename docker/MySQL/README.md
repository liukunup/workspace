# MySQL
![MySQL](https://d1q6f0aelx0por.cloudfront.net/product-logos/library-mysql-logo.png)

## 文档推荐
* 官网 [MySQL](https://www.mysql.com/)
* 镜像 [DockerHub](https://hub.docker.com/_/mysql)
* 菜鸟教程 [RUNOOB](https://www.runoob.com/mysql/mysql-tutorial.html)
* W3Cschool [W3Cschool](https://www.w3cschool.cn/mysql/)

## 镜像拉取
``` bash
docker pull mysql:8
```

## 镜像运行

### 准备工作
``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/mysql
```

### 拉起镜像
``` bash
docker run -d \
    -p 3306:3306 \
    -v ${HOME}/docker/mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=wZ6try8MCNGi6n8P \
    --restart=always \
    --name=workspace-mysql \
    mysql:8 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci
```

### 拉起镜像(拉起时创建数据库和管理账户密码)
``` bash
docker run -d \
    -p 3306:3306 \
    -v ${HOME}/docker/mysql:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=wZ6try8MCNGi6n8P \
    -e MYSQL_DATABASE=db_school \
    -e MYSQL_USER=admin \
    -e MYSQL_PASSWORD=123456 \
    --restart=always \
    --name=workspace-mysql \
    mysql:8 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci
```

## 测试验证
* 使用"MySQL Workbench"或"phpMyAdmin"来连接数据库进行验证和体验
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
