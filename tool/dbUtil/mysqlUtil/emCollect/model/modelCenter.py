import json

from .modelDefine import MapperCityDataBaseName
from .modelBase import *
from ..common.baseDBOperate import DbConfigure
from sqlalchemy import orm
from ..common.baselog import  *

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
        #return orm.Query( self.sess.query(ormClazz) )
        return self.sess.query(ormClazz)
    def delete(self,ormClazz):
        pass

    def getSession(self):
        return self.sess

    def __del__(self):
        self.sess.close()
        pass


def insertMapperCityDataBaseName(sessOrm, mcObj,IsForce=True ):
    li= sessOrm.select(MapperCityDataBaseName).filter(MapperCityDataBaseName.generateDate == mcObj.generateDate,
                                                  MapperCityDataBaseName.cityCode == mcObj.cityCode,
                                                  MapperCityDataBaseName.deviceType == mcObj.deviceType).all()
    print( li)
    if len(li  )  > 0 :
        logger.error("记录已经存在")
        if  not IsForce :
            return False

        # TODO 删除记录
        logger.info("正在 删除已存在的记录")
        sessOrm.select(MapperCityDataBaseName).filter(MapperCityDataBaseName.generateDate == mcObj.generateDate,
                                                      MapperCityDataBaseName.cityCode == mcObj.cityCode,
                                                      MapperCityDataBaseName.deviceType == mcObj.deviceType).delete()
    #ToDO  插入记录
    if sessOrm.insert(mcObj):
        logger.info("路径映射信息已成功插入")



    return  True

def selectMapperCityDataBaseName(sessOrm  , cityName="",cityPinYin="",cityCode="",startTime="",deviceType=""):
    query =sessOrm.select(MapperCityDataBaseName)
    if len(cityCode) > 0:
        query=query.filter(MapperCityDataBaseName.cityCode==cityCode)
    if len(startTime) > 0:
        query=query.filter(MapperCityDataBaseName.generateDate >= startTime)
    if len(deviceType) > 0:
        query=query.filter(MapperCityDataBaseName.deviceType == deviceType)
    if len(cityPinYin) > 0:
        query=query.filter(MapperCityDataBaseName.cityPinYin.like( cityPinYin+"%") )
    if len(cityName) > 0 :
        query=query.filter(MapperCityDataBaseName.cityName.like(cityName+"%") )

    return query.limit(20).all()



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

if __name__ == '__main__':
    # mysql://root:em-data-9527@192.168.20.115:3306/dongguan_test?charset=utf-8
    # mysql://root:em-data-9527@192.168.20.115:3306/dongguan_test?charset=utf8
    sess = OrmOperateDB('./conf/db.conf.json')
    #test_ormOperate(sess)

    val = selectMapperCityDataBaseName(sess,cityPinYin="dong")
    print("-------------------------------")
    for item in val:
        item.toString()


    #insertMapperCityDataBaseName(sess, saveItem)

    # sess.add(saveItem)
    # sess.commit()
    # sess.close()
