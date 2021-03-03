# -*- encoding:utf-8 -*-
"""
@File   :text01.py
@Time   :2021/1/15 14:30
@Author :Chen
@Software:PyCharm
"""
import os
import threading
import time

from tool.baseUtil.getBaseUtil import BaseProgressBar


def sing():
    for i in range(num):
        print("sing%d" % i)
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print("dancing%d" % i)
        time.sleep(0.5)


def main():
    """创建启动线程"""
    t_sing = threading.Thread(target=sing, args=(5,))
    t_dance = threading.Thread(target=dance, args=(6, ))
    t_sing.start()
    t_dance.start()


if __name__ == '__main__':
    main()
