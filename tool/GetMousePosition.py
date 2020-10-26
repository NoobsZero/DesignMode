# -*- encoding:utf-8 -*-
"""
@File   :GetMousePosition.py
@Time   :2020/10/23 18:59
@Author :Chen
@Software:PyCharm
"""
import os
import time

import pyautogui as pag


def getMousePosition():
    try:
        while True:
            print("Press Ctrl-C to end")
            x, y = pag.position()  # 返回鼠标的坐标
            posStr = "Position:" + str(x).rjust(4) + ',' + str(y).rjust(4)
            print(posStr)  # 打印坐标
            time.sleep(5)
            os.system('cls')  # 清楚屏幕
    except KeyboardInterrupt:
        print('end....')


if __name__ == '__main__':
    getMousePosition()
