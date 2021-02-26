# -*- coding: UTF-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

# from zope.sqlalchemy import ZopeTransactionExtension
# from zope.sqlalchemy import register

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# 创建对象的基类:
Base = declarative_base()


# Alembic 和 SQLAlchemy-Migrate
# setattr(MapperCityDataBaseName, "cityPinYin", (Column("cityPinYin", String(32), comment="啥也不是")))

def initOrmHandle(mysqlUrl):
    # 初始化数据库连接:
    engine = create_engine(mysqlUrl, encoding='utf-8', echo=False)
    Base.metadata.create_all(engine)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    return DBSession()
