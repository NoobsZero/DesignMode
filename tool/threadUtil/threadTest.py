# -*- encoding:utf-8 -*-
"""
@File   :text01.py
@Time   :2021/1/15 14:30
@Author :Chen
@Software:PyCharm
"""
from multiprocessing import Pool

import pymysql
from dbutils.pooled_db import PooledDB

def mysql_connection():
    maxconnections = 15  # 最大连接数
    blocking = True
    pool = PooledDB(
        pymysql,
        maxconnections=maxconnections,
        blocking=blocking,
        host='192.168.50.100', user='root', password='EmDataMysql2020###',
        database='em_vehicle', charset='utf8',
        use_unicode=True)
    return pool.connection()


def f(x):
    return x*x

if __name__ == '__main__':
    conn = mysql_connection()
    cur = conn.cursor()
    SQL = "select * from cj_cities"
    r = cur.execute(SQL)
    r = cur.fetchall()
    print(r)
    cur.close()
    conn.close()
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))