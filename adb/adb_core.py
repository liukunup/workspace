#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-25 00:07:55

import subprocess


def execute(cmd, ip=None, port=5555, device_id=None, debug=False):
    """
    在命令行执行`adb [cmd]`指令
    :param cmd:       命令行
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 执行结果
    """
    # 执行指令时加装 地址:端口
    if not ip and port > 1000:
        cmd = f'adb {ip}:{port} {cmd}'
    # 执行指令时加装 设备ID 高优先级哦
    if not device_id:
        cmd = f'adb {device_id} {cmd}'
    # 打印待执行指令
    if debug:
        print(cmd)
    # 使用subprocess来执行命令
    with subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p:
        # 获取执行结果
        lines = p.stdout.readlines()
        if debug:
            for line in lines:
                print(line)
        p.stdout.close()
        p.kill()
    # 返回执行结果
    return lines


def shell(cmd, ip=None, port=5555, device_id=None, debug=False):
    """
    在命令行执行`adb shell [cmd]`指令
    :param cmd:       命令行
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 执行结果
    """
    return execute(f'shell {cmd}', ip=ip, port=port, device_id=device_id, debug=debug)
