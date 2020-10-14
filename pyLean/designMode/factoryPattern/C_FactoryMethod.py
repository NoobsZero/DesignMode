# -*- encoding:utf-8 -*-
"""
@File   :C_FactoryMethod.py
@Time   :2020/10/13 19:41
@Author :Chen
@Software:PyCharm
工厂模式
        顾名思义就是我们可以通过一个指定的“工厂”获得需要的“产品”，在设计模式中主要用于抽象对象的创建过程，
    让用户可以指定自己想要的对象而不必关心对象的实例化过程。
        这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象的实例，
    隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。
"""
import abc

from pyLean.designMode.factoryPattern.A_NoFactories import Mercedes, BMW

"""
    工厂方法
        虽然有了一个简单的工厂，但在实际使用工厂的过程中，我们会发现新问题：如果我们要新增一个“产品”，例如Audi的汽车，
    我们除了新增一个Audi类外还要修改SimpleCarFactory内的product_car方法。
        这样就违背了软件设计中的开闭原则[1]，即在扩展新的类时，尽量不要修改原有代码。
        所以我们在简单工厂的基础上把SimpleCarFactory抽象成不同的工厂，每个工厂对应生成自己的产品，这就是工厂方法。
"""


class AbstractFactory(object):
    """
        工厂方法
            工厂方法模式继承了简单工厂模式的优点又有所改进，其不再通过一个工厂类来负责所有产品的创建，
        而是将具体创建工作交给相应的子类去做，这使得工厂方法模式可以允许系统能够更高效的扩展。
            实际应用中可以用来实现系统的日志系统等，比如具体的程序运行日志，网络日志，数据库日志等都可以用具体的工厂类来创建。

    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass


class MercedesFactory(AbstractFactory):
    """ 梅赛德斯工厂
    """

    def product_car(self):
        return Mercedes()


class BMWFactory(AbstractFactory):
    """ 宝马工厂
    """

    def product_car(self):
        return BMW()

    """
        我们把工厂抽象出来用abc模块实现了一个抽象的基类AbstractFactory，这样就可以通过特定的工厂来获得特定的产品实例了：
    """


def factoryMethod():
    mb = MercedesFactory().product_car()
    bmw = BMWFactory().product_car()
    print('factoryMethod():\n\t{}\n\t{}'.format(['梅赛德斯：', mb], ['宝马：', bmw]))


"""
    每个工厂负责生产自己的产品也避免了我们在新增产品时需要修改工厂的代码，而只要增加相应的工厂即可。
    如新增一个Audi产品，只需新增一个Audi类和AudiFactory类。
"""
if __name__ == '__main__':
    factoryMethod()
