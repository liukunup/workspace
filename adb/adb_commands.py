#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-25 00:46:55

import re
from adb import adb_core


def list_device(debug=False):
    """
    列举设备
    :param debug: 调试开关(默认关闭)
    :return: 设备列表
    """
    lines = adb_core.execute('devices', debug=debug)
    device_list = list()
    for line in lines:
        res = re.search(re.compile(r'(?P<device>[A-Za-z0-9\\.\\:]+)\\tdevice\\r\\n'), str(line))
        if res:
            device = res.group('device')
            search_ip_addr_res = re.search(re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|'
                                                      r'2[0-4][0-9]|[01]?[0-9][0-9]?)\b'), device)
            if search_ip_addr_res:
                device_list.append(search_ip_addr_res.group())
            else:
                device_list.append(device)
    if debug:
        for device in device_list:
            print(device)
    return device_list


def push(fr, to, ip=None, port=5555, device_id=None, debug=False):
    """
    导入文件
    :param fr:        文件源地址
    :param to:        文件目标地址
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.execute(f'push -p {fr} {to}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def pull(fr, to, ip=None, port=5555, device_id=None, debug=False):
    """
    导出文件
    :param fr:        文件源地址
    :param to:        文件目标地址
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.execute(f'pull -p -a {fr} {to}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def install(apk, mode='', ip=None, port=5555, device_id=None, debug=False):
    """
    安装APK
    :param apk:       apk文件
    :param mode:      模式
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute(f'install {mode} {apk}', ip=ip, port=port, device_id=device_id, debug=debug)


def uninstall(pkg, mode='', ip=None, port=5555, device_id=None, debug=False):
    """
    卸载APK
    :param pkg:       apk包名
    :param mode:      模式
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute(f'uninstall {mode} {pkg}', ip=ip, port=port, device_id=device_id, debug=debug)


def connect(ip, port=5555, debug=False):
    """
    通过 地址:端口 来连接设备
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute(f'connect {ip}:{port}', debug=debug)


def disconnect(ip, debug=False):
    """
    断开连接
    :param ip:        地址
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute(f'disconnect {ip}', debug=debug)


def remount(ip=None, port=5555, device_id=None, debug=False):
    """
    重新挂载
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('remount', ip=ip, port=port, device_id=device_id, debug=debug)


def shutdown(ip=None, port=5555, device_id=None, debug=False):
    """
    关机
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('shutdown', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def reboot(ip=None, port=5555, device_id=None, debug=False):
    """
    重启
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('reboot', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def reboot_bootloader(device_id=None, debug=False):
    """
    重启至bootloader
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('reboot-bootloader', device_id=device_id, debug=debug)


def reboot_recovery(device_id=None, debug=False):
    """
    重启至recovery
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('reboot recovery', device_id=device_id, debug=debug)


def root(ip=None, port=5555, device_id=None, debug=False):
    """
    获取root权限
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('root', ip=ip, port=port, device_id=device_id, debug=debug)


def usb(debug=False):
    """
    切换到usb模式
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('usb', debug=debug)


def tcpip(port=5555, debug=False):
    """
    切换到tcpip模式(网络模式)
    :param port:      端口(默认值5555)
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute(f'tcpip {port}', debug=debug)


def show_version(ip=None, port=5555, device_id=None, debug=False):
    """
    获取adb版本
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('version', ip=ip, port=port, device_id=device_id, debug=debug)


def show_help(ip=None, port=5555, device_id=None, debug=False):
    """
    获取adb帮助信息
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    return adb_core.execute('help', ip=ip, port=port, device_id=device_id, debug=debug)
