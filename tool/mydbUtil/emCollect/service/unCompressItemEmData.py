
from .unCompressItem import *
from .parseConf import *
from ..common.dataDecode import convertCodeData
from ..common.baseDefine import *
from distutils import  dir_util
import os.path
from ..model.modelCenter import getNextWuPanNumber

#################该文件 为了兼容web导出工具导出的数据目录格式
#################

# 获取一个目录下的日期目录
def getPathDates(rpath):
    if not os.path.exists(rpath):
        return False,[]
    li = []
    isOk = False
    for _,ds,_ in os.walk(rpath):
        for dsItem in ds :
            if len(dsItem) == len("2020-01-01"):
                li.append(dsItem)
                isOk = True
    return isOk, li

#web导出数据解析
class UnCompressItemWebExport (UnCompressItem):
    def __init__(self,filePath, normalConfPath,dbConfFile):
        super().__init__( filePath , normalConfPath, dbConfFile)


    def checkDBFilesImport(self):
        pass

    def ParseFromUnCompressDir(self):
        rPath=self.baseCityInfo.tmpRoot
        if len(self.baseCityInfo.deviceType) == 0  or  len(self.baseCityInfo.cityCode) == 0:
            return False

        basePath = os.path.join(rPath,self.baseCityInfo.deviceType  )
        sqlFilePath  = os.path.join(basePath,"sqlFiles", self.baseCityInfo.cityCode )
        photoFilePath = os.path.join(basePath,self.baseCityInfo.cityCode )

        isokPhoto, tmpPhotoData = getPathDates(photoFilePath)
        isOkSqlFiles, tmpSQLData =  getPathDates(sqlFilePath)
        if not (isokPhoto and isOkSqlFiles) :
            return  False

        self.baseCityInfo.dateStr = tmpSQLData[0]

        #### sql Files
        sqlFilePath += "/"+self.baseCityInfo.dateStr
        for _,_,sqlFiles in os.walk(sqlFilePath):
            for fItem in   sqlFiles :
                fItem.endswith(".sql")
                self.unCompressObj.allSqlFiles.append(os.path.join(sqlFilePath,fItem) )

        if len(self.unCompressObj.allSqlFiles) < 2:
            strSqlErrMessage="没有检测到sql文件{}".format(sqlFilePath)
            logger.error( strSqlErrMessage )
            raise SQLFilesError(strSqlErrMessage)
        #### sql File end
        ###  photos dirs
        for item in tmpPhotoData:
            self.baseCityInfo.datePhotoDirs.append(item)

        logger.info("photo date:{} , sqlFilePath:{}".format(self.baseCityInfo.datePhotoDirs,self.baseCityInfo.dateStr))
        ### photos dirs end
    def deCodePhotoData(self):
        if len(self.unCompressObj.decodeVersion)  == 0 :
            return
        for item in  self.baseCityInfo.datePhotoDirs:
            rawDir = self.confSaveRules.getTmpPhotoPath(item)
            decodeDir = self.confSaveRules.getTmpPhotoDecodePath(item)
            convertCodeData(rawDir,decodeDir,self.unCompressObj.decodeVersion)
        pass

    def movePhotoData(self):

        isEncode = len(self.unCompressObj.decodeVersion)  > 0
        pathSrc = self.confSaveRules.getTmpPhotoBase(isEncode)+"/"
        pathDst = self.confSaveRules.getRootPhotoPath()+"/"

        logger.info("cp 照片:from:[{}]".format( pathSrc ) )
        logger.info("to:[{}]".format( pathDst )  )
        dir_util.copy_tree(pathSrc, pathDst)
        logger.info("##########图片更新完毕！##########################")

    def moveVideoData(self):
        pathSrc = self.confSaveRules.getTmpVideoBase()+ "/"
        pathDst = self.confSaveRules.getRootVideoPath() + "/"

        logger.info("更新视频:from:[{}]".format( pathSrc ) )
        logger.info("to:[{}]".format( pathDst )  )
        dir_util.copy_tree(pathSrc, pathDst)

        pass

class UnCompressItemWebExportWuPan(UnCompressItemWebExport):
    def __init__(self,filePath, normalConfPath,dbConfFile):
        super().__init__( filePath , normalConfPath, dbConfFile)
        self.fixNumber = "00"
        self.confSaveRules.basePathRename("emDataWuPan")
    def fixDBName(self):
        # todo 查询最新的 number
        # 否则 00 ;
        self.fixNumber = getNextWuPanNumber(self.ormSess,self.baseCityInfo.cityCode,self.baseCityInfo.dateStr,  self.packageName )
        self.DbName += "_"+self.fixNumber
        logger.info("fixName:{}".format(self.DbName))
        pass
    def genarateOrmRecordObj(self):
        val = None
        if self.callBackGenerateRecord is not None:
            val = self.callBackGenerateRecord(self.baseCityInfo.cityCode, self.baseCityInfo.deviceType, self.baseCityInfo.dateStr, self.DbName,
                               self.confSaveRules.getRootPhotoPath(),self.confSaveRules.getRootAlgConfPath(),os.path.basename(self.filePath),self.fixNumber)

        return val

