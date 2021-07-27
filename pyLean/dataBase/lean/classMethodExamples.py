# encoding: utf-8
"""
@file: classMethodExamples.py
@time: 2021/6/17 14:17
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""


class ClassMethodExamples(object):
    """ @classmethod简单例子 """
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    # @classmethod 修饰符对应的函数不需要实例化
    # 不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def get_date(cls, data_as_string):
        # 分解成 year，month，day 三个变量，然后转成int
        year, month, day = map(int, data_as_string.split('-'))
        # 这里第一个参数是cls， 表示调用当前的类名
        # 返回的是一个初始化后的类
        # cls(year,month,day)相当于Data_test2(year,month,day)
        date1 = cls(year, month, day)
        return date1

    def out_date(self):
        print("year :", self.year)
        print("month :", self.month)
        print("day :", self.day)


if __name__ == '__main__':
    # 这样子等于先调用get_date（）对字符串进行出来，然后才使用Data_test的构造函数初始化
    ClassMethodExamples.get_date('2018-01-17').out_date()
