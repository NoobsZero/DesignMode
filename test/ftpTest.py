# -*- encoding:utf-8 -*-
"""
@File   :ftpTest.py
@Time   :2020/8/26 13:01
@Author :Chen
@Software:PyCharm
"""
import os
import re
import socket
import time
import requests
import requests_ftp


class FTPFileApi(object):
    """
        #FTP传输文件操作
        :param name: 传输文件名字
        :param remotepath: ftp远程路径
        :param localpath: 本地
        :param size: 文件大小
        :param size: 状态
    """

    # 初始化
    def __init__(self, name: str, remotepath: str, localpath: str = None, size: int = 0, state: int = 0):
        '''
        :param name:                文件名
        :param remotepath:          FTP文件路径
        :param localpath:           本地路径
        :param size:                文件大小
        :param state:               状态码：0:失败    1：成功    2:未完成   3:不存在
        '''
        self.name = name
        self.remotepath = remotepath
        self.localpath = localpath
        self.size = size
        self.state = state


class FTP_REQUESTS(object):
    '''
        通过requests操作FTP文件
    '''
    requests_ftp.monkeypatch_session()
    s = requests.Session()

    def __init__(self, ftp_url: str = 'ftp://ftp.ptree.jaxa.jp', username: str = '15174506817_163.com',
                 password: str = 'SP+wari8', s: requests_ftp.ftp.FTPSession = s):
        self.s = s
        self.ftp_url = ftp_url
        self.username = username
        self.password = password

    # 时间转换url
    def get_timeToUrl(self, ftp_url: str = None, tim=None):
        '''
        :param ftp_url: FTP 远程路径
        :param tim: 时间
        :return: url
        默认返回路径：ftp://ftp.ptree.jaxa.jp/jma/hsd/
        '''
        strp = ''
        strf = ''
        if ftp_url == None:
            ftp_url = self.ftp_url + '/jma/hsd/'
        if tim == None:
            if bool(re.search(r'^[\d]{9,10}$', str(tim))):
                strp = "%Y%m%d%H"
                strf = '%Y%m/%d/%H/'
            elif bool(re.search(r'^[\d]{7,8}$', str(tim))):
                strp = "%Y%m%d"
                strf = '%Y%m/%d/'
            elif bool(re.search(r'\d{6}', str(tim))):
                strp = "%Y%m"
                strf = '%Y%m/'
            if strp != '' and strf != '':
                ftp_url = time.strftime(ftp_url + strf, time.strptime(str(tim), strp))
        return ftp_url

    # FTP根据url和过滤条件，返回一个list
    def get_ftp_urls(self, remotepath, conditions=None):
        '''
        :param remotepath: ftp远程路径
        :param conditions: 过滤条件
        :return: list result
        '''
        socket.setdefaulttimeout(6)
        try:
            if remotepath == None:
                remotepath = self.ftp_url
            resp = self.s.list(remotepath, auth=(self.username, self.password))
            datas_urls = []
            if resp.status_code == 226:
                print('226  Transfer complete')
                if conditions != None:
                    fliter_name = '.*' + conditions + '.*'
                    for i in resp.text.split('\n'):
                        s = re.finditer(fliter_name, i)
                        for i in s:
                            datas_urls.append(i.group())
                else:
                    for i in resp.text.split('\n'):
                        datas_urls.append(i)
            elif 400 <= resp.status_code < 500:
                if resp.status_code == 404:
                    print("目录或文件不存在！")
                raise u'%s Client Error: %s for url: %s' % (resp.status_code, remotepath)
            return datas_urls
        except(socket.error, socket.gaierror):
            print("\033[0;32;40mERROR: 链接超时: [{}:{}]\033[0m".format('get_ftp_urls', remotepath))
        return None

    def download_file(self, ftp_file_path: str or FTPFileApi, dst_file_path):
        """
        从ftp下载文件到本地
        :param ftp_file_path: ftp下载文件
        :param dst_file_path: 本地存放
        :return:
        """
        if isinstance(ftp_file_path, FTPFileApi):
            remote_file = ftp_file_path.remotepath
            # 文件总大小
            remote_file_size = ftp_file_path.size
        else:
            remote_file = ftp_file_path
            # 文件总大小
            remote_file_size = self.s.size(remote_file,
                                           auth=(self.username, self.password))
        if 400 <= remote_file_size.status_code < 500:
            if remote_file_size.status_code == 404:
                print("目录或文件不存在！")
                # raise (u'%s Client Error: %s for url: %s' % (remote_file_size.status_code, remote_file))
            return 0
        else:
            remote_file_size = int(remote_file_size.headers.get('Content-Length'))
            print('remote filesize [{}]'.format(remote_file_size))
        cmpsize = 0  # 下载文件初始大小
        lsize = 0
        # check local file isn't exists and get the local file size
        # 实现断点续传
        if os.path.exists(dst_file_path):
            lsize = os.stat(dst_file_path).st_size
            if lsize >= remote_file_size:
                print('local file({}b) is bigger or equal remote file({}b)'.format(lsize, remote_file_size))
                return 1
        start = time.time()

        headers = {'Range': 'bytes={}-'.format(lsize)}

        retrs = self.s.retr(remote_file,
                            auth=(self.username, self.password), headers=headers, stream=True)

        if 400 <= retrs.status_code < 500:
            if retrs.status_code == 404:
                print("目录或文件不存在！")
            raise u'%s Client Error: %s for url: %s' % (retrs.status_code, remote_file)
            return 0

        with open(dst_file_path, "ab") as data:
            data.write(retrs.content)
        end = time.time()
        print(remote_file + '完成！花费时间：', (end-start))


if __name__ == '__main__':
    str_urls = FTP_REQUESTS().download_file(
        'ftp://ftp.ptree.jaxa.jp/jma/hsd/202007/31/00/HS_H08_20200731_0000_B01_FLDK_R10_S0110.DAT.bz2',
        'C:/Users/标注/Desktop/test/HS_H08_20200731_0000_B01_FLDK_R10_S0110.DAT.bz2')
# str_urls = FTP_REQUESTS().get_ftp_urls(remotepath=ftp_url)
#     str_urls = FTP_REQUESTS().get_timeToUrl()
#     print(str_urls)
# str_url = []
# [str_url for element in str_urls if
#     bool(re.compile(u'[a-zA-Z]').search(element)) or bool(re.search(r'\d', element))]
#
# print(len(str_url))
# print(str_url)
# for i in str_urls:
#     print(i)
#     print(i.split(' ')[0][0])
# if i.split(' ')[0][0] == 'd':
#     print('是目录：' + i)

# str_lis = str_urls.split('\n')
# for i in str_urls:
#     print(i)
# print(type(str_urls))
# str2 = '-rw-r--r--   1 2101     210       4157998 Jul 27 00:09 HS_H08_20200727_0000_B01_FLDK_R10_S0110.DAT.bz2'
# str1 = str2.split(' ')
# print(str1[0],str1[-1],str1[-5])
# get_ftp_urls('ftp://ftp.ptree.jaxa.jp/jma/hsd/202007/27/00/')
#     requests_ftp.monkeypatch_session()
#     s = requests.Session()
# resp = s.list('ftp://ftp.ptree.jaxa.jp/jma/hsd/202007/27/00/', auth=('15174506817_163.com', 'SP+wari8'))
# resp.status_code
# print(resp.text)

# data_size = s.size('ftp://ftp.ptree.jaxa.jp/jma/hsd/202007/27/00/HS_H08_20200727_0000_B01_FLDK_R10_S0110.DAT.bz2',
#                    auth=('15174506817_163.com', 'SP+wari8'))

# def size_format(b):
#     if b < 1000:
#         return '%i' % b + 'B'
#     elif 1000 <= b < 1000000:
#         return '%.1f' % float(b / 1000) + 'KB'
#     elif 1000000 <= b < 1000000000:
#         return '%.1f' % float(b / 1000000) + 'MB'
#     elif 1000000000 <= b < 1000000000000:
#         return '%.1f' % float(b / 1000000000) + 'GB'
#     elif 1000000000000 <= b:
#         return '%.1f' % float(b / 1000000000000) + 'TB'
#
#
# lsize = os.stat(dst_file_path).st_size
# if lsize == len(data_size.content):
#     print('相等')
# print(size_format(lsize))
