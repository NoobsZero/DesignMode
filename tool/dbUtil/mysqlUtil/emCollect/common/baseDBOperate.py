import os
import pymysql
from .baseConfig import BaseConfig
from .baselog import logger


class DbConfigure:
    def __init__(self, configPath):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root"
        self.passwd = "em-data-9527"
        self.db = "chejian_refactor"

        self.objMap = BaseConfig().loadConf(configPath).objMap
        self.InitFromConfigure(self.objMap)

    def getSource(self):
        return "mysql://{user}:{password}@{ipaddr}:{port}/{dbname}?charset=utf8". \
            format(user=self.user, password=self.passwd, ipaddr=self.host, port=self.port, dbname=self.db)

    def InitFromConfigure(self, dbconf):
        self.host = dbconf["dbHost"]
        self.port = int(dbconf["dbPort"])
        self.passwd = dbconf["dbPass"]
        self.user = dbconf["dbUser"]
        return True


class OperateDB:
    def __init__(self, configPath, isUsedDB=True, renameDb=""):
        self.dbconf = DbConfigure(configPath)
        if len(renameDb) > 0:
            self.dbconf.db = renameDb
        self.cursor = None
        self.dbhandle = None
        self.connect(self.dbconf, isUsedDB)

    @classmethod
    def InitByConfObj(cls, dbconf, isUsedDB=True):
        self = cls.__new__(cls)
        self.dbconf = dbconf
        self.connect(dbconf, isUsedDB)
        return self

    def connect(self, dbconf, isUsedDB):
        if isUsedDB:
            self.dbhandle = pymysql.connect(host=dbconf.host, port=dbconf.port, user=dbconf.user, passwd=dbconf.passwd,
                                            db=dbconf.db, charset='utf8')
        else:
            self.dbhandle = pymysql.connect(host=dbconf.host, port=dbconf.port, user=dbconf.user, passwd=dbconf.passwd,
                                            charset='utf8')
        # self.dbhandle = MySQLdb.connect("192.168.20.115", "root", "em-data-9527", "chejian_refactor", charset='utf8')
        self.cursor = self.dbhandle.cursor()

    def select(self, sqlstr):
        # print(sqlstr)
        try:
            self.cursor.execute(sqlstr)
        except Exception as e:
            logger.error("error： 查询操作出错")
            logger.error("error:[{}]".format(e))
            return ""
        return self.cursor.fetchall()

    def insert(self, sqlstr):
        try:
            self.cursor.execute(sqlstr)
            self.dbhandle.commit()
        except Exception as e:
            logger.error("error： 插入操作失败：[{}]".format(sqlstr))
            logger.error("error reason:{}".format(e))
            self.dbhandle.rollback()
            return False
        return True

    def impDBFile(self, filepath):

        sh = "mysql -h" + self.dbconf.host + " -P" + str(self.dbconf.port) + " -u" + self.dbconf.user + \
             " -p" + self.dbconf.passwd + " -B " + self.dbconf.db + "  < " + filepath
        print("command:", sh)
        return os.system(sh)

    def impDBFileList(self, fileList):
        for item in fileList:
            self.impDBFile(item)

    def __del__(self):
        self.dbhandle.close()
        pass


def createDataBase(configPath, dbname=""):
    try:
        odb = OperateDB(configPath, isUsedDB=False)
        if len(dbname) == 0:
            dbname = odb.dbconf.db
        val = odb.insert("create database IF NOT EXISTS " + dbname + " default charset utf8 collate utf8_general_ci ")
    except Exception as e:
        val = False
        logger.error("数据库创建失败:[{}]".format(dbname))
        logger.error("error:{}".format(e))
    print("创建数据库:", dbname)
    return val


def test_select():
    dbHandle = OperateDB("./conf/db.conf.json");
    result = dbHandle.select("select * from photo_info limit 1");
    print(result)


def test_create():
    createDataBase("./conf/db.conf.json", "cheajian_test_123")


if __name__ == '__main__':
    test_select()
