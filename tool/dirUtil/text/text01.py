# -*- encoding:utf-8 -*-
"""
@File   :text01.py
@Time   :2021/1/15 14:30
@Author :Chen
@Software:PyCharm
"""
# 导入pymysql模块
import datetime
import os
import random
import re
import shutil
import pymysql
import sys
from ast import literal_eval
import requests
from tomorrow import threads
from pymysql import ProgrammingError
from dateutil.parser import parse


def validate(date_text, type=None):
    """
        时间检验，注意文件时间要符合日期规则超出无效！
    :param type:
    :param date_text: 字符串
    :return: boolean
    """
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        re = True
    except ValueError:
        if type == 'zip':
            re = False
        else:
            try:
                datetime.datetime.strptime(date_text, '%Y%m%d')
                re = True
            except ValueError:
                re = False
    return re


def getDate(time_dst_dir):
    time_t1 = re.search(r'(\d{4}-\d{2}-\d{2})', time_dst_dir)
    time_t2 = re.search(r'(\d{4}\d{2}\d{2})', str(time_dst_dir))
    time_t3 = re.search(r'(\d{4}年\d{2}月\d{2}日)', str(time_dst_dir))
    if time_t1 and validate(time_t1.group(1)):
        return time_t1.group(1)
    elif time_t2 and validate(time_t2.group(1)):
        return parse(time_t2.group(1)).strftime('%Y-%m-%d')
    elif time_t3:
        return parse(re.sub(r'\D', "", time_t3.group(1))).strftime('%Y-%m-%d')
    else:
        return None


if __name__ == '__main__':
    # print(getDate('西宁车管所_所有照片_2019年6月5日'))
    li_1 = '/empool/vehicle_data/chejian_raw/work/rawdata/chejian/南昌/yasuo/20210309/11.南昌车管所车检/zip/2019.05.17/150(从)/2019-05-17.tar.gz'
    li_2 = '/empool/vehicle_data/chejian_raw/work/rawdata/chejian/南昌/yasuo/20210309/11.南昌车管所车检/zip/2019.05.17/150(从)/2019_05_17.tar.gz'
    print(li_1 != li_2)