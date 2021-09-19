#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 11:51:55

import time
import datetime


def timestamp_num(style='毫秒级'):
    """
    获取时间戳
    :param style: 输出数值的样式
    :return: 时间戳字符串
    """
    t = time.time()
    t2str = {
        '原始': t,
        '秒级': int(t),
        '毫秒级': int(round(t * 1000)),
        '微秒级': int(round(t * 1000000)),
    }
    return t2str[style] if style in t2str else None


def timestamp_str(fmt='%Y-%m-%d %H:%M:%S'):
    """
    获取时间戳
    :param fmt: 输出字符串的格式
    :return: 时间戳字符串
    """
    return datetime.datetime.now().strftime(fmt)
