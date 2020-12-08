# -*- encoding:utf-8 -*-
"""
@File   :test.py.py
@Time   :2020/12/8 10:30
@Author :Chen
@Software:PyCharm
"""
import re
from bs4 import SoupStrainer
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import scrapy


class QuotesSpider(scrapy.Spider):
    lis_str = []

    def for_list(self, list_x):
        for x in list_x:
            if len(x) > 1:
                self.for_list(x)
            else:
                # 过滤所有标签
                pattern = re.compile("<(.*?)>")
                sub_str = re.sub(pattern, "", str(x))
                if bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str)):
                    self.lis_str.append(sub_str)

    name = "test"

    def start_requests(self):
        fo = open('che1.txt', encoding='utf8', errors='ignore')
        fileList = fo.readlines()
        matches = (x for x in fileList if ('tarid' in x and 'tarid_nobase' not in x) or ('img' in x))
        urlList = {}
        for i in matches:
            if 'img' in i:
                url = re.findall(r'(https?://\S*?jpg|\S*?JPG)+', str(i))[1]
            else:
                result = re.sub('\W+', '', i.split(':')[1]).replace("_", '')
                urlList[url] = 'http://chinacar.com.cn/ggcx_new/search_view.html?id=' + result
        for url in urlList:
            yield scrapy.Request(url=urlList[url], callback=self.parse)


    def parse(self, response):
        browser = webdriver.PhantomJS()
        browser.get(response.url)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="con_two_p1"]/table')))
        only_a_tags = SoupStrainer('div', attrs={"id": "con_two_p1"})
        soup = BeautifulSoup(browser.page_source, 'html.parser', parse_only=only_a_tags)
        self.for_list(soup)
        browser.close()
        yield {'content': self.lis_str}
        self.lis_str.clear()