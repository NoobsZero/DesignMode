# -*- encoding:utf-8 -*-
"""
@File   :WindyKey.py
@Time   :2020/10/23 17:18
@Author :Chen
@Software:PyCharm
"""
import time

import pyautogui as pag
import selenium
from browsermobproxy import Server
from bs4 import BeautifulSoup
from selenium import webdriver
import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindyKey(object):

    def mouseAndKeyboard(self):
        server = Server("E:\\JetBrains\\maven\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat", {'port': 8080})
        server.start()
        proxy = server.create_proxy()
        chrome_options = Options()
        chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
        driver = webdriver.Chrome(options=chrome_options)
        base_url = "https://www.windy.com/zh/-%E5%8D%AB%E6%98%9F%E4%BA%91%E5%9B%BE-satellite?satellite,13.561,114.697,5"
        proxy.new_har('windy', options={'captureHeaders': True, 'captureContent': True})
        driver.get(base_url)
        driver.maximize_window()  # 窗口最大化
        secs_between_keys = 0.1  # 输入间隔时间
        time.sleep(0.2)
        pag.leftClick(x=1895, y=94)  # 关闭测试弹框
        pag.hotkey('F11', interval=secs_between_keys)  # 进入全屏
        time.sleep(5)
        pag.leftClick(x=1851, y=172)
        pag.leftClick(x=946, y=1062)
        pag.leftClick(x=755, y=1061)
        pag.leftClick(x=593, y=1040)
        driver.implicitly_wait(10)
        driver.find_elements_by_class_name('timecode main-timecode')  # 点击播放键
        print('OK')
        # print(driver.find_element_by_id('radar-bar2').get_attribute("value"))
        # _dict = {}
        # while True:
        #     time.sleep(10)
        #     result = proxy.har
        #     for entry in result['log']['entries']:
        #         _url = entry['request']['url']
        #         if 'info.json' in str(_url):
        #             key = str(_url).split('?')[1]
        #             _dict[key] = _url
        #     if len(_dict) >= 5:
        #         break
        #
        # for key, values in _dict.items():
        #     print(values)
        time.sleep(1000)
        server.stop()
        driver.quit()

        # 946,1062 12小时
        # 703,1063 VISIBLE
        # 755,1061 INFRA+
        # 593,1040 播放键
        # 1859, 145 气象雷达
        # 1851, 172 卫星云图
        # 15,  13 关闭离线弹窗


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.windy.com/zh/-%E5%8D%AB%E6%98%9F%E4%BA%91%E5%9B%BE-satellite?satellite,13.561,114.697,5")
    try:
        # 点击事件
        driver.find_element_by_css_selector("[data-do='set,radar']").click()  # 点击气象雷达
        # driver.implicitly_wait(10)
        time.sleep(20)
        # title = WebDriverWait(driver, 60).until(EC.title_is(u"Windy: 卫星云图"))
        # 调用driver的page_source属性获取页面源码
        print(driver.find_elements_by_css_selector("[data-ref='play']"))
        pageSource = driver.page_source
        # 打印页面源码 html5lib解决获取不全html页面
        soup = BeautifulSoup(pageSource.encode("UTF-8", "ignore"), features="html5lib")
        print(soup.prettify())
        # 窗口切换
        # handles = browser.window_handles
        # for handle in handles:
        #     if handle != browser.current_window_handle:
        #         browser.close()
        #         browser.switch_to.window(handle)

        # if title:
        #     driver.find_element_by_css_selector("[data-ref='play']").click()  # 加载点击播放键
        # else:
        #     print('False')
        # print(driver.find_element_by_css_selector("[data-ref='play']").get_attribute('class'))
        # driver.implicitly_wait(10)
        # data = WebDriverWait(driver, 10).until(
        #         EC.invisibility_of_element_located(
        #             (By.CSS_SELECTOR, "[data-ref='play']")))
        # print(data)
        # driver.find_element_by_css_selector("[data-ref='play']").click()
        # driver.find_element_by_css_selector("[class='play-pause iconfont clickable off']").click()

        # driver.implicitly_wait(10)    # 隐式等待
        # 显示等待
        # els = WebDriverWait(driver, 120).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "[class='play-pause iconfont clickable off']"))
        # )
        # print(els.get_attribute('class'))
        # driver.find_element_by_css_selector('[data-ref]').get_attribute('data-ref')
    except TimeoutException as e:
        print('超时！')
    # finally:
    #     driver.quit()
