# -*- codeing = utf-8 -*-
# @Time :2020/8/6 18:55
# @Author:Eric
# @File : test07.py
# @Software: PyCharm
import re
import requests
import re, csv
import json
# from contextlib import closing
# from pyquery import PyQuery as pq
from requests import RequestException
from bs4 import BeautifulSoup

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pyperclip  # python实现复制粘贴
import time
from pykeyboard import PyKeyboard
import win32clipboard as w
import win32con
from selenium.common.exceptions import NoSuchElementException


class BidWinning(object):
    def __init__(self, changeZBDWdisplsy, changeZBJEdisplsy, changeLXRdisplsy, changeLXDHdisplsy, changeCGXMLXRdisplsy,
                 changeCGXMLXDHdisplsy):
        self.changeZBDWdisplsy = changeZBDWdisplsy
        self.changeZBJEdisplsy = changeZBJEdisplsy
        self.changeLXRdisplsy = changeLXRdisplsy
        self.changeLXDHdisplsy = changeLXDHdisplsy
        self.changeCGXMLXRdisplsy = changeCGXMLXRdisplsy
        self.changeCGXMLXDHdisplsy = changeCGXMLXDHdisplsy


def get_text():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d.decode('GBK')


def set_text(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()


def main():
    browser = webdriver.Chrome()
    url = 'http://www.ccgp.gov.cn/cggg/dfgg/zbgg/201901/t20190122_11556445.htm'
    browser.get(url)  # 在当前浏览器中访问百度
    k = PyKeyboard()
    try:
        browser.find_element_by_id('displayGG').click()
        # # #模拟键盘点击ctrl+v
        k.press_key(k.control_key)
        k.tap_key('a')
        k.tap_key('c')
        time.sleep(1)
    except NoSuchElementException:
        k = PyKeyboard()
        # # #模拟键盘点击ctrl+v
        k.press_key(k.control_key)
        k.tap_key('a')
        k.tap_key('c')
        time.sleep(1)
    url_lis = str(get_text()).split('\n')
    url_BidWinning:[BidWinning] = []
    for i in range(len(url_lis)):
        if bool(re.compile(u'[\u4e00-\u9fa5]').search(url_lis[i])) or bool(re.search(r'\d', url_lis[i])):
            if bool(re.compile(u'废标').search(url_lis[i])):
                break
            elif bool(re.compile(
                    u'成交价|成交金额|联系方式|采购人|采购人联系方式|采购单位|中标供应商|中标价格|中标内容|供应商名称|总中标金额|中标总金额|中标金额|采购项目|公司|中标供货商金额|联系人|联系电话').search(
                url_lis[i])) and not bool(
                re.compile(u'采购项目名称|评审意见|采购项目预算金额|中标供应商地址|采购人地址|代理|中标公告|项目编号|中标结果如下').search(url_lis[i])):

                print(url_lis[i])




if __name__ == '__main__':
    main()
