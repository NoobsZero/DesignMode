# encoding: utf-8
"""
@file: comsql.py
@time: 2021/7/28 9:20
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import environ
from urllib.parse import quote


def initOrmHandle(mysqlURL):
    # 初始化数据库连接:
    engine = create_engine(mysqlURL, encoding='utf-8', future=True, echo=True)


def engine_connection():
    maxconnections = 15  # 最大连接数
    engine = create_engine(
        f'mysql+pymysql://root:root@192.168.41.69:3306/mysql_test',
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=maxconnections,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1,  # 多久之后对线程池中的线程进行一次连接的回收(重置)
        pool_pre_ping=True,
        future=True,
        echo=True
    )
    # SessionFactory = sessionmaker(bind=engine)
    return engine


if __name__ == '__main__':
    # session = sessionmaker(bind=engine_connection(), future=True)()
    # result = session.execute(text('select * from mysql_test.ivvs_source_data;'))
    # print(result.all())
    # with session as conn:
    #     result = conn.execute(text('select * from mysql_test.ivvs_source_data;'))
    #     print(result.all())

    db_connect_string = f'mysql+pymysql://{cfg.database_user}:{quote(cfg.database_password)}@{cfg.database_ip}:{cfg.database_port}/{cfg.database_name}'

