# encoding: utf-8
"""
@file: weifa_Mysql_name.py
@time: 2021/7/23 17:24
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import re
import shutil
from datetime import datetime

import pandas
from sqlalchemy import create_engine


def mysql_connection_text():
    maxconnections = 15  # 最大连接数
    user = 'root'
    password = 'root'
    host = '192.168.41.69'
    port = 3306
    base = 'mysql_test'
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


def sqlToDf(sql):
    # 显示所有列
    pandas.set_option('display.max_columns', None)
    # 显示所有行
    # pandas.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    # pandas.set_option('max_colwidth', 100)
    engine = mysql_connection_text()
    pd = pandas.read_sql_query(sql, engine)
    return pd


if __name__ == '__main__':
    weifa_pd = sqlToDf('SELECT uuid, hpzl, hphm, sbbh, wfsj, wfxw, zpstr1, zpstr2, zpstr3, zpstr4, zpstr5, zpstr6 FROM '
                       'mysql_test.ivvs_source_data;')
    weifa_tupian_lis = [i for i in list(weifa_pd) if 'zpstr' in i]
    weifa_tupian = weifa_pd[weifa_tupian_lis].stack().reset_index(level=1)
    weifa_tupian.columns = ['图片ID', '图片名称']
    weifa_tupian.dropna(axis=0, how='any', inplace=True)
    weifa_pd = weifa_pd.drop(weifa_tupian_lis, axis=1).join(weifa_tupian[weifa_tupian['图片名称'] != '']) \
        .rename(columns={'sbbh': '设备编号', 'hpzl': '车牌类型', 'hphm': '号牌号码', 'wfsj': '违法时间', 'wfxw': '违法类型代码'})
    weifa_pd['人工结果'] = 0
    weifa_pd.loc[:, '图片时间'] = weifa_pd['图片名称'].apply(
        lambda x: datetime.strptime(re.search(r'(\d{4}-\d{1,2}-\d{1,2})', x).group(), '%Y-%m-%d'))
    weifa_pd = weifa_pd[(weifa_pd['图片时间'] >= '2021-07-19') & (weifa_pd['图片时间'] <= '2021-07-21')]
    weifa_pd = weifa_pd.reindex(
        columns=['uuid', '设备编号', '号牌号码', '违法类型代码', '车牌类型', '违法时间', '人工结果', '图片ID', '图片名称']).astype(
        str)
    weifa_pd.loc[:, '违法时间'] = weifa_pd['违法时间'].apply(lambda x: re.sub(r'[: ]', '#', x))
    weifa_pd.loc[:, '人工结果'] = weifa_pd['人工结果'].apply(
        lambda x: str(x.replace('nan', '0').replace('不违法', '2').replace('未违法', '2').replace('违法', '1')))
    weifa_pd.loc[:, '图片ID'] = weifa_pd['图片ID'].apply(lambda x: 'a' + str(re.sub(r'\D', '', x)))
    weifa_pd.loc[:, '新图片名称'] = weifa_pd['违法类型代码'] + '\\' + weifa_pd['设备编号'] + '\\' + weifa_pd['设备编号'] + '+' + weifa_pd[
        '号牌号码'] + '+' + weifa_pd['违法类型代码'] + '+' + weifa_pd['设备编号'] + '+' + weifa_pd['车牌类型'] + '+0+@' + weifa_pd[
                                   'uuid'] + '@@@' + weifa_pd['违法时间'] + '+' + weifa_pd['图片ID'] + '+' + weifa_pd[
                                   '人工结果'] + '.jpg'
    weifa_pd.loc[:, '新图片名称'] = weifa_pd['新图片名称'].apply(lambda x: x.replace('nan', ''))
    weifa_pd = weifa_pd.reindex(columns=['图片名称', '新图片名称'])
    weifa_pd.loc[:, '图片名称'] = weifa_pd['图片名称'].apply(lambda x: os.path.split(x)[-1])
    weifa_pd_index_lis = weifa_pd.index.tolist()
    for i in [i for i in weifa_pd_index_lis if weifa_pd_index_lis.count(i) < 2]:
        weifa_pd.loc[i, '新图片名称'] = weifa_pd.loc[i, '新图片名称'].replace('a', 'a0').replace('a1', 'a0')
    weifa_pd_dic = weifa_pd.set_index("图片名称").to_dict()["新图片名称"]
    file_dir = r'C:\Users\afakerchen\Desktop\0722-张家口\violation'
    fileCont = 0
    newFileCont = 0
    for home, dirs, files in os.walk(file_dir, topdown=True):
        for filename in files:
            fileCont += 1
            try:
                file_name_old = os.path.join(home, filename)
                file_name_new = os.path.join(r'C:\Users\afakerchen\Desktop\0722-张家口\0722', weifa_pd_dic[filename])
                if not os.path.isdir(os.path.dirname(file_name_new)):
                    os.makedirs(os.path.dirname(file_name_new))
                shutil.copyfile(file_name_old, file_name_new)
                newFileCont += 1
            except Exception as e:
                continue
    print('图片总数：', fileCont)
    print('修改图片：', newFileCont)
