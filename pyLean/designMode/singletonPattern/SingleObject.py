# -*- encoding:utf-8 -*-
"""
@File   :SingleObject.py
@Time   :2020/10/12 15:29
@Author :Chen
@Software:PyCharm
单例模式（Singleton）---创建型
一、单例模式的使用场景
    （1）、当创建一个对象所占用的资源很多，但同时又需要使用到该对象
    （2）、当堆系统内的资源要求统一读写时，比如读写的配置信息，此时必须要求创建的实例信息相同
    （3）、当有多个实例可能会引起程序错误时
    总结：单例模式适用于只需要创建一个实例对象，程序全部使用同一个实例对象
二、实现方法
    根据使用场景提炼出要点：
        （1）、某个类只能有一个实例
        （2）、必须要自行创建实例
        （3）、必须向整个系统提供这个实例
    实现方法：
        （1）、只提供私有的构造方法
        （2）、含有一个该类的静态私有对象
        （3）、要提供一个静态的公用方法用于获取、创建私有对象
    根据上面的描述，提供了俩种实现单例模式的方法分别为饿汉式和懒汉式
    饿汉式：简单来说就是空间换时间，因为上来就实例化一个对象，占用了内存，（也不管你用还是不用）
    懒汉式：简单的来说就是时间换空间，与饿汉式正好相反
"""


# 饿汉式

class EagerSingleton(object):
    """
        饿汉式单例模式
        实现预先加载，急切初始化，单例对象在类实例化前创建。
        优点：
            1、线程安全
            2、在类实例化前已经创建好了一个静态对象，调用时反应速度快
            3、直接执行其它方法或静态方法时，单例实例不会被初始化
        缺点：
            1、不管使用与否，实例化前就初始化静态对象，有点资源浪费。
    """
    # 重写创建实例的__new__方法
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 如果类没有实例属性，进行实例化，否则返回实例
        if not hasattr(cls, '_instance'):
            cls.instance = super(EagerSingleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls._instance


# 懒汉式


class LazySingleton(object):
    """
    懒汉式单例模式
    只有在使用时才创建单例对象，实例化时不创建。
    优点：
        1、资源利用合理，不调用get_instance方法不创建单例对象
    缺点：
        1、线程不安全，多线程时可能会获取到不同单例对象的情况。
        解决办法是加互斥锁，但会降低效率
    """
    __instance = None

    def __init__(self):
        if not self.__instance:
            print('调用__init__,实例未创建')
        else:
            print('调用__init__,实例已经创建过了：', self.__instance)

    @classmethod
    def get_instance(cls):
        # 调用get_instance类方法的时候才会生成Singleton实例
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

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
    # 单例类Singleton通过重写静态__new__方法来实现实例生成过程的控制。用户无论构建多少次该类的对象都会返回同一个结果。


if __name__ == '__main__':
    # s3 = LazySingleton()
    # s1 = LazySingleton.get_instance()
    # s2 = LazySingleton.get_instance()
    # print(id(s1), id(s2))

    c1 = EagerSingleton()
    c2 = EagerSingleton()
    print(id(c1), id(c2))
