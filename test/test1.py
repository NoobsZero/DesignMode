# -*- codeing = utf-8 -*-
# @Time :2020/8/7 17:57
# @Author:Eric
# @File : test1.py
# @Software: PyCharm
import ssl
import time
from ftplib import FTP, FTP_TLS

from tool.base64Util.getBase64Util import get_decode_base64
from tool.ftpUtil.getFtpUtil import FTP_OPS
import os
import re

from ftplib import FTP

from tool.getConfigUtil import get_ftp_config


class MyFTP(FTP):
    encoding = "gbk"  # 默认编码

    def getSubdir(self, *args):
        '''拷贝了 nlst() 和 dir() 代码修改，返回详细信息而不打印'''
        cmd = 'LIST'
        func = None
        if args[-1:] and type(args[-1]) != type(''):
            args, func = args[:-1], args[-1]
        for arg in args:
            cmd = cmd + (' ' + arg)
        files = []
        self.retrlines(cmd, files.append)
        return files

    def getdirs(self, dirname=None):
        """返回目录列表，包括文件简要信息"""
        if dirname != None:
            self.cwd(dirname)
        files = self.getSubdir()

        # 处理返回结果，只需要目录名称
        r_files = [file.split(" ")[-1] for file in files]

        # 去除. ..
        return [file for file in r_files if file != "." and file != ".."]

    def getfiles(self, dirname=None):
        """返回文件列表，简要信息"""
        if dirname != None:
            self.cwd(dirname)  # 设置FTP当前操作的路径
        return self.nlst()  # 获取目录下的文件

    # 这个感觉有点乱，后面再说,
    # def getalldirs(self, dirname=None):
    #     """返回文件列表，获取整个ftp所有文件夹和文件名称简要信息"""
    #     if dirname != None:
    #         self.cwd(dirname)  # 设置FTP当前操作的路径
    #     files = []
    #     dirs = set(self.getdirs()) - set(self.getfiles())
    #     if dirs != {}:
    #         for name in dirs:
    #             self.cwd("..")  # 返回上级
    #             files += self.getalldirs(name)
    #     return files




if __name__ == '__main__':
    ftps = FTP_OPS()
    # 获取第一层目录下的文件
    ftp = ftps.ftp_connect()
    ftp.voidcmd('TYPE I')
    print(ftp.size('/jma/hsd/202007/27/00/HS_H08_20200727_0000_B04_FLDK_R10_S0710.DAT.bz2'))
    # ftps.download_file('/jma/hsd/202007/26/00/HS_H08_20200726_0000_B01_FLDK_R10_S0110.DAT.bz2', 'C:/Users/标注/Desktop/test/HS_H08_20200726_0000_B01_FLDK_R10_S0110.DAT.bz2')

