# -*- encoding:utf-8 -*-
"""
@File   :unCompress.py
@Time   :2021/2/26 11:00
@Author :Chen
@Software:PyCharm
"""
import logging
import os
import re
import shutil
import tarfile
import zipfile
import rarfile
import gzip

from tool.baseUtil.getBaseUtil import BaseProgressBar
from tool.dirUtil.getDirUtil import checkDir
from tool.mylogUtil.baselog import logger


def preStart(tmpDir):
    try:
        if os.path.exists(tmpDir):
            shutil.rmtree(tmpDir)
        os.makedirs(tmpDir)
    except Exception as e:
        logger.error("临时文件创建失败:{}".format(e))
        return False
    return True


class Uncompress:
    def __init__(self, targetPath):
        self.fd = None
        self.tmpFilePath = ""
        self.targetPath = targetPath
        self.objProgress = None
        self.decodeVersion = ""

    def filterSpecialFIle(self, name, index):
        logger.debug("name:{}".format(name))
        if logger.level > logging.DEBUG:
            self.objProgress.progressBarFlush(index)

    def getFileList(self):
        return []

    def start(self, systemType='linux'):
        self.objProgress = BaseProgressBar(len(self.getFileList()))
        if checkDir(self.targetPath) < 0:
            return False
        index = 0
        for name in self.getFileList():
            self.filterSpecialFIle(name, index)
            # win系统特殊字符需要替换
            if systemType == 'windows':
                for fn in self.fd:
                    fn.name = re.sub(r'[\/:*?"<>|]', '_', fn.name)
                name = re.sub(r'[\/:*?"<>|]', '_', name)
            self.fd.extract(name, self.targetPath)
            index += 1
        self.fd.close()
        return True


class unCompressZIP(Uncompress):
    """
        unCompressZIP
            解压zip压缩包
    Args:
        filePath: 原始路径
        targetPath: 目标路径
    """

    def __init__(self, filePath, targetPath):
        super().__init__(targetPath)
        self.getHandle(filePath)

    def getHandle(self, srcPath):
        self.fd = zipfile.ZipFile(srcPath)

    def getFileList(self):
        return self.fd.namelist()


class unCompressTGZ(Uncompress):
    """
        unCompressTGZ
            解压tgz压缩包
    Args:
        filePath: 原始路径
        targetPath: 目标路径
    """

    def __init__(self, filePath, targetPath):
        super().__init__(targetPath)
        self.getHandle(filePath)

    def getHandle(self, srcPath):
        self.fd = tarfile.open(srcPath)

    def getFileList(self):
        return self.fd.getnames()


class unCompressRAR(Uncompress):
    """
        unCompressRAR
            解压rar压缩包
    Args:
        filePath: 原始路径
        targetPath: 目标路径
    """

    def __init__(self, filePath, targetPath):
        super().__init__(targetPath)
        self.getHandle(filePath)

    def getHandle(self, srcPath):
        self.fd = rarfile.RarFile(srcPath)

    def getFileList(self):
        return self.fd.namelist()


class unCompressGZ(Uncompress):
    """
        unCompressRAR
            解压rar压缩包
    Args:
        filePath: 原始路径
        targetPath: 目标路径
    """

    def __init__(self, filePath, targetPath):
        super().__init__(targetPath)
        self.getHandle(filePath)

    def getHandle(self, srcPath):
        self.fd = gzip.GzipFile(srcPath)

    def getFileList(self):
        return self.fd.filename()


def parseSourceFile(filePath, targetPath):
    """
        解压源文件
    Args:
        filePath: 原始路径
        targetPath: 目标路径

    Returns:

    """
    if not os.path.isfile(filePath):
        print("不是一个压缩文件", filePath)
        return False, None
    print("开始解析文件 ...", filePath)

    strTail = ""
    if filePath.endswith(".zip"):
        un_compress_obj = unCompressZIP(filePath, targetPath)
        strTail = ".zip"
    elif filePath.endswith(".tar.gz"):
        un_compress_obj = unCompressTGZ(filePath, targetPath)
        strTail = ".tar.gz"
    elif filePath.endswith(".rar"):
        un_compress_obj = unCompressRAR(filePath, targetPath)
        strTail = ".rar"
    elif filePath.endswith(".gz"):
        un_compress_obj = unCompressGZ(filePath, targetPath)
        strTail = ".gz"
    else:
        print("文件格式无法进行处理,[%s]{}", strTail, filePath)
        return False, None

    fileName = os.path.basename(filePath)
    fendNameLi = fileName.split("V.")
    decodeVersion = ""
    if len(fendNameLi) == 2:
        tmpVersion = fendNameLi[1]
        if tmpVersion.endswith(strTail):
            decodeVersion = tmpVersion.split(".")[0]
    un_compress_obj.decodeVersion = decodeVersion
    return True, un_compress_obj


if __name__ == '__main__':
    res, unCompressObj = parseSourceFile(filePath='E:\\chejian\\20210225-中山车检-赵振强-已完成\\chejian_4420_20210225133614.tar.gz',
                                         targetPath='E:\\chejian\\20210225-中山车检-赵振强-已完成')
    if res:
        unCompressObj.start(systemType='windows')
