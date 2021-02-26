from .unCompressItemEmData import *
from .unCompressItem import *
from ..model.modelCenter import *
from .cityinfo import cityMapper
from .parseCommand import *

sessOrm = None


class UnCompressCenter:
    def __init__(self, CommandParameter):
        """
            UnCompressCenter
            解压缩文件所需配置信息
        Args:
            CommandParameter:
        """
        self.CommandParameter = CommandParameter
        self.normalConfPath = "./conf/normal.conf.json"
        self.dbConfPath = "./conf/db.conf.json"
        self.srcFilePaths = []
        self.LOCAL_TIME_NAME = baseTool.getLocalTimeForName()
        self.nginxRoot = baseTool.BaseConfig().loadConf(self.normalConfPath).objMap["nginxRoot"]
        logger.info("self.nginxRoot:[{}]".format(self.nginxRoot))

    def generateRecord(self, cityCode, deviceType, dateStr, DbName, RootPhotoPath, RootAlgConfPath):
        mc = MapperCityDataBaseName(cityCode=cityCode, deviceType=deviceType,
                                    generateDate=dateStr, dbname=DbName, photoPath=RootPhotoPath,
                                    algConfPath=RootAlgConfPath)
        mc.inDbTime = getLocalTime()
        mc.cityName = cityMapper.getCityName(mc.cityCode)
        mc.cityPinYin = getPinyin(mc.cityName)
        mc.subPath = mc.photoPath.split(self.nginxRoot)[1]
        return mc

    def generateRecordWuPan(self, cityCode, deviceType, dateStr, DbName, RootPhotoPath, RootAlgConfPath, packageName,
                            number):
        mc = MapperCityDataBaseNameWuPan(cityCode=cityCode, deviceType=deviceType,
                                         generateDate=dateStr, dbname=DbName, photoPath=RootPhotoPath,
                                         algConfPath=RootAlgConfPath, packageName=packageName, number=number)
        mc.inDbTime = getLocalTime()
        mc.cityName = cityMapper.getCityName(mc.cityCode)
        mc.cityPinYin = getPinyin(mc.cityName)
        mc.subPath = mc.photoPath.split(self.nginxRoot)[1]
        return mc

    # def getResultPath(self):
    #     return ROOT_TMP_DATA_PATH + "/" + self.LOCAL_TIME_NAME
    #
    # def getSuccessDir(self):
    #     return self.getResultPath() + "/success/"
    #
    # def getFailureDir(self):
    #     return self.getResultPath() + "/failure/"

    def setSourceFile(self, fileList=[]):
        self.srcFilePaths = fileList
        return self

    def setSourceDir(self, dirPath):
        if os.path.exists(dirPath):
            liDirs = os.listdir(dirPath)
            for item in liDirs:
                item = dirPath + "/" + item
                if not (item.endswith(".zip") or item.endswith("tar.gz")):
                    continue
                if os.path.isfile(item) or os.path.islink(item):
                    self.srcFilePaths.append(item)
        return self

    def printProcessList(self):
        logger.info("处理文件列表如下:")
        logger.info("")
        logger.info(self.srcFilePaths)

    def start(self):
        logger.info("start .....")
        # checkDir(self.getFailureDir() )
        # checkDir(self.getSuccessDir() )
        li_result = []
        countSuccess = 0
        for item in self.srcFilePaths:
            isOk, message = self.UnCompressStart(item)
            li_result.append((isOk, item, message))
            if self.CommandParameter.noMove:
                continue
            if isOk:
                countSuccess += 1
                moveTarget2Dir(item, self.getSuccessDir())
            else:
                moveTarget2Dir(item, self.getFailureDir())
                pass

        if len(li_result) > 0:
            ResultContent = []
            ResultContent.append("")
            ResultContent.append("")
            ResultContent.append("处理文件共计:{}个, 成功数量:{}个".format(len(li_result), countSuccess))
            ResultContent.append("")
            ResultContent.append("the result:")
            ResultContent.append("")
            ResultContent.append("处理是否成功\t\t\t文件\t\t\t错误信息")
            for item in li_result:
                ResultContent.append("{}\t{}\t{}".format(item[0], item[1], item[2]))
            ResultContent.append("---------------------------the end------------------------------------------")

            checkDir(self.getResultPath())
            fdHandle = open(self.getResultPath() + "/report.txt", 'w')
            for item in ResultContent:
                logger.info(item)
                fdHandle.write(item + "\n")
            fdHandle.close()
        else:
            logger.warn("没有 处理结束的压缩文件")

    def UnCompressStart(self, filePath):
        retCode = False
        retMessage = "数据归档失败"
        try:
            isWuPan = os.path.basename(filePath).find("CJWP") > 0
            isWebExport = os.path.basename(filePath).startswith("emData_")

            upc = None
            if not isWebExport:
                upc = UnCompressItem(filePath=filePath, normalConfPath=self.normalConfPath, dbConfFile=self.dbConfPath)
            else:
                if isWuPan:
                    upc = UnCompressItemWebExportWuPan(filePath=filePath, normalConfPath=self.normalConfPath,
                                                       dbConfFile=self.dbConfPath).setOrmSess(sessOrm)
                else:
                    upc = UnCompressItemWebExport(filePath=filePath, normalConfPath=self.normalConfPath,
                                                  dbConfFile=self.dbConfPath)

            if not isWuPan:
                upc.callBackGenerateRecord = self.generateRecord
                upc.cbInsertFunc = insertMapperCityDataBaseName
            else:
                upc.callBackGenerateRecord = self.generateRecordWuPan
                upc.cbInsertFunc = insertMapperCityDataBaseNameWuPan

            isOk, mc = upc.start()
            if isOk:
                # print("@@@@@@@@@@@@@@@@@@@@@@@:",dict(mc) )
                retMessage = "城市:{} ,日期: {} 归档完毕！".format(mc.cityName, mc.generateDate)
                retCode = upc.insertOrmRecordObj(sessOrm, mc)
                if not retCode:
                    retMessage = "{}:映射表_{} 插入失败".format(retMessage, "City_DataBaseName")

        except TarContentError as ex:
            logger.error(ex)
            retMessage = "{}:{}".format(retMessage, ex)
        except Exception as ex:
            logger.error(ex)
            retMessage = "{}:{}".format(retMessage, ex)
            traceback.print_exc()
        return retCode, retMessage


def initOrmHandle():
    global sessOrm
    sessOrm = OrmOperateDB('./conf/db.conf.json')


# def collectData():
#     initOrmHandle()
#     pcenter = UnCompressCenter()
#     # pcenter.setSourceFile(["/home/public/software/test_photo/bak/chejian.zip"]).start()
#     pcenter.setSourceDir("/home/public/software/test_photo/bak").start()
#
#
# def selectData():
#     initOrmHandle()


def main(listArgs):
    initOrmHandle()

    commandParam = ReadCommandParameter().parseCommandArgs(sys.argv[1:])

    logger.setLevel(commandParam.logLevel)

    pcenter = UnCompressCenter(commandParam)

    if commandParam.sourceType == SOURCE_TYPE_FILES:
        pcenter.setSourceFile(commandParam.sourceData)
    elif commandParam.sourceType == SOURCE_TYPE_DIRS:
        pcenter.setSourceDir(commandParam.sourceData[0])
    elif commandParam.sourceType == SOURCE_TYPE_URLS:
        logger.error("目前 还未支持该功能")
        sys.exit(1)

    pcenter.printProcessList()
    if commandParam.isRun:
        pcenter.start()


# if __name__ == '__main__':
    # collectData()
    # test_progressBar()
