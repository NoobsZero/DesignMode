# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :chinacarPicture.py
@Time   :2020/12/31 10:40
@Author :Chen
@Software:PyCharm
"""
import os
import shutil
import traceback
import time
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import json
import random
import imghdr
import eventlet


def ModifDocuments(infileName, downLoadDir):
    dirs = [i for i in os.listdir(downLoadDir) if os.path.isdir(os.path.join(downLoadDir, i, ''))]
    lines = []
    with open(infileName, encoding='utf8', errors='ignore') as er:
        for dirname in er.readlines():
            if dirname.strip() not in dirs:
                lines.append(dirname.strip())
    return lines


def InspectFileCount(imgCount, downLoadDir):
    """
    问题：
        1、下载文件数目少
        2、文件没有下载完整
        3、文件就是损坏文件
    :param imgCount:
    :param downLoadDir:
    :return:
    """
    jpgLis = []
    count = True
    while count:
        for home, dirs, files in os.walk(downLoadDir):
            for filename in files:
                if filename[-3:] == 'jpg':
                    jpgLis.append(os.path.join(home, filename))
        print(key+"总数量:"+str(imgCount)+" / "+str(len(jpgLis)))
        if imgCount == len(jpgLis):
            break
        else:
            jpgLis = []
            time.sleep(2)
    images = []
    jpgLis = sorted(jpgLis)
    while count:
        for filename in jpgLis:
            if filename not in images:
                check = imghdr.what(filename)
                if check:
                    images.append(filename)
                    print(key, os.path.split(filename)[1])
        if len(jpgLis) == len(images):
            images.clear()
            for iago in jpgLis:
                images.append(os.path.split(iago)[1])
            break
        else:
            time.sleep(2)
    return images

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
    options.add_experimental_option("prefs", prefs)
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
        # try:
            downloadDir = os.path.join(download, key, '')
            prefs = {"download.default_directory": downloadDir}
            browser = webdriver.Chrome(desired_capabilities=capo, service_args=proxy_data, chrome_options=options)
            browser.get('http://chinacar.com.cn/Login/iLogin.html')
            browser.add_cookie(cookie_dict=cookies)
            browser.get('http://chinacar.com.cn/ggcx_new/search_view.html?id=' + key)
            img_list = browser.find_elements_by_class_name('list_text')
            if not os.path.exists(downloadDir):
                os.makedirs(downloadDir)
            index = 0
            eventlet.monkey_patch()  # 必须加这条代码
            for li in img_list:
                index += 1
                browser.execute_script('arguments[0].click();', li)
                with eventlet.Timeout(5, False):
                    InspectFileCount(index, downloadDir)
        #     with eventlet.Timeout(600, False):  # 设置超时时间为600秒
        #         jpg_lis = InspectFileCount(len(img_list), downloadDir)
            browser.quit()
        #     if len(jpg_lis) == len(img_list):
        #         for img in jpg_lis:
        #             prJson = json.dumps({'ID': key, 'img': img}, ensure_ascii=False).encode('utf-8')
        #             requests.post(url=r'http://192.168.50.100:3018/api/v1/chinacar/img', data=prJson)
        #         time.sleep(random.randint(1, 2))
        #     else:
        #         if os.path.exists(downloadDir):
        #             shutil.rmtree(downloadDir)
        # except Exception as e:
        #     fo = open("error.txt", "a")
        #     fo.write(key + '\n' + traceback.format_exc() + '\n')
        #     fo.flush()
        #     fo.close()
        #     continue
