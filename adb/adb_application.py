#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-25 01:01:55

import re
import datetime

from adb import adb_core, adb_commands


def screen_shot(save_to='./', ip=None, port=5555, device_id=None, debug=False):
    """
    屏幕截图
    :param save_to:   保存到XXX路径(默认为当前路径)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 截屏文件名
    """
    adb_core.shell('screencap -p /sdcard/screen.png', ip=ip, port=port, device_id=device_id, debug=debug)
    ts = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    fn = f'{save_to}/screen_{ts}.png'
    adb_commands.pull('/sdcard/screen.png', fn, ip=ip, port=port, device_id=device_id, debug=debug)
    adb_core.shell('rm -f /sdcard/screen.png', ip=ip, port=port, device_id=device_id, debug=debug)
    return fn


def uiautomator(save_to='./', ip=None, port=5555, device_id=None, debug=False):
    """
    导出当前屏幕UI布局
    :param save_to:   保存到XXX路径(默认为当前路径)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 截屏文件名
    """
    adb_core.shell('uiautomator dump /sdcard/ui.xml', ip=ip, port=port, device_id=device_id, debug=debug)
    ts = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    fn = f'{save_to}/ui_{ts}.xml'
    adb_commands.pull('/sdcard/ui.xml', fn, ip=ip, port=port, device_id=device_id, debug=debug)
    adb_core.shell('rm -f /sdcard/ui.xml', ip=ip, port=port, device_id=device_id, debug=debug)
    return fn


def mem_info(ip=None, port=5555, device_id=None, debug=False):
    """
    获取内存信息
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('dumpsys meminfo', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def cpu_info(ip=None, port=5555, device_id=None, debug=False):
    """
    获取CPU信息
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('dumpsys cpuinfo', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def battery(ip=None, port=5555, device_id=None, debug=False):
    """
    获取电池信息
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('dumpsys battery', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def wifi(ip=None, port=5555, device_id=None, debug=False):
    """
    获取WIFI信息
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('dumpsys wifi', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def display(ip=None, port=5555, device_id=None, debug=False):
    """
    获取屏幕显示信息
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell('dumpsys display | grep DisplayDeviceInfo', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def __locate_app_by_name(filename, app_name):
    """
    根据名字定位桌面app图标的位置
    :param filename: ui.xml文件
    :param app_name: app名称
    :return: 坐标
    """
    with open(filename, encoding='UTF-8') as f:
        contents = f.readline()
        pattern = re.compile(r'\<node '
                             r'index="[0-9]*" '
                             r'text="%s" '
                             r'resource-id="[A-Za-z0-9\\.\\:_\\/]*" '
                             r'class="[A-Za-z0-9\\.]*" '
                             r'package="[A-Za-z0-9\\.]*" '
                             r'content-desc="" '
                             r'checkable="\b(true|false)\b" '
                             r'checked="\b(true|false)\b" '
                             r'clickable="\b(true|false)\b" '
                             r'enabled="\b(true|false)\b" '
                             r'focusable="\b(true|false)\b" '
                             r'focused="\b(true|false)\b" '
                             r'scrollable="\b(true|false)\b" '
                             r'long-clickable="\b(true|false)\b" '
                             r'password="\b(true|false)\b" '
                             r'selected="\b(true|false)\b" '
                             r'bounds="'
                             r'\[(?P<left>[0-9]+),'
                             r'(?P<top>[0-9]+)\]'
                             r'\[(?P<right>[0-9]+),'
                             r'(?P<bottom>[0-9]+)\]" \/\>' % app_name)
        res = re.search(pattern, str(contents))
        f.close()
    if res:
        return res.group('left'), res.group('top'), res.group('right'), res.group('bottom')
    else:
        return None, None, None, None


def locate_app(app_name, ip=None, port=5555, device_id=None, debug=False):
    """
    根据名字定位桌面app图标的位置
    :param app_name:  app名称
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 坐标, UI文件
    """
    fn = uiautomator(ip=ip, port=port, device_id=device_id, debug=debug)
    res = __locate_app_by_name(fn, app_name)
    return res, fn
