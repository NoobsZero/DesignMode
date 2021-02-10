# -*- encoding:utf-8 -*-
"""
@File   :weifa_Change_name.py
@Time   :2021/2/1 14:47
@Author :Chen
@Software:PyCharm
"""
import os
import re
import shutil
import pandas


def get_filelist(dir, fileCondition='', topdown=True):
    """
            递归获取目录下所有后缀为suffix的路径
        :param fileCondition:后缀为(zip:压缩包, sql:sql文件, suffix:jpg路径和非jpg文件路径, '':所有文件路径)
        :param dir: 指定URL是目录（'dir'）
        :return: Filelist:list URL集合
        """
    Filelist = []
    suffix = ['.ini', '.local', 'log', '.log', '.DAT', '.xlsx', '.z01', '.json', '.rar', '.zip', '.cer', '.py', '.exe',
              '.sh',
              '.txt',
              '.html', '.dll', '.h', '.c',
              '.cpl', '.jsa', '.md', '.properties', '.jar', '.data', '.bfc', '.src', '.ja', '.dat', '.cfg',
              '.pf', '.gif', '.ttf', '.jfc', '.access', '.template', '.certs', '.policy', '.security', '.libraries',
              '.sym', '.idl', '.lib', '.clusters', '.conf', '.xml', '.tar', '.gz', '.csv', '.sql', '.xml_hidden',
              '.lic']
    list_jpg_dir = []
    for home, dirs, files in os.walk(dir, topdown=topdown):
        for filename in files:
            # 文件名列表，包含完整路径
            if fileCondition is 'zip':
                if filename.endswith('.rar') or filename.endswith('.gz') or filename.endswith('.tar') or \
                        os.path.splitext(filename)[-1].endswith('.z', 0, 2) and (
                        'sql' not in filename):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'sql':
                if filename.endswith('.sql'):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'rar':
                if filename[-3:] == 'rar':
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'suffix':
                if os.path.splitext(filename)[1] in suffix or filename[-3:] in suffix:
                    Filelist.append(os.path.join(home, filename))
                elif home not in list_jpg_dir:
                    list_jpg_dir.append(home)
            elif fileCondition is '':
                Filelist.append(os.path.join(home, filename))
    if fileCondition is 'suffix':
        return Filelist, list_jpg_dir
    else:
        return Filelist


if __name__ == '__main__':
    # uuid	设备编号	号牌号码	违法地址	违法时间	违法类型代码	图片名称1	图片名称2	图片名称3	图片名称4	算法结果	人工结果
    # uuid	设备编号	号牌号码	违法地址	违法时间	违法类型代码	图片名称	算法结果	人工结果
    # 829457	441938000000023270	粤S2MZ95	441938000000023270-八一路光明二路路口北往南（卡口）	2021/2/2 18:08:27	1223	/violation/20210202/733fb035-cede-4408-aec9-93e6f0982d9c.jpg	违法
    weifa_path = r'E:\chejian\误识别\识别.xlsx'
    # 显示所有列
    pandas.set_option('display.max_columns', None)
    # 显示所有行
    pandas.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pandas.set_option('max_colwidth', 1000)
    weifa_pd = pandas.read_excel(weifa_path)
    weifa_tupian_lis = [i for i in list(weifa_pd) if '图片名称' in i]
    weifa_tupian = weifa_pd[weifa_tupian_lis].stack().reset_index(level=1)
    weifa_tupian.columns = ['图片ID', '图片名称']
    weifa_pd = weifa_pd.drop(weifa_tupian_lis, axis=1).join(weifa_tupian)
    weifa_pd = weifa_pd.reindex(
        columns=['uuid', '设备编号', '号牌号码', '违法类型代码', '车牌类型', '违法时间', '人工结果', '图片ID', '图片名称']).astype(
        str)
    weifa_pd.loc[:, '违法时间'] = weifa_pd['违法时间'].apply(lambda x: re.sub(r':| ', '#', x))
    weifa_pd.loc[:, '人工结果'] = weifa_pd['人工结果'].apply(
        lambda x: str(x.replace('nan', '0').replace('不违法', '2').replace('未违法', '2').replace('违法', '1')))
    weifa_pd.loc[:, '图片ID'] = weifa_pd['图片ID'].apply(lambda x: 'a' + str(re.sub(r'\D', '', x)))
    weifa_pd.loc[:, '新图片名称'] = weifa_pd['违法类型代码'] + '\\' + weifa_pd['设备编号'] + '\\' + weifa_pd['设备编号'] + '+' + weifa_pd[
        '号牌号码'] + '+' + weifa_pd['违法类型代码'] + '+' + weifa_pd['设备编号'] + '+' + \
                               weifa_pd[
                                   '车牌类型'] + '+0+@' + weifa_pd['uuid'] + '@@@' + weifa_pd['违法时间'] + '+' + weifa_pd[
                                   '图片ID'] + '+' + weifa_pd[
                                   '人工结果'] + '.jpg'
    weifa_pd.loc[:, '新图片名称'] = weifa_pd['新图片名称'].apply(lambda x: x.replace('nan', ''))
    weifa_pd = weifa_pd.reindex(columns=['图片名称', '新图片名称'])
    weifa_pd.loc[:, '图片名称'] =weifa_pd['图片名称'].apply(lambda x: os.path.split(x)[-1])
    weifa_pd_index_lis = weifa_pd.index.tolist()
    for i in [i for i in weifa_pd_index_lis if weifa_pd_index_lis.count(i) < 2]:
        weifa_pd.loc[i, '新图片名称'] = weifa_pd.loc[i, '新图片名称'].replace('a', 'a0').replace('a1', 'a0')
    weifa_pd_dic = weifa_pd.set_index("图片名称").to_dict()["新图片名称"]
    file_dir = r'E:\chejian\误识别\get_pic'
    # Filelist = get_filelist(file_dir)
    # for i in Filelist:
    #     try:
    #         file_name = os.path.split(i)[-1]
    #         file_name_old = i
    #         file_name_new = os.path.join(file_dir, weifa_pd_dic[file_name])
    #         file_path_new = os.path.split(file_name_new)[0]
    #         if not os.path.isdir(file_path_new):
    #             os.makedirs(file_path_new)
    #         shutil.move(file_name_old, file_name_new)
    #         print(file_name_old, 'to', file_name_new)
    #     except Exception as e:
    #         continue
    # 写到xlsx文件
    # writer = pandas.ExcelWriter('my.xlsx')
    # weifa_pd.to_excel(writer, float_format='%.5f')
    # writer.save()
