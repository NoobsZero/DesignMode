# encoding: utf-8
"""
@file: dateObject.py
@time: 2021/6/24 10:08
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
@introduce: 关于datetime.date常用方法介绍
"""
from datetime import date, timedelta

if __name__ == '__main__':
    # 1、date对象所能表示的最大最小日期，返回的是datetime.date类型的对象
    print(date.max, date.min)
    # 2、date.today() 函数：返回一个当前本地日期的date类型的对象
    print(date.today())
    # 3、日期时间加减
    print((date.today() + timedelta(days=10)).strftime("%Y_%m_%d"))
