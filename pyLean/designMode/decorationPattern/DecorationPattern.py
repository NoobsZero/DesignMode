# -*- encoding:utf-8 -*-
"""
@File   :DecorationPattern.py
@Time   :2020/10/19 19:27
@Author :Chen
@Software:PyCharm
"""


class Data_test(object):
    day = 0
    month = 0
    year = 0

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Data_test, cls).__new__(cls)
        return cls.instance

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    # 在Date_test类里面创建一个成员函数， 前面用了@classmethod装饰。
    # 它的作用就是有点像静态类，比静态类不一样的就是它可以传进来一个当前类作为第一个参数.
    @classmethod
    def get_date(cls, data_as_string):
        # 这里第一个参数是cls， 表示调用当前的类名
        year, month, day = map(int, data_as_string.split('-'))
        date1 = cls(year, month, day)
        # 返回的是一个初始化后的类
        return date1

    def out_date(self):
        print("year :", self.year)
        print("month :", self.month)
        print("day :", self.day)


if __name__ == '__main__':
    data_as_string = '2020-10-20'
    year, month, day = map(int, data_as_string.split('-'))
    dt1 = Data_test(year, month, day)
    print('dt1:', id(dt1))
    dt1.out_date()
    dt2 = Data_test(2020, 12, 11)
    print('dt2:', id(dt2))
    dt2.out_date()
    print('dt1:', id(dt1))
    dt1.out_date()
    # gd = dt.get_date('2020-10-20')
    # print(id(gd))
    # gd.out_date()
