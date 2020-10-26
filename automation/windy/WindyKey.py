# -*- encoding:utf-8 -*-
"""
@File   :WindyKey.py
@Time   :2020/10/23 17:18
@Author :Chen
@Software:PyCharm
"""
import time
import unittest
from unittest import TestCase

import pyautogui as pag
from browsermobproxy import Server
from selenium import webdriver
import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindyKey(unittest.TestCase):

    def mouseAndKeyboard(self):
        server = Server("E:\\JetBrains\\maven\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
        server.start()
        proxy = server.create_proxy()
        # chrome_options = Options()
        # chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
        # driver = webdriver.Chrome(chrome_options=chrome_options)
        # base_url = "https://www.windy.com/zh/-%E5%8D%AB%E6%98%9F%E4%BA%91%E5%9B%BE-satellite?satellite,13.561,114.697,5"
        # proxy.new_har('windy', options={'captureHeaders': True, 'captureContent': True})
        # driver.get(base_url)
        # time.sleep(3)
        # result = proxy.har
        # for entry in result['log']['entries']:
        #     _url = entry['request']['url']
        #     print(_url)
        #
        # server.stop()
        # driver.quit()

        # chromedriver = "C:/Users/标注/AppData/Local/Google/Chrome/Application/chromedriver"
        # os.environ["webdriver.chrome.driver"] = chromedriver
        # driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
        # driver.get(
        #     "https://www.windy.com/zh/-%E5%8D%AB%E6%98%9F%E4%BA%91%E5%9B%BE-satellite?satellite,13.561,114.697,5")
        # driver.maximize_window()  # 窗口最大化
        # secs_between_keys = 0.1  # 输入间隔时间
        # time.sleep(0.2)
        # pag.leftClick(x=1895, y=94)  # 关闭测试弹框
        # pag.hotkey('F11', interval=secs_between_keys)  # 进入全屏
        # time.sleep(5)
        # pag.leftClick(x=1851, y=172)
        # pag.leftClick(x=946, y=1062)
        # pag.leftClick(x=755, y=1061)
        # pag.leftClick(x=593, y=1040)


        # try:
        #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        #     print(element)
        # finally:
        #     driver.quit()
        time.sleep(1000)
        # 946,1062 12小时
        # 703,1063 VISIBLE
        # 755,1061 INFRA+
        # 593,1040 播放键
        # 1859, 145 气象雷达
        # 1851, 172 卫星云图
        # 15,  13 关闭离线弹窗


if __name__ == '__main__':
    WindyKey().mouseAndKeyboard()
