# -*- codeing = utf-8 -*-
# @Time :2020/8/5 16:49
# @Author:Eric
# @File : test04.py
# @Software: PyCharm
import requests
from chardet import detect
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1596532129,1597288096,1597305671,1597305767; Hm_lpvt_9f8bda7a6bb3d1d7a9c7196bfed609b5=1597309892",
    "Host": "www.ccgp.gov.cn",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}


def get_url_table(url):
    reponse = urllib.request.urlopen(url)
    only_fist_table_tags = SoupStrainer('table',
                                        attrs={"width": "600", "border": "0", "cellspacing": "1", "bgcolor": "#bfbfbf",
                                               "style": "text-align:left;"})  # 截取隐藏
    bs = BeautifulSoup(reponse.read().decode('utf-8'), 'html.parser', parse_only=only_fist_table_tags)
    lis_str_data = []
    for item in bs.find_all('td'):
        lis_str_data.append(item.text)
    zz_money = lis_str_data[lis_str_data.index('总中标金额') + 1]
    cglx_money = lis_str_data[lis_str_data.index('采购单位联系方式') + 1]
    print(zz_money, cglx_money)


lis_str = []


def for_list(list_x):
    for x in list_x:
        if len(x) > 1:
            for_list(x)
        else:
            # 过滤所有标签
            pattern = re.compile("<(.*?)>")
            sub_str = re.sub(pattern, "", str(x))
            if (bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str))):
                if bool(re.compile(u'采购|联系|中标|电话|传真|成交').search(sub_str)):
                    lis_str.append(sub_str)


def get_url_text(url):
    p_x_list = []
    reponse = requests.get(url=url, headers=headers)
    reponse.encoding = 'utf-8'
    # reponse = urllib.request.urlopen(url.strip())
    only_text_tags = SoupStrainer('div', attrs={"class": "vF_detail_content_container"})
    only_text2 = SoupStrainer('table', attrs={"class": "MsoNormalTable", "border": "1"})
    # p_x_list = BeautifulSoup(reponse.read().decode('utf-8'), 'html.parser', parse_only=only_text2)
    print(reponse.text)
    # p_x_list = BeautifulSoup(reponse.text, 'html.parser')
    # for x in p_x_list:
        # pattern = re.compile("<(.*?)>")
        # sub_str = re.sub(pattern, "", str(x))
        # #     print(sub_str.text)
        # if (bool(re.compile(u'[\u4e00-\u9fa5]').search(str(sub_str))) or bool(
        #         re.search(r'\d', str(sub_str)))):
        #     if bool(re.compile(u'采购|联系|中标|电话|传真|成交').search(str(sub_str))):
        # print(x.text)


# for_list(p_x_list)


lis_url_str = []
if __name__ == '__main__':
    url = 'http://www.ccgp.gov.cn/cggg/dfgg/zbgg/202008/t20200813_14829965.htm'.strip()
    get_url_text(url)
    for i in lis_str:
        print(i)
    # lis_url_str.append(dl_name)
    # lis_url_str.append(dl_numb)
    # lis_strs.append(lis_url_str)

# lisUrls = []
# with open('C:/Users/标注/Desktop/test/cleardata/数据集.txt', 'r', encoding='utf-8') as fo:
#     lisUrls = fo.read().splitlines()
# test = pd.DataFrame(data=lis_str)
# file_name = 'C:/Users/标注/Desktop/test/test/01.txt'
# test.to_string(file_name, encoding='utf-8')
