# -*- encoding:utf-8 -*-
"""
@File   :testdir.py
@Time   :2020/12/4 18:17
@Author :Chen
@Software:PyCharm
"""
import os
import shutil

if __name__ == '__main__':
    url = 'info.txt'
    lis = []
    with open(url, encoding='utf8', errors='ignore') as er:
        for dirname in er.readlines():
            if dirname not in lis:
                lis.append(dirname.strip())
    for i in lis:
        if os.path.exists(i):
            shutil.rmtree(i)
    # os.remove(path)  # 删除文件
    # os.removedirs(path)  # 删除空文件夹
    # shutil.rmtree(path)  # 递归删除文件夹
    # os.removedirs(spe_path)  # 删除整个目录
    # os.rmdir(spe_path)  # 删除当前目录，目录内容必须为空