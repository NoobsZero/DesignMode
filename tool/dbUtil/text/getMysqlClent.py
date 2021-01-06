# 导入pymysql模块
import os
import pymysql
from ast import literal_eval
import sys


# from pyspark import SparkConf,SparkContext

def get_filelist(dir, fileCondition=''):
    """
            递归获取目录下所有后缀为jpg的路径
        :param fileCondition:
        :param dir: 指定URL是目录（'dir'）
        :return: Filelist:list URL集合
        """
    Filelist = []
    Dirlist = []
    suffix = ['log', '.log', '.DAT', '.xlsx', '.z01', '.json', '.rar', '.zip', '.cer', '.py', '.exe', '.sh', '.txt',
              '.html', '.dll', '.h', '.c',
              '.cpl', '.jsa', '.md', '.properties', '.jar', '.data', '.bfc', '.src', '.ja', '.dat', '.cfg',
              '.pf', '.gif', '.ttf', '.jfc', '.access', '.template', '.certs', '.policy', '.security', '.libraries',
              '.sym', '.idl', '.lib', '.clusters', '.conf', '.xml', '.tar', '.gz', '.csv', '.sql', '.xml_hidden',
              '.lic']
    jpglist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 文件名列表，包含完整路径
            if fileCondition is 'zip':
                if filename[-3:] == 'rar' or filename[-3:] == '.gz' or filename[-3:] == 'tar' or filename[
                                                                                                 -3:] == 'zip' and (
                        'sql' not in filename):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'sql':
                if 'sql' in filename:
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'rar':
                if filename[-3:] == 'rar':
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'if':
                if os.path.splitext(filename)[1] in suffix or filename[-3:] in suffix:
                    Dirlist.append(home)
                    Filelist.append(os.path.join(home, filename))
                else:
                    jpglist.append(home)
            elif fileCondition is '':
                Filelist.append(os.path.join(home, filename))
    if len(jpglist) != 0:
        print('------------------输出jpg目录结构-------------------------------')
        for _ in list(set(jpglist)):
            print(_)
        print('------------------------------------------------------------')
    if len(Dirlist) != 0:
        print('------------------输出非jpg目录结构-------------------------------')
        for i in list(set(Dirlist)):
            print(i)
        print('------------------------------------------------------------')
    return Filelist


def createTable(cursor, city):
    # 1、插入城市
    cursor.execute("INSERT INTO cj_citys(name,created_at,updated_at) VALUES(%s,NOW(),NOW());", (list(city.values())[0]))
    cursor.execute("DROP TABLE IF EXISTS `cj_" + list(city.keys())[0] + "_checks`")
    # 定义要执行的SQL语句
    sql = """
    CREATE TABLE `cj_%(city)s_checks` (
            `id` bigint(20) NOT NULL AUTO_INCREMENT,
            `jylsh` varchar(255) DEFAULT NULL,
            `jyjgbh` varchar(255) DEFAULT NULL,
            `jylb` varchar(255) DEFAULT NULL,
            `hpzl_id` int(11) DEFAULT NULL,
            `hphm` varchar(255) DEFAULT NULL,
            `clsbdh` varchar(255) DEFAULT NULL,
            `syr` varchar(255) DEFAULT NULL,
            `sjhm` varchar(255) DEFAULT NULL,
            `sxrq` varchar(255) DEFAULT NULL,
            `zzrq` varchar(255) DEFAULT NULL,
            `cllx_id` int(11) DEFAULT NULL,
            `syxz` varchar(255) DEFAULT NULL,
            `zbzl` varchar(255) DEFAULT NULL,
            `kssj` varchar(255) DEFAULT NULL,
            `jssj` varchar(255) DEFAULT NULL,
            `fdjh` varchar(255) DEFAULT NULL,
            `clpp_id` int(11) DEFAULT NULL,
            `clxh` varchar(255) DEFAULT NULL,
            `ccdjrq` varchar(255) DEFAULT NULL,
            `ccrq` varchar(255) DEFAULT NULL,
            `wgjcjyy` varchar(255) DEFAULT NULL,
            `xszbh` varchar(255) DEFAULT NULL,
            `fzrq` varchar(255) DEFAULT NULL,
            `rlzl` varchar(255) DEFAULT NULL,
            `zpzs` varchar(255) DEFAULT NULL,
            `spzs` varchar(255) DEFAULT NULL,
            `bdbhgs` int(11) DEFAULT NULL,
            `csys_id` int(11) DEFAULT NULL,
            `pl` varchar(255) DEFAULT NULL,
            `gl` varchar(255) DEFAULT NULL,
            `zxxs` varchar(255) DEFAULT NULL,
            `cwkc` varchar(255) DEFAULT NULL,
            `cwkk` varchar(255) DEFAULT NULL,
            `cwkg` varchar(255) DEFAULT NULL,
            `hxnbcd` varchar(255) DEFAULT NULL,
            `hxnbkd` varchar(255) DEFAULT NULL,
            `hxnbgd` varchar(255) DEFAULT NULL,
            `gbthps` varchar(255) DEFAULT NULL,
            `zs` varchar(255) DEFAULT NULL,
            `zj` varchar(255) DEFAULT NULL,
            `qlj` varchar(255) DEFAULT NULL,
            `hlj` varchar(255) DEFAULT NULL,
            `ltgg` varchar(255) DEFAULT NULL,
            `lts` varchar(255) DEFAULT NULL,
            `zzl` varchar(255) DEFAULT NULL,
            `hdzzl` varchar(255) DEFAULT NULL,
            `hdzk` varchar(255) DEFAULT NULL,
            `zqyzl` varchar(255) DEFAULT NULL,
            `qpzk` varchar(255) DEFAULT NULL,
            `hpzk` varchar(255) DEFAULT NULL,
            `clyt_id` int(11) DEFAULT NULL,
            `ytsx` varchar(255) DEFAULT NULL,
            `sfxny` varchar(255) DEFAULT NULL,
            `xnyzl` varchar(255) DEFAULT NULL,
            `yxqz` varchar(255) DEFAULT NULL,
            `fzjg` varchar(255) DEFAULT NULL,
            `hbdbqk` varchar(255) DEFAULT NULL,
            `qzbfqz` varchar(255) DEFAULT NULL,
            `xzqh` varchar(255) DEFAULT NULL,
            `gcjk` varchar(255) DEFAULT NULL,
            `dybj` varchar(255) DEFAULT NULL,
            `zzg` varchar(255) DEFAULT NULL,
            `clpp2` varchar(255) DEFAULT NULL,
            `jyhgbzbh` varchar(255) DEFAULT NULL,
            `sfmj` varchar(255) DEFAULT NULL,
            `zt` varchar(255) DEFAULT NULL,
            `djrq` varchar(255) DEFAULT NULL,
            `zsxzqh` varchar(255) DEFAULT NULL,
            `zzxzqh` varchar(255) DEFAULT NULL,
            `fdjxh` varchar(255) DEFAULT NULL,
            `sgcssbwqk` varchar(255) DEFAULT NULL,
            `bmjyy` varchar(255) DEFAULT NULL,
            `glbm` varchar(255) DEFAULT NULL,
            `zzcmc_id` int(11) DEFAULT NULL,
            `jylsh2` varchar(255) DEFAULT NULL,
            `is_video_check` varchar(255) DEFAULT NULL,
            `station_status` int(11) DEFAULT NULL,
            `center_status` int(11) DEFAULT NULL,
            `is_pass` int(11) DEFAULT NULL,
            `device_id` int(11) DEFAULT NULL,
            `check_created_at` datetime DEFAULT NULL,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
    sql = sql % dict(city=list(city.keys())[0])
    # 执行SQL语句
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS `cj_" + list(city.keys())[0] + "_infos`")
    # 定义要执行的SQL语句
    sql = """
    CREATE TABLE `cj_%(city)s_infos` (
        `id` bigint(20) NOT NULL AUTO_INCREMENT,
        `vehicle_check_id` int(11) DEFAULT NULL,
        `category` varchar(255) DEFAULT NULL,
        `name` varchar(255) DEFAULT NULL,
        `result` varchar(255) DEFAULT NULL,
        `reason` varchar(255) DEFAULT NULL,
        `info_created_at` datetime DEFAULT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
    sql = sql % dict(city=list(city.keys())[0])
    # 执行SQL语句
    cursor.execute(sql)


def getSqlData(url):
    table_checks_bool = False
    table_infos_bool = False
    checks_start = "INSERT INTO `vehicle_checks` VALUES ("
    infos_start = "INSERT INTO `check_infos` VALUES ("
    end = ");"
    lis = None
    with open(url, 'r', encoding='utf-8', errors="ignore") as fo:
        lis = fo.readlines()
    checks_lis = []
    infos_lis = []
    table_checks_lis = []
    table_infos_lis = []
    for i in lis:
        i = i.strip()
        if i.startswith("CREATE TABLE `vehicle_checks` ("):
            table_checks_bool = True
            table_infos_bool = False
        if i.startswith("CREATE TABLE `check_infos` ("):
            table_infos_bool = True
            table_checks_bool = False
        if 'COMMENT' in i and table_checks_bool and not table_infos_bool:
            table_checks_lis.append(i.split(' ')[0].strip('`'))
        elif 'COMMENT' in i and table_infos_bool and not table_checks_bool:
            table_infos_lis.append(i.split(' ')[0].strip('`'))
        if i.startswith(checks_start) and i.endswith(end):
            checks_data = i.lstrip(checks_start).rstrip(end)
            for v in checks_data.split('),('):
                if v.startswith('('):
                    v = v[1:]
                elif v.endswith(')'):
                    v = v[:-1]
                checks_lis.append(literal_eval('(' + v.replace('NULL', "'NULL'") + ')'))
        elif i.startswith(infos_start) and i.endswith(end):
            infos_data = i.lstrip(infos_start).rstrip(end)
            for v in infos_data.split('),('):
                if v.startswith('('):
                    v = v[1:]
                elif v.endswith(')'):
                    v = v[:-1]
                infos_lis.append(literal_eval('(' + v.replace('NULL', "'NULL'") + ')'))
    return table_checks_lis, checks_lis, table_infos_lis, infos_lis

def getSqlDatas(url):
    table_checks_bool = False
    table_infos_bool = False
    checks_start = "INSERT INTO `vehicle_checks` VALUES "
    infos_start = "INSERT INTO `check_infos` VALUES "
    end = ";"
    lis = None
    with open(url, 'r', encoding='utf-8', errors="ignore") as fo:
        lis = fo.readlines()
    checks_lis = []
    infos_lis = []
    table_checks_lis = []
    table_infos_lis = []
    for i in lis:
        i = i.strip()
        if i.startswith(infos_start) and i.endswith(end):
            infos_data = i.lstrip(infos_start).rstrip(end)
            for v in infos_data.split('),('):
                if v.startswith('('):
                    v = v[1:]
                if v.endswith(')'):
                    v = v[:-1]
                print(v)
    return table_checks_lis, checks_lis, table_infos_lis, infos_lis

if __name__ == '__main__':
    # urlpath = r'\\192.168.90.10\data\chejian\chejian\滨州\sql'
    # sqlurls = get_filelist(urlpath, 'sql')
    # for sqlurl in sqlurls:
    #     print(sqlurl)
    table_checks_lis, checks_lis, table_infos_lis, infos_lis = getSqlData(r"\\192.168.90.10\data\chejian\chejian\滨州\sql\滨州车管所数据库-243-2019-12-17.sql")
    if len(checks_lis) != 0 and len(infos_lis) != 0:
        print(len(table_checks_lis), len(checks_lis[0]), len(table_infos_lis), len(infos_lis[0]))
    # 连接database
    # conn = pymysql.connect(host='192.168.50.100', user='root', password='EmDataMysql2020###',
    #                        database='emTest_cj_vehicle_20210105', charset='utf8')
    # city = {'baoding': '蚌埠'}
    # # 得到一个可以执行SQL语句的光标对象
    # cursor = conn.cursor()
    # 创建表
    # cursor.execute("select * from vehicle_checks where id=22126;")
    # results = cursor.fetchall()
    # print(type(results[0]))
    # print(len(list(results[0])))
    # for row in results:
    #     print(row[0])
    # createTable(cursor, city)
    # 插入信息

    # # 关闭光标对象
    # cursor.close()
    # # 关闭数据库连接
    # conn.close()
