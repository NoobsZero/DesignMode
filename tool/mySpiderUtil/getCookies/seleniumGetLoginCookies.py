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
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pynput.keyboard import Controller, Key, Listener

brower = webdriver.Chrome()


def on_release(key):
    if key == Key.esc:
        return False


def start_listen():
    """开始监听"""
    with Listener(on_release=on_release) as listener:
        listener.join()


def getCookies(fileName, url, loginURL):
    # get login cookies
    WebDriverWait(brower, 10)
    brower.get(loginURL)
    kb = Controller()
    kb.press(Key.space)
    start_listen()
    while True:
        print("Please login in {}!".format(url))
        # if login in successfully, url  jump to www.taobao.com
        tbCookies = brower.get_cookies()
        cookies = {}
        for item in tbCookies:
            cookies[item['name']] = item['value']
        brower.quit()
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
    # 登录后esc退出，并返回对应Cookies
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
