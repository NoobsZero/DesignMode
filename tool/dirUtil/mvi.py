# -*- encoding:utf-8 -*-
# coding=utf-8
import os
import shutil
import random
import paramiko


def getSSh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect()
    # ssh.exec_command("cd "+dirs)
    ssh.close
    return ssh


def mvFileToDir(root_src_dir, root_dst_dir):
    root_src_dir = os.path.join(os.getcwd(), root_src_dir, '')
    root_dst_dir = os.path.join(os.getcwd(), root_dst_dir, '')
    print(str(root_src_dir) + " to " + str(root_dst_dir))
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                # in case of the src and dst are the same file
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)


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


def get_filelist(dir, fileCondition=''):
    """
            递归获取目录下所有后缀为jpg的路径
        :param fileCondition:
        :param dir: 指定URL是目录（'dir'）
        :return: Filelist:list URL集合
        """
    Filelist = []
    Dirlist = []
    suffix = ['log', '.log', '.DAT', '.xlsx', '.z01', '.json', '.rar', '.zip', '.cer', '.py', '.exe', '.sh', '.txt', '.html', '.dll', '.h', '.c',
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


def delDir(dirPath):
    """
        递归删除指定目录下空文件及目录
        :param dirPath:目录路径
    """
    for root, dirs, files in os.walk(dirPath, topdown=False):
        for file in files:
            src_file = os.path.join(root, file)
            if os.path.getsize(src_file) == 0:
                os.remove(src_file)
    for root, dirs, files in os.walk(dirPath, topdown=False):
        if not os.listdir(root):
            os.system('rmdir ' + root)


def decompressionZIP(dirs, sqlPath):
    os.system('mkdir ' + sqlPath)
    zip = get_filelist(dirs, 'zip')
    for i in zip:
        pathname, filename = os.path.split(i)
        newpath = os.path.join(pathname, filename.split('.')[0], '')
        print(newpath)
        os.system('mkdir ' + newpath)
        os.system('echo ' + i + ' ... ...')
        if filename[-3:] == '.gz' or filename[-3:] == 'tar':
            os.system('tar -xf ' + i + ' -C ' + newpath + ' && rm ' + i)
        elif filename[-3:] == 'zip':
            os.system('unzip -O gbk ' + i + ' -d ' + newpath + ' && rm ' + i)
        elif filename[-3:] == 'rar' and ('.part' not in filename):
            os.system('rar e -o+ -y ' + i + ' -C ' + newpath + ' && rm ' + i)
        print(i)
        os.system('echo ' + i + ' ok')
        moveFileToDir(dirs, sqlPath, fileCondition='sql')


if __name__ == '__main__':
    # sqlPath = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'sql', '')
    # os.system('mkdir ' + sqlPath)
    # moveFileToDir(os.getcwd(), sqlPath, 'sql')
    # print('葵花解压手')
    # decompressionZIP(os.getcwd(),sqlPath)
    # print('乾坤大挪移')
    # root_dst_dir={}
    # for root_src_dir in root_dst_dir:
    #     mvFileToDir(root_src_dir, root_dst_dir[root_src_dir])
    print('佛山清空脚')
    delDir(os.getcwd())
    print('万花写轮眼')
    dic = get_filelist(os.getcwd(), 'if')
    print('------------------输出文件-------------------------------')
    for i in dic:
        print(i)
    print('------------------------------------------------------------')
