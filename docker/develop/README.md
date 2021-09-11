# Develop

基于此目录可快速在Docker环境下搭建合适您的日常开发环境😏

## 配置差别

* MINI (docker-compose-mini.yaml)
    * Portainer
    * Jupyter Notebook
    * phpMyAdmin
    * MySQL
    * Redis Commander
    * Redis
    * MinIO
    * RabbitMQ Management
    * Nginx

* BASE (docker-compose-base.yaml)
    * Portainer
    * Jupyter Notebook
    * phpMyAdmin
        * MySQL
            * 测试环境
            * 生产环境
    * Redis Commander
        * Redis 测试环境
        * Redis 生产环境
    * MinIO
        * 测试环境
        * 生产环境
    * RabbitMQ Management
        * 测试环境
        * 生产环境
    * Nginx
        * 测试环境
        * 生产环境

* FULL (docker-compose-full.yaml)
    * Portainer
    * Jupyter Notebook
    * Grafana
    * phpMyAdmin
        * MySQL
            * 测试环境
            * 生产环境
        * MariaDB
            * 测试环境
            * 生产环境
    * Redis Commander
        * Redis 测试环境
        * Redis 生产环境
    * MinIO
        * 测试环境
        * 生产环境
    * RabbitMQ Management
        * 测试环境
        * 生产环境
    * Nginx
        * 测试环境
        * 生产环境

## 安装步骤

以BASE配置为例, 环境安装步骤如下:

``` shell
1. 创建持久化目录
sh mkdirs_base.sh

2. 创建容器服务
docker-compose -p dev-base -f docker-compose-base.yaml up -d

3. 停止容器服务
docker-compose stop

4. 重启容器服务
docker-compose restart

5. 移除容器服务
docker-compose down
```

#### 已支持的应用列表

* 可视化容器管理
    * ✅Portainer
* 数据库 DB
    * 关系型数据库
        * ✅phpMyAdmin
        * ✅MySQL
        * ✅MariaDB
        * ❌PostgreSQL
    * NoSQL数据库
        * ✅Redis Commander
        * ✅Redis
        * ❌MongoDB
        * ❌Memcached
* 对象存储 OS
    * ✅MinIO
    * ❌Ceph
* 消息队列 MQ
    * ✅RabbitMQ
    * ❌RocketMQ
    * ❌Kafka
    * ❌MQTT
* 日志服务 SLS
    * ELK
        * ❌ElasticSearch
        * ❌Kibana
        * ❌Logstash
* 负载均衡 SLB
    * ✅Nginx
* 监控 Monitor
    * ❌Prometheus
        * ❌cadvisor
        * ❌node-exporter
        * ❌dcgm-exporter
    * ✅Grafana
