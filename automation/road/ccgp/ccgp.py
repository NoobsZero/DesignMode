# -*- encoding:utf-8 -*-
"""
@File   :ccgp.py
@Time   :2020/12/23 12:29
@Author :Chen
@Software:PyCharm
"""
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import re
from bs4 import BeautifulSoup
from lxml import etree
import requests
from tomorrow import threads


def get_url_text(url):
    proxy_data = [
        '--proxy=%s' % '61.135.185.152:80',  # 设置的代理ip
        '--proxy-type=http',  # 代理类型
        '--ignore-ssl-errors=true',  # 忽略https错误
    ]
    reponse = requests.get(url=url, property=proxy_data)
    reponse.encoding = 'utf-8'
    html = etree.HTML(reponse.text)
    html_data = html.xpath('/html/body/div[2]/div/div[2]/div/div[2]/table/tr')
    ccgp = {}
    index = 0
    for i in html_data:
        index += 1
        name = i.xpath('td[1]/text()')
        data = i.xpath('td[2]/text()')
        if name != [] and data == []:
            ccgp[name[0]] = '无'
        elif name and data != []:
            ccgp[name[0]] = data[0]
        if index == 5:
            name = i.xpath('td[3]/text()')
            data = i.xpath('td[4]/text()')
            if name != [] and data == []:
                ccgp[name[0]] = '无'
            elif name and data != []:
                ccgp[name[0]] = data[0]
    return ccgp


lis_str = []

def for_list(list_x):
    list_x = list_x.splitlines()
    for x in list_x:
        pattern = re.compile("<(.*?)>")
        sub_str = re.sub(pattern, "", str(x))
        if bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str)):
            if bool(re.compile(u'供应商名称|公司|中心').search(sub_str)) and not bool(re.compile(u'地址|代理|编码').search(sub_str)):
                lis_str.append(sub_str.strip())
        # if len(x) > 1:
        #     for_list(x)
        # else:
        #     # 过滤所有标签
        #     pattern = re.compile("<(.*?)>")
        #     sub_str = re.sub(pattern, "", str(x))
        #     if bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str)):
        #         # if bool(re.compile(u'供应商').search(sub_str)):
        #         lis_str.append(sub_str)


def get_url_lis(url):
    p_x_list = []
    reponse = urllib.request.urlopen(url.strip())
    only_a_tags = SoupStrainer('tbody', attrs={"class": "table","style": "display: block;"})
    only_text_tags = SoupStrainer('div', attrs={"class": "vF_detail_content_container"})
    p_x_list = BeautifulSoup(reponse.read().decode('utf-8'), 'html.parser')
    for_list(p_x_list.prettify()) # 美化


if __name__ == '__main__':
    url = 'http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202006/t20200619_14509569.htm'.strip()
    get_url_lis(url)
    # for i in lis_str:
    #     print(i)
    gys = [i for i in lis_str if '供应商' in i][0]
    gs = [i for i in lis_str[lis_str.index(gys):] if '公司' in i or '中心' in i][0]
    print(gys, gs)
    # for i in lis_str:
    #     print(i)


