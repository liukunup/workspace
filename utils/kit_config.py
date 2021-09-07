#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-08-27 23:46:55

import os
import yaml
import pymysql


class Config(object):

    __debug = False
    __mode = None
    __filename = None
    __yaml = None
    __host = "127.0.0.1"
    __port = 3306
    __username = "root"
    __password = "123456"
    __database = "secret"
    __table = "config"

    def __init__(self, filename=None, host=None, port=None, username=None, password=None, debug=False):
        if filename is None:
            self.__construct_database(host, port, username, password, debug)
        elif None in [host, port, username, password]:
            self.__construct_yaml(filename, debug)
        else:
            pass
        pass

    def __construct_database(self, host, port, username, password, debug=True):
        self.__mode = "database"
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__debug = debug
        pass

    def __construct_yaml(self, filename, debug=True):
        self.__mode = "yaml"
        self.__filename = filename
        self.__debug = debug
        self.__load()
        pass

    def __load(self):
        if not os.access(self.__filename, os.F_OK):
            print(f'The config file {self.__filename} not exist!!!')
            return None
        with open(self.__filename, 'r') as f:
            self.__yaml = yaml.load(f, Loader=yaml.FullLoader)
            if self.__debug:
                print(self.__yaml)
        pass

    def get_database(self, tag):
        if self.__mode == "yaml":
            return self.__get_conf_from_yaml('database', tag)
        elif self.__mode == "database":
            return self.__get_conf_from_database('database', tag)
        else:
            return None

    def get_object_storage(self, tag):
        if self.__mode == "yaml":
            return self.__get_conf_from_yaml('object-storage', tag)
        elif self.__mode == "database":
            return self.__get_conf_from_database('object-storage', tag)
        else:
            return None

    def __get_conf_from_database(self, node, tag):
        db = pymysql.connect(host=self.__host, port=self.__port, user=self.__username, password=self.__password, database=self.__database)
        cursor = db.cursor()
        params = None
        try:
            sql = f"SELECT params FROM `{self.__table}` WHERE `node` = '{node}' AND `tag` = '{tag}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is not None and len(result) == 1:
                params = result[0]
        except Exception:
            print("ERROR: ", sql)
        db.close()
        return params

    def __get_conf_from_yaml(self, node, tag):
        if node not in self.__yaml:
            print(f'Can not find {node} in yaml!!!')
            return None
        for e in self.__yaml[node]:
            if tag not in e.keys():
                continue
            return e[tag]
        print(f'Can not find {node} tag={tag} in yaml!!!')
        return None


if __name__ == '__main__':
    inst = Config(filename='../resources/config.yaml')
    # inst = Config(host='127.0.0.1', port=3306, username='root', password='123456')
    print('-' * 100)
    print(inst.get_database('ds218-plus-test'))
    print(inst.get_object_storage('ds218-plus-test'))
    pass
