#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-08-27 23:46:55

import os
import yaml


class Config(object):
    
    __debug = False
    __filename = None
    __yaml = None
    
    def __init__(self, filename, debug=False):
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
        return self.__get_conf('database', tag)
    
    def get_object_storage(self, tag):
        return self.__get_conf('object-storage', tag)
    
    def __get_conf(self, node, tag):
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
    inst = Config('../resources/config.yaml')
    print('-' * 100)
    print(inst.get_database('ds218-plus-test'))
    print(inst.get_object_storage('ds218-plus-test'))
    pass
