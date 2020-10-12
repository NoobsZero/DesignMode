# -*- codeing = utf-8 -*-
# @Time :2020/8/6 12:12
# @Author:Eric
# @File : test05.py
# @Software: PyCharm
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import re

lis_str = []

def for_list(list_x):
    for x in list_x:
        if len(x) > 1:
            for_list(x)
        else:
            # 过滤所有标签
            pattern = re.compile("<(.*?)>")
            sub_str = re.sub(pattern, "", str(x))
            if bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str)):
                if bool(re.compile(u'采购|联系|中标|电话|传真|成交').search(sub_str)):
                    lis_str.append(sub_str)


def get_url_lis(url):
    p_x_list = []
    reponse = urllib.request.urlopen(url.strip())
    only_a_tags = SoupStrainer('div', attrs={"class": "vF_detail_content_container"})
    p_x_list = BeautifulSoup(reponse.read().decode('utf-8'), 'html.parser', parse_only=only_a_tags)
    for_list(p_x_list)


if __name__ == '__main__':
    url = 'http://www.ccgp.gov.cn/cggg/dfgg/zbgg/201706/t20170616_8393462.htm'
    get_url_lis(url)
    for i in lis_str:
        print(i)
