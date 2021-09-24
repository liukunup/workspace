#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 23:39:01

import re
import time
import requests

from bs4 import BeautifulSoup
from utils import kit_config, kit_mysql


def request_chapter_list(domain, book_id, url_builder):
    # 请求页面
    chapter_url = url_builder(domain, book_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url=chapter_url, headers=headers)
    # 使用BeautifulSoup加载页面
    soup = BeautifulSoup(response.content, features="lxml")
    # 按标签查找
    div_list = soup.find('div', id='list')
    a_list = div_list.find_all("a")
    chapter_list = list()
    for a in a_list:
        href = a["href"]
        if not str(href).startswith('http'):
            href = chapter_url + href
        text = a.text.strip().replace("\n", "").replace("\r", "")
        chapter_list.append({'text': text, 'href': href, })
    return chapter_list


def url_builder_base(domain, book_id):
    """
    通用的链接拼装方法实现
    :param domain:  域名
    :param book_id: 小说ID
    :return: 小说章节列表链接
    """
    return f'http://www.{domain}/{book_id}/'


def parse_chapter_name(name):
    """
    解析章节名字符串
    :param name: 章节名字符串
    :return: 章节编号, 章节名
    """
    pattern = r'^(\u7b2c[\u4e00-\u9fa50-9]+\u7ae0)\s?([\u4e00-\u9fa5]+)\s?'
    result = re.findall(pattern, name)
    if result is not None and len(result) == 1:
        chapter_num = result[0][0]
        chapter_title = result[0][1]
        return chapter_num, chapter_title
    return None, None


def parse_chapter_content(url, retry=0):
    # 请求页面
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    # 使用BeautifulSoup加载页面
    soup = BeautifulSoup(response.content, features="lxml")
    # 按标签查找
    div_content = soup.find('div', id='content')
    if div_content is None and retry < 3:
        time.sleep(3)
        print(f'[{retry}]retry {url}')
        return parse_chapter_content(url, retry=retry+1)
    return None if div_content is None else div_content.text.strip()


def do_crawler(domain, book_id):
    """
    执行爬取任务
    :param domain:
    :param book_id:
    :return:
    """
    inst = kit_config.Config(filename='../../resources/config.yaml')
    params = inst.get_database('ds218-plus-test')
    params.update({'database': 'db_biquge'})
    is_skip = True
    latest_chapter_num = kit_mysql.std_sql_exec(None, latest_chapter, params)
    chapter_list = request_chapter_list(domain, book_id, url_builder_base)
    for chapter in chapter_list:
        chapter_num, chapter_title = parse_chapter_name(chapter['text'])
        if latest_chapter_num is None or chapter_num == latest_chapter_num:
            is_skip = False
        if is_skip:
            continue
        print(chapter['text'], chapter['href'])
        chapter_content = parse_chapter_content(chapter['href'])
        args = [chapter_num, chapter_title, chapter_content]
        kit_mysql.std_sql_exec(args, persistence_chapter, params)
    pass


def persistence_chapter(args, database, cursor):
    """
    持久化章节信息
    :param args:     SQL预处理参数
    :param database: 数据库链接
    :param cursor:   数据库游标
    :return: 查询结果
    """
    sql = """
    INSERT INTO `t_wangushendi`(
        `id`,
        `chapter`,
        `title`,
        `content`,
        `create_time`,
        `update_time`
    )
    VALUES(
        NULL, %s, %s, %s,
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    )
    """
    cursor.execute(sql, args)
    database.commit()
    return True


def latest_chapter(args, database, cursor):
    """
    获取最新章节
    :param args:     SQL预处理参数
    :param database: 数据库链接
    :param cursor:   数据库游标
    :return: 查询结果
    """
    sql = """
    SELECT
        `chapter`
    FROM
        `t_wangushendi`
    WHERE
        1 = 1
    ORDER BY `id` DESC
    LIMIT 1
    """
    cursor.execute(sql)
    result = cursor.fetchone()
    return None if result is None else result[0]


if __name__ == '__main__':
    do_crawler('biquwx.la', '49_49066')
    pass
