# -*- encoding:utf-8 -*-
"""
@File   :testdir.py
@Time   :2020/12/4 18:17
@Author :Chen
@Software:PyCharm
"""
import glob
import os
import shutil

from tool.dirUtil.getDirUtil import my_move, get_filelist

if __name__ == '__main__':
    indir = r'\\192.168.90.10\data\chejian\chejian\东营\zip\1231-东营车检-赵群-正在上传\5\2019-12-31'
    todir = r'\\192.168.90.10\data\chejian\chejian\东营\zip\2019\2019-12-31'
    file1 = get_filelist(indir)
    file2 = os.listdir(todir)
    for i in file1:
        newSql = os.path.split(i)[1]
        if newSql not in file2:
            shutil.move(i, todir)
        elif newSql in file2:
            print(i)
            os.remove(i)