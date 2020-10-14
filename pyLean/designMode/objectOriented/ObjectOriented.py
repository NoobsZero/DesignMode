# -*- encoding:utf-8 -*-
"""
@File   :ObjectOriented.py
@Time   :2020/10/13 8:55
@Author :Chen
@Software:PyCharm
"""


class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2
        return area


class Square:
    def __init__(self, size):
        self.size = size

    def getArea(self):  # 同一个方法在不同的类中最终呈现出不同的效果，即为多态
        area = self.size * self.size
        return area


if __name__ == '__main__':
    a = Triangle(5, 5)
    print(a.getArea())
    b = Square(5)
    print(b.getArea())