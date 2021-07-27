# encoding: utf-8
"""
@file: staticMethodExamples.py
@time: 2021/6/17 14:47
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import math


class Pizza(object):
    def __init__(self, height, radius):
        self.radius = radius
        self.height = height

    @staticmethod
    def compute_area(radius):
        return math.pi * (radius ** 2)

    @classmethod
    def compute_volume(cls, height, radius):
        # 调用@staticmethod方法
        return height * cls.compute_area(radius)

    def get_volume(self):
        return self.compute_volume(self.height, self.radius)


if __name__ == '__main__':
    print(Pizza(1, 2).get_volume())
