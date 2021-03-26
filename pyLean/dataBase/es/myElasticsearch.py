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
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from tool.mydbUtil.common.baseDBOperate import OperateDB


def es_create(es):
    # 创建index
    mappings = {
        "template": "chejian",
        "mappings": {
            "_doc": {
                "properties": {
                    "id": {
                        "type": "text"
                    },
                    "riqi": {
                        "type": "text"
                    },
                    "hpzl": {
                        "type": "text"
                    },
                    "hphm": {
                        "type": "text"
                    },
                    "syr": {
                        "type": "text"
                    },
                    "cllx": {
                        "type": "text"
                    },
                    "csys": {
                        "type": "text"
                    },
                    "clyt": {
                        "type": "text"
                    },
                    "fdjxh": {
                        "type": "text"
                    },
                    "zzcmc": {
                        "type": "text"
                    },
                    "check_created_at": {
                        "type": "text"
                    },
                    "infos": {
                        "type": "nested",
                        "properties": {
                            "category_id": {
                                "type": "text"
                            },
                            "name": {
                                "type": "text"
                            }
                        }
                    }
                }
            }
        }
    }
    result = es.indices.create(index='chejian', body=mappings, ignore=400)
    return result


def es_delete(es, index):
    # 删除index
    result = es.indices.delete(index=index, ignore=[400, 404])
    return result


def es_index():
    dbHandle = OperateDB(r'G:\JetBrains\PycharmProjects\untitled\source\db.conf.json')
    result = dbHandle.select('show tables')
    datas_list = dbHandle.select(
        "SELECT cj.id, riqi.data_at as riqi, hpzl.name as hpzl, hphm, syr,cllx.name as cllx, csys.name as csys,clyt.name as clyt,fdjxh,zzcmc.name as zzcmc,check_created_at, GROUP_CONCAT(infos.category) as category, GROUP_CONCAT(infos.name) as name FROM cj_anshun_checks cj join (SELECT id, data_at FROM cj_riqis) as riqi join (SELECT id,name FROM cj_hpzls) as hpzl join (SELECT id,name FROM cj_cllxes) as cllx join (SELECT id,name FROM cj_csies) as csys join (SELECT id,name FROM cj_clyts) as clyt join (SELECT id,name FROM cj_zzcmcs) as zzcmc join (SELECT vehicle_check_id,category.category,name FROM cj_anshun_infos join (SELECT id, category FROM cj_codes) as category on cj_anshun_infos.category_id=category.id) as infos on riqi.id=cj.riqi_id and hpzl.id=cj.hpzl_id and cllx.id=cj.cllx_id and csys.id=cj.csys_id and clyt.id=cj.clyt_id and zzcmc.id=cj.zzcmc_id and infos.vehicle_check_id=cj.id group by cj.id limit 1;")
    comments_list = ['id', 'riqi', 'hpzl', 'hphm', 'syr', 'cllx', 'csys', 'clyt', 'fdjxh', 'zzcmc', 'check_created_at',
                     'infos', 'category', 'name']
    # for db in [list(i)[0] for i in result]:
    # result = es.indices.create(index=db, ignore=400)
    # print(result)
    # datas_list = dbHandle.select('select * from %s;' % db)
    # comments_list = dbHandle.select("select COLUMN_NAME, column_comment from INFORMATION_SCHEMA.Columns where "
    #                                 "table_name='%s';" % db)
    # actions = [{
    #     "_index": "chejian",
    #     "_type": "_doc",
    #     "_source":
    #         dict(zip(comments_list, data))
    # } for data in [list(i) for i in datas_list]]
    info = [dict(zip(comments_list, data)) for data in [list(i) for i in datas_list]]
    return info
    # print(zip(str(info[0]['category']), str(info[0]['name'])))
    # helpers.bulk(es, actions)


def es_search(es):
    # dsl = {
    #     'query': {
    #         'match': {
    #             'reason': '1'
    #         }
    #     }
    # }
    result = es.search(index='check_infos', body={'query': {'match_all': {}}}, scroll='5m', size=5000)
    return result
    # # # _search
    # results = result['hits']['hits']  # es查询出的结果第一页
    # total = result['hits']['total']  # es查询出的结果总量
    # scroll_id = result['_scroll_id']  # 游标用于输出es查询出的所有结果
    # print(results)
    # print(total)
    # print(scroll_id)
    # print(json.dumps(result, indent=2, ensure_ascii=False))


def query_data_by_page(es, index_name, page_count=50, page_num=1):
    """
        分页查询
    Args:
        es:
        index_name:
        page_count:
        page_num:

    Returns:

    """
    from_page = int(page_count) * (int(page_num) - 1)
    data_array = es.search(index=index_name, size=int(page_count), from_=from_page)
    return data_array


if __name__ == '__main__':
    es = Elasticsearch(hosts='192.168.90.10')
    # result = es.search(index='chejian', body={'query': {'match_all': {}}})
    # print(result)
    # start = time.time()
    info = es_index()
    infosLis = info[0]['infos'].split(',')
    categoryLis = info[0]['category'].split(',')
    print(len(infosLis))
    print(len(categoryLis))
    # for info, category in infosLis, categoryLis:
    #     print({"name": info, "category": category})
    # end = time.time()
    # print(end - start)
    # print(es_delete(es, 'chejian'))
