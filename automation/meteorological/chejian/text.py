# -*- encoding:utf-8 -*-
"""
@File   :text.py
@Time   :2021/2/2 18:10
@Author :Chen
@Software:PyCharm
"""
import requests


def get():
    session=requests.Session()
    cookies={'UserContextToken':'fffffffffff'}
    for i in range(0,1,1):
        count = 47762729 + i
        url=f'https:fffffffff&id={count}'
        print(count)
        responsetext=session.get(url,cookies=cookies,timeout=20).text

        print(responsetext)