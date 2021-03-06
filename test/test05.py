# -*- codeing = utf-8 -*-
# @Time :2020/8/6 12:12
# @Author:Eric
# @File : test05.py
# @Software: PyCharm
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import re
import datetime
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
                if bool(re.compile(u'供应商').search(sub_str)):
                    lis_str.append(sub_str)


def get_url_lis(url):
    p_x_list = []
    reponse = urllib.request.urlopen(url.strip())
    only_a_tags = SoupStrainer('tbody', attrs={"class": "table", "style": "display: block;"})
    only_text_tags = SoupStrainer('div', attrs={"class": "vF_detail_content_container"})
    p_x_list = BeautifulSoup(reponse.read().decode('utf-8'), 'html.parser', parse_only=only_text_tags)
    for_list(p_x_list)


if __name__ == '__main__':
    url = 'http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202006/t20200619_14509569.htm'.strip()
    get_url_lis(url)
    for i in lis_str:
        print(i)
    # browser = webdriver.Chrome()
    # browser = webdriver.PhantomJS()
    # browser.get("http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202012/t20201218_15656341.htm")
    # ss = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/table').contents
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="con_two_p1"]/table')))
    # only_a_tags = SoupStrainer('div', attrs={"id": "con_two_p1"})
    # soup = BeautifulSoup(browser.page_source, 'html.parser', parse_only=only_a_tags)
    # soup = BeautifulSoup(browser.page_source, "lxml")
    # for_list(soup)
    # browser.close()
