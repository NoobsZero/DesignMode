# encoding: utf-8
"""
@file: getUseragent.py
@time: 2021/6/30 8:53
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from fake_useragent import UserAgent

if __name__ == '__main__':
    # 代码出现BUG，禁用浏览器缓存问题即可 use_cache_server
    ua = UserAgent(use_cache_server=False)
    headers = {'User-Agent': ua.random}
    print(headers)
