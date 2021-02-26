from .unCompressFunc import *
from .parseConf import *
from ..common.dataDecode import convertCodeData
from ..common.baseDefine import *
from distutils import dir_util
import os.path


def preStart(tmpDir):
    # 创建临时文件
    try:
        if os.path.exists(tmpDir):
            shutil.rmtree(tmpDir)
        os.makedirs(tmpDir)
    except Exception as e:
        logger.error("临时文件创建失败:{}".format(e))
        return False
    return True


def parseSourceFile(filePath, tmpDir):
    unCompressObj = None
    if not os.path.isfile(filePath):
        print("不是一个压缩文件", filePath)
        return False, None
    print("开始解析文件 ...", filePath)

    strTail = ""
    # unCompressclazz = None
    if filePath.endswith(".zip"):
        # unCompressclazz = unCompressZIP
        unCompressObj = unCompressZIP(filePath, tmpDir)
        strTail = ".zip"
    elif filePath.endswith(".tar.gz"):
        unCompressObj = unCompressTGZ(filePath, tmpDir)
        strTail = ".tar.gz"
        # unCompressclazz = unCompressTGZ
    else:
        print("文件格式无法进行处理,[%s]{}", strTail, filePath)
        return False, None

    # unCompressObj.setFilterFunc(self.parseBaseConf)
    fileName = os.path.basename(filePath)
    fendNameLi = fileName.split("V.")
    decodeVersion = ""
    if len(fendNameLi) == 2:
        tmpVersion = fendNameLi[1]
        if tmpVersion.endswith(strTail):
            decodeVersion = tmpVersion.split(".")[0]

    unCompressObj.decodeVersion = decodeVersion

    return True, unCompressObj


class UnCompressItem:
    def __init__(self, filePath="", normalConfPath="./conf/normal.conf.json", dbConfFile="./conf/db.conf.json"):
        self.filePath = filePath
        self.packageName = os.path.basename(filePath)

        self.baseCityInfo = RawDataBaseInfo()
        self.DbName = ""

        # self.tmpDir = ROOT_TMP_DATA_PATH+"/_Data_photos/"
        # self.successSource =  ROOT_TMP_DATA_PATH+"/success/"
        # self.failureSource =  ROOT_TMP_DATA_PATH+"/failure/"

        self.dbConfFile = dbConfFile
        self.unCompressObj = None
        self.confSaveRules = DataSaveConf(normalConfPath)
        self.callBackGenerateRecord = None
        self.cbInsertFunc = None
        self.ormSess = None

        logger.info("初始化完毕...")

    def setOrmSess(self, ormSess):
        self.ormSess = ormSess
        return self

    def preCheck(self):
        if not self.parse():
            logger.error("待解压文件检测失败, 程序终止")
            return False
        if not preStart(self.confSaveRules.getTmpDir()):
            return False
        logger.info("解压 前置检测完毕 ...")
        return True

    def parse(self):
        isOk, self.unCompressObj = parseSourceFile(self.filePath, self.confSaveRules.getTmpDir())
        if isOk:
            self.unCompressObj.setFilterFunc(self.parseBaseConf)
        return isOk

    # 从已解压的目录中获取信息
    def ParseFromUnCompressDir(self):
        pass

    # 解压到 临时文件
    def startUnCompress(self):
        if self.unCompressObj is None:
            return False
        RetVal = self.unCompressObj.start()

        # 在临时目录里 填充相关信息
        self.ParseFromUnCompressDir()

        return RetVal and self.IsParseSuccess()

    def IsParseSuccess(self):
        return self.unCompressObj.IsParseSuccess

    def parseBaseConf(self):
        if self.unCompressObj is None:
            return False
        isOk, self.baseCityInfo = self.unCompressObj.parseBaseConfInfo()
        return isOk

    def clearAlgConf(self):
        # 查看临时文件是否有配置文件
        tmpConf = self.confSaveRules.getTmpAlgConfPath()
        logger.info("临时城市配置文件[{}]".format(tmpConf))
        if not os.path.exists(tmpConf):
            logger.warn("压缩文件找不到现场配置")
            return False

        local = self.confSaveRules.getRootAlgConfPath()
        logger.info("开始清除旧的城市配置..... [{}]".format(local))
        if os.path.exists(local):
            shutil.rmtree(local)
        return True

    def deCodePhotoData(self):
        if len(self.unCompressObj.decodeVersion) == 0:
            return
        rawDir = self.confSaveRules.getTmpPhotoPath()
        decodeDir = self.confSaveRules.getTmpPhotoDecodePath()
        convertCodeData(rawDir, decodeDir, self.unCompressObj.decodeVersion)

        pass

    def movePhotoData(self):
        # dstPhoto = self.savePath
        oldPhotoPath = self.confSaveRules.getRootPhotoPath() + "/" + self.baseCityInfo.dateStr
        dstPhotoPath = oldPhotoPath + "/"

        tmpPhotoPath = self.confSaveRules.getTmpPhotoPath()
        if len(self.unCompressObj.decodeVersion) > 0:
            tmpPhotoPath = self.confSaveRules.getTmpPhotoDecodePath()

        logger.info("移动照片:from:[{}]".format(tmpPhotoPath))
        logger.info("to:[{}]".format(dstPhotoPath))

        if os.path.exists(oldPhotoPath):
            logger.warn("#####################文件路径已存在####################################")
            logger.info("正在清理旧 图片数据")
            shutil.rmtree(oldPhotoPath)

        shutil.move(tmpPhotoPath, oldPhotoPath + "/")
        logger.info("图片更新完毕！")

    def moveAlgConFigure(self):
        # shutil.move(self.getTmpAlgConfPath(), self.confSaveRules.getRootAlgConfPath())
        tmpPath = self.confSaveRules.getTmpAlgConfPath()
        photoPath = self.confSaveRules.getRootAlgConfPath() + "/"
        logger.info("移动配置:from:[{}]".format(tmpPath))
        logger.info("to:[{}]".format(photoPath))
        shutil.move(tmpPath, photoPath)

    def moveVideoData(self):
        pass

    def loadTmpData2Destination(self):
        self.clearAlgConf()

        self.dBFIlesImport()
        # self.insertMappingRecord()
        self.moveAlgConFigure()

        self.deCodePhotoData()

        self.movePhotoData()

        self.moveVideoData()

    def fixDBName(self):
        pass

    def dBFIlesImport(self):
        isOk, liFiles = self.getDBFilesImport()
        logger.info("被导入的数据库表格文件liFiles:[{}]".format(liFiles))
        if not isOk:
            logger.warn("缺少数据库文件")
            return False

        self.DbName = self.confSaveRules.getNewDateBaseName()
        self.fixDBName()

        logger.info("准备创建数据库 ...")
        if not createDataBase(self.dbConfFile, self.DbName):
            return False

        # 导入数据表
        logger.info("开始导入数据库记录 ...")
        handle = OperateDB(self.dbConfFile, renameDb=self.DbName)
        handle.impDBFileList(liFiles)

        # self.DbName = dbName
        pass

    def checkDBFilesImport(self):
        # 导入文件
        # "chejian/4419/2020-08-28/vehicle_info_20200828145137.sql"
        # "chejian/4419/2020-08-28/photo_info_20200828145137.sql"

        photo_info_table = ""
        vehicle_table = ""
        jiaoQiangXian_table = ""
        if len(self.unCompressObj.photo_info_files) > 0:
            photo_info_table = max(self.unCompressObj.photo_info_files)

        if len(self.unCompressObj.vehicle_info_files) > 0:
            vehicle_table = max(self.unCompressObj.vehicle_info_files)

        if len(self.unCompressObj.chaYanVehicle_info_files) > 0:
            vehicle_table = max(self.unCompressObj.chaYanVehicle_info_files)
        if len(self.unCompressObj.jiaoQiangXian_info_files) > 0:
            jiaoQiangXian_table = max(self.unCompressObj.jiaoQiangXian_info_files)
        if len(photo_info_table) == 0 or len(vehicle_table) == 0:
            return False, []

        photo_info_path = self.confSaveRules.getTmpDir() + "/" + photo_info_table
        vehicle_path = self.confSaveRules.getTmpDir() + "/" + vehicle_table
        jiaoQiangXian_path = self.confSaveRules.getTmpDir() + "/" + jiaoQiangXian_table

        self.unCompressObj.allSqlFiles = [photo_info_path, vehicle_path, jiaoQiangXian_path]

    def getDBFilesImport(self):
        # todo 创建db
        self.checkDBFilesImport()
        return len(self.unCompressObj.allSqlFiles) > 0, self.unCompressObj.allSqlFiles

    def insertOrmRecordObj(self, ormHandle, objData):
        return self.cbInsertFunc(ormHandle, objData)

    def genarateOrmRecordObj(self):
        val = None
        if self.callBackGenerateRecord is not None:
            val = self.callBackGenerateRecord(self.baseCityInfo.cityCode, self.baseCityInfo.deviceType,
                                              self.baseCityInfo.dateStr, self.DbName,
                                              self.confSaveRules.getRootPhotoPath(),
                                              self.confSaveRules.getRootAlgConfPath())
        return val

    def start(self):
        val = None
        if not self.preCheck():
            return False, val
        if not self.startUnCompress():
            message = "解压缩数据 目录结构不符合要求"
            raise TarContentError(message)

        print("")
        self.confSaveRules.setBaseCityInfo(self.baseCityInfo).format()

        logger.info("解压成功 ..., 开始数据整理....")
        self.loadTmpData2Destination()
        val = self.genarateOrmRecordObj()
        # print(callBackGenerateRecord)
        # if  callBackGenerateRecord is not None:
        # val = callBackGenerateRecord(self.baseCityInfo.cityCode, self.baseCityInfo.deviceType, self.baseCityInfo.dateStr, self.DbName,
        #                        self.confSaveRules.getRootPhotoPath(),self.confSaveRules.getRootAlgConfPath())

        return True, val


# /home/public/dataBack/chejian/
# /home/public/dataBack/chayan/

# 城市代码/日期：
# 配置：  /CheJianConfig

def test_start():
    # filepath = "/home/public/software/test_photo/bak/chejian.zip"
    filepath = "/home/public/software/test_photo/bak/chejian.tar.gz"
    Dstpath = "./conf/normal.conf.json"
    dbConfPath = "./conf/db.conf.json"
    logger.info("start .....")
    upc = UnCompressItem(filePath=filepath, normalConfPath=Dstpath, dbConfFile=dbConfPath)
    upc.start()


def test_insertSqlFile():
    val = [
        '/home/public/software/test_photo/bak/chejiantest9528/demo/chejian/4419/2020-08-28/photo_info_20200828145137.sql',
        '/home/public/software/test_photo/bak/chejiantest9528/demo/chejian/4419/2020-08-28/vehicle_info_20200828145137.sql']
    dbConfPath = "./conf/db.conf.json"
    dbName = "chejian_test_12345"
    handle = OperateDB(dbConfPath, renameDb=dbName)
    for item in val:
        handle.impDBFile(item)


def test_movedirs():
    pathSrc = "/home/yuyang/develop/temp/test/dotest/source" + "/"
    pathDst = "/home/yuyang/develop/temp/test/dotest/dst" + "/"
    # shutil.move(pathSrc,pathDst)
    dir_util.copy_tree(pathSrc, pathDst)


if __name__ == '__main__':
    # test_insertSqlFile()
    # test_start()
    test_movedirs()
