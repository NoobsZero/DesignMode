# encoding: utf-8
"""
@file: ProxyPool.py
@time: 2021/3/5 9:49
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
https://github.com/Python3WebSpider/ProxyPool
"""
import requests
from random import choice


class ProxyPool(object):

    def __init__(self, proxypool_url, target_url='https://www.baidu.com/'):
        self.proxypool_url = proxypool_url
        self.target_url = target_url
        self.proxy = None
        self.response = self.crawl()

    def get_random_proxy(self):
        return requests.get(self.proxypool_url).text.strip()

    def crawl(self):
        while True:
            proxy = self.get_random_proxy()
            response = requests.get(url=self.target_url, proxies=eval(proxy))
            if response.status_code == 200:
                self.proxy = proxy
                print('get random proxy', proxy)
                return response


class ProxyMiddleware(object):

    def __init__(self, file_url, target_url='https://www.baidu.com/'):
        self.file_url = file_url
        self.target_url = target_url
        self.proxy = None
        self.process_request()

    def process_request(self):
        # 以下为：1、从csv中读取代理IP 2、验证IP请求指定网址返回状态码是否为200
        proxy_list = self.get_random_proxy()
        proxy_ip = choice(proxy_list).strip()
        self.verify_net(proxy_ip, proxy_list)

    def verify_net(self, proxy_ip, proxy_list):
        # 验证代理IP是否适合指定的爬虫网站
        proxies = {proxy_ip.split("://")[0]: proxy_ip.split("://")[1]}
        conn = requests.get(self.target_url, proxies=proxies, verify=False)
        res = conn.status_code
        print(res)
        if res == 200:
            self.proxy = proxy_ip
        else:
            proxy_ip = choice(proxy_list).strip()
            self.verify_net(proxy_ip, proxy_list)

    def get_random_proxy(self):
        with open(self.file_url) as f:
            proxies = f.readlines()
        return proxies


if __name__ == '__main__':
    # url = 'http://product.weather.com.cn/alarm/grepalarm_cn.php?_=%d' % get_stamp13()
    # print(url)
    print(ProxyPool('https://poi.mapbar.com/baoding/GA0/').response)


