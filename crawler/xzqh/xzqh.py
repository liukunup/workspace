#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 23:39:01

import re
import requests

from utils import kit_config, kit_mysql
from bs4 import BeautifulSoup


def get_xzqh(page_url):
    """
    获取行政区划信息
    :param page_url: 网页链接地址
    :return: 行政区划信息[[行政区划代码, 单位名称]]
    """
    # 行政区划
    data_list = list()
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36'
    }
    # 执行HTTP请求
    response = requests.get(url=page_url, headers=headers)
    # 使用BeautifulSoup加载页面
    soup = BeautifulSoup(response.content, features="lxml")
    # 表格数据解析
    tr_list = soup.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        # 判断表格行数是否符合要求
        if len(td_list) < 2:
            print('表格行数太少跳过')
            continue
        # 去除HTML信息仅保留文本
        row_list = [td.text.strip() for td in td_list]
        # 检查文本是否为行政区划代码
        if re.search(r'^(\d{6})$', row_list[1]) is None:
            print('跳过非行政区划代码')
            continue
        # 只有符合条件的数据才能被收集
        data_list.append(row_list[1:3])
    return data_list


def inf_insert_xzqh(args, database, cursor):
    """
    持久化行政区划信息
    [行政区划代码, 单位名称, 年份版本]
    :param args:     SQL预处理参数
    :param database: 数据库链接
    :param cursor:   数据库游标
    :return: 不涉及
    """
    sql = """
    INSERT INTO `t_xzqh` (
        `id`,
        `code`,
        `name`,
        `version`,
        `create_time`,
        `update_time`
    ) VALUES (
        NULL, %s, %s, %s,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    )
    """
    cursor.execute(sql, args)
    database.commit()
    return None


if __name__ == '__main__':
    # 默认数据库配置
    inst = kit_config.Config(filename='../../resources/config.yaml')
    params = inst.get_database('ds218-plus-test')
    params.update({'database': 'db_open_information'})
    # 年份版本
    version = 2020
    # 获取行政区划信息
    data = get_xzqh('http://www.mca.gov.cn/article/sj/xzqh/2020/20201201.html')
    for dat in data:
        print(dat)
        # 持久化行政区划信息
        args = [dat[0], dat[1], version]
        kit_mysql.std_sql_exec(args, inf_insert_xzqh, params)
    pass
