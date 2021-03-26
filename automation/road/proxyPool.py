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

from tool.mytimeUtil.dataTime import get_stamp13


class ProxyPool(object):

    def __init__(self, target_url='https://www.baidu.com/'):
        self.proxypool_url = 'http://192.168.50.149:5010/get/'
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


if __name__ == '__main__':
    # url = 'http://product.weather.com.cn/alarm/grepalarm_cn.php?_=%d' % get_stamp13()
    # print(url)
    print(ProxyPool('https://poi.mapbar.com/baoding/GA0/').response)


