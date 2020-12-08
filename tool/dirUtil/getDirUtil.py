# -*- encoding:utf-8 -*-
"""
@File   :getDirUtil.py
@Time   :2020/12/2 19:19
@Author :Chen
@Software:PyCharm
"""
import random
from nltk import infile
import os
import shutil
import glob


def my_move(srcfn, dstdir):  ##定义移动函数，参数为待移动的文件路径和目标目录
    if not os.path.isfile(srcfn):  ##判断文件是否存在
        print('srcfn error')

    else:
        srcdir, fn = os.path.split(srcfn)  ##分离绝对路径和相对路径，获得文件名

        if not os.path.exists(dstdir):  ##如果目录不存在，创建目录
            os.makedirs(dstdir)

        dstfn = dstdir + fn  ##生成目录下的文件名
        shutil.move(srcfn, dstfn)  ##移动


def copy_dir(yuan, target):

    '''将一个目录下的全部文件和目录,完整地<拷贝并覆盖>到另一个目录'''
    # yuan 源目录
    # target 目标目录

    if not (os.path.isdir(yuan) and os.path.isdir(target)):
        # 如果传进来的不是目录
        # print("传入目录不存在")
        return

    for a in os.walk(yuan):
        #递归创建目录
        for d in a[1]:
            dir_path = os.path.join(a[0].replace(yuan,target),d)
            if not os.path.isdir(dir_path):
                os.makedirs(dir_path)
        #递归拷贝文件
        for f in a[2]:
            dep_path = os.path.join(a[0],f)
            arr_path = os.path.join(a[0].replace(yuan,target),f)
            shutil.copy(dep_path, arr_path)


def delDir(dir):
    for home, dirs, files in os.walk(dir):
        for dirname in dirs:
            if not os.listdir(os.path.join(home, dirname)):
                os.rmdir(os.path.join(home, dirname))
                print(dirname)


def get_filelist(dir, fileCondition=''):
    """
            递归获取目录下所有后缀为jpg的路径
        :param fileCondition:
        :param dir: 指定URL是目录（'dir'）
        :return: Filelist:list URL集合
        """
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 文件名列表，包含完整路径
            if fileCondition is 'zip':
                if filename[-3:] == '.gz' or filename[-3:] == 'tar' or filename[-3:] == 'rar' and ('sql' not in filename):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'sql':
                if 'sql' in filename:
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is '':
                Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist


def moveFileToDir(infile, todir, fileCondition=''):
    todoList = get_filelist(infile, fileCondition)
    sqlList = get_filelist(todir)
    num = 0
    for i in todoList:
        num = num + 1
        print(num)
        newSql = os.path.join(todir, os.path.split(i)[1])
        if newSql in sqlList:
            name = os.path.split(i)[1].split('.')
            new = os.path.join(todir, ".".join(["".join(name[0:-1]) + '_' + str(random.randint(0, 1000)), name[-1]]))
            os.renames(i, new)
            print(i + "\tto\t" + new)
        else:
            shutil.move(i, newSql)
            print(newSql)


if __name__ == '__main__':
    # fns = glob.glob(r'E:\toos\test\image\*.jpg')  ##获取当前目录下所有jpg格式的文件
    indir = r'\\192.168.90.10\data\chejian\chejian\嘉兴\zip\20190705-0717'
    todir = r'\\192.168.90.10\data\chejian\chejian\嘉兴\zip'
    moveFileToDir(indir, todir, 'zip')
    # delDir(indir)

    # lis = os.listdir(indir)
    # lis_sql = []
    # for i in lis:
    #     if i[-3:] == 'sql':
    #         lis_sql.append(os.path.join(indir,i))
    # todoList = lis_sql
    # sqlList = get_filelist(todir)
    # num = 0
    # for i in todoList:
    #     num = num + 1
    #     print(num)
    #     newSql = os.path.join(todir, os.path.split(i)[1])
    #     if newSql in sqlList:
    #         name = os.path.split(i)[1].split('.')
    #         new = os.path.join(todir, ".".join(["".join(name[0:-1]) + '_' + str(random.randint(0, 1000)), name[-1]]))
    #         os.renames(i, new)
    #         print(i + "\tto\t" + new)
    #     else:
    #         shutil.move(i, newSql)
    #         print(newSql)


    # file1 = get_filelist(indir)
    # file2 = os.listdir(todir)
    #
    # for i in file1:
    #     newSql = os.path.split(i)[1]
    #     if newSql not in file2:
    #         print(newSql)
    #         shutil.move(i, todir)
    #     else:
    #         os.remove(i)

    # fns = glob.glob('H:/dataset/*.jpg')  ##获取当前目录下所有jpg格式的文件
    # src_fns = [fn for fn in fns if fn[-7:-4] == 'src']  ##获取当前目录下的所有原始数据，存为一个list
    # for ind in range(len(src_fns)):  ##循环移动所有文件
    #     my_move(src_fns[ind], 'H:/dataset/src/')

        # print(i)

    # num = 0
    # for i in todoList:
    #     num = num + 1
    #     print(num)
    #     newSql = os.path.join(todir, os.path.split(i)[1])
    #     if newSql in sqlList:
    #         name = os.path.split(i)[1].split('.')
    #         new = os.path.join(todir, ".".join(["".join(name[0:-1]) + '_' + str(random.randint(0, 100)), name[-1]]))
    #         os.renames(i, new)
    #         print(i + "\tto\t" + new)
    #     else:
    #         shutil.move(i, newSql)
    #         print(newSql)

