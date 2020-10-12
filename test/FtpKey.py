# -*- encoding:utf-8 -*-
"""
@File   :FtpKey.py
@Time   :2020/8/31 17:48
@Author :Chen
@Software:PyCharm
"""
import time
from pymouse import *
from pykeyboard import PyKeyboard

def MouseAndKeyboard():
    ms = PyMouse()
    kb = PyKeyboard()
    # 鼠标移动到坐标(x,y)
    # ms.move(210, 1060)
    ms.click(180, 1060, 1, 1)
    time.sleep(1)
    start = time.time()
    while(True):
        end = time.time()
        if int((end - start)) >= 300:
            ms.click(70, 1000, 1, 1)
            time.sleep(1)
            ms.click(200, 670, 2, 1)
            kb.tap_key('q')
            time.sleep(30)
            ms.click(200, 670, 2, 1)
            kb.tap_key('q')
            start = time.time()
            time.sleep(1)
        ms.click(170, 1000, 1, 1)
        time.sleep(1)
        ms.click(200, 670, 2, 1)
        time.sleep(1)
        kb.tap_key('r')
        time.sleep(10)

if __name__ == '__main__':
    MouseAndKeyboard()