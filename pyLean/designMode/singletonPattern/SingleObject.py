# -*- encoding:utf-8 -*-
"""
@File   :SingleObject.py
@Time   :2020/10/12 15:29
@Author :Chen
@Software:PyCharm
"""


class SingleObject(object):
    """
    单例模式
    由于Python语言中并没有构造函数私有化的手段，所以要使用另外的策略。
    Python语言在构造新对象时要先调用__new__方法取得内存空间，然后调用__init__方法初始化该空间。
    因此，在Python语言中为保证只生成一个实例，实现单例的方式就是重写__new__方法，通过这种方式实现的单例类Singleton。
    """

    # Python中 _ 和 __ 的含义
    # 在python的类中，没有真正的私有化，不管是方法还是属性，
    # 为了编程的需要，约定加了下划线 _ 的属性和方法不属于API，不应该在类的外面访问，也不会被from M import * 导入。

    # _*:类的私有属性或方法：不建议在类的外面直接调用这个属性或方法，但是也可以调用
    # __*:python中的__和一项称为name mangling的技术有关，name mangling (又叫name decoration命名修饰).
    # 在很多现代编程语言中,这一技术用来解决需要唯一名称而引起的问题,比如命名冲突/重载等.
    __instance = None
    _data = 0

    # 单例类Singleton通过重写静态__new__方法来实现实例生成过程的控制。用户无论构建多少次该类的对象都会返回同一个结果。
    def __new__(cls):
        print('__instance:', not cls.__instance, cls.__instance)
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.data = 1
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
