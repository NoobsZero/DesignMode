# encoding: utf-8
"""
@file: asyncHronous.py
@time: 2021/6/18 17:54
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""

from flask import Flask
import time

# 定义一个Flask服务
app = Flask(__name__)


@app.route('/')
def index():
    """每次请求接口至少要耗时3秒"""
    time.sleep(3)
    return 'Hello!'


if __name__ == '__main__':
    # threaded：启动Flask多线程模式，默认只有一个线程
    # 如果不开启多线程模式，同一时刻遇到多个请求的时候，只能顺次处理，这样即使我们使用协程异步请求了这个服务，也只能一个一个排队等待，瓶颈就会出现在服务端。
    # 所以，多线程模式是有必要打开的。
    app.run(threaded=True)
