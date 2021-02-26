#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import uuid
import shutil
from xpinyin import Pinyin
from .baseDBOperate import *
from .baseConfig import *
from .baselog import logger


def generateUUID():
    return str(uuid.uuid4()).replace("-", "")


def getPinyin(value=""):
    ret = ""
    if len(value) > 0:
        ret = Pinyin().get_pinyin(value, "")
    return ret


def getLocalTime(format="%Y-%m-%d %H:%M:%S"):
    return time.strftime(format, time.localtime())


def getLocalTimeForName():
    return getLocalTime(format="%Y%m%d_%H%M%S")


def checkDir(targetPath):
    Flag = 0
    if os.path.isdir(targetPath):
        pass
    else:
        try:
            os.makedirs(targetPath)
        except Exception as e:
            logger.error("文件夹创建失败{}".format(targetPath))
            logger.error("error:{}".format(e))
            Flag = -1
        Flag = 1
    return Flag


def moveTarget2Dir(targetFile, dirPath):
    Flag = False
    if os.path.exists(targetFile):
        if checkDir(dirPath) >= 0:
            shutil.move(targetFile, dirPath)
            Flag = True
    return Flag


class BaseProgressBar:

    def __init__(self, count):
        self.count = count
        self.interval = 1
        interTmp = int(self.count / 100)
        if interTmp > 1:
            self.interval = interTmp
        # print("interval:",self.interval)

    def progressBarFlush(self, index):
        if self.count < 2:
            return
        if (index < self.interval) or (index % self.interval != 0):
            return
        # print("#####",index,"###",index % self.interval )
        i = int(index * 100 / (self.count - 1))
        # print("index,",index,"count:",self.count,"@@@@",i,"@@@",100-i)
        s1 = "\r[%s%s]%d%%" % ("#" * i, " " * (100 - i), i)
        sys.stdout.write(s1)
        sys.stdout.flush()


def test_progressBar():
    count = 88
    handle = BaseProgressBar(count)
    for i in range(count):
        handle.progressBarFlush(i)


if __name__ == '__main__':
    test_create()
