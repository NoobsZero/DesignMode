# -*- encoding:utf-8 -*-
"""
@File   :SingleObject.py
@Time   :2020/10/12 15:29
@Author :Chen
@Software:PyCharm
"""


class SingleObject(object):
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(SingleObject, cls).__new__(cls)
            cls.__instance.data = 0
        return cls.__instance

    def __init__(self):
        print('Singleton.__init__(),id=', id(self))

    def set_value(self, data):
        print('set data to', data)
        self.data = data

    def get_data(self):
        return self.data

    def __str__(self):
        return 'id={},data={}'.format(id(self), self.data)


if __name__ == '__main__':
    s1 = SingleObject()
    print(s1)
    s2 = SingleObject()
    print(s2)
    s2.set_value(10)
    print(s2.get_data())
    print(s1.get_data())
    s1.set_value(20)
    print(s2.get_data())
    print(s1.get_data())
