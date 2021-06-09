# encoding: utf-8
"""
@file: test10.py
@time: 2021/6/7 11:28
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import base64
import os
import time

from fontTools.ttLib import TTFont


if __name__ == '__main__':
    code_list = '&#x8810c;&#x88110;&#x8810e;&#x88111;&#x8810d;&#x88111;&#x8810b;&#x88111;&#x8810b;&#x88110;&#x88110;'
    # 替换&#为0，用于后面直接转换为10进制数
    code_list = code_list.replace("&#", "0")
    # 转换成列表
    code_list = code_list.split(';')[:-1]
    # 确定第一个号码1对应的10进制值
    c1 = int(code_list[0], base=16)
    # 创建0-9对应的10进制值
    int_list = range(c1 - 1, c1 + 9)
    # 将其转换为
    hex_list = [str(hex(i)) for i in int_list]
    # 创建0-9的数字对应列表
    str_list = [str(i) for i in range(0, 10)]
    # 组装成字典方便对应
    code_dict = dict(zip(hex_list, str_list))
    # 见证奇迹的时刻，把电话号码翻译过来
    phone = "".join([code_dict[p] for p in code_list])
    print(phone)
