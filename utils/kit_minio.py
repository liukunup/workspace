#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-08-27 23:46:55

class MinIO(object):
    
    def __init__(self):
        pass
    
    def xxx(self):
        print("Hello")
        pass
    
    def yyy(self):
        self.xxx()
        pass

if __name__ == '__main__':
    inst = MinIO()
    inst.yyy()
    pass
