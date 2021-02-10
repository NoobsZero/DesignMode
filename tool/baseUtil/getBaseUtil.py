# -*- encoding:utf-8 -*-
"""
@File   :parseConf.py
@Time   :2021/2/10 9:42
@Author :Chen
@Software:PyCharm
"""
import base64  # 想将字符串转编码成base64,要先将字符串转换成二进制数据
import datetime
import os
import re
import shutil
import sys
import time
import uuid

import jieba
from dateutil.parser import parse
from xpinyin import Pinyin
from tool.mylogUtil.baselog import logger


def get_encode_base64(k, v=None):
    try:
        if v is not None:
            data = k + '/' + v
        else:
            data = k
        clearBytesData = data.encode('utf-8')
        encodeData = base64.b64encode(clearBytesData)  # 被编码的参数必须是二进制数据
    except ValueError:
        print('无效参数！')
    else:
        print('加密成功！')
    return encodeData


def get_decode_base64(v):
    decodeData = base64.b64decode(v).decode('utf-8')
    return str(decodeData).split('/')[-1]


def generateUUID():
    """
    获取UUID
    Returns: UUID

    """
    return str(uuid.uuid4()).replace("-", "")


def getPinyin(value=""):
    """
    获取中文拼音
    Args:
        value: 中文

    Returns: 拼音

    """
    ret = ""
    if len(value) > 0:
        ret = Pinyin().get_pinyin(value, "")
    return ret


def getLocalTime(timestamp=time.localtime(), timeformat="%Y-%m-%d %H:%M:%S"):
    """
    获取当前时间
    Args:
        timeformat: 时间格式

    Returns:格式化的时间

    """
    return time.strftime(timeformat, timestamp)


def TimeStampToTime(timestamp, timeformat="%Y-%m-%d %H:%M:%S"):
    """
    时间戳转换时间
    Args:
        timestamp: 时间戳
        timeformat: 时间格式

    Returns: 格式化的时间

    """
    timeStruct = time.localtime(timestamp)
    return getLocalTime(timestamp=timeStruct, timeformat=timeformat)


def getDate(time_dst_dir):
    time_t1 = re.search(r'(\d{4}-\d{2}-\d{2})$', time_dst_dir)
    time_t2 = re.search(r'(\d{4}\d{2}\d{2})$', str(time_dst_dir))
    time_t3 = re.search(r'(\d{4}年\d{2}月\d{2}日)$', str(time_dst_dir))
    if time_t1 and validate(time_t1.group(1)):
        return time_dst_dir
    elif time_t2 and validate(time_t2.group(1)):
        return parse(time_t2.group(1)).strftime('%Y-%m-%d')
    elif time_t3:
        return parse(re.sub(r'\D', "", time_t3.group(1))).strftime('%Y-%m-%d')
    else:
        return None


def validate(date_text, type='%Y-%m-%d'):
    """
        时间检验，注意文件时间要符合日期规则超出无效！
    :param type:
    :param date_text: 字符串
    :return: boolean
    """
    try:
        datetime.datetime.strptime(date_text, type)
        re = True
    except ValueError:
        re = False
    return re


def checkDir(targetPath):
    """
    检查目录
    :param targetPath:目录路径
    :return Flag:存在 0，创建 1， 创建失败 -1
    """
    Flag = 0
    if os.path.isdir(targetPath):
        pass
    else:
        try:
            os.makedirs(targetPath)
        except Exception as e:
            logger.error("文件夹创建失败{}".format(targetPath))
            logger.error("error:{}".format(e))
            return -1
        Flag = 1
    return Flag


def moveTarget2Dir(targetFile, dirPath):
    """
    移动文件到指定目录
    :param targetFile:文件路径
    :param dirPath:目录路径
    :return Flag: bool
    """
    Flag = False
    if os.path.exists(targetFile):
        if checkDir(dirPath) >= 0:
            shutil.move(targetFile, dirPath)
            Flag = True
    return Flag


class BaseProgressBar:
    """
    进度条
        列：
        count = 8888888
        handle = BaseProgressBar(count)
        for i in range(count):
            handle.progressBarFlush(i)
    """

    def __init__(self, count):
        self.count = count
        self.interval = 1
        interTmp = int(self.count / 100)
        if interTmp > 1:
            self.interval = interTmp

    def progressBarFlush(self, index):
        if self.count < 2:
            return
        if (index < self.interval) or (index % self.interval != 0):
            return
        i = int(index * 100 / (self.count - 1))
        s1 = "\r[%s%s]%d%%" % ("#" * i, " " * (100 - i), i)
        sys.stdout.write(s1)
        sys.stdout.flush()


def getChengshi(url, chengshi, suffix):
    """
        获取城市名
        通过查询城市列表匹配地址中的城市名称并去掉后缀
    Args:
        url: 字符串
        chengshi: 城市列表
        suffix: 市、区、省

    Returns:城市名

    """
    jieba.setLogLevel(jieba.logging.INFO)
    seg_list = jieba.lcut(url)
    for i in seg_list:
        for k in chengshi:
            # linux
            i = i.encode('utf-8')
            if i.endswith(suffix):
                i = i.rstrip(suffix)
            if k.startswith(i):
                if suffix == '市':
                    return i
                elif suffix == '区':
                    return i
                elif suffix == '省':
                    return i

sheng = [cs_id[i] for i in cs_id if i[-4:] == '0000']
shi = [cs_id[i] for i in cs_id if i[-4:] != '0000' and i[-2:] == '00']
qu = [cs_id[i] for i in cs_id if i[-2:] != '00']


def lisdir(zip_url, urllis, type='dir'):
    """
        使用递归算法根据城市（区、市、省）匹配字符串中相应的城市并返回结果
    :param zip_url: 下载数据所在地址
    :param urllis: key：城市名 valuse：文件夹地址
    :return: urllis
    """
    for url in os.listdir(zip_url):
        url = os.path.join(zip_url, url)
        if os.path.isdir(url) and type == 'dir' or type == 'file':
            cs_key = getChengshi(url, shi, '市')
            if cs_key is None:
                cs_key = getChengshi(url, qu, '区')
            if cs_key is None:
                cs_key = getChengshi(url, sheng, '省')
            if cs_key is None:
                urllis = lisdir(url, urllis, type)
            else:
                if cs_key in urllis:
                    urllis[cs_key].append(url)
                else:
                    urllis[cs_key] = [url]
    return urllis