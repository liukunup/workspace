#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-10-17 20:26:55

import random
import threading
from adb import adb_input


class LikeThread(threading.Thread):
    """
    这是一个刷赞的线程
    """

    # 以目标点为中心,随机坐标偏置,请设置最大的偏置值
    __offset_max = 5

    def __init__(self, point):
        threading.Thread.__init__(self)
        self.point = point
        pass

    def run(self):
        # 持续刷赞哈哈哈
        while True:
            print('-' * 25, 'tid = %s' % threading.current_thread().getName(), '-' * 25)
            x_offset = random.randint(self.__offset_max * -1, self.__offset_max)
            y_offset = random.randint(self.__offset_max * -1, self.__offset_max)
            adb_input.tap(self.point[0] + x_offset, self.point[1] + y_offset, debug=True)
        pass


if __name__ == '__main__':
    # 点赞按钮图标的位置
    # 微信公众直播 -> 点赞 (985, 2205)
    icon_like_pos = [985, 2205]
    # 刷赞线程数
    thread_num = 4
    # 多线程刷赞程序
    thread_list = list()
    for i in range(thread_num):
        t = LikeThread(icon_like_pos)
        t.setDaemon(True)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    pass
