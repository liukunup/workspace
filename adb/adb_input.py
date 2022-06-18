#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-25 00:29:55

from adb import adb_core


def kb_text(msg, ip=None, port=5555, device_id=None, debug=False):
    # https://github.com/senzhk/ADBKeyBoard
    # https://github.com/senzhk/ADBKeyBoard/raw/master/ADBKeyboard.apk
    # 支持中文 记得按照app哟
    adb_core.shell(f"am broadcast -a ADB_INPUT_TEXT --es msg '{msg}'", ip=ip, port=port, device_id=device_id, debug=debug)


def kb_clean(ip=None, port=5555, device_id=None, debug=False):
    # https://github.com/senzhk/ADBKeyBoard
    # https://github.com/senzhk/ADBKeyBoard/raw/master/ADBKeyboard.apk
    # 清空输入框用这个
    adb_core.shell('am broadcast -a ADB_CLEAR_TEXT', ip=ip, port=port, device_id=device_id, debug=debug)


def text(msg, src='touchscreen', ip=None, port=5555, device_id=None, debug=False):
    """
    模拟文本框输入内容(注意需要先Focus在对应文本框)
    :param msg:       输入内容
    :param src:       源(默认为touchscreen)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell(f'input {src} text {msg}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def key_event(key, src='keyboard', ip=None, port=5555, device_id=None, debug=False):
    """
    模拟键盘事件
    :param key:       键值或键代码
    :param src:       源(默认为keyboard)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell(f'input {src} keyevent {key}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def tap(x, y, src='touchscreen', ip=None, port=5555, device_id=None, debug=False):
    """
    模拟点击事件
    :param x:         X坐标
    :param y:         Y坐标
    :param src:       源(默认为touchscreen)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell(f'input {src} tap {x} {y}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def swipe(xs, ys, xe, ye, duration=None, src='touchscreen', ip=None, port=5555, device_id=None, debug=False):
    """
    模拟滑动事件
    :param xs:        起点X坐标
    :param ys:        起点Y坐标
    :param xe:        终点X坐标
    :param ye:        终点Y坐标
    :param duration:  滑动耗费时间(单位: ms)
    :param src:       源(默认为touchscreen)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    if not duration:
        adb_core.shell(f'input {src} swipe {xs} {ys} {xe} {ye} {duration}', ip=ip, port=port, device_id=device_id, debug=debug)
    else:
        adb_core.shell(f'input {src} swipe {xs} {ys} {xe} {ye}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def press(src='trackball', ip=None, port=5555, device_id=None, debug=False):
    """
    模拟轨迹球按下(废弃)
    :param src:       源(默认为trackball)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell(f'input {src} press', ip=ip, port=port, device_id=device_id, debug=debug)
    pass


def roll(dx, dy, src='trackball', ip=None, port=5555, device_id=None, debug=False):
    """
    模拟轨迹球滚动(废弃)
    :param dx:        X方向位移
    :param dy:        Y方向位移
    :param src:       源(默认为trackball)
    :param ip:        地址
    :param port:      端口(默认值5555)
    :param device_id: 设备ID
    :param debug:     调试开关(默认关闭)
    :return: 不涉及
    """
    adb_core.shell(f'input {src} roll {dx} {dy}', ip=ip, port=port, device_id=device_id, debug=debug)
    pass
