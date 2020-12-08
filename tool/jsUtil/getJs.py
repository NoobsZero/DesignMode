# -*- encoding:utf-8 -*-
"""
@File   :getJs.py
@Time   :2020/12/7 18:19
@Author :Chen
@Software:PyCharm
"""
from bs4 import SoupStrainer
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

lis_str = []


def for_list(list_x):
    for x in list_x:
        if len(x) > 1:
            for_list(x)
        else:
            # 过滤所有标签
            pattern = re.compile("<(.*?)>")
            sub_str = re.sub(pattern, "", str(x))
            if bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str)):
                lis_str.append(sub_str)


if __name__ == '__main__':
    # fo = open('che.txt', encoding='utf8', errors='ignore')
    # fileList = fo.readlines()
    # matches = (x for x in fileList if ('tarid' in x and 'tarid_nobase' not in x) or ('img' in x))
    # urlList = {}
    # for i in matches:
    #     if 'img' in i:
    #         url = re.findall(r'(https?://\S*?jpg|\S*?JPG)+', str(i))[1]
    #     else:
    #         result = re.sub('\W+', '', i.split(':')[1]).replace("_", '')
    #         # urlList[url] = 'http://chinacar.com.cn/ggcx_new/search_view.html?id=' + result
    #         print('http://chinacar.com.cn/ggcx_new/search_view.html?id=' + result)
    # for key in urlList:
        browser = webdriver.PhantomJS()
        # browser.get(urlList[key])
        browser.get("http://chinacar.com.cn/ggcx_new/search_view.html?id=OTI1MjUy")
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="con_two_p1"]/table')))
        only_a_tags = SoupStrainer('div', attrs={"id": "con_two_p1"})
        soup = BeautifulSoup(browser.page_source, 'html.parser', parse_only=only_a_tags)
        # for_list(soup)
        browser.close()
        print(soup)
        lis_str.clear()
