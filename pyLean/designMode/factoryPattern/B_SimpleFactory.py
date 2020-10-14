# -*- encoding:utf-8 -*-
"""
@File   :B_SimpleFactory.py
@Time   :2020/10/13 19:33
@Author :Chen
@Software:PyCharm
工厂模式
        顾名思义就是我们可以通过一个指定的“工厂”获得需要的“产品”，在设计模式中主要用于抽象对象的创建过程，
    让用户可以指定自己想要的对象而不必关心对象的实例化过程。
        这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象的实例，
    隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。
"""
from pyLean.designMode.factoryPattern.A_NoFactories import Mercedes, BMW


class SimpleFactory(object):
    """
    简单工厂
        简单工厂模式适用于需创建的对象较少，不会造成工厂方法中的业务逻辑太过复杂的情况下，而且用户只关心那种类型的实例被创建，
    并不关心其初始化过程时，比如多种数据库(MySQL/MongoDB)的实例，多种格式文件的解析器(XML/JSON)等。
    """

    # 静态方法：类中用 @staticmethod装饰的不带 self 参数的方法。类的静态方法可以直接使用类名调用。
    #   对于不需要访问类实例属性，类实例方法，和类属性的函数定义成静态函数
    # 类方法: 默认有个cls参数，可以被类和对象调用，需要加上 @classmethod装饰器
    #   对于需要访问类属性的定义成类函数
    # 普通方法: 默认有个self参数，且只能被对象调用。
    #   对于需要访问实例属性、实例方法的定义成实例函数

    @staticmethod
    def product_car(name):
        if name == 'mb':
            return Mercedes()
        elif name == 'bmw':
            return BMW()


"""
        有了SimpleCarFactory类后，就可以通过向固定的接口传入参数获得想要的对象实例，如下：
"""


def simpleFactory():
    mb = SimpleFactory().product_car('mb')
    bmw = SimpleFactory().product_car('bmw')
    print('simpleFactory():\n\t{}\n\t{}'.format(['梅赛德斯：', mb], ['宝马：', bmw]))


if __name__ == '__main__':
    # 有无()很重要，没有返回对象地址，有返回函数值
    simpleFactory()
