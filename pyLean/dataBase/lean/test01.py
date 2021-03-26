# encoding: utf-8
"""
@file: test01.py
@time: 2021/3/23 8:28
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""


class ListGeneration(object):
    def oneList(self):
        """
            字符串赋值给多个变量
        Returns:
            str => km=, a, b, c
        """
        s = '51 5000 10000'
        k, a, b = [int(item) for item in s.split()]
        print(k, a, b)


    def twoList(self):
        """
            规律生成列表
        Returns:
            [1**2,2**2,3**2,4**2,...,n**2]
        """


    def threeList(self):
        print([r for r in range(2, 11, 2)])


if __name__ == '__main__':
    print(359 ** 2)
