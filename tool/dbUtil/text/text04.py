# -*- encoding:utf-8 -*-
"""
@File   :text04.py
@Time   :2021/1/13 11:28
@Author :Chen
@Software:PyCharm
"""
import os
import random
import shutil
from ast import literal_eval

# def get_filelist(dir, fileCondition=''):
#     """
#             递归获取目录下所有后缀为jpg的路径
#         :param fileCondition:
#         :param dir: 指定URL是目录（'dir'）
#         :return: Filelist:list URL集合
#         """
#     Filelist = []
#     Dirlist = []
#     suffix = ['log', '.log', '.DAT', '.xlsx', '.z01', '.json', '.rar', '.zip', '.cer', '.py', '.exe', '.sh', '.txt',
#               '.html', '.dll', '.h', '.c',
#               '.cpl', '.jsa', '.md', '.properties', '.jar', '.data', '.bfc', '.src', '.ja', '.dat', '.cfg',
#               '.pf', '.gif', '.ttf', '.jfc', '.access', '.template', '.certs', '.policy', '.security', '.libraries',
#               '.sym', '.idl', '.lib', '.clusters', '.conf', '.xml', '.tar', '.gz', '.csv', '.sql', '.xml_hidden',
#               '.lic']
#     jpglist = []
#     for home, dirs, files in os.walk(dir):
#         for filename in files:
#             # 文件名列表，包含完整路径
#             if fileCondition is 'zip':
#                 if filename[-3:] == 'rar' or filename[-3:] == '.gz' or filename[-3:] == 'tar' or filename[
#                                                                                                  -3:] == 'zip' and (
#                         'sql' not in filename):
#                     Filelist.append(os.path.join(home, filename))
#             elif fileCondition is 'sql':
#                 if 'sql' in filename:
#                     Filelist.append(os.path.join(home, filename))
#             elif fileCondition is 'rar':
#                 if filename[-3:] == 'rar':
#                     Filelist.append(os.path.join(home, filename))
#             elif fileCondition is 'if':
#                 if os.path.splitext(filename)[1] in suffix or filename[-3:] in suffix:
#                     Dirlist.append(home)
#                     Filelist.append(os.path.join(home, filename))
#                 else:
#                     jpglist.append(home)
#             elif fileCondition is '':
#                 Filelist.append(os.path.join(home, filename))
#     if len(jpglist) != 0:
#         print('------------------输出jpg目录结构-------------------------------')
#         for _ in list(set(jpglist)):
#             print(_)
#         print('------------------------------------------------------------')
#     if len(Dirlist) != 0:
#         print('------------------输出非jpg目录结构-------------------------------')
#         for i in list(set(Dirlist)):
#             print(i)
#         print('------------------------------------------------------------')
#     return Filelist


# def moveFileToDir(infile, todir):
#     sqlList = get_filelist(todir)
#     if not os.path.isdir(todir):
#         os.mkdir(todir)
#     newSql = os.path.join(todir, os.path.split(infile)[1])
#     if newSql in sqlList:
#         name = os.path.split(infile)[1].split('.')
#         newSql = os.path.join(todir, ".".join(["".join(name[0:-1]) + '_' + str(random.randint(0, 1000)), name[-1]]))
#         os.renames(infile, newSql)
#     else:
#         shutil.move(infile, newSql)
#     return newSql


# def typeof(variate):
#     type = None
#     if isinstance(variate, int):
#         type = "int"
#     elif isinstance(variate, str):
#         type = "str"
#     elif isinstance(variate, float):
#         type = "float"
#     elif isinstance(variate, list):
#         type = "list"
#     elif isinstance(variate, tuple):
#         type = "tuple"
#     elif isinstance(variate, dict):
#         type = "dict"
#     elif isinstance(variate, set):
#         type = "set"
#     return type


table_infos_new_dic = {'UUID': 'id', 'cheLiangUid': 'vehicle_check_id', 'zhaoPianLeiXing': 'category',
                       'localPath': 'name', 'jieGuo': 'result', 'shuoMing': 'reason', 'inDbTime': 'created_at'}
table_checks_new_dic = {'UUID': 'id', 'liuShuiHao': 'jylsh', 'jianYanJiGouBianHao': 'jyjgbh', 'jianYanLeiBie': 'jylb',
                        'haoPaiZhongLei': 'hpzl', 'chePaiHao': 'hphm', 'cheJiaHao': 'clsbdh', 'shiYongRen': 'syr',
                        'shouJiHaoMa': 'sjhm', 'shengXiaoRiQi': 'sxrq', 'zhongZhiRiQi': 'zzrq',
                        'cheLiangLeiXing': 'cllx', 'shiYongXingZhi': 'syxz', 'zhengBeiZhiLiang': 'zbzl',
                        'jianYanKaiShiShiJian': 'kssj', 'jianYanJieShuShiJian': 'jssj', 'faDongJiHao': 'fdjh',
                        'cheLiangPinPai': 'clpp', 'cheLiangXingHao': 'clxh', 'chuCiDengJiRiQi': 'ccdjrq',
                        'zhiZaoRiQi': 'ccrq', 'cheLiangWaiGuanJianYanYuan': 'wgjcjyy',
                        'xingShiZhengXinBianHao': 'xszbh', 'faZhengRiQi': 'fzrq', 'ranLiangZhongLei': 'rlzl',
                        'xuYaoDuiBiZhaoPianZongShu': 'zpzs', 'xuYaoDuiBiShiPinZongShu': 'spzs',
                        'duiBiBuHeGeShu': 'bdbhgs', 'cheLiangYanSe': 'csys', 'paiLiang': 'pl', 'gongLv': 'gl',
                        'zhuanXiangXingShi': 'zxxs', 'cheWaiKuoChang': 'cwkc', 'cheWaiKuoKuan': 'cwkk',
                        'cheWaiKuoGao': 'cwkg', 'huoXiangNeiBuChangDu': 'hxnbcd', 'huoXiangNeiBuKuanDu': 'hxnbkd',
                        'huoXiangNeiBuGaoDu': 'hxnbgd', 'gangBanTanPianShu': 'gbthps', 'zhouShu': 'zs', 'zhouJu': 'zj',
                        'qianLunJu': 'qlj', 'houLunJu': 'hlj', 'lunTaiGuiGe': 'ltgg', 'lunTaiShu': 'lts',
                        'zongZhiLiang': 'zzl', 'heDingZaiZhiLiang': 'hdzzl', 'heDingZaiKeShu': 'hdzk',
                        'zhunQianYinZhiLiang': 'zqyzl', 'jiaShiShiQianPaiZaiKeRenShu': 'qpzk',
                        'jiaShiShiHouPaiZaiKeRenShu': 'hpzk', 'cheLiangYongTu': 'clyt', 'yongTuShuXing': 'ytsx',
                        'shiFouXinNengYuanQiChe': 'sfxny', 'xinNengYuanZhongLei': 'xnyzl', 'yanYnaYouXiaoQiZhi': 'yxqz',
                        'faZhengJiGuan': 'fzjg', 'huanBaoDaBiaoQingKuang': 'hbdbqk', 'qiangZhiBaoFeiQiZhi': 'qzbfqz',
                        'guanLiXiaQu': 'xzqh', 'guoChanJinKou': 'gcjk', 'diYanBiaoJi': 'dybj', 'zhiZaoGuo': 'zzg',
                        'yinWenPinPai': 'clpp2', 'jianYanHeGeBiaoJi': 'jyhgbzbh', 'shiFouMianJian': 'sfmj',
                        'jiDongCheZhuangTai': 'zt', 'zuiJinDingJianRiQi': 'djrq', 'zhuSuoDiZhiXingZhengQuHua': 'zsxzqh',
                        'lianXiDiZhiXingZhengQuHua': 'zzxzqh', 'faDongJiXingHao': 'fdjxh',
                        'shiGuSunShangBuWeiQingKuang': 'sgcssbwqk', 'buMianJianYuanYin': 'bmjyy', 'guanLiBuMen': 'glbm',
                        'zhiZaoChangMingCheng': 'zzcmc', 'jianYanLiuShuiHao': 'jylsh2',
                        'downloadVideoState': 'is_video_check', 'isRepeat': 'station_status',
                        'centerStatus': 'center_status', 'isPass': 'is_pass', 'soapReplyCode': 'device_id',
                        'inDbTime': 'created_at'}


def newTableToOldTable(table_lis: list, types):
    if types == 'table_infos':
        new_table_lis = [table_infos_new_dic[i] if i in table_infos_new_dic else i for i in table_lis]
    elif types == 'table_checks':
        new_table_lis = [table_checks_new_dic[i] if i in table_checks_new_dic else i for i in table_lis]
    return new_table_lis


def getSqlData(url, re='old'):
    if re == 'old':
        checks_start = "INSERT INTO `vehicle_checks` VALUES ("
        infos_start = "INSERT INTO `check_infos` VALUES ("
        table_checks_start = "CREATE TABLE `vehicle_checks` ("
        table_infos_start = "CREATE TABLE `check_infos` ("
    elif re == 'new':
        checks_start = "INSERT INTO `vehicle_info` VALUES ("
        infos_start = "INSERT INTO `photo_info` VALUES ("
        table_checks_start = "CREATE TABLE `vehicle_info` ("
        table_infos_start = "CREATE TABLE `photo_info` ("
    table_checks_bool = False
    table_infos_bool = False
    end = ");"
    checks_lis = []
    infos_lis = []
    table_checks_lis = []
    table_infos_lis = []
    with open(url, 'rb') as fo:
        for i in fo:
            i = i.decode(encoding='utf-8', errors="ignore").strip()
            if i.startswith(table_checks_start):
                table_checks_bool = True
                table_infos_bool = False
            elif i.startswith(table_infos_start):
                table_infos_bool = True
                table_checks_bool = False
            data = i.split(' ')[0].strip('`')
            if 'COMMENT' in i and table_checks_bool and not table_infos_bool and data not in table_checks_lis:
                table_checks_lis.append(data)
            elif 'COMMENT' in i and table_infos_bool and not table_checks_bool and data not in table_infos_lis:
                table_infos_lis.append(data)
            try:
                if i.startswith(checks_start) and i.endswith(end):
                    checks_data = i.lstrip(checks_start).rstrip(end)
                    for v in checks_data.split('),('):
                        if v.startswith('('):
                            v = v[1:]
                        elif v.endswith(')'):
                            v = v[:-1]
                        checks = literal_eval('(' + v.replace('NULL', "'NULL'") + ')')
                        if checks not in checks_lis:
                            checks_lis.append(checks)
                elif i.startswith(infos_start) and i.endswith(end):
                    infos_data = i.lstrip(infos_start).rstrip(end)
                    for v in infos_data.split('),('):
                        if v.startswith('('):
                            v = v[1:]
                        elif v.endswith(')'):
                            v = v[:-1]
                        infos = literal_eval('(' + v.replace('NULL', "'NULL'") + ')')
                        if infos not in infos_lis:
                            infos_lis.append(infos)
            except SyntaxError:
                continue
    # 对于车检新表做出调整
    if re == 'new':
        table_infos_lis = newTableToOldTable(table_infos_lis, 'table_infos')
        table_checks_lis = newTableToOldTable(table_checks_lis, 'table_checks')
    check_datas_lis = []
    for data in checks_lis:
        data = list(data)
        if len(table_checks_lis) == len(data):
            check_datas_lis.append(dict(zip(table_checks_lis, data)))
    info_datas_lis = []
    for data in infos_lis:
        data = list(data)
        if len(table_infos_lis) == len(data):
            info_datas_lis.append(dict(zip(table_infos_lis, data)))
    return info_datas_lis, check_datas_lis


del_key_info_lis = ['zhaoPianBianHao', 'zhaoPianXiaZaiDiZhi', 'zhaoPianXiaZaiShiJian', 'suanFaFenXiShiJian',
                    'suanfaYunXingShiJian', 'sheBeiIp', 'jiSuanShiJian']
del_key_check_lis = ['shenQingShenHeShiJian', 'isPassReason']


def filter_lis_key(info_datas_lis, types):
    if types == 'info':
        del_key_lis = del_key_info_lis
    elif types == 'check':
        del_key_lis = del_key_check_lis
    for del_key in del_key_lis:
        for info in info_datas_lis:
            if del_key in info:
                info.pop(del_key)


if __name__ == '__main__':
    sqlurl = (r'E:\dbsql\test\photo_info_20201021102832.sql', r'E:\dbsql\test\vehicle_info_20201021102832.sql')
    # sqlurl = (r'\\192.168.90.10\data\chejian\chejian\上海\sql\photo_info_20201026160123.sql',
    #           r'\\192.168.90.10\data\chejian\chejian\上海\sql\vehicle_info_20201026160123.sql')
    # sqlurl = r'E:\dbsql\test\2019-09-10_52.sql'
    if isinstance(sqlurl, tuple):
        info_datas_lis = getSqlData(sqlurl[0], 'new')[0]
        filter_lis_key(info_datas_lis, 'info')
        check_datas_lis = getSqlData(sqlurl[1], 'new')[1]
        filter_lis_key(check_datas_lis, 'check')
    elif isinstance(sqlurl, str):
        info_datas_lis, check_datas_lis = getSqlData(sqlurl)
    print('check_datas_lis\n')
    print(check_datas_lis[0])
    print('info_datas_lis\n')
    print(info_datas_lis[0])
