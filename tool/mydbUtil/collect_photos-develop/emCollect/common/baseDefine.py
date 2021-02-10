# -*- coding: UTF-8 -*-

class TarContentError(Exception):
    def __init__(self,msg):
        self.message = msg
        pass
    def __str__(self):
        return "压缩包格式不符合要求:[{}]".format(self.message)

class SQLFilesError(Exception):
    def __init__(self,msg):
        self.message = msg
        pass
    def __str__(self):
        return "sql文件错误:[{}]".format(self.message)