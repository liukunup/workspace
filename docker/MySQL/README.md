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

### 1. 单实例

#### 1.1 准备工作

``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/mysql
```

#### 1.2 拉起镜像

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

### 1.3 拉起镜像(拉起时创建数据库和管理账户密码)

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

### 2. 主从热备(一主一从)

#### 2.1 准备工作

``` bash
mkdir ${HOME}/docker
mkdir ${HOME}/docker/mysql
mkdir ${HOME}/docker/mysql/main
mkdir ${HOME}/docker/mysql/replica
mkdir ${HOME}/docker/mysql/conf
mkdir ${HOME}/docker/mysql/conf/main
mkdir ${HOME}/docker/mysql/conf/replica
```

#### 2.2 拉起镜像

``` bash
docker run -d \
    -p 3306:3306 \
    -v ${HOME}/docker/mysql/main:/var/lib/mysql \
    -v ${HOME}/docker/mysql/conf/main:/etc/mysql/conf.d:ro \
    -e MYSQL_ROOT_PASSWORD=wZ6try8MCNGi6n8P \
    --restart=always \
    --name=xxx-mysql-main \
    mysql:8 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci
```

``` bash
docker run -d \
    -p 63306:3306 \
    -v ${HOME}/docker/mysql/replica:/var/lib/mysql \
    -v ${HOME}/docker/mysql/conf/replica:/etc/mysql/conf.d:ro \
    -e MYSQL_ROOT_PASSWORD=wZ6try8MCNGi6n8P \
    --restart=always \
    --name=xxx-mysql-replica \
    mysql:8 \
    --character-set-server=utf8mb4 \
    --collation-server=utf8mb4_unicode_ci
```

#### 2.3 数据库配置

**主服务器配置**

- 配置清单

``` text
[mysqld]
## 同一局域网内注意要唯一
server-id=100
## 二进制日志
log-bin=mysql-bin
## 日志格式
binlog_format=mixed
## 日志文件大小
max_binlog_size=100m
```

- 创建同步用户

``` sql
# 创建用户
CREATE USER 'HEebDKdG'@'%' IDENTIFIED BY 'FnVYR8Hno&kHp3sN';
# 备注: MySQL 8.0 密码认证插件需要修改(caching_sha2_password), 改完记得密码也改一下. 或者手动创建这个用户.
ALTER USER 'HEebDKdG'@'%' IDENTIFIED WITH mysql_native_password BY 'FnVYR8Hno&kHp3sN';
# 分配权限
GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'HEebDKdG'@'%';
# 刷新权限
FLUSH PRIVILEGES;
```

- 获取主服务器状态

``` sql
# 获取Master状态
SHOW MASTER STATUS;
```

记录查询到的File/Position值.(例如: mysql-bin.000003/1164)

**从服务器配置**

- 配置清单

``` text
[mysqld]
## 同一局域网内注意要唯一
server-id=101
## 二进制日志
log-bin=mysql-bin
## 中继日志
relay-log=mysql-relay-bin
```

- 数据库设置

``` sql
# 配置同步参数
CHANGE REPLICATION SOURCE TO 
SOURCE_HOST = 'mysql-main',
SOURCE_USER = 'HEebDKdG',
SOURCE_PASSWORD = 'FnVYR8Hno&kHp3sN',
SOURCE_PORT = 3306,
SOURCE_LOG_FILE = 'mysql-bin.000003',
SOURCE_LOG_POS = 1164,
SOURCE_CONNECT_RETRY = 30;
# 查询Slave状态
SHOW SLAVE STATUS;

# 开始同步
START REPLICA;
# 获取同步状态
SHOW REPLICA STATUS;
# 停止同步
STOP REPLICA;
```

### 3. Docker Compose 脚本文件

``` docker-compose
version: '3'

services:

  phpmyadmin:
    container_name: mysql-stack-phpmyadmin
    image: phpmyadmin/phpmyadmin:5.1.1
    hostname: phpmyadmin
    restart: always
    ports:
      - "9080:80"
    environment:
      - PMA_HOSTS=mysql-main,mysql-replica
      - PMA_PORT=3306
    links:
      - mysql-main
      - mysql-replica
    depends_on:
      - mysql-main
      - mysql-replica
    networks:
      - mysql-stack

  mysql-main:
    container_name: mysql-stack-main
    image: mysql:8
    hostname: mysql-main
    restart: always
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    ports:
      - "3306:3306"
    volumes:
      - ${HOME}/docker/mysql/main:/var/lib/mysql
      - ${HOME}/docker/mysql/conf/main:/etc/mysql/conf.d:ro
    environment:
      - MYSQL_ROOT_PASSWORD=wZ6try8MCNGi6n8P
    networks:
      - mysql-stack

  mysql-replica:
    container_name: mysql-stack-replica
    image: mysql:8
    hostname: mysql-replica
    restart: always
    command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    ports:
      - "3307:3306"
    volumes:
      - ${HOME}/docker/mysql/replica:/var/lib/mysql
      - ${HOME}/docker/mysql/conf/replica:/etc/mysql/conf.d:ro
    environment:
      - MYSQL_ROOT_PASSWORD=wZ6try8MCNGi6n8P
    networks:
      - mysql-stack

networks:
  mysql-stack:
    driver: bridge
```

- 拉起、销毁的脚本

``` shell
docker-compose -f xxx.yaml up -d
docker-compose down
```


## 测试验证

* 使用"MySQL Workbench"或"phpMyAdmin"来连接数据库进行验证和体验
* enjoy >_<
