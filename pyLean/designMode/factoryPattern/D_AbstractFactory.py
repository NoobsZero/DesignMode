# -*- encoding:utf-8 -*-
"""
@File   :D_AbstractFactory.py
@Time   :2020/10/13 19:48
@Author :Chen
@Software:PyCharm
工厂模式
        顾名思义就是我们可以通过一个指定的“工厂”获得需要的“产品”，在设计模式中主要用于抽象对象的创建过程，
    让用户可以指定自己想要的对象而不必关心对象的实例化过程。
        这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象的实例，
    隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。
"""

import abc

# 两种小汽车

from abc import ABC


class Mercedes_C63(object):
    """梅赛德斯 C63
    """

    def __repr__(self):
        return "Mercedes-Benz: C63"


class BMW_M3(object):
    """宝马 M3
    """

    def __repr__(self):
        return "BMW: M3"


# 　两种SUV
class Mercedes_G63(object):
    """梅赛德斯 G63
    """

    def __repr__(self):
        return "Mercedes-Benz: G63"


class BMW_X5(object):
    """宝马 X5
    """

    def __repr__(self):
        return "BMW: X5"


# 　两种颜色
class Colour_red(object):
    """白色
    """

    def __repr__(self):
        return "Colour: red"


class Colour_black(object):
    """黑色
    """

    def __repr__(self):
        return "Colour: black"


"""
    抽象工厂
        工厂方法虽然解决了我们“修改代码”的问题，但如果我们要生产很多产品，就会发现我们同样需要写很多对应的工厂类。
        比如如果MercedesFactory和BMWFactory不仅生产小汽车，还要生产SUV，那我们用工厂方法就要再多构造两个生产SUV的工厂类。
        所以为了解决这个问题，我们就要再更进一步的抽象工厂类，让一个工厂可以生产同一类的多个产品，这就是抽象工厂。具体实现如下：
"""


class AbstractFactory(object):
    """抽象工厂类
        用来定义工厂类的接口，在需要实现共通功能的时候定义即可，可以提高代码的复用性。
        可以生产小汽车外，还可以生产SUV
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass

    @abc.abstractmethod
    def product_suv(self):
        pass

    @abc.abstractmethod
    def product_colour(self):
        pass


class MercedesFactory(AbstractFactory, ABC):
    """梅赛德斯工厂
    """

    def product_car(self):
        return Mercedes_C63()

    def product_suv(self):
        return Mercedes_G63()

    def product_colour(self):
        return Colour_black()


class BMWFactory(AbstractFactory, ABC):
    """宝马工厂
    """

    def product_car(self):
        return BMW_M3()

    def product_suv(self):
        return BMW_X5()


"""
    我们让基类AbstractFactory同时可以生产汽车和SUV，
    然后令MercedesFactory和BMWFactory继承AbstractFactory并重写product_car和product_suv方法即可。
"""


def abstractFactory():
    c1 = MercedesFactory().product_car()
    s1 = MercedesFactory().product_suv()
    b1 = MercedesFactory().product_colour()
    s2 = BMWFactory().product_suv()
    c2 = BMWFactory().product_car()
    print('abstractFactory():\n\t{}\n\t{}'.format([c1, s1, b1], [c2, s2]))


"""
    抽象工厂模式与工厂方法模式最大的区别在于，抽象工厂中的一个工厂对象可以负责多个不同产品对象的创建 ，这样比工厂方法模式更为简单、有效率。
"""

if __name__ == '__main__':
    abstractFactory()
