#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-09-19 11:51:55

import pymysql


def std_sql_exec(args, callback, db_params):
    """
    SQL执行标准化接口
    :param args:      SQL预处理参数
    :param callback:  SQL回调执行函数
    :param db_params: 数据库连接信息
    :return: 执行/查询结果
    """
    # 建立数据库链接
    db_connection = pymysql.connect(host=db_params['host'], port=db_params['port'],
                                    user=db_params['username'], password=db_params['password'],
                                    database=db_params['database'])
    # 创建游标
    db_cursor = db_connection.cursor()
    # 准备返回值
    ret = None
    try:
        # 执行SQL语句
        ret = callback(args, db_connection, db_cursor)
    except Exception as e:
        # 打印错误日志
        print('ERROR', e)
        # 发生错误时回滚
        db_connection.rollback()
    # 关闭数据库连接
    db_connection.close()
    # 返回SQL执行结果 有时候不需要返回
    return ret


def callback_demo(args, database, cursor):
    """
    回调演示函数
    :param args:     SQL预处理参数
    :param database: 数据库链接
    :param cursor:   数据库游标
    :return: 查询结果
    """
    # 使用 execute() 方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据
    data = cursor.fetchone()
    # 打印查询到的信息
    print("Database version : %s " % data)
    return data
