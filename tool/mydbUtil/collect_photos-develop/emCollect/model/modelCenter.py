import json

from .modelDefine import MapperCityDataBaseName
from .modelDefine import MapperCityDataBaseNameWuPan
from .modelBase import *
from ..common.baseDBOperate import DbConfigure
from sqlalchemy import *
from sqlalchemy.orm import Query
from ..common.baselog import *


class OrmOperateDB:
    def __init__(self, configPath):
        self.dbConf = DbConfigure(configPath)
        url = self.getMysqlUrl()
        print("url:", url)
        try:
            self.sess = initOrmHandle(url)
        except Exception as e:
            print("orm 数据库连接失败")
            print("异常信息", e)

    def getMysqlUrl(self):
        return "mysql://{}:{}@{}:{}/{}?charset=utf8".format(self.dbConf.user, self.dbConf.passwd, self.dbConf.host,
                                                            self.dbConf.port, self.dbConf.db)

    def insert(self, ormObj):
        try:
            self.sess.add(ormObj)
            self.sess.commit()
        except Exception as ex:
            logger.error(ex)
            return False
        return True

    def select(self, ormClazz):
        # orm.Query().filter()
        # return orm.Query( self.sess.query(ormClazz) )
        return self.sess.query(ormClazz)

    def delete(self, ormClazz):
        pass

    def getSession(self):
        return self.sess

    def __del__(self):
        self.sess.close()
        pass


def insertMapperCityDataBaseName(sessOrm, mcObj, IsForce=True):
    li = sessOrm.select(MapperCityDataBaseName).filter(MapperCityDataBaseName.generateDate == mcObj.generateDate,
                                                       MapperCityDataBaseName.cityCode == mcObj.cityCode,
                                                       MapperCityDataBaseName.deviceType == mcObj.deviceType).all()
    print(li)
    if len(li) > 0:
        logger.error("记录已经存在")
        if not IsForce:
            return False

        # TODO 删除记录
        logger.info("正在 删除已存在的记录")
        sessOrm.select(MapperCityDataBaseName).filter(MapperCityDataBaseName.generateDate == mcObj.generateDate,
                                                      MapperCityDataBaseName.cityCode == mcObj.cityCode,
                                                      MapperCityDataBaseName.deviceType == mcObj.deviceType).delete()
    # ToDO  插入记录
    if sessOrm.insert(mcObj):
        logger.info("路径映射信息已成功插入")

    return True


def insertMapperCityDataBaseNameWuPan(sessOrm, mcObj, IsForce=True):
    li = sessOrm.select(MapperCityDataBaseNameWuPan).filter(
        MapperCityDataBaseNameWuPan.generateDate == mcObj.generateDate,
        MapperCityDataBaseNameWuPan.cityCode == mcObj.cityCode,
        MapperCityDataBaseNameWuPan.deviceType == mcObj.deviceType,
        MapperCityDataBaseNameWuPan.packageName == mcObj.packageName).all()
    print(li)
    if len(li) > 0:
        logger.error("记录已经存在")
        if not IsForce:
            return False

        # TODO 删除记录
        logger.info("正在 删除已存在的记录")
        sessOrm.select(MapperCityDataBaseNameWuPan).filter(
            MapperCityDataBaseNameWuPan.generateDate == mcObj.generateDate,
            MapperCityDataBaseNameWuPan.cityCode == mcObj.cityCode,
            MapperCityDataBaseNameWuPan.deviceType == mcObj.deviceType,
            MapperCityDataBaseNameWuPan.packageName == mcObj.packageName).delete()
    # ToDO  插入记录
    if sessOrm.insert(mcObj):
        logger.info("路径映射信息已成功插入")

    return True


def selectMapperCityDataBaseName(sessOrm, cityName="", cityPinYin="", cityCode="", startTime="", deviceType=""):
    query = sessOrm.select(MapperCityDataBaseName)
    if len(cityCode) > 0:
        query = query.filter(MapperCityDataBaseName.cityCode == cityCode)
    if len(startTime) > 0:
        query = query.filter(MapperCityDataBaseName.generateDate >= startTime)
    if len(deviceType) > 0:
        query = query.filter(MapperCityDataBaseName.deviceType == deviceType)
    if len(cityPinYin) > 0:
        query = query.filter(MapperCityDataBaseName.cityPinYin.like(cityPinYin + "%"))
    if len(cityName) > 0:
        query = query.filter(MapperCityDataBaseName.cityName.like(cityName + "%"))

    return query.limit(20).all()


def selectMapperCityDataBaseNameWuPan(sessOrm, cityCode="", generateDate="", packageName=""):
    query = sessOrm.select(MapperCityDataBaseNameWuPan)
    if len(cityCode) > 0:
        query = query.filter(MapperCityDataBaseNameWuPan.cityCode == cityCode)
    if len(generateDate) > 0:
        query = query.filter(MapperCityDataBaseNameWuPan.generateDate == generateDate)
    if len(packageName):
        query = query.filter(MapperCityDataBaseNameWuPan.packageName == packageName)

    objlist = query.order_by(desc(MapperCityDataBaseNameWuPan.number)).limit(1).all()

    # for item in objlist:
    #     print("@@@:{}",item.number)

    if len(objlist) > 0:
        print("#####################################:" + objlist[0].number)
        return True, objlist[0].number
    else:
        return False, ""
        # print(objlist[0]["number"])

    ######str(int("14") + 1)


def getNextWuPanNumber(sessOrm, cityCode, generateDate, packageName):
    isOk, num = selectMapperCityDataBaseNameWuPan(sessOrm, cityCode, generateDate, packageName)
    if isOk:  # 改包已经导过  本次是覆盖操作
        logger.warn("包已经导过, num is:{} ".format(num))
        return num

    isOk, num = selectMapperCityDataBaseNameWuPan(sessOrm, cityCode, generateDate, "")
    if isOk:
        return "{:0>2d}".format(int(num) + 1)
    return "00"


def test_ormOperate(sess):
    saveItem = MapperCityDataBaseName(mid=0, index="00",
                                      generateDate="2020-10-10",
                                      cityName="上海", cityCode="3201", cityPinYin="nanjing").generateDbName(
        "chejian")

    # sess.insert(saveItem)
    objlist = sess.select(MapperCityDataBaseName).filter(MapperCityDataBaseName.cityCode == "3201"). \
        filter(MapperCityDataBaseName.generateDate == "2020-10-10").limit(1).from_self()

    # sess.select(MapperCityDataBaseName).
    for item in objlist:
        print(item.toString())


def test_wupan(sess):
    # isOk, num = selectMapperCityDataBaseNameWuPan(sess, cityCode="4419", generateDate="2020-07-20",
    #                      packageName="emData_chejian_4419_20210114140321_CJWP.tar.gz")
    # print("isok:", isOk, "num:", num)

    num = getNextWuPanNumber(sess, cityCode="4419", generateDate="2020-07-20",
                             packageName="emData_chejian_4419_20210114140321_CJWP.tar.gz")
    print("num:", num)

    num = getNextWuPanNumber(sess, cityCode="4419", generateDate="2020-07-20",
                             packageName="emData_chejian_4419_202101141240321_CJWP.tar.gz")
    print("num:", num)


if __name__ == '__main__':
    # mysql://root:em-data-9527@192.168.20.115:3306/dongguan_test?charset=utf-8
    # mysql://root:em-data-9527@192.168.20.115:3306/dongguan_test?charset=utf8
    sess = OrmOperateDB('./conf/db.conf.json')
    # test_ormOperate(sess)
    test_wupan(sess)
