# -*- codeing = utf-8 -*-
# @Time :2020/8/3 18:57
# @Author:Eric
# @File : reptileHtmlToCSV.py
# @Software: PyCharm
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == '__main__':
    lisUrls = []
    with open('C:/Users/标注/Desktop/test/车管所01.txt', 'r', encoding='utf-8') as fo:
        lisUrls = fo.read().splitlines()
        # lis_strs = []
        # 1、遍历数据集
        # for i in range(len(lisUrls)):
        #     lis_url_str = lisUrls[i].split('\t')  # list：读取文件中第一条数据
        #     url = lis_url_str[-2].strip()
        #     lis_strs.append(url)
        lis_strs1 = sorted(set(lisUrls),key=lisUrls.index)
            # reponse = urllib.request.urlopen(url)
            # bs = BeautifulSoup(reponse.read().decode('utf-8'), 'html.parser')
            # lis_str = []
            # try:
            #     for item in bs.table.find_all('td'):
            #         lis_str.append(item.text)
            #     dl_name = lis_str[lis_str.index('代理机构名称') + 1]
            #     dl_numb = lis_str[lis_str.index('代理机构联系方式') + 1]
            #     lis_url_str.append(dl_name)
            #     lis_url_str.append(dl_numb)
            #     lis_strs.append(lis_url_str)
            # except Exception:
            #     try:
            #         index = 0
            #         for item in bs.find_all('div', style='TEXT-ALIGN: left; LINE-HEIGHT: 28pt; TEXT-INDENT: 24pt'):
            #             param = str(item.text).split('：')[-1]
            #             if '采购代理机构：' in item.text and index == 0:
            #                 cg_name = param
            #                 index = 1
            #             elif '项目联系人：' in item.text and index == 1:
            #                 xm_name = param
            #                 index = 2
            #             elif '联系电话：' in item.text and index == 2:
            #                 lx_numb = param
            #                 index = 0
            #         lis_url_str.append(cg_name)
            #         lis_url_str.append(xm_name + ' ' + lx_numb)
            #         lis_strs.append(lis_url_str)
            #     except Exception:
            #         lis_url_str.append('')
            #         lis_url_str.append('')
            #         lis_strs.append(lis_url_str)
            #         print(url)
            # finally:
            #     lis_str.clear()
        for i in lis_strs1:
            print(i)
        # file_name = 'C:/Users/标注/Desktop/test/大数据局01.csv'
        # # # name = ['代理机构名称', '代理机构联系方式']
        # # test = pd.DataFrame(columns=name, data=lis_strs)  # 数据有三列，列名分别为one,two,three
        # test = pd.DataFrame(data=lis_strs1)  # 数据有三列，列名分别为one,two,three
        # test.to_csv(file_name, encoding='gbk')
