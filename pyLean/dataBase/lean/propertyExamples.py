# encoding: utf-8
"""
@file: propertyExamples.py
@time: 2021/6/17 16:11
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""


class Rectangle(object):

    def __init__(self):
        self.width = 10
        self.height = 20

    @property
    # 与类属性名一致
    def width(self):
        return self.true_width

    @property
    # 与类属性名一致
    def height(self):
        return self.true_height


if __name__ == '__main__':
    r = Rectangle()
    # 这里保证了类属性无法更改
    r.width = 1.0
    print(r.width, r.height)


class Rectangle(object):

    def __init__(self):
        self.width = 10
        self.height = 20

    @property
    def width(self):
        return self.true_width

    @width.setter
    # 与property定义的方法名要一致
    def width(self, input_width):
        self.true_width = input_width

    @property
    def height(self):
        return self.true_height

    @height.setter
    # 与property定义的方法名要一致
    def height(self, input_height):
        self.true_height = input_height

    @height.deleter
    def height(self):
        del self.true_height


if __name__ == '__main__':
    s = Rectangle()
    s.width = 1024
    s.height = 768
    print(s.width, s.height)


class Rectangle(object):

    def __init__(self):
        self.width = 10
        self.height = 20

    @property
    # 与类属性名一致
    def width(self):
        return self.true_width

    @property
    # 与类属性名一致
    def height(self):
        return self.true_height


if __name__ == '__main__':
    r = Rectangle()
    # 这里保证了类属性无法更改
    r.width = 1.0
    print(r.width, r.height)


class Rectangle(object):

    def __init__(self):
        self.width = 10
        self.height = 20


if __name__ == '__main__':
    r = Rectangle()
    print(r.width, r.height)
    r.width = 1.0
    print(r.width, r.height)
