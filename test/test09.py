# -*- encoding:utf-8 -*-
"""
@File   :test09.py
@Time   :2020/8/28 8:16
@Author :Chen
@Software:PyCharm
"""
import ftplib
import json
import socket
import time
from _ssl import _SSLSocket
from importlib import import_module
import os

from pyquery.pyquery import callback

from tool.ftpUtil.getFtpUtil import FTP_OPS, FTP_REQUESTS, get_timeToUrl, FTPFileApi, dict2obj

if __name__ == '__main__':
    # lis1 = FTP_REQUESTS().get_ftp_urls('ftp://ftp.ptree.jaxa.jp/jma/hsd/202008/31/00/', 'FLDK')
    ftp = FTP_OPS()
    # ftps = ftp.ftp_connect()
    # url = '202009'
    storagePath = 'C:/Users/标注/Desktop/test/06/'
    ftp_head = "jma/hsd/"
    # url = '202009'
    url = 20191110
    fileConditions = '06001'
    ftpHead_netcdf = '/jma/netcdf/'
    remotePath = get_timeToUrl(ftp_url=url, dirOrFile='dir', ftp_head=ftpHead_netcdf)
    remotepath = get_timeToUrl(remotePath)
    localpath = get_timeToUrl(storagePath)
    for i in range(20):
        url = url + 1
    # try:
    # ftp.ftp_FileAPI_RecursionDownload(remotepath=remotePath, localpath=storagePath, fileConditions=fileConditions,
    #                                       ftp=ftps)
    # except Exception as e:
    #     ftp.ftp_FileAPI_RecursionDownload(remotepath=remotePath, localpath=storagePath, fileConditions=fileConditions,
    #                                       ftp=ftps)

    # 1、通过os.walk方法遍历读取目录或文件，返回字典类型{dir:dirname},{file:filename}
    # 2、字典
    # for root, dirs, files in os.walk(storagePath, topdown=False):
    #     for name in files:
    #         filePath = os.path.join(get_timeToUrl(root), name)
    #         print(filePath)
    #     for name in dirs:
    #         filePath = os.path.join(get_timeToUrl(root), name)
    #         print(filePath)

    # remotePath = get_timeToUrl(ftp_url=url, dirOrFile='dir', ftp_head=ftp_head)
    # ftp.ftp_FileAPI_RecursionDownload(remotepath=remotePath, localpath=storagePath, fileConditions='FLDK', ftp=ftps)
    # ftp.ftp_connect()
    # int(time.strftime('%Y%m%d', time.localtime())) - 1
    # def test(url='C:/Users/标注/Desktop/test/06/jma/hsd/202008/31/00/'):
    #     if os.path.exists(url):
    #         for i in os.listdir(url):
    #             if os.path.exists(url + i + '/'):
    #                 test(url + i + '/')
    #             else:
    #                 bufsize = 1024 * 1024
    #                 print("***************开始下载***************")
    #                 with open(url + i, 'r', encoding='utf-8') as load_f:
    #                     lines = load_f.readlines()  # 读取全部内容 ，并以列表方式返回
    #                     for i in lines:
    #                         f = json.loads(i)
    #                         ftpFile: FTPFileApi = dict2obj(f)
    #                         # ftp.download_file(ftp=ftps, ftp_file_path=ftpFile.remotepath, dst_file_path=ftpFile.localpath)
    #                         ftp.download_file(ftp=ftps, ftpFile=ftpFile)
    # ftps.close()

# f = json.loads('{"__class__": "FTPFileApi", "__module__": "tool.ftpUtil.getFtpUtil", "name": "HS_H08_20200831_0030_B12_FLDK_R20_S0810.DAT.bz2", "remotepath": "jma/hsd/202008/31/00/HS_H08_20200831_0030_B12_FLDK_R20_S0810.DAT.bz2", "localpath": "C:/Users/标注/Desktop/test/06/jma/hsd/202008/31/00/HS_H08_20200831_0030_B12_FLDK_R20_S0810.DAT.bz2", "size": 2084495, "datatype": "file", "state": 0, "modify": 20200831004356, "adfr": "adfr(0644)", "ownername": "15174506817_163.com nrt_ptree"}')
# ftpfile = dict2obj(f)
# ftp.download_file(ftp=ftps, ftpFile=ftpfile)
# print(os.stat('C:/Users/标注/Desktop/test/06/jma/hsd/202008/31/00/HS_H08_20200831_0030_B12_FLDK_R20_S0510.DAT.bz2').st_size)
# lis1 = FTP_OPS().get_ftp_urls(url)
# for i in lis1:
#     print(i)

# facts = ['modify', 'perm', 'size', 'type', 'unix.groupname', 'unix.mode', 'unix.ownername']
# gen = ftp.ftp_connect().mlsd('jma/hsd/202008/31/', facts)
# gen = ftp.ftp_urlsToFileAPI(url='jma/hsd/202008/31/00/HS_H08_20200831_0050_B16_FLDK_R20_S0710.DAT.bz2')
# print(gen)
# ftp.ftp_FileAPI_Download('jma/hsd/202008/31/', 'C:/Users/标注/Desktop/test/06/text.json')
# ftp.test(ftp.ftp_connect(), 'C:/Users/标注/Desktop/test/06/jma/hsd/202008/31/00/')
# name = i[0], modify = int(i[1].get('modify')), remotepath = url + i[0],
#                        size=int(i[1].get('size')),
#                        adfr=i[1].get('perm') + "(" + i[1].get('unix.mode') + ")",
#                        ownername=i[1].get('unix.ownername') + " " + i[1].get('unix.groupname'),
#                        datatype=i[1].get('type')
# ftp.ftp_FileAPI_RecursionDownload(remotepath='/jma/hsd/202009/01/', localpath='C:/Users/标注/Desktop/test/06', fileConditions='FLDK', ftp=ftps)

# str1 = 'C:/Users/标注/Desktop/test/06//jma/hsd/202008/31/00/'
# print(get_timeToUrl(str1, dirOrFile='dir'))
# for i in range(len(str2)):
#     if str2[i].strip() != '' and i != len(str2)-1:
#         print(str2[i])

# if str1.split('/')
# lis1 = [('HS_H08_20200831_0050_B16_FLDK_R20_S0710.DAT.bz2', {'modify': '20200831010427', 'perm': 'adfr', 'size': '2054263', 'type': 'file', 'unix.groupname': 'nrt_ptree', 'unix.mode': '0644', 'unix.ownername': '15174506817_163.com'})]
# for i in lis1:
#     print(i[1].get('type'))
# gens = json.dumps(gen, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# gen = ftp.ftp_urlsToList(url='jma/hsd/202008/31/00/')
# print(len(gen))
# try:
#     ftp.ftp_connect().cwd('jma/hsd/202008/31/00/HS_H08_20200831_0050_B16_FLDK_R20_S0710.DAT.bz2')
# except Exception as e:
#     if "Not a directory" in str(e):
#         print("do something with {}".format(e))
# jso = json.dumps(gen, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# with open('C:/Users/标注/Desktop/test/06/text.json', 'a+') as fp:
#     fp.write(jso)
#     fp.flush()
# i.show()

# st = [i for i in lis1 if i[0].find('FLDK') != -1]
# for i in st:
#     print(i)
