#!/bin/bash

# 如果任何命令失败,则退出脚本(非零值)
set -e

# 打印当前日期
date

# 执行花生壳指令
# 启动
phddns start
# 等待3秒
sleep 3s
# 状态
phddns status
# 开机自启动
phddns enable

# 回显帮助文档链接
echo "see https://service.oray.com/question/11630.html"

# 重定向输入变量
exec "$@"
