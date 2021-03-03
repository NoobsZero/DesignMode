# -*- encoding:utf-8 -*-
"""
@File   :parseConf.py
@Time   :2021/2/10 9:42
@Author :Chen
@Software:PyCharm
"""
import base64  # 想将字符串转编码成base64,要先将字符串转换成二进制数据
import os
import sys
import time
import uuid
import jieba
from xpinyin import Pinyin
from tool.myconfigUtil.JsonConfig import JsonConfig
from tool.mylogUtil.baselog import logger
from tqdm import tqdm


def get_encode_base64(k, v=None):
    """
        密码加密
    Args:
        k: 密码
        v: 

    Returns:

    """
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
    """
        密码解密
    Args:
        v: 加密密码

    Returns:

    """
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


def is_all_chinese(sirs):
    """
        判断是否是中文
    :param sirs:
    :return:
    """
    for _char in sirs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def is_number(s):
    """
        判断字符串是否为数字
    Args:
        s: 字符串

    Returns:bool

    """
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


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
        self.count = int(count)
        self.interval = 1
        interTmp = int(self.count / 100)
        if interTmp > 1:
            self.interval = interTmp

    def progressBarFlush(self, index):
        index = int(index)
        if self.count < 2:
            return
        if (index < self.interval) or (index % self.interval != 0):
            return
        i = int(index * 100 / (self.count - 1))
        s1 = "\r[%s%s]%d%%" % ("#" * i, " " * (100 - i), i)
        sys.stdout.write(s1)
        sys.stdout.flush()

    def tqdmBarFlush(self, filePath):
        with tqdm(total=self.count) as pbar:
            if not os.path.isfile(filePath):
                raise FileNotFoundError(filePath)
            while True:
                try:
                    index = os.path.getsize(filePath)
                    pbar.update(index - self.interval)
                    if index >= self.count:
                        return True
                    time.sleep(0.1)
                    self.interval = index
                except FileNotFoundError as e:
                    pbar.update(self.count - self.interval)
                    return True


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


class CsID:
    def __init__(self, filePath=r'E:\JetBrains\PycharmProjects\untitled\tool\baseUtil\csId.json'):
        self.cityConfPath = filePath
        self.cityMapper = {}
        self.readCityName()

    def readCityName(self):
        self.cityMapper = JsonConfig().loadConf(self.cityConfPath).getValue(
            'cs_id')

    def getSheng(self):
        return [self.cityMapper[i] for i in self.cityMapper if i[-4:] == '0000']

    def getShi(self):
        return [self.cityMapper[i] for i in self.cityMapper if i[-4:] != '0000' and i[-2:] == '00']

    def getQu(self):
        return [self.cityMapper[i] for i in self.cityMapper if i[-2:] != '00']

    def getCityName(self, citycode):
        cityName = ""
        try:
            cityName = self.cityMapper[citycode]
        except KeyError:
            logger.error("未知的citycode：[{}]".format(citycode))
        return cityName


def getCslisdir(zip_url, urlLis=None, fileType='dir'):
    """
        使用递归算法根据城市（区、市、省）匹配字符串中相应的城市并返回结果
    :param zip_url: 下载数据所在地址
    :param urlLis: key：城市名 valuse：文件夹地址
    :param fileType: 判断文件类型
    :return: urlLis
    """
    if urlLis is None:
        urlLis = {}
    for url in os.listdir(zip_url):
        url = os.path.join(zip_url, url)
        if os.path.isdir(url) and fileType == 'dir' or fileType == 'file' and os.path.isfile(url):
            cs_key = getChengshi(url, CsID().getShi(), '市')
            if cs_key is None:
                cs_key = getChengshi(url, CsID().getQu(), '区')
            if cs_key is None:
                cs_key = getChengshi(url, CsID().getSheng(), '省')
            if cs_key is None:
                urlLis = getCslisdir(url, urlLis, fileType)
            else:
                if cs_key in urlLis:
                    urlLis[cs_key].append(url)
                else:
                    urlLis[cs_key] = [url]
    return urlLis


if __name__ == '__main__':
    count = 8888888
    handle = BaseProgressBar(count)
    for i in range(count):
        handle.progressBarFlush(i)
