# encoding: utf-8
"""
@file: chejianQuery.py
@time: 2021/3/22 10:26
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import requests
from tool.mydbUtil.common.baseDBOperate import OperateDB


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
              '.lic', '.docx']
    list_jpg_dir = []
    for home, dirs, files in os.walk(dir, topdown=topdown):
        for filename in files:
            # 文件名列表，包含完整路径
            if fileCondition == 'zip':
                if filename.endswith('.rar') or filename.endswith('.gz') or filename.endswith('.tar') or \
                        os.path.splitext(filename)[-1].endswith('.z', 0, 2) and (
                        'sql' not in filename):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition == 'sql':
                if filename.endswith('.sql'):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition == 'rar':
                if filename[-3:] == 'rar':
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition == 'suffix':
                if len([i for i in suffix if i in os.path.splitext(filename)[1] or filename[-3:] in i]) > 0:
                    Filelist.append(os.path.join(home, filename))
                elif home not in list_jpg_dir:
                    list_jpg_dir.append(home)
            elif fileCondition == '':
                Filelist.append(os.path.join(home, filename))
    if fileCondition == 'suffix':
        return Filelist, list_jpg_dir
    else:
        return Filelist


def urldownload(url, filename=None):
    """
    下载文件到指定目录
    :param url: 文件下载的url
    :param filename: 要存放的目录及文件名，例如：./test.xls
    :return:
    """
    down_res = requests.get(url)
    if not os.path.isdir(os.path.split(filename)[0]):
        os.makedirs(os.path.split(filename)[0])
    with open(filename, 'wb') as file:
        file.write(down_res.content)


def test():
    db = 'emTest_cj_vehicle_20210105'
    dbHandle = OperateDB(r'G:\JetBrains\PycharmProjects\untitled\source\db.conf.json', renameDb=db)
    result = dbHandle.select('SELECT localPath FROM emTest_cj_vehicle_20210105.photo_info;')
    for photo in [list(i)[0] for i in result]:
        print('http://192.168.90.10:7002/rawdata/chayan/photos/3701' + photo)
        print(r'F:\chejian\济南查验20210322' + '\emTest_chayan_3701_20210317' + str(photo).replace('/', '\\'))
        urldownload('http://192.168.90.10:7002/rawdata/chayan/photos/3701' + photo,
                    r'F:\chejian\济南查验20210322' + '\emTest_chayan_3701_20210317' + str(photo).replace('/', '\\'))


if __name__ == '__main__':
    # "truncate table emTest_cj_vehicle_20210105.chaYanVehicle_info;"
    # "truncate table emTest_cj_vehicle_20210105.photo_info;"
    test()
    # code = ['0192', '0205', '0206', '0207', '0217', '0222', '0227', '0241', '0206']
    # dbNames = ['emTest_chayan_3701_20210317']
    # # dbNames = ['emTest_chayan_3701_20210311', 'emTest_chayan_3701_20210310', 'emTest_chayan_3701_20210316',
    # #            'emTest_chayan_3701_20210308', 'emTest_chayan_3701_20210304', 'emTest_chayan_3701_20210108',
    # #            'emTest_chayan_3701_20201209', 'emTest_chayan_3701_20201207', 'emTest_chayan_3701_20201201',
    # #            'emTest_chayan_3701_20201130' 'emTest_chayan_3701_20210317']
    # # tableNames = ['chaYanVehicle_info', 'photo_info']
    # sqlInfos = {}
    # cheLiangUids = {}
    # for db in dbNames:
    #     infos = []
    #     for i in code:
    #         infos.append(
    #             "SELECT distinct cheLiangUid FROM {}.{} WHERE localPath LIKE '%{}%';".format(db, 'photo_info', i))
    #     sqlInfos[db] = infos
    # for db in sqlInfos:
    #     dbHandle = OperateDB(r'G:\JetBrains\PycharmProjects\untitled\source\db.conf.json', renameDb=db)
    #     cheLiangUidLis = []
    #     for sqlInfo in sqlInfos[db]:
    #         result = dbHandle.select(sqlInfo)
    #         cheLiangUidLis += [list(i)[0] for i in result]
    #     cheLiangUids[db] = list(set(cheLiangUidLis))
    # infodata = {}
    # for db in cheLiangUids:
    #     dbHandle = OperateDB(r'G:\JetBrains\PycharmProjects\untitled\source\db.conf.json', renameDb=db)
    #     # dataLis = []
    #     for cheLiangUid in cheLiangUids[db]:
    #         sqlPhoto = "INSERT INTO emTest_cj_vehicle_20210105.photo_info SELECT * FROM {}.photo_info WHERE cheLiangUid='{}';".format(
    #             db, cheLiangUid)
    #         sqlChaYanVehicle = "INSERT INTO emTest_cj_vehicle_20210105.chaYanVehicle_info SELECT * FROM {}.chaYanVehicle_info WHERE UUID='{}';".format(
    #             db, cheLiangUid)
    #         print(sqlPhoto)
    #         print(sqlChaYanVehicle)
    #         with open('F:\chejian\济南查验20210322\{}\{}.txt'.format(db, db), 'a', encoding='utf-8', errors="ignore") as fo:
    #             fo.write(sqlPhoto + '\n')
    #             fo.write(sqlChaYanVehicle + '\n')
    #             fo.flush()
