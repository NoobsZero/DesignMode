# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :getJs.py
@Time   :2020/12/7 18:19
@Author :Chen
@Software:PyCharm
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

data_list = []


# def getCar(soup):
    # for idx, tr in enumerate(soup.find('tbody', id='gridview-1046-body')):
    #     if idx != 0:

            # parameters = {}
            # tds = tr.find_all('td')
            # parameters['clxh'] = tds[0].text
            # parameters['dpxh'] = tds[1].text
            # parameters['fdjxh'] = tds[2].text
            # parameters['fdjscs'] = tds[3].text
            # parameters['fdjpl'] = tds[4].text
            # parameters['fdjgl'] = tds[5].text
            # parameters['rszl'] = tds[6].text
            # parameters['zs'] = tds[7].text
            # parameters['pc'] = tds[8].text
            # data_list.append(parameters)


# 61.135.185.152:80
proxy_data = [
    '--proxy=%s' % '91.205.174.26:80',  # 设置的代理ip
    '--proxy-type=http',  # 代理类型
    '--ignore-ssl-errors=true',  # 忽略https错误
]

capa = DesiredCapabilities.PHANTOMJS
url1 = 'http://192.168.50.100:3018/api/v1/chinacar'
url2 = 'http://192.168.50.100:3018/api/v1/chinacar/fdj'

options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
# options.add_argument('--headless')

if __name__ == '__main__':
    chinacarurl = 'http://chinacar.com.cn/search.html'
    infilename = 'Automobile.txt'
    fo = open(infilename, encoding='utf8', errors='ignore')
    fileList = fo.readlines()
    for car in fileList:
        car = car.strip()
        browser = webdriver.Chrome(desired_capabilities=capa, service_args=proxy_data, chrome_options=options)
        browser.get(chinacarurl)
        browser.find_element_by_id('s1').send_keys(car)
        waitsear = WebDriverWait(browser, 10)
        waitsear.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchbtn"]')))
        browser.find_element_by_xpath('//*[@id="searchbtn"]').click()
        waittable = WebDriverWait(browser, 60)
        waittable.until(EC.presence_of_element_located((By.ID, 'gridview-1046-body')))
        # soup = BeautifulSoup(browser.page_source, 'html.parser')
        browser.find_element_by_xpath('//*[@id="gridview-1046-record-ext-record-1"]').click()
        # getCar(soup)
    #     htIdex = str(browser.find_element_by_xpath(
    #         '//*[@id="body_h"]/div[2]/div[3]/div[4]/div/div[3]/ul/li[1]/font[3]').text).split(
    #         '/')[1]
    #     for i in range(int(htIdex)):
    #         wait = WebDriverWait(browser, 10)
    #         wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="body_h"]/div[2]/div[3]/div[4]/div/table')))
    #         soup = BeautifulSoup(browser.page_source, 'html.parser')
    #         getVIN(soup, vin)
    #         browser.find_element_by_xpath('//*[@id="body_h"]/div[2]/div[3]/div[4]/div/div[3]/ul/li[2]/a').click()
    #     for i in data_list:
    #         print(i)
    #         chinacar = json.dumps(i, ensure_ascii=False).encode('utf-8')
    #         requests.post(url='http://192.168.50.100:3018/api/v1/chinacar/vin', data=chinacar)
        # browser.quit()
