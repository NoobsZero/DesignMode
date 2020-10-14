# -*- encoding:utf-8 -*-
"""
@File   :A_NoFactories.py
@Time   :2020/10/13 17:59
@Author :Chen
@Software:PyCharm
工厂模式
        顾名思义就是我们可以通过一个指定的“工厂”获得需要的“产品”，在设计模式中主要用于抽象对象的创建过程，
    让用户可以指定自己想要的对象而不必关心对象的实例化过程。
        这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象的实例，
    隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。
"""

"""
    简单工厂
        首先，我们先看一个简单的例子：
"""


class Mercedes(object):
    """ 梅赛德斯
    """

    def __repr__(self):
        return "Mercedes-Benz"


class BMW(object):
    """ 宝马
    """

    def __repr__(self):
        return "BMW"


"""
        假设我们有两个“产品”分别是Mercedes和BMW的汽车，如果没有“工厂”来生产它们，我们就要在代码中自己进行实例化，如：
"""


def noFactories():
    mer = Mercedes()
    bmw = BMW()
    print('noFactories():\n\t{}\n\t{}'.format(['梅赛德斯：', mer], ['宝马：', bmw]))


"""
        但现实中，你可能会面对很多汽车产品，而且每个产品的构造参数还不一样，这样在创建实例时会遇到麻烦。
        这时就可以构造一个“简单工厂”把所有汽车实例化的过程封装在里面。
"""


if __name__ == '__main__':
    # 有无()很重要，没有返回对象地址，有返回函数值
    noFactories()
