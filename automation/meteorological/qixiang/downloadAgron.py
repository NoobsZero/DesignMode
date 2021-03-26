# encoding: utf-8
"""
@file: downloadAgron.py
@time: 2021/3/23 14:35
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import requests
import time


# 进度条模块
from tomorrow import threads


def progressbar(url, path, file_name):
    '''
    url:下载链接
    path:存储路径
    file_name:文件名
    需要的包为：os,requests,time
    '''
    if not os.path.exists(path):  # 看是否有该文件夹，没有则创建文件夹
        os.mkdir(path)
    start = time.time()  # 下载开始时间
    response = requests.get(url, stream=True)
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:  # 判断是否响应成功
            print('Start download' + file_name + '[File size]:{size:.2f} MB'.format(
                size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小
            filepath = path + file_name
            with open(filepath, 'wb') as file:  # 显示进度条
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    print('\r' + '[下载进度]:%s%.2f%%' % (
                    '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
            end = time.time()  # 下载结束时间
        print('Download completed!,times: %.2f秒' % (end - start))  # 输出下载用时时间
    except:
        print('Error!')


@threads(5)
def main(file_url):
    # 下载皮卡丘图片
    # file_url = ['https://mrms.agron.iastate.edu/2020/10/14/2020101400.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101401.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101402.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101403.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101404.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101405.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101406.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101407.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101408.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101409.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101410.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101411.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101412.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101413.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101414.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101415.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101416.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101417.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101418.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101419.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101420.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101421.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101422.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/14/2020101423.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101500.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101501.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101502.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101503.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101504.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101505.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101506.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101507.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101508.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101509.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101510.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101511.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101512.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101513.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101514.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101515.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101516.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101517.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101518.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101519.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101520.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101521.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101522.zip',
    #             'https://mrms.agron.iastate.edu/2020/10/15/2020101523.zip']

    file_path = 'C:\\qixiang\\'
    file_name = file_url.split('/')[-1]
    progressbar(file_url, file_path, file_name)


if __name__ == '__main__':
    file_url = [
                'https://mrms.agron.iastate.edu/2020/10/14/2020101413.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101414.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101415.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101416.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101417.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101418.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101419.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101420.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101421.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101422.zip',
                'https://mrms.agron.iastate.edu/2020/10/14/2020101423.zip']
    for file in file_url:
        main(file)

