# -*- coding: utf-8 -*-
import configparser


def setConfigIni(filename,liArgs):
    handle = configparser.ConfigParser()
    handle.read(filename)
    #callback(config,liArgs)

    a = handle.get("alembic", "sqlalchemy.url")
    print(a)

    for item in liArgs:
        handle.set(item[0], item[1], item[2])
        print("##############################",item[2])
    with open(filename, "w+") as f:
        handle.write(f)



def test_config_ini():
    config = configparser.ConfigParser()
    config.read('./alembic.ini')
    a = config.get("alembic","sqlalchemy.url")
    print(a)

if __name__ == '__main__':
    test_config_ini()
    pass