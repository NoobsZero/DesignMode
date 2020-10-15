# -*- encoding:utf-8 -*-
"""
@File   :PrototypePattern.py
@Time   :2020/10/14 18:28
@Author :Chen
@Software:PyCharm
设计模式——原型模式
    原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象
    当系统中需要大量创建相同或者相似的对象时，就可以通过“原型设计模式”来实现，通过拷贝指定的“原型实例（对象）”，
创建根该对象一样的新对象（克隆指定对象）。
。

原型模式是用场景:需要大量的基于某个基础原型进行微量修改而得到新原型时使用，软件开发完成后或者在程序运行时增加新的类型。
"""
__author__ = 'Andy'

from copy import copy, deepcopy


class IPrototype(object):
    """
        原型接口类
            定义一个接口对继承类进行约束，接口里有什么方法，继承类就必须有什么方法，接口中不能任何功能代码
            在其他的语言里，比如Java，继承类没有重写接口方法是会报错的，而在python里不会，就是因为python没这个类型，
        所以只是在我们编程过程的一个规定，以I开头的类视为接口。
    """
    def clone(self):
        """
            浅拷贝
            1、当类的成员变量是基本数据类型时，浅拷贝会复制该属性的值赋值给新对象。
            2、当成员变量是引用数据类型时，浅拷贝复制的是引用数据类型的地址值。这种情况下，
            当拷贝出的某一个类修改了引用数据类型的成员变量后，会导致所有拷贝出的类都发生改变。
        """
        pass

    def deep_clone(self):
        """
            深拷贝
            深拷贝不仅会复制成员变量为基本数据类型的值，给新对象。
            还会给是引用数据类型的成员变量申请储存空间，并复制引用数据类型成员变量的对象。
            这样拷贝出的新对象就不怕修改了是引用数据类型的成员变量后，对其它拷贝出的对象造成影响了。
        """
        pass


class WorkExperience(object):
    """
        工作经历类
    """
    def __init__(self):
        self.timeArea = ''
        self.company = ''

    def set_workexperience(self, timeArea, company):
        self.timeArea = timeArea
        self.company = company


class Resume(IPrototype):
    """
        简历类
    """
    def __init__(self, name):
        self.name = name
        self.workexperience = WorkExperience()

    def set_personinfo(self, sex, age):
        self.sex = sex
        self.age = age
        pass

    def set_workexperience(self, timeArea, company):
        self.workexperience.set_workexperience(timeArea, company)

    def display(self):
        print(self.name)
        print(self.sex, self.age)
        print('工作经历', self.workexperience.timeArea, self.workexperience.company)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


class ConcreateType(object):
    def __init__(self):
        self.dicts = {}

    def clone(self):
        c = ConcreateType()
        c.dicts = copy(self.dicts)
        return c

    def clone2(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)

    def setDicts(self, key, value):
        self.dicts[key] = value

    def __str__(self):
        return self.dicts.__str__()


if __name__ == '__main__':
    # obj1 = Resume('andy')
    # obj2 = obj1.clone()  # 浅拷贝对象
    # obj3 = obj1.deep_clone()  # 深拷贝对象
    # obj1.set_personinfo('男', 28)
    # obj1.set_workexperience('2010-2015', 'AA')
    # obj2.set_personinfo('男', 27)
    # obj2.set_workexperience('2011-2017', 'AA')  # 修改浅拷贝的对象工作经历
    # obj3.set_personinfo('男', 29)
    # obj3.set_workexperience('2016-2017', 'AA')  # 修改深拷贝的对象的工作经历
    # obj1.display()
    # obj2.display()
    # obj3.display()
    print('Test ConcreateType')
    ct = ConcreateType()
    ct.setDicts(5, 'five')
    print('ct:', ct)
    cct = ct.clone()
    sct = ct.clone2()
    dct = ct.deep_clone()
    print('clone ct')
    print('ct:', ct)
    print('cct', cct)
    print('sct', sct)
    print('dct', dct)
    print('change ct')
    ct.setDicts(6, 'six')
    print('ct:', ct)
    print('cct', cct)
    print('sct', sct)
    print('dct', dct)