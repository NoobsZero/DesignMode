# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :oldchinacar1.py
@Time   :2020/12/7 18:19
@Author :Chen
@Software:PyCharm
"""
import os
import shutil
import traceback
import time
from urllib.request import Request, urlopen
import requests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import json
import random


def ModifDocuments(infilename, dick):
    lines = []
    with open(infilename, encoding='utf8', errors='ignore') as f:
        for i in f.readlines():
            car = i.strip()
            if car not in dick:
                lines.append(car)

    with open(infilename, 'w', encoding='utf8') as g:
        for line in lines:
            if line not in dick:
                g.write(line + '\n')


def registerUrl():
    try:
        url = "http://192.168.50.100:3018/chinacar/ids"
        request = Request(url)
        data = urlopen(request).read()
        data_dict = json.loads(data)
        data = list(data_dict['data'])
        return data
    except Exception as e:
        print(e)

def tex():
    while True:
        time.sleep(1)
        print('没有跳过这条输出')

if __name__ == '__main__':
    import time
    import eventlet  # 导入eventlet这个模块

    eventlet.monkey_patch()  # 必须加这条代码
    with eventlet.Timeout(2, False):  # 设置超时时间为2秒
        tex()
    print('跳过了输出')
    # url = "http://192.168.50.100:3018/chinacar/ids"
    # request = Request(url)
    # data = urlopen(request).read()
    # data_dict = json.loads(data)
    # data = list(data_dict['data'])
    # with open(r"E:\jpg\key1.txt", 'a', encoding="utf-8") as fo:
    #     for i in data:
    #         fo.write(i + '\n')
    #         fo.flush()

    # url = "http://192.168.50.100:3018//api/v1/chinacar/img_ids"
    # request = Request(url)
    # data = urlopen(request).read()
    # data_dict = json.loads(data)
    # ModifDocuments(r"E:\jpg\key.txt", list(data_dict['data']))
# if __name__ == '__main__':
#     url = r'http://192.168.50.100:3018/api/v1/chinacar/img'
#     proxy_data = [
#         '--proxy=%s' % '61.135.185.152:80',  # 设置的代理ip
#         '--proxy-type=http',  # 代理类型
#         '--ignore-ssl-errors=true',  # 忽略https错误
#     ]
#     prefs = {"profile.managed_default_content_settings.images": 2}
#     dict = {'port': 8090}
#     capa = DesiredCapabilities.PHANTOMJS
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("prefs", prefs)
#     urlList = registerUrl()
#
#     browser = webdriver.Chrome(desired_capabilities=capa, service_args=proxy_data, chrome_options=options)
#     browser.get('http://chinacar.com.cn/Login/iLogin.html')
#     cookies = {
#         'value': 'think%3A%7B%22id%22%3A%22292931%22%2C%22nick%22%3A%22%25E6%25B1%25BD%25E8%25BD%25A6%25E7%25BD%2591%25E7%25BD%2591%25E5%258F%258B6817%22%2C%22headpic%22%3A%22http%253A%252F%252Fwww.chinacar.com.cn%252FPublic%252Fperson%252Fimages%252Fheadpic6.png%22%2C%22mobile%22%3A%2215174506817%22%2C%22mark_type%22%3A%22%22%2C%22user_code%22%3A%2261dc198113963ab734167e0a00a3dd93%22%7D',
#         'name': 'LOGIN_USER_INFO'}
#     browser.add_cookie(cookie_dict=cookies)
#     for key in urlList:
#         try:
#             browser.get('http://chinacar.com.cn/ggcx_new/search_view.html?id=' + key)
#             time.sleep(random.randint(5, 10))
#             img_list = browser.find_elements_by_class_name('list_text')
#             for li in img_list:
#                 browser.execute_script('arguments[0].click();', li)
#             jpg_lis = []
#             for home, dirs, files in os.walk(r'C:\Users\标注\Downloads'):
#                 for filename in files:
#                     if filename[-3:] == 'jpg':
#                         jpg_lis.append(os.path.join(home, filename))
#             if len(jpg_lis) != 0:
#                 jpg_dir = os.path.join(r'E:\jpg', key, '')
#                 if not os.path.exists(jpg_dir):
#                     os.makedirs(jpg_dir)
#                 for jpg in jpg_lis:
#                     img = os.path.join(os.path.split(jpg)[1])
#                     shutil.move(jpg, os.path.join(jpg_dir, img))
#                     prJson = json.dumps({'ID': key, 'img': img}, ensure_ascii=False).encode('utf-8')
#                     requests.post(url=url, data=prJson)
#                     print(prJson)
#                     time.sleep(1)
#         except Exception as e:
#             fo = open("error.txt", "a")
#             fo.write(key + '\n' + traceback.format_exc() + '\n')
#             fo.flush()
#             fo.close()
#             continue
