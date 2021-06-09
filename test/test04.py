# -*- codeing = utf-8 -*-
# @Time :2020/8/5 16:49
# @Author:Eric
# @File : test04.py
# @Software: PyCharm

# 懒汉式


class Singleton(object):
    __instance = None

    def __init__(self):
        if not self.__instance:
            self.start = ""
            print('调用__init__， 实例未创建')
        else:
            print('调用__init__，实例已经创建过了:', self.__instance)

    @classmethod
    def get_instance(cls):
        # 调用get_instance类方法的时候才会生成Singleton实例
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

    def setStart(self, start_time):
        self.start = start_time


if __name__ == '__main__':
    print(Singleton.get_instance().start)
    print(Singleton.get_instance().setStart('123'))
    print(Singleton.get_instance().start)
    print(Singleton.get_instance().start)
    print(Singleton.get_instance().start)

