#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 11:51:55

import os
import cv2


def read(filename):
    """
    读图像
    :param filename: 图像文件名
    :return: 图像对象
    """
    if not os.access(filename, os.F_OK):
        return None
    return cv2.imread(filename)


def write(filename, image):
    """
    写图像
    :param filename: 图像文件名
    :param image: 图像对象
    :return: 无
    """
    if os.access(filename, os.F_OK):
        os.remove(filename)
    cv2.imwrite(filename, image)
    pass


def get_size(filename, debug=False):
    """
    获取宽高以及通道数
    :param filename: 图像文件名
    :param debug: 调试开关
    :return: 宽, 高, 通道数
    """
    if not os.access(filename, os.F_OK):
        return None, None, None
    image = cv2.imread(filename)
    height, width, channel = image.shape
    if debug:
        print(f"Image {filename}, WxH={width}x{height}, Channel={channel}.")
    return width, height, channel
