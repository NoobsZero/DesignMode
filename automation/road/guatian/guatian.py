# encoding: utf-8
"""
@file: guatian.py
@time: 2021/6/23 13:40
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import requests
import json
import os
import time
import random
import datetime


def token_one(token_value=''):
    url = "http://guatian.jy-tech.com.cn/rest/user/token"

    headers = {
        "token": token_value,
        'api_version': '17',
        "Content-Type": 'application/json; charset=UTF-8',
        "Content-Length": '58',
        "Host": 'guatian.jy-tech.com.cn',
        "Connection": 'Keep-Alive',
        "Accept-Encoding": 'gzip',
        "Cookie": "token: " + token_value,
        "User-Agent": 'okhttp/2.5.0',
    }
    body = {"id": 0, "refreshToken": "8cee816450684edaa2cfb755a2cce5f2"}
    # {"id": 0, "refreshToken": "4cc1266c03c140f4a7634b9735d197ba"}

    response = requests.post(url=url, headers=headers, data=json.dumps(body))

    response.endcoding = 'utf-8'
    # {"code":0,"payload":{"id":9810,"admin":false,"accessToken":"9810:1568273031191:9feaINBbgfR7+YPlE0WBaA==","refreshToken":"4cc1266c03c140f4a7634b9735d197ba"}}
    ret = json.loads(response.text)
    # print(ret)
    # print(ret['payload']['accessToken'])

    return ret['payload']['accessToken']


def request_json(token_value, i):
    base_url = "http://guatian.jy-tech.com.cn/rest/questions/all-communication?currentPage=" + str(i) + "&pageSize=20"
    headers = {
        "Content-Type": "application/json",
        "token": "{}".format(token_value),
        "api_version": "17",
        "Host": "guatian.jy-tech.com.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "Cookie": "{}={}".format('token', token_value),
        "User-Agent": "okhttp/2.5.0"
    }

    response = requests.get(url=base_url, headers=headers)
    response.endcoding = 'utf-8'
    # print(response.text)
    return response.text


def folder_exist(dir_path):
    '''
    1. 作用:判断文件夹路径是否存在,不存在则创建
    2. 参数:dir_path:文件夹路径
    3. 返回值:None
    '''
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def save_json(json_data, i):
    today = datetime.datetime.today()
    str_today = datetime.datetime.strftime(today, '%Y%m%d%H')
    base_dir = 'json_data{}'
    json_dir = base_dir.format(str_today)
    folder_exist(json_dir)
    json_path = os.path.join(json_dir, 'page_{}.json'.format(i))
    with open(json_path.format(str_today, i), 'w', encoding='utf-8') as f:
        print(json_path.format(str_today, i))
        f.write(json_data)
    return "{}:第{}页json存储成功".format(json_dir, i)


def pic_url(json_info):
    pic_list = []
    pic_dict = json.loads(json_info)
    ret = pic_dict["payload"]["list"]
    for i in ret:
        # print("pic", i['pictures'][0])
        pic_list.append(i['pictures'][0])
    return pic_list


if __name__ == '__main__':
    token_value = ''
    for i in range(5):
        token_value = token_one(token_value)
        json_info = request_json(token_value, i)
        # print(json_info)
        result = save_json(json_info, i)
        print(result)
        time.sleep(random.randint(2, 10))
