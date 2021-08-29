#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : Liu Kun
# date   : 2021-08-29 23:31:55

import os
from minio import Minio


class MinIO(object):
    
    __client = None
    
    def __init__(self, host, port, access_key, secret_key):
        self.__client = Minio(f"{host}:{port}", access_key=access_key, secret_key=secret_key, secure=False)
        pass
    
    def upload(self, fr, to, bucket):
        if not os.access(fr, os.F_OK):
            return None
        if not self.__client.bucket_exists(bucket):
            self.__client.make_bucket(bucket)
        result = self.__client.fput_object(bucket, to, fr)
        print("created {0} object; etag: {1}, version-id: {2}".format(
            result.object_name, result.etag, result.version_id,),)
        pass
    
    def download(self, fr, to, bucket):
        if os.access(to, os.F_OK):
            os.remove(to)
        self.__client.fget_object(bucket, fr, to)
        pass
    
    def remove(self, target, bucket):
        self.__client.remove_object(bucket, target)
        pass
