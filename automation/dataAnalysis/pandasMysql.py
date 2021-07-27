# encoding: utf-8
"""
@file: pandasMysql.py
@time: 2021/6/28 11:36
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from tool.dirUtil.getDirUtil import project_root_path
from tool.mydbUtil.common.baseDBOperate import OperateDB


def sqlToDf(sql):
    # 显示所有列
    # pandas.set_option('display.max_columns', None)
    # 显示所有行
    # pandas.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    # pandas.set_option('max_colwidth', 100)
    engine = OperateDB(os.path.join(project_root_path(), 'source', 'mydb.conf.json')).engine_connection()
    return pd.read_sql_query(sql, engine)


if __name__ == '__main__':
    huangye_pd = sqlToDf('select * from mysql_test.huangye')
    # print(huangye_pd.head())
    huangye_pd.loc[:, 'time'] = huangye_pd['time'].apply(lambda x: str(x).split('-')[0])
    year_counts = huangye_pd['time'].value_counts().to_frame().reset_index()
    year_counts.columns = ['time', 'count']
    year_counts.sort_index().plot(kind='bar')
    fig = plt.figure(num=1, figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.set_xticklabels(year_counts['time'].tolist(), fontproperties="SimHei", fontsize=12)
    plt.show()
