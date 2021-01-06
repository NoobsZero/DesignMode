# -*- encoding:utf-8 -*-
"""
@File   :fliteData.py
@Time   :2021/1/5 16:37
@Author :Chen
@Software:PyCharm
"""
if __name__ == '__main__':
    lis = []
    url = r'C:\Users\标注\Desktop\car\jpg\2019-08-19.sql'
    tourl = r'C:\Users\标注\Desktop\car\jpg\test.txt'
    start = "INSERT INTO `vehicle_checks` VALUES ("
    end = ");"
    with open(url, 'r', encoding='utf-8') as fo:
        lis = fo.readlines()
    sql_lis = []
    for i in lis:
        i = i.strip()
        if i.startswith(start) and i.endswith(end):
            data = i.lstrip(start).rstrip(end)
            for v in data.split('),('):
                lis = []
                for f in v.split(','):
                    if f.startswith('\'') and f.endswith('\''):
                        f = f.strip('\'')
                    elif f.startswith('\"') and f.endswith('\"'):
                        f = f.strip('\"')
                    lis.append(f)
                sql_lis.append(lis)
    for i in sql_lis:
        print(i)
