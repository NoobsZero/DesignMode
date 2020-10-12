# -*- codeing = utf-8 -*-
# @Time :2020/7/24 13:26
# @Author:Chen
# @File : getFtpUtil.py
# @Software: PyCharm
import ftplib
import json
import math
import operator
import os, sys, stat
import re
import socket
import time
from _ssl import _SSLSocket
from ftplib import FTP_TLS
from ftplib import error_perm, FTP
from importlib import import_module
from typing import Optional

from tool.base64Util.getBase64Util import get_decode_base64
from tool.getConfigUtil import get_ftp_config

"""An FTP_OPS client class and some helper functions.

Based on RFC 412: File Transfer Protocol (FTP_OPS), by Chen

Example:

>>> from tool.ftpUtil import FTP_OPS
>>> ftp = FTP_OPS.ftp_connect # config.ini:connect to host,username,password,port
'230 Guest login ok, access restrictions apply.'
>>> ftp.download_file(ftp_file_path, dst_file_path)
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 Type set to I\n'
*resp* '200 Type set to I'
*cmd* 'SIZE fileName'
*put* 'SIZE fileNane\r\n'
*get* '213 fileSize\n'
*resp* '213 fileSize'
remote filesize [0]
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 Type set to I\n'
*resp* '200 Type set to I'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (xxx,xx,xx,xxx,xxx,xxx).\n'
*resp* '227 Entering Passive Mode (xxx,xx,xx,xxx,xxx,xxx).'
*cmd* 'REST 0'
*put* 'REST 0\r\n'
*get* '350 Restarting at 0. Send STORE or RETRIEVE to initiate transfer\n'
*resp* '350 Restarting at 0. Send STORE or RETRIEVE to initiate transfer'
*cmd* 'RETR ftp_file_path'
*put* 'RETR ftp_file_path\r\n'
*get* '150 Opening BINARY mode data connection for ftp_file_path (0 bytes)\n'
*resp* '150 Opening BINARY mode data connection for ftp_file_path (0 bytes)'
[==================================================] 100.00%
consume time [19.157651901245117]
local filesize [0] filepath:[dst_file_path]
>>> ftp.quit()
'221 Goodbye.'
"""


def run_time(func):
    def call_func(*args, **kwargs):
        begin_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        Run_time = end_time - begin_time
        print(str(func.__name__) + "Function Run time is:" + str(Run_time))
        return ret

    return call_func


'''序列化和反序列化'''


def obj2dict(obj):
    d = {'__class__': obj.__class__.__name__, '__module__': obj.__module__}
    d.update(obj.__dict__)
    return d


def dict2obj(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = import_module(module_name)
        class_ = getattr(module, class_name)
        args = dict((key, value) for key, value in d.items())
        instance = class_(**args)
    else:
        instance = d
    return instance


'''未完成'''


class tyFTP(FTP_TLS):
    def connect_user(self, host='', port=990, timeout=-999, source_address=None):
        """Connect to host.  Arguments are:
         - host: hostname to connect to (string, default previous host)
         - port: port to connect to (integer, default previous port)
         - timeout: the timeout to set against the ftp socket(s)
         - source_address: a 2-tuple (host, port) for the socket to bind
           to as its source address before connecting.
        """
        if host != '':
            self.host = host
        if port > 0:
            self.port = port
        if timeout != -999:
            self.timeout = timeout
        if source_address is not None:
            self.source_address = source_address
        self.sock = socket.create_connection((self.host, self.port), self.timeout,
                                             source_address=self.source_address)
        self.af = self.sock.family
        self.file = self.sock.makefile('r', encoding=self.encoding)
        self.welcome = self.getresp()
        return self.welcome


class FTPFileApi:
    '''
    FTP传输文件操作
    name: 传输文件名字
	remotepath: ftp远程路径
	localpath: 本地
	size: 文件大小
	datatype: 类型（文件或目录）
	state: 状态 （0:未完成    1：成功    2:失败   3:不存在）
	modify: 最后修改时间
	adfr: 文件权限
	ownername: 所属组
	("name": "PI_H08_20200831_0050_TRC_FLDK_R10_PGPFD.png",
	"remotepath": "jma/hsd/202008/31/00/PI_H08_20200831_0050_TRC_FLDK_R10_PGPFD.png",
	"localpath": "C:/Users/标注/Desktop/test/06/jma/hsd/202008/31/00/PI_H08_20200831_0050_TRC_FLDK_R10_PGPFD.png",
	"size": 124495637, "datatype": "file", "state": 0, "modify": 20200831010549, "adfr": "adfr(0644)",
	"ownername": "15174506817_163.com nrt_ptree")
    '''

    # 初始化
    def __init__(self, name: str, modify: int, datatype: str, remotepath: str, localpath: str = None, size: int = 0,
                 state: int = 0,
                 adfr: str = None, ownername: str = None):
        self.name = name
        self.remotepath = remotepath
        self.localpath = localpath
        self.size = size
        self.datatype = datatype
        self.state = state
        self.modify = modify
        self.adfr = adfr
        self.ownername = ownername

    def __repr__(self):
        return "FTPFileApi[fileName={0}, size={1}, remotepath={2}, localpath={3}, state={4}, modify={5}, adfr={6}, " \
               "ownername={7}, datatype={8}]".format(
            self.name, self.size, self.remotepath, self.localpath, self.state, self.modify, self.adfr,
            self.ownername, self.datatype)

    def __str__(self):
        return "fileName={0}, size={1}, remotepath={2}, localpath={3}, state={4}, modify={5}, adfr={6}, ownername={" \
               "7}, datatype={8}".format(
            self.name, self.size, self.remotepath, self.localpath, self.state, self.modify, self.adfr,
            self.ownername, self.datatype)


def get_timeToUrl(ftp_url: int or str, dirOrFile: str = None, ftp_head: str = None):
    """
        时间转换url
    :param dirOrFile: 指定URL是文件或者目录（'file' Or 'dir'）
    :param ftp_url: URL
    :param ftp_head: 用于传入time类型转换后拼接的头信息，默认返回路径：'/jma/hsd/' + ftp_url(int)
    :return: url
    """
    strp = ''
    strf = ''
    if str(ftp_url).isdigit():
        if bool(re.search(r'^[\d]{9,10}$', str(ftp_url))):
            strp = "%Y%m%d%H"
            strf = '%Y%m/%d/%H/'
        elif bool(re.search(r'^[\d]{7,8}$', str(ftp_url))):
            strp = "%Y%m%d"
            strf = '%Y%m/%d/'
        elif bool(re.search(r'\d{6}', str(ftp_url))):
            strp = "%Y%m"
            strf = '%Y%m/'
        if strp != '' and strf != '':
            try:
                ftp_url = time.strftime(strf, time.strptime(str(ftp_url), strp))
            except ValueError as e:
                print('\033[1;31;47m%s\033[1;31;47m' % 'get_timeToUrl:param ftp_url')
                print('\"' + ftp_url + '\"日期输入错误!')
                e.with_traceback()
    if ftp_head is not None:
        ftp_url = get_timeToUrl(ftp_url=ftp_head, dirOrFile='dir', ftp_head=None) + ftp_url
    url_lis = ftp_url.replace('\\', '/').split('/')
    ftp_url = '/'.join([url_lis[i] for i in range(len(url_lis)) if url_lis[i].strip() != '']) + '/'
    if dirOrFile == 'dir' and ftp_url.split('/')[-1] != '':
        ftp_url = ftp_url + '/'
    elif dirOrFile == 'file' and ftp_url.split('/')[-1] == '':
        ftp_url = ftp_url[:-1]
    return ftp_url


# 进度条
def processBar(cur, total):
    """
    进度条显示
    cur表示当前的数值，total表示总的数值。
    :param cur:
    :param total:
    :return:
    """
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' %
                     ('\033[0;32;40m=\033[0m' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')


def ftp_LocalQueries(url, dirOrFile='dir', storagePath=None, fileConditions=None):
    """
    根据url查询本地
    :param fileConditions: 文件过滤条件
    :param url: ftp目录或文件
    :param dirOrFile: 目录或文件
    :param storagePath:
    :return:
    """
    localQuerise: [FTPFileApi] = []
    fileSuffix = '.json'

    def LocalQueries(urlPath=url, urlType=dirOrFile, storageHead=storagePath, fileCondition=fileConditions,
                     suffix=fileSuffix):
        localUrl = get_timeToUrl(urlPath, dirOrFile=urlType, ftp_head=storageHead)
        if dirOrFile is 'dir' and os.path.isdir(localUrl):
            for i in os.listdir(localUrl):
                if os.path.isdir(localUrl + i):
                    LocalQueries(urlPath=localUrl + i, urlType='dir', storageHead='', fileCondition=fileCondition)
                elif suffix in i and os.path.isfile(get_timeToUrl(i, 'file', ftp_head=localUrl)):
                    with open(get_timeToUrl(i, 'file', ftp_head=localUrl), 'r', encoding='utf-8') as load_f:
                        lines = load_f.readlines()
                        for line in lines:
                            ftpFile: FTPFileApi = dict2obj(json.loads(line))
                            if (fileCondition is not None) and (fileCondition in ftpFile.name):
                                localQuerise.append(ftpFile)
                            elif fileCondition is None:
                                localQuerise.append(ftpFile)
        elif dirOrFile is 'file':
            url_lis = url.split('/')
            file_name = url_lis[-1]
            LocalQueries(urlPath='/'.join(url_lis[:-1]), urlType='dir', storageHead='', fileCondition=file_name)
    LocalQueries()
    return localQuerise


class FTP_OPS(FTP):
    """
    ftp文件操作
    """
    # 获取ftp配置信息，并指定‘email’section
    ftp_config = get_ftp_config('email')
    host = ftp_config.get('host')
    username = ftp_config.get('username')
    password = get_decode_base64(ftp_config.get('password'))
    port = int(ftp_config.get('port'))

    # 初始化
    def __init__(self, ftp_ip=host, ftp_port=port, ftp_user=username, ftp_pwd=password):
        super().__init__()
        self.ftp_ip = ftp_ip
        self.ftp_port = ftp_port
        self.ftp_user = ftp_user
        self.ftp_pwd = ftp_pwd

    # 获取链接
    def ftp_connect(self):
        """
        连接ftp
        :return:
        """
        socket.setdefaulttimeout(30)  # 超时FTP时间设置为60秒
        ftp = FTP()
        ftp.connect(self.ftp_ip, self.port)
        # 测试时，调试模式可以设置为0不显示，默认为0
        ftp.set_debuglevel(2)  # 开启调试模式:2显示详细信息
        ftp.encoding = 'utf-8'
        try:
            ftp.login(self.ftp_user, self.ftp_pwd)
            # print(
            #     '[{}]login ftp {}'.format(
            #         self.ftp_user,
            #         ftp.getwelcome()))  # 打印欢迎信息

        except(socket.error, socket.gaierror):  # ftp 连接错误
            print(
                "ERROR: cannot connect [{}:{}]".format(
                    self.ftp_ip, self.ftp_port))
            return None
        except error_perm:  # 用户登录认证错误
            print("ERROR: user Authentication failed ")
            return None
        except Exception as e:
            print(e)
            return None
        return ftp

    # 根据目录下载文件地址（可以改进成递归创建目录下载文件地址到指定目录）
    def ftp_FileAPI_RecursionDownload(self, remotepath: str, localpath: str, fileConditions=None, dirConditions=None,
                                      ftp: ftplib.FTP = None):
        postfix = '.json'
        ftpSir = ''
        remotepath = get_timeToUrl(remotepath)
        localpath = get_timeToUrl(localpath)
        # ftpapi_datas:返回目录或文件列表,如果不存在则返回None
        ftpapi_datas = self.ftp_urlsToFileAPI(url=remotepath, fileConditions=fileConditions,
                                              dirConditions=dirConditions, connect=ftp)
        # 返回None的三种情况：1、remotepath目录或文件不存在 2、remotepath目录是个空目录 3、出现异常
        if ftpapi_datas is not None:
            for i in ftpapi_datas:
                localpath_dirOrFile = get_timeToUrl(ftp_url=localpath + i.remotepath, dirOrFile=i.datatype)
                if i.datatype == 'dir':
                    if not os.path.exists(localpath_dirOrFile):
                        os.makedirs(localpath_dirOrFile)
                    self.ftp_FileAPI_RecursionDownload(remotepath=i.remotepath, localpath=localpath,
                                                        fileConditions=fileConditions)
                elif i.datatype == 'file':
                    filePaths = localpath_dirOrFile.split('/')
                    if not os.path.exists('/'.join(filePaths[:-1])):
                        os.makedirs('/'.join(filePaths[:-1]))
                    filePaths[-1] = filePaths[-2] + postfix
                    filePath = '/'.join(filePaths)
                    try:
                        if os.path.isfile(filePath) and ftpSir is '':
                            with open(filePath, 'r', encoding='utf8') as rd:
                                ftpSir = ','.join(rd.readlines())
                                rd.flush()
                            rd.close()
                        if (ftpSir is '') or (i.name not in ftpSir):
                            i.localpath = localpath_dirOrFile
                            ftpapi_json = json.dumps(obj2dict(i), ensure_ascii=False)
                            with open(filePath, 'a+', encoding='utf8') as fp:
                                fp.write(ftpapi_json + '\n')
                                fp.flush()
                            fp.close()
                    except Exception as e:
                        print(e.with_traceback())
                        print(i.remotepath, localpath, fileConditions)
                        sys.exit(0)


    def ftp_urlsToList(self, url='/jma/hsd', conditions=None):
        """
            FTP根据url和过滤条件，返回一个list
        :param url: ftp路径（文件或目录）
        :param conditions: 过滤条件
        :return: list
        """
        socket.setdefaulttimeout(6)
        ftp = self.ftp_connect()
        try:
            datas_name = ftp.nlst(url)
            datas_urls = []
            if conditions is not None:
                fliName = '.*' + conditions + '.*'
                for i in datas_name:
                    s = re.finditer(fliName, i)
                    for f in s:
                        datas_urls.append(f.group())
            else:
                return datas_name
            return datas_urls
        except(socket.error, socket.gaierror):
            print("\033[0;32;40mERROR: 链接超时: [{}:{}]\033[0m".format('get_ftp_urls', url))
            return None

    def ftp_urlsToFileAPI(self, url='/jma/hsd',dirConditions=None, fileConditions=None, connect: ftplib.FTP = None):
        """
        FTP根据url和过滤条件，返回一个list[FTPFileApi]
        :param url: ftp路径（文件或目录）
        :param conditions: 过滤条件
        :param connect:
        :return: list[FTPFileApi]
        """
        socket.setdefaulttimeout(6)
        if connect is None:
            ftp = self.ftp_connect()
        else:
            ftp = connect
        ftpapi_datas: [FTPFileApi] = []
        facts = ['modify', 'perm', 'size', 'type', 'unix.groupname', 'unix.mode', 'unix.ownername']
        opts_mlst: [(str, {str, str})] = None
        forwardSlash = '/'
        try:
            opts_mlst = list(ftp.mlsd(url, facts))
        except ftplib.error_perm as e:
            # 判断是否是文件
            if opts_mlst is None and '550' in str(e):
                url_lis = url.split(forwardSlash)
                url = forwardSlash.join(url_lis[:-2]) + forwardSlash
                opts_mlst = [i for i in list(ftp.mlsd(url, facts)) if i[0].find(url_lis[-2]) != -1]
            else:
                return None
        except(socket.error, socket.gaierror):
            print("\033[0;32;40mERROR: 链接超时: [{}:{}]\033[0m".format('get_ftp_urls', url))
            return None
        except Exception as e:
            return None
        if dirConditions is not None:
            opts_mlst = [i for i in opts_mlst if i[0].find(dirConditions) != -1]
        for i in opts_mlst:
            if i[1].get('type') == 'file':
                if ((fileConditions is not None) and (i[0].find(fileConditions) != -1)) or (fileConditions is None):
                    ftpapi_datas.append(
                        FTPFileApi(name=i[0], modify=int(i[1].get('modify')), remotepath=url + i[0],
                                    size=int(i[1].get('size')),
                                    adfr=i[1].get('perm') + "(" + i[1].get('unix.mode') + ")",
                                    ownername=i[1].get('unix.ownername') + " " + i[1].get('unix.groupname'),
                                    datatype=i[1].get('type')))
            elif i[1].get('type') == 'dir':
                ftpapi_datas.append(
                    FTPFileApi(name=i[0], modify=int(i[1].get('modify')), remotepath=url + i[0],
                                ownername=i[1].get('unix.ownername') + " " + i[1].get('unix.groupname'),
                                datatype=i[1].get('type')))
        cmpfun = operator.attrgetter('name', 'size')
        ftpapi_datas.sort(key=cmpfun)
        return ftpapi_datas

    def get_url_download_file(self, urls: str, downloadPath: str):
        lisUrls = []
        with open(urls, 'r+') as fo:
            lisUrls = fo.read().splitlines()
            lisUrls.sort()
        ifs = 1
        while ifs <= 1:
            print('\033[0;32;40m剩余下载文件数量:' + str(len(lisUrls)) + '\033[0m')
            try:
                for i in lisUrls:
                    url_name = i.split('/')[-1]
                    if not downloadPath.split('/')[-1] is '':
                        downloadPath = downloadPath + '/'
                    print('\033[0;32;40m下载文件 [{}]:\033[0m'.format(url_name))
                    re = self.download_file(i.strip(), downloadPath + url_name)
                    if re == 1:
                        lisUrls.remove(i)
                    ifs += 1
                    print('\033[0;32;40m下载文件 [{}]:成功！\033[0m'.format(url_name))
            except Exception:
                ifs = 1

    @run_time
    def upload_file(self, ftp: FTP, remotepath: str,
                    localpath: str, file: str):
        """
         # 从本地上传文件到ftp
        :param ftp: ftp对象
        :param remotepath: ftp远程路径
        :param localpath: 本地
        :return:
        """
        flag = False
        buffer_size = 10240  # 默认是8192
        print(ftp.getwelcome())  # 显示登录ftp信息

        fp = open(os.path.join(localpath, file), 'rb')

        try:
            ftp.cwd(remotepath)  # 进入远程目录
            print(
                "found folder [{}] in ftp server, upload processing.".format(remotepath))
            print('进入目录', ftp.pwd())
            # 将传输模式改为二进制模式 ,避免提示 ftplib.error_perm: 550 SIZE not allowed in
            # ASCII
            ftp.voidcmd('TYPE I')
            ftp.storbinary('STOR ' + file, fp, buffer_size)
            ftp.set_debuglevel(0)
            print("上传文件 [{}] 成功".format(file))
            flag = True
        except error_perm as e:
            print('文件[{}]传输有误,{}'.format(file, str(e)))
        except TimeoutError:
            print('文件[{}]传输超时'.format(file))
            pass
        except Exception as e:
            print('文件[{}]传输异常'.format(file, str(e)))
            pass
        finally:
            fp.close()
        return {'file_name': file, 'flag': flag}

    '''
        ftp下载操作
    '''

    def download_file(self, ftp: Optional[FTP], ftpFile: FTPFileApi = None, ftp_file_path=None, dst_file_path=None):
        """
        从ftp下载文件到本地
        :param ftpFile: FTPFileApi
        :param ftp: ftp连接
        :param ftp_file_path: ftp下载文件
        :param dst_file_path: 本地存放
        """
        try:
            if (ftp_file_path is None) and (dst_file_path is None):
                remote_file_size = ftpFile.size
                dst_file_path = ftpFile.localpath
                ftp_file_path = ftpFile.remotepath
            elif ftpFile is None:
                ftp.voidcmd('TYPE I')
                remote_file_size = ftp.size(ftp_file_path)  # 文件总大小
            print('remote filesize [{}]'.format(remote_file_size))
        except Exception:
            return
        # 判断文件是否存在并实现断点续传
        lsize = self.ftp_cute(dst_file_path, remote_file_size)
        if lsize is None:
            return
        try:
            start = time.time()
            loop = 0
            while loop < 3:
                try:
                    if self.ftp_download(ftp, dst_file_path, ftp_file_path, remote_file_size, lsize):
                        break
                except:
                    loop = loop + 1
                    print('download_file:error 下载失败：', dst_file_path)
        except:
            return
        finally:
            end = time.time()
            print('consume time [{}]'.format(end - start))
            file_size = os.stat(dst_file_path).st_size
            if remote_file_size == file_size:
                print('local filesize [{}] filepath:[{}]'.format(
                    file_size, dst_file_path))

    def ftp_download(self, ftp: Optional[FTP], dst_file_path: str, ftp_file_path: str, remote_file_size: int,
                     lsize: int):
        # 将传输模式改为二进制模式 ,避免提示 ftplib.error_perm: 550 SIZE not allowed in ASCII
        ftp.voidcmd('TYPE I')
        # 改为被动模式下载
        ftp.set_pasv(True)
        buffer_size = 10240  # 缓存（默认是8192）
        cmpsize = 0  # 下载文件初始大小
        mode = 'wb' if lsize == 0 else 'ab'
        file_handle = open(dst_file_path, mode).write
        with ftp.transfercmd('RETR {0}'.format(ftp_file_path), lsize) as conn:
            while 1:
                data = conn.recv(buffer_size)
                if not data:
                    break
                file_handle(data)
                cmpsize += len(data)
                # 打印进度条
                processBar(cmpsize, remote_file_size)
            # shutdown ssl layer
            if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                conn.unwrap()
        # result = ftp.voidcmd('NOOP')
        # print('keep alive cmd success')
        return ftp.voidresp()

    def ftp_cute(self, dst_file_path, remote_file_size):
        '''
        check local file isn't exists and get the local file size
        :param dst_file_path: local文件地址
        :param remote_file_size: service文件大小
        :return: lsize: 偏移量
        '''
        lsize = 0
        if os.path.exists(dst_file_path):
            lsize = os.stat(dst_file_path).st_size
        if lsize >= remote_file_size:
            print('local file is bigger or equal remote file')
            return
        return lsize

    def ftp_close(self, ftp: Optional[FTP] = None):
        '''关闭socket连接并退出ftp
            :param ftp ftp连接
        '''
        try:
            # ftp.voidresp()
            print('No loop cmd')
            ftp.quit()
        except Exception as e:
            ftp.quit
            pass


class FTP_REQUESTS(object):
    '''
        通过requests操作FTP文件
        其实底层还是FTP还是Soket
        可以用于Web项目使用作参考（其实也没有那个必要）
    '''
    import requests, requests_ftp
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
                if conditions is not None:
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
        print(remote_file + '完成！花费时间：', (end - start))


if __name__ == '__main__':
    ftps = FTP_OPS()
    ftp = ftps.ftp_connect()
    url = 20191101
    storagePath = 'C:/Users/标注/Desktop/test/06/'
    ftpHead_jma = 'jma/hsd/'
    ftpHead_netcdf = '/jma/netcdf/'
    conditions = '06001'
    for i in range(20):
        remotePath = get_timeToUrl(ftp_url=url, dirOrFile='dir', ftp_head=ftpHead_netcdf)
        ftpLis: FTPFileApi = ftp_LocalQueries(url=remotePath, storagePath=storagePath, dirOrFile='dir')
        if len(ftpLis) is 0:
            ftps.ftp_FileAPI_RecursionDownload(remotepath=remotePath, localpath=storagePath, fileConditions=conditions,
                                           ftp=ftp)
            ftpLis = ftp_LocalQueries(url=remotePath, storagePath=storagePath, dirOrFile='dir')
        for i in ftpLis:
            ftps.download_file(ftp=ftp, ftpFile=i)
        url = url + 1
    # ftp_LocalQueries 结合 ftp_FileAPI_RecursionDownload实现:
    #     根据FTPFileApi查询本地是否存在.json文件，
    #       如果不存在，则将list[FTPFileApi]转换成json格式存储到本地存储路径xx.json文件中
    #       如果存在，则查找本地存储路径xx.json文件中，是否存在FTPFileApi对象
    #           如果.json中不存在，则将FTPFileApi转换成json格式存储到本地存储路径xx.json文件中
    #     最终返回查询结果：存在返回数据集，否则None
    # 以对象为最小原子，传参、改参等操作
    # （需改进并查找本地路径中是否存在文件，并验证文件名、大小等，确保文件的完整性）
    # 需求验证器函数：（下载完一小时，或一天，或一个月验证一次）
    #   1、查看.json中是否存在，并修改state状态
    #   2、如果.json中所有state状态都是已完成，
    #   则根据传入相关参数等信息（FTPFileApi），判断文件是否存在，文件名是否正确，文件大小（大于或等于）
    #   3、验证结束后，删除.json文件
    # 下载后验证文件完整性，并修改state参数