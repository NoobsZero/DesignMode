# -*- coding: utf-8 -*-
"""
@File   :JsonConfig.py
@Time   :2021/2/8 15:21
@Author :Chen
@Software:PyCharm
"""
import configparser


def setConfigIni(filename, liArgs):
    handle = configparser.ConfigParser()
    handle.read(filename)

    a = handle.get("alembic", "sqlalchemy.url")
    print(a)

    for item in liArgs:
        handle.set(item[0], item[1], item[2])
        print("##############################", item[2])
    with open(filename, "w+") as f:
        handle.write(f)


def test_config_ini():
    config = configparser.ConfigParser()
    config.read(r'E:\JetBrains\PycharmProjects\untitled\tool\mydbUtil\collect_photos-develop\alembic.ini')
    a = config.get("alembic", "sqlalchemy.url")
    print(a)


if __name__ == '__main__':
    test_config_ini()
    pass
