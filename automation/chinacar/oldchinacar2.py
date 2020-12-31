# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :getJs.py
@Time   :2020/12/7 18:19
@Author :Chen
@Software:PyCharm
"""
import re
import time

from bs4 import BeautifulSoup
from scipy.signal.windows import windows
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
import json
import requests
import os
import random


#   从外部获取参数
#   argv = sys.argv
#   argc = len(argv)
#   if argc < 2:
#     print "Usage: %s <file>" %(os.path.basename(argv[0]))
#     exit()

def ModifDocuments(infilename, dick):
    lines = []
    with open(infilename, encoding='utf8', errors='ignore') as f:
        for i in f.readlines():
            car = i.strip()
            if car not in list(dick.keys()):
                lines.append(car)

    with open(infilename, 'w', encoding='utf8') as g:
        for line in lines:
            if line not in dick.keys():
                g.write(line + '\n')


# 61.135.185.152:80
# 91.205.174.26:80
proxy_data = [
    '--proxy=%s' % '61.135.185.152:80',  # 设置的代理ip
    '--proxy-type=http',  # 代理类型
    '--ignore-ssl-errors=true',  # 忽略https错误
]

capa = DesiredCapabilities.PHANTOMJS
url1 = 'http://192.168.50.100:3018/api/v1/chinacar'
url2 = 'http://192.168.50.100:3018/api/v1/chinacar/fdj'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
# options.add_argument('--headless')


if __name__ == '__main__':
    dict = {'port': 8090}
    server = Server(r"C:\Users\EM\Desktop\car\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat", dict)
    server.start()
    proxy = server.create_proxy()
    options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    proxy.new_har('chinacar', options={'captureHeaders': True, 'captureContent': True})
    chinacarurl = 'http://chinacar.com.cn/search.html'
    infilename = r'C:\Users\EM\Desktop\car\Automobile.txt'
    browser = webdriver.Chrome(desired_capabilities=capa, service_args=proxy_data, chrome_options=options)
    browser.get(chinacarurl)
    re = True
    dick = {}
    handles = []
    while re:
        re = False
        fo = open(infilename, encoding='utf8', errors='ignore')
        fileList = fo.readlines()
        random.shuffle(fileList)
        for car in fileList:
            try:
                browser.current_window_handle
                car = car.strip()
                browser.find_element_by_id('s1').clear()
                browser.find_element_by_id('s1').send_keys(car)
                waitsear = WebDriverWait(browser, 60)
                waitsear.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchbtn"]')))
                # 解决点击事件被拦截问题
                searchbtn = browser.find_element_by_xpath('//*[@id="searchbtn"]')
                browser.execute_script('arguments[0].click();', searchbtn)
                browser.find_element_by_id('s1').clear()
                # 获取所有权柄
                handles = browser.window_handles
                # 切换新窗口权柄
                browser.switch_to.window(handles[1])
                condition = True
                count = 0
                while condition:
                    waittb = WebDriverWait(browser, 60)
                    waittb.until(EC.presence_of_element_located((By.ID, 'gridview-1046-table')))
                    time.sleep(5)
                    result = proxy.har
                    for entry in result['log']['entries']:
                        data = ''
                        url = entry['request']['url']
                        if ('http://chinacar.com.cn/Home/GonggaoSearch/GonggaoSearch/search_json?_dc=' in url) and (
                                url not in dick):
                            try:
                                data = entry['response']['content']['text']
                            except KeyError:
                                data = ''
                            if ('没有查到相关数据，请更改查询条件' not in data) and data != '':
                                dick[url] = car
                                print(car, url)
                                with open(r'C:\Users\EM\Desktop\car\file.txt', 'a', encoding="utf-8") as fo:
                                    fo.write(data + '\n')
                                ModifDocuments(infilename, dick)
                                pageCount = int(browser.find_element_by_id('tbtext-1015').text[-3])
                                count = count + 1
                                if pageCount == count and pageCount != 0:
                                    condition = False
                                else:
                                    btnIconEl = browser.find_element_by_xpath('//*[@id="button-1017-btnIconEl"]')
                                    browser.execute_script('arguments[0].click();', btnIconEl)
                            elif '没有查到相关数据，请更改查询条件' in data:
                                condition = False
            except Exception:
                re = True
            finally:
                if len(handles) > 1:
                    browser.close()
                browser.switch_to.window(handles[0])
                time.sleep(random.randint(5, 50))
