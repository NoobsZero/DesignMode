# encoding: utf-8
"""
@file: threadTest02.py
@time: 2021/6/9 10:39
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
# coding=utf-8
import time, json
import requests
import threading
from contextlib import closing
# 导入包，配合队列实现线程池
from threading import Thread
from queue import Queue

# windows路径
from tool.threadUtil.myThread import ThreadPool

dir_name = 'F:\\chejian\\img\\file'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}


# 下载图片
def DownloadImg(img_url, dir_name, img_name):
    try:
        with closing(requests.get(img_url, headers=headers, stream=True, timeout=20)) as r:
            rc = r.status_code
            if 299 < rc or rc < 200:
                print('returnCode%s\t%s' % (rc, img_url))
                return
            content_length = int(r.headers.get('content-length', '0'))
            if content_length == 0:
                print('size0\t%s' % img_url)
                # return
            try:
                with open(dir_name + img_name, 'wb') as f:
                    for data in r.iter_content(1024):
                        f.write(data)
                    print('==========图片下载成功=========')
            except:
                print('保存失败可能含有特殊字符 \t%s' % img_url + '\n' + '失败图片已保存到"失败图片.csv"')
    except:
        print('图片下载失败可能网络问题 \t%s' % img_url + '\n' + '失败图片已保存到"失败图片.csv"')


# def download_img(img_url, img_name):# 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
#     r = requests.get(img_url, headers=headers, stream=True)
#     print(r.status_code) # 返回状态码
#     if r.status_code == 200:
#         open('D:\\01llg\\zazzle\\img\\'+img_name, 'wb').write(r.content) # 将内容写入图片
#         print("done")
#     del r

# 进入首页取页码
def by_to_zazzle(url_one):
    rs = requests.get(url_one, verify=False)
    tags_data = json.loads(rs.text)
    url_img = tags_data['data']
    for x in url_img:
        url_one = x['img']
        img_name = url_one.split('-')[1]
        thread.apply_async(func=DownloadImg, args=(url_one, dir_name, img_name))
        # download_img(url_one, img_name)
        # thread = MyThread(url_one,dir_name,img_name)
        # thread.start()
        # thread.join()
        # if i%50 == 0:
        # 	time.sleep(10)


if __name__ == '__main__':
    url = 'http://192.168.50.100:3020/api/project/wallhaven_cc'
    thread = ThreadPool(6)
    by_to_zazzle(url)
    thread.join()
# for key in keywords:
# 	url = 'https://www.zazzle.com/s/'+key
# 	by_to_zazzle(url,key)