# -*- encoding:utf-8 -*-
"""
@File   :unCompressltem.py
@Time   :2021/2/10 9:31
@Author :Chen
@Software:PyCharm
"""
import tarfile
import zipfile
import logging

from tool.mydbUtil.emCollect.service.parseConf import RawDataBaseInfo


def parsePathInfo(tmpNameItem):
    rdbi = RawDataBaseInfo()
    if len(tmpNameItem) == 0:
        print("tmpNameItem is null")
        return False, None
    try:
        nameList = tmpNameItem.split("/", 1)
        rdbi.deviceType = nameList[0]
        tmpNameItem = nameList[1]
        nameList = tmpNameItem.split("/", 1)
        rdbi.cityCode = nameList[0]
        rdbi.dateStr = nameList[1].split("/", 1)[0]
    except Exception as e:
        return False, None

    rootDir = ["chejian", "chayan"]
    if not (rdbi.deviceType in rootDir):
        raise TarContentError("{} is not in {}".format(rdbi.deviceType, rootDir))
        # return False,None
    if (not rdbi.cityCode.isdigit()) or (len(rdbi.cityCode) is not 4):
        return False, None
    if (len(rdbi.dateStr) is not len("2020-10-10")) or (not rdbi.dateStr[0:4].isdigit()):
        # print("date@@@@@@@")
        return False, None
    # print("")
    # print("=============================================================")
    # print("self.deviceType:{} self.cityCode:{} self.dateStr:{} ".format(rdbi.deviceType, rdbi.cityCode,
    #                                                                    rdbi.dateStr))
    return True, rdbi


class Uncompress:
    # def getHandle(self, srcPath):
    #     pass
    def __init__(self, targetPath):
        self.fd = None
        self.tmpFilePath = ""
        self.targetPath = targetPath
        self.photo_info_files = []
        self.vehicle_info_files = []
        self.chaYanVehicle_info_files = []
        self.jiaoQiangXian_info_files = []

        self.allSqlFiles = []
        self.filterFunc = None
        self.IsParseSuccess = False
        self.objProgress = None
        self.decodeVersion = ""

    def setFilterFunc(self, callback):
        self.filterFunc = callback

    def filterSqlFile(self, name):
        if name.endswith(".sql"):
            index = name.rfind("/")
            shortName = name[index + 1:]
            if shortName.startswith("chaYanVehicle"):
                self.chaYanVehicle_info_files.append(name)
                pass
            elif shortName.startswith("photo_info"):
                self.photo_info_files.append(name)
                pass
            elif shortName.startswith("vehicle_info"):
                self.vehicle_info_files.append(name)
                pass
            elif shortName.startswith("jiaoQiangXian_info"):
                self.jiaoQiangXian_info_files.append(name)
                pass
            # print("shortname:", shortName)

    def filterSpecialFIle(self, name, index):
        logger.debug("name:{}".format(name))
        if logger.level > logging.DEBUG:
            self.objProgress.progressBarFlush(index)
        # if  name[-4:] == ".sql":
        if not self.IsParseSuccess:
            # 用于读取城市名 时间
            # print("###############################################")
            self.tmpFilePath = name
            if self.filterFunc is not None:
                self.filterFunc()
        self.filterSqlFile(name)

    def parseBaseConfInfo(self):
        isOk, obj = parsePathInfo(self.tmpFilePath)
        if isOk:
            self.IsParseSuccess = True
        return isOk, obj

    def getFileList(self):
        return []

    def start(self):
        self.objProgress = BaseProgressBar(len(self.getFileList()))
        if checkDir(self.targetPath) < 0:
            return False
        index = 0
        for name in self.getFileList():
            self.filterSpecialFIle(name, index)
            self.fd.extract(name, self.targetPath)
            index += 1
        self.fd.close()
        return True

    # def checkDir(self):
    #     pass


class unCompressZIP(Uncompress):

    def __init__(self, filePath, targetPath):
        super().__init__(targetPath)
        self.getHandle(filePath)

    def getHandle(self, srcPath):
        self.fd = zipfile.ZipFile(srcPath)

    def getFileList(self):
        return self.fd.namelist()


class unCompressTGZ(Uncompress):

    def __init__(self, filePath, targetPath):
        super().__init__(targetPath)
        self.getHandle(filePath)

    def getHandle(self, srcPath):
        self.fd = tarfile.open(srcPath)

    def getFileList(self):
        return self.fd.getnames()
