# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :chinacarPicture.py
@Time   :2020/12/31 10:40
@Author :Chen
@Software:PyCharm
"""
import os
import traceback
import time
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import json
import random


def ModifDocuments(infileName, downLoadDir):
    dirs = [i for i in os.listdir(downLoadDir) if os.path.isdir(os.path.join(downLoadDir, i, ''))]
    lines = []
    with open(infileName, encoding='utf8', errors='ignore') as er:
        for dirname in er.readlines():
            if dirname.strip() not in dirs:
                lines.append(dirname.strip())
    return lines


def InspectFileCount(imgCount, downLoadDir):
    jpgLis = []
    count = True
    index = 0
    while count:
        index += 1
        for home, dirs, files in os.walk(downLoadDir):
            for filename in files:
                if filename[-3:] == 'jpg':
                    jpgLis.append(filename)
        print(len(jpgLis))
        if imgCount != len(jpgLis):
            jpgLis = []
            time.sleep(5)
            if index >= 5:
                break
        elif imgCount == len(jpgLis):
            for i in jpgLis:
                print(key, i)
            break
        else:
            de = open("chinacarPictureLog.txt", "a")
            de.write(key + ',' + str(jpgLis) + ',' + str(imgCount) + '\n')
            de.flush()
            de.close()
    return jpgLis


if __name__ == '__main__':
    infilename = r"E:\jpg\key.txt"
    download = r"E:\jpg"
    proxy_data = [
        '--proxy=%s' % '61.135.185.152:80',  # 设置的代理ip
        '--proxy-type=http',  # 代理类型
        '--ignore-ssl-errors=true',  # 忽略https错误
    ]
    prefs = {"profile.managed_default_content_settings.images": 2}
    capo = DesiredCapabilities.PHANTOMJS
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    urlList = ModifDocuments(infilename, download)
    cookies = {
        'value': 'think%3A%7B%22id%22%3A%22292931%22%2C%22nick%22%3A%22%25E6%25B1%25BD%25E8%25BD%25A6%25E7%25BD%2591'
                 '%25E7%25BD%2591%25E5%258F%258B6817%22%2C%22headpic%22%3A%22http%253A%252F%252Fwww.chinacar.com.cn'
                 '%252FPublic%252Fperson%252Fimages%252Fheadpic6.png%22%2C%22mobile%22%3A%2215174506817%22%2C'
                 '%22mark_type%22%3A%22%22%2C%22user_code%22%3A%2261dc198113963ab734167e0a00a3dd93%22%7D',
        'name': 'LOGIN_USER_INFO'}
    browser = None
    for key in urlList:
        # noinspection PyBroadException
        try:
            downloadDir = os.path.join(download, key, '')
            prefs = {"download.default_directory": downloadDir}
            options.add_experimental_option("prefs", prefs)
            browser = webdriver.Chrome(desired_capabilities=capo, service_args=proxy_data, chrome_options=options)
            browser.get('http://chinacar.com.cn/Login/iLogin.html')
            browser.add_cookie(cookie_dict=cookies)
            browser.get('http://chinacar.com.cn/ggcx_new/search_view.html?id=' + key)
            img_list = browser.find_elements_by_class_name('list_text')
            if not os.path.exists(downloadDir):
                os.makedirs(downloadDir)
            for li in img_list:
                browser.execute_script('arguments[0].click();', li)
                time.sleep(random.randint(2, 3))
            jpg_lis = InspectFileCount(len(img_list), downloadDir)
            browser.quit()
            for img in jpg_lis:
                prJson = json.dumps({'ID': key, 'img': img}, ensure_ascii=False).encode('utf-8')
                requests.post(url=r'http://192.168.50.100:3018/api/v1/chinacar/img', data=prJson)
            time.sleep(random.randint(1, 2))
        except Exception as e:
            fo = open("error.txt", "a")
            fo.write(key + '\n' + traceback.format_exc() + '\n')
            fo.flush()
            fo.close()
            continue

