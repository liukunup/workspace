#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 12:38:34

import os


def ls(path, type_list=None, suffix_list=None, is_recursive=True, level=1, debug=False):
    """
    列举文件夹下的文件或子文件夹
    实现类似os.walk()功能
    :param path: 目标根路径
    :param type_list: 文件(file)或子文件夹(dir)类型过滤
    :param suffix_list: 文件后缀名过滤
    :param is_recursive: 是否遍历子文件夹
    :param level: 层级信息
    :param debug: 调试开关
    :return: 文件或子文件夹列表
    """
    # 输出列表
    files = list()
    # 路径不可访问时直接返回
    if not os.access(path, os.F_OK):
        return files
    # 默认类型过滤
    if type_list is None:
        type_list = ['file', 'dir']
    # 遍历文件或文件夹
    file_list = os.listdir(path)
    for file in file_list:
        # 跳过
        if file == '.DS_Store':
            continue
        # 文件全路径
        file_path = os.path.join(path, file)
        # 如果是路径, 则递归操作
        if os.path.isdir(file_path):
            print('*' * 100)
            if debug:
                print('+' * level * 3, file_path)
            # 如果需要文件夹
            if 'dir' in type_list:
                files.append(file_path)
            # 判断是否需要递归操作
            if is_recursive:
                ret = ls(file_path, type_list=type_list, suffix_list=suffix_list, is_recursive=is_recursive,
                         level=level+1, debug=debug)
                if ret is not None and len(ret) > 0:
                    files.extend(ret)
        # 如果是文件, 直接过滤添加
        if os.path.isfile(file_path):
            if debug:
                print('-' * level * 3, file_path)
            # 如果需要文件
            if 'file' in type_list:
                # 如果需要过滤后缀名
                if suffix_list is not None:
                    suffix_splits = file.split('.')
                    if len(suffix_splits) == 2 and suffix_splits[1] in suffix_list:
                        files.append(file_path)
                else:
                    files.append(file_path)
    return files
