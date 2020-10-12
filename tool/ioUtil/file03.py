# -*- codeing = utf-8 -*-
# @Time :2020/8/4 10:28
# @Author:Eric
# @File : file03.py
# @Software: PyCharm
import re
import pandas as pd

if __name__ == '__main__':
    lisUrls = []
    # with open('C:/Users/标注/Desktop/test/数据/数据集.txt', 'r', encoding='utf-8') as fo:
    with open('C:/Users/标注/Desktop/test/车管所01.txt', 'r', encoding='utf-8') as fo:
        lisUrls = fo.read().splitlines()
        lisUrls = sorted(set(lisUrls), key=lisUrls.index)
    cg_datas = []  # 车管所
    dsg_datas = []  # 大数据局
    jg_datas = []  # 交管局
    jgzd_datas = []  # 交警支队
    wx_datas = []  # 无效数据
    # 1、遍历数据集 1756条
    for i in range(len(lisUrls)):
        lis_one_str = lisUrls[i].split('\t')  # list：读取文件中每一条数据
        jg_datas.append(lis_one_str)
        # lx_numb = lis_one_str[-1].strip()
        # if bool(re.search(r'\d', lx_numb)):
        #     if '交警支队' in lis_one_str[-1]:
        #         jgzd_datas.append(lis_one_str)
        #     elif '车管所' in lis_one_str[-1]:
        #         cg_datas.append(lis_one_str)
        #     elif '大数据局' in lis_one_str[-1]:
        #         dsg_datas.append(lis_one_str)
        #     elif '交管局' in lis_one_str[-1]:
        #         jg_datas.append(lis_one_str)
        # else:
        #     wx_datas.append(lis_one_str)

    # datas = {'车管所':cg_datas,'大数据局':dsg_datas,'交管局':jg_datas,'交警支队':jgzd_datas,'无效数据':wx_datas}
    datas = {'车管所01': jg_datas}
    for i in datas.keys():
        file_name = 'C:/Users/标注/Desktop/test/cleardata/' + i + '.csv'
        test = pd.DataFrame(data=datas[i])
        try:
            test.to_csv(file_name, encoding='gbk')
        except Exception:
            test.to_csv(file_name, encoding='gb18030')
