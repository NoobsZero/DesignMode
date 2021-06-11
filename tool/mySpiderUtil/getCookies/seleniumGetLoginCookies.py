# encoding: utf-8
"""
@file: seleniumGetLoginCookies.py
@time: 2021/6/11 10:26
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

brower = webdriver.Chrome()


def getCookies(fileName, url, loginURL):
    # get login cookies
    WebDriverWait(brower, 10)
    brower.get(loginURL)
    while True:
        print("Please login in {}!".format(url))
        time.sleep(3)
        # if login in successfully, url  jump to www.taobao.com
        while brower.current_url == url:
            tbCookies = brower.get_cookies()
            brower.quit()
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open(fileName+'.pickle', 'wb')
            pickle.dump(cookies, outputPath)
            outputPath.close()
            return cookies


def readCookies(fileName, url=None, loginURL=None):
    if os.path.exists(fileName+'.pickle'):
        readPath = open(fileName+'.pickle', 'rb')
        tbCookies = pickle.load(readPath)
    else:
        tbCookies = getCookies(fileName, url, loginURL)
    return tbCookies


if __name__ == '__main__':
    fileName = 'huangye88'
    url = 'https://www.huangye88.com'
    loginURL = 'https://my.huangye88.com/login.html'
    tbCookies = readCookies(fileName, url, loginURL)
    print(tbCookies)
    # brower.get(loginURL)
    # for cookie in tbCookies:
    #     brower.add_cookie({
    #         "domain": ".huangye88.com",
    #         "name": cookie,
    #         "value": tbCookies[cookie],
    #         "path": '/',
    #         "expires": None
    #     })
    # brower.get(url)
