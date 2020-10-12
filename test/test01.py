# -*- codeing = utf-8 -*-
# @Time :2020/7/23 12:57
# @Author:Eric
# @File : test01.py
# @Software: PyCharm
import random
import time
import os

# 打开一个文件
# lis_urls = []
# str1 = None
#
# with open('C:/Users/标注/Desktop/test/url.txt','r+') as fo:
#     lis_urls = fo.read().split(',')
# from untitled.tool.ftpUtil.getFtpUtil import FTP_OPS
# import os
# ftp = FTP_OPS()
# doc_urls = ftp.get_ftp_urls('/jma/hsd/202007/04')
# doc_urls
import re
from tool.ftpUtil.getFtpUtil import FTP_OPS

if __name__ == '__main__':
    ftp = FTP_OPS()
    url = '/jma/hsd/202007/07/'
    localpath = "C:/Users/标注/Desktop/test/07/"
    try:
        doc_urls = ftp.get_ftp_urls(url)
        print('\033[0;32;40m获取路径:' + url + ',下的列表,成功!\033[0m')
        doc_urls.sort()
    # str1 = '/jma/hsd/202007/06/00'
        for doc_url in doc_urls:
            print('\033[0;32;40m读取:' + doc_url + ',读取中。。。。。。\033[0m')
            lis_urls = None
            while lis_urls == None:
                print('\033[0;32;40m读取失败：:' + doc_url + ',重新读取。。。。。。\033[0m')
                lis_urls = ftp.get_ftp_urls(doc_url, 'FLDK')
                print(lis_urls)
            print('\033[0;32;40m读取:' + doc_url + '成功！开始写入。。。。。。\033[0m')
            for i in lis_urls:
                with open(localpath + doc_url.split('/')[-1] + ".txt", 'w') as fp:
                    fp.write(i + '\n')
                    fp.flush()
            print('\033[0;32;40m执行写入成功！文件名字为:' + doc_url.split('/')[-1] + '\033[0m')
    except Exception:
        if lis_urls == 1 or doc_urls == 1:
            print('错误')
