import os

from tool.dbUtil.mysqlUtil.emCollect.common import baseTool

#
# {
#     "basePath": "/opt/vehicle/rawdata",
#     "photoDir":"photos",
#     "cityConfDir":"CheJianConfig",
#
# }
from tool.dbUtil.mysqlUtil.emCollect.common.baselog import logger

ROOT_TMP_DATA_PATH = "../_Data_emCollect"


class RawDataBaseInfo:
    def __init__(self):
        self.deviceType = "None"
        self.cityCode = "None"
        self.dateStr = "None"


class DataSaveConf:
    def __init__(self, confPath):
        bconf = baseTool.BaseConfig().loadConf(confPath)
        print(bconf.__dict__)
        self.basePath = bconf.objMap["basePath"]
        self.photoDir = bconf.objMap["photoDir"]
        self.cityConfDir = "CheJianConfig"

        self.tmpDir = ROOT_TMP_DATA_PATH + "/_Data_photos/"

        self.photoPath = None
        self.cityConfPath = None
        self.baseCityInfo = RawDataBaseInfo()

        self.format()

    def setBaseCityInfo(self, baseCityInfo):
        self.baseCityInfo = baseCityInfo
        self.printBaseInfo()
        return self

    def format(self):
        self.photoPath = self.basePath + "/" + self.baseCityInfo.deviceType + "/" + self.photoDir + "/" + self.baseCityInfo.cityCode
        self.cityConfPath = self.basePath + "/" + self.baseCityInfo.deviceType + "/" + self.cityConfDir + "/" \
                            + self.baseCityInfo.cityCode + "/" + self.baseCityInfo.dateStr
        return self

    def printBaseInfo(self):
        logger.info("self.baseCityInfo.deviceType:{},self.baseCityInfo.cityCode:{},self.baseCityInfo.dateStr:{}".
                    format(self.baseCityInfo.deviceType, self.baseCityInfo.cityCode, self.baseCityInfo.dateStr))

    def getNewDateBaseName(self):
        tableName = "emTest_{deviceType}_{cityCpde}_{dataStr}".format(deviceType=self.baseCityInfo.deviceType,
                                                                      cityCpde=self.baseCityInfo.cityCode,
                                                                      dataStr=self.baseCityInfo.dateStr.replace("-",
                                                                                                                ""))
        return tableName

    def getTmpPhotoPath(self):
        return self.tmpDir + "/" + self.baseCityInfo.deviceType + "/" + self.baseCityInfo.cityCode + "/" + self.baseCityInfo.dateStr

    def getTmpAlgConfPath(self):
        return "{}/{}/{}".format(self.tmpDir, self.baseCityInfo.deviceType, "CheJianConfig")

    def getRootPhotoPath(self):
        return self.photoPath

    def getRootAlgConfPath(self):
        return self.cityConfPath

    def getTmpDir(self):
        return self.tmpDir

    def printValue(self):
        print(self.__dict__)


class ReadCompressData:
    def __init__(self, filePath):
        if not os.path.isfile(filePath):
            print("文件格式无法进行处理,{}", filePath)
        print("开始解析文件{} ...", filePath)
        pass


def test_normalConfigure(filepath):
    dsc = DataSaveConf(filepath)
    dsc.printValue()


if __name__ == '__main__':
    ReadCompressData(r"C:\Users\标注\Desktop\car\text\collect_photos-develop.zip")
    # test_normalConfigure("./conf/normal.conf.json")
    pass
