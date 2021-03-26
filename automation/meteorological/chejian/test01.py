# encoding: utf-8
"""
@file: test01.py
@time: 2021/3/17 17:23
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import json
import os
import shutil

import requests


def create_file(filename):
        """
        创建日志文件夹和日志文件
        :param filename:
        :return:
        """
        # path = filename[0:filename.rfind("/")]
        # if not os.path.isdir(path):  # 无文件夹时创建
        #     os.makedirs(path)
        if not os.path.isfile(filename):  # 无文件时创建
            fd = open(filename, mode="w", encoding="utf-8")
            fd.close()
        else:
            pass


def urldownload(url, filename=None):
    """
    下载文件到指定目录
    :param url: 文件下载的url
    :param filename: 要存放的目录及文件名，例如：./test.xls
    :return:
    """
    down_res = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(down_res.content)


if __name__ == '__main__':
    # code = ['0192', '0205', '0206', '0207', '0217', '0222', '0227', '0241', '0206']
    # for i in code:
    #     data = requests.get(
    #         f'http://192.168.50.100:3018/api/v1/chejian?cityCode=3701&generateDate=2021-03-16&deviceType=chayan&zhaoPianLeiXing={i}')
    #     for picture in json.loads(data.text)['data']:
    #         dirName = rf'F:\picture\{i}'
    #         if not os.path.isdir(dirName):
    #             os.makedirs(dirName)
    #         fileName = os.path.join(dirName, os.path.basename(picture))
    #         print(fileName)
    #         create_file(fileName)
    #         urldownload(picture, fileName)
    urls = 'http://192.168.90.10:7002/rawdata/chayan/photos/3701/2021-03-16/0101_A001LS_LGBM4AE49GS320240'
    urldownload(urls, r'F:\chejian\济南查验20210322\0101_A001LS_LGBM4AE49GS320240')