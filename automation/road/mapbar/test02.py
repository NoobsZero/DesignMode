# encoding: utf-8
"""
@file: test02.py
@time: 2021/3/17 9:04
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import json

if __name__ == '__main__':
    with open('csCrossing.txt', 'r') as f:
        datas = f.readlines()
    for i in datas:
        data = json.loads(i)
        with open('csCro.txt', 'a', encoding='utf8', errors='ignore') as f:
            f.write(' '.join([data['city_name'], data['type'], data['address'], data['hash']]))
            f.write('\n')
