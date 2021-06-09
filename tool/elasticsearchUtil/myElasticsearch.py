# encoding: utf-8
"""
@file: myElasticsearch.py
@time: 2021/3/15 11:39
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import json
import time
from datetime import datetime
import pandas as pd

from es_pandas import es_pandas
import pandas
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from sqlalchemy import create_engine

from tool.mydbUtil.common.baseDBOperate import OperateDB


def mysql_connection_text():
    maxconnections = 15  # 最大连接数
    user = 'root'
    password = 'root'
    host = '192.168.41.69'
    port = 3306
    base = 'test'
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}:{port}/{base}',
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=maxconnections,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1,  # 多久之后对线程池中的线程进行一次连接的回收(重置)
        pool_pre_ping=True
    )
    # SessionFactory = sessionmaker(bind=engine)
    return engine


def mysql_connection_em():
    maxconnections = 15  # 最大连接数
    user = 'root'
    password = 'EmDataMysql2020###'
    host = '192.168.50.100'
    port = 3306
    base = 'em_vehicle'
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}:{port}/{base}',
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=maxconnections,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1,  # 多久之后对线程池中的线程进行一次连接的回收(重置)
        pool_pre_ping=True
    )
    # SessionFactory = sessionmaker(bind=engine)
    return engine


class ElasticSearch:
    def __init__(self, hosts, port):
        self.es = Elasticsearch(hosts=hosts, port=port)

    def es_create(self, index, mappings):
        return self.es.indices.create(index=index, body=mappings, ignore=400)

    def es_delete(self, index):
        return self.es.indices.delete(index=index, ignore=[400, 404])

    def es_get_indices(self, index):
        # es.indices.get_alias("*")
        return self.es.indices.get_alias(index)

    def es_del_indices(self, index):
        return self.es.indices.delete(index)

    def es_query_by_page(self, index_name, page_count=50, page_num=1):
        from_page = int(page_count) * (int(page_num) - 1)
        return self.es.search(index=index_name, size=int(page_count), from_=from_page)

    def es_search(self, index, body, doc_type='_doc'):
        search = {
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"id": "4643"}},
                        {"term": {"infos.category": "0167"}},
                    ]
                }
            }
        }
        # result = es.get_source(index='cj_anshun', id='4643', _source=["infos.category", "infos.name"])
        return self.es.search(index='cj_*', doc_type='_doc', body=search)
        # # # _search
        # results = result['hits']['hits']  # es查询出的结果第一页
        # total = result['hits']['total']  # es查询出的结果总量
        # scroll_id = result['_scroll_id']  # 游标用于输出es查询出的所有结果
        # print(results)
        # print(total)
        # print(scroll_id)
        # print(json.dumps(result, indent=2, ensure_ascii=False))


def sqlToDf(sql):
    # 显示所有列
    # pandas.set_option('display.max_columns', None)
    # 显示所有行
    # pandas.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    # pandas.set_option('max_colwidth', 100)
    engine = mysql_connection_em()
    pd = pandas.read_sql_query(sql, engine)
    return pd


def es_index():
    dbHandle = OperateDB(r'G:\JetBrains\PycharmProjects\untitled\source\mydb.conf.json')
    # result = dbHandle.select('show tables')
    # for db in [list(i)[0] for i in result]:
    # result = es.indices.create(index=db, ignore=400)
    db = "check_infos"
    datas_list = dbHandle.select('select * from %s;' % db)
    comments_list = dbHandle.select("select COLUMN_NAME, column_comment from INFORMATION_SCHEMA.Columns where "
                                    "table_name='%s';" % db)
    actions = [{
        "_index": "chejian",
        "_type": "_doc",
        "_source":
            dict(zip([list(i)[0] for i in comments_list], data))} for data in [list(i) for i in datas_list]]
    helpers.bulk(es, actions)


def test():
    # Information of es cluseter
    es_host = '192.168.90.10:9200'
    index = 'chejian'
    # crete es_pandas instance
    ep = es_pandas(es_host)

    # Example data frame
    db = "check_infos"
    df = sqlToDf(
        "SELECT cj.id, riqi.data_at as riqi, hpzl.name as hpzl, hphm, syr,cllx.name as cllx, csys.name as csys,clyt.name as clyt,fdjxh,zzcmc.name as zzcmc,check_created_at, GROUP_CONCAT(infos.category separator '&') as category, GROUP_CONCAT(infos.name separator '&') as name FROM em_vehicle.cj_anshun_checks cj join (SELECT id, data_at FROM em_vehicle.cj_riqis) as riqi join (SELECT id,name FROM em_vehicle.cj_hpzls) as hpzl join (SELECT id,name FROM em_vehicle.cj_cllxes) as cllx join (SELECT id,name FROM em_vehicle.cj_csies) as csys join (SELECT id,name FROM em_vehicle.cj_clyts) as clyt join (SELECT id,name FROM em_vehicle.cj_zzcmcs) as zzcmc join (SELECT vehicle_check_id,category.category,name FROM em_vehicle.cj_anshun_infos join (SELECT id, category FROM em_vehicle.cj_codes) as category on em_vehicle.cj_anshun_infos.category_id=category.id) as infos on riqi.id=cj.riqi_id and hpzl.id=cj.hpzl_id and cllx.id=cj.cllx_id and csys.id=cj.csys_id and clyt.id=cj.clyt_id and zzcmc.id=cj.zzcmc_id and cj.id=4642 group by cj.id;")
    # # init template if you want
    doc_type = '_doc'
    df.loc[:, 'name'] = df['name'].apply(lambda x: len(x.split('&')))
    df.loc[:, 'category'] = df['category'].apply(lambda x: x.split('&'))
    print(df['name'])
    # ep.init_es_tmpl(df, doc_type)
    #
    # # Example of write data to es, use the template you create
    # ep.to_es(df, index, doc_type=doc_type, thread_count=2, chunk_size=10000)
    #
    # # set use_index=True if you want to use DataFrame index as records' _id
    # ep.to_es(df, index, doc_type=doc_type, use_index=True, thread_count=2, chunk_size=10000)
    #
    # # delete records from es
    # ep.to_es(df.iloc[5000:], index, doc_type=doc_type, _op_type='delete', thread_count=2, chunk_size=10000)
    #
    # # Update doc by doc _id
    # df.iloc[:1000, 1] = 'Bye'
    # df.iloc[:1000, 2] = pd.datetime.now()
    # ep.to_es(df.iloc[:1000, 1:], index, doc_type=doc_type, _op_type='update')
    #
    # # Example of read data from es
    # df = ep.to_pandas(index)
    # print(df.head())
    #
    # # return certain fields in es
    # heads = ['Num', 'Date']
    # df = ep.to_pandas(index, heads=heads)
    # print(df.head())
    #
    # # set certain columns dtype
    # dtype = {'Num': 'float', 'Alpha': object}
    # df = ep.to_pandas(index, dtype=dtype)
    # print(df.dtypes)
    #
    # # infer dtype from es template
    # df = ep.to_pandas(index, infer_dtype=True)
    # print(df.dtypes)
    #
    # # Example of write data to es with pandas.io.json
    # ep.to_es(df, index, doc_type=doc_type, use_pandas_json=True, thread_count=2, chunk_size=10000)
    print('write es doc with pandas.io.json finished')


# def es_index():
#     dbHandle = OperateDB(r'G:\JetBrains\PycharmProjects\untitled\source\db.conf.json')
#     result = dbHandle.select('show tables')
#     # datas_list = dbHandle.select(
#     #     "SELECT cj.id, riqi.data_at as riqi, hpzl.name as hpzl, hphm, syr,cllx.name as cllx, csys.name as csys,"
#     #     "clyt.name as clyt,fdjxh,zzcmc.name as zzcmc,check_created_at FROM em_vehicle.cj_anshun_checks cj join ("
#     #     "SELECT id, data_at FROM em_vehicle.cj_riqis) as riqi join (SELECT id,name FROM em_vehicle.cj_hpzls) as hpzl "
#     #     "join (SELECT id,name FROM em_vehicle.cj_cllxes) as cllx join (SELECT id,name FROM em_vehicle.cj_csies) as "
#     #     "csys join (SELECT id,name FROM em_vehicle.cj_clyts) as clyt join (SELECT id,name FROM em_vehicle.cj_zzcmcs) "
#     #     "as zzcmc on riqi.id=cj.riqi_id and hpzl.id=cj.hpzl_id and cllx.id=cj.cllx_id and csys.id=cj.csys_id and "
#     #     "clyt.id=cj.clyt_id and zzcmc.id=cj.zzcmc_id limit 5;"
#     # )
#     datas_list = dbHandle.select(
#         "SELECT cj.id, hpzl.name as hpzl FROM em_vehicle.cj_anshun_checks cj join ("
#         "SELECT id, data_at FROM em_vehicle.cj_riqis) as riqi join (SELECT id,name FROM em_vehicle.cj_hpzls) as hpzl "
#         "join (SELECT id,name FROM em_vehicle.cj_cllxes) as cllx join (SELECT id,name FROM em_vehicle.cj_csies) as "
#         "csys join (SELECT id,name FROM em_vehicle.cj_clyts) as clyt join (SELECT id,name FROM em_vehicle.cj_zzcmcs) "
#         "as zzcmc on riqi.id=cj.riqi_id and hpzl.id=cj.hpzl_id and cllx.id=cj.cllx_id and csys.id=cj.csys_id and "
#         "clyt.id=cj.clyt_id and zzcmc.id=cj.zzcmc_id limit 5;"
#     )
#     comments_list = ['id', 'hpzl']
#     # comments_list = ['id', 'riqi', 'hpzl', 'hphm', 'syr', 'cllx', 'csys', 'clyt', 'fdjxh', 'zzcmc', 'check_created_at',
#     #                  'infos']
#     # for db in [list(i)[0] for i in result]:
#     # result = es.indices.create(index=db, ignore=400)
#     # print(result)
#     # datas_list = dbHandle.select('select * from %s;' % db)
#     # comments_list = dbHandle.select("select COLUMN_NAME, column_comment from INFORMATION_SCHEMA.Columns where "
#     #                                 "table_name='%s';" % db)
#     # info = [dict(zip(comments_list, data)) for data in [list(i) for i in datas_list]]
#     # names_list = ['category', 'name']
#     # infos_list = dbHandle.select(
#     #     f"SELECT category.category,name FROM em_vehicle.cj_anshun_infos join (SELECT id, category FROM em_vehicle.cj_codes) as category on em_vehicle.cj_anshun_infos.category_id=category.id and vehicle_check_id='{info[0]['id']}';")
#     # infos = [dict(zip(names_list, data)) for data in [list(i) for i in infos_list]]
#     # info[0]['infos'] = infos
#     actions = [{
#         "_index": "chejian",
#         "_type": "_doc",
#         "_source": dict(zip(comments_list, data))} for data in [list(i) for i in datas_list]]
#     # print(zip(str(info[0]['category']), str(info[0]['name'])))
#     helpers.bulk(es, actions)
#     return actions


if __name__ == '__main__':
    es = Elasticsearch(hosts='192.168.50.100', port='2999')
    es.cat.segments().create(index='cj_anshun', params=['chejian'])
    # print(es_create(es))
    # result = es_search(es)
    # es.get_source(index='chejian', id='4643')
    # print(es_delete(es, 'chejian'))
    # 删除索引
    # es_create(es)
