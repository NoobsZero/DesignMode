# -*- encoding:utf-8 -*-
# coding=utf-8
import os
import shutil
import random
import paramiko

from tool.mylogUtil.baselog import logger


def preStart(tmpDir):
    """
    创建临时目录（路径存在则递归删除再创建）
    Args:
        tmpDir: 目录路径

    Returns:boolean

    """
    try:
        if os.path.exists(tmpDir):
            # 递归地删除文件
            shutil.rmtree(tmpDir)
        os.makedirs(tmpDir)
    except Exception as e:
        logger.error("临时文件创建失败:{}".format(e))
        return False
    return True


def mvDirToDir(root_src_dir, root_dst_dir):
    """
        移动目录下所有文件到目录
    :param root_src_dir: 源目录
    :param root_dst_dir: 指定目录
    """
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


def moveFileToDir(root_src_file, root_dst_dir):
    """
        移动文件到目录（文件存在则改名）
    :param root_src_file: 源文件
    :param root_dst_dir: 指定目录
    """
    if os.path.isfile(root_src_file):
        if not os.path.exists(root_dst_dir):
            os.makedirs(root_dst_dir)
        root_dst_file = os.path.join(root_dst_dir, os.path.split(root_src_file)[-1])
        root_dst_lis = get_filelist(root_dst_dir)
        if root_dst_file in root_dst_lis:
            new_i = os.path.split(root_dst_file)
            new_root_src_file = os.path.join(new_i[0],
                                             os.path.split(os.path.split(root_dst_file)[0])[-1] + '_' + new_i[-1])
            os.renames(root_src_file, new_root_src_file)
        else:
            shutil.move(root_src_file, root_dst_file)


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
              '.lic']
    list_jpg_dir = []
    for home, dirs, files in os.walk(dir, topdown=topdown):
        for filename in files:
            # 文件名列表，包含完整路径
            if fileCondition is 'zip':
                if filename.endswith('.rar') or filename.endswith('.gz') or filename.endswith('.tar') or \
                        os.path.splitext(filename)[-1].endswith('.z', 0, 2) and (
                        'sql' not in filename):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'sql':
                if filename.endswith('.sql'):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'rar':
                if filename[-3:] == 'rar':
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'suffix':
                if os.path.splitext(filename)[1] in suffix or filename[-3:] in suffix:
                    Filelist.append(os.path.join(home, filename))
                elif home not in list_jpg_dir:
                    list_jpg_dir.append(home)
            elif fileCondition is '':
                Filelist.append(os.path.join(home, filename))
    if fileCondition is 'suffix':
        return Filelist, list_jpg_dir
    else:
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


def getZipSubsection(sc, lis):
    lis_sub_zip = []
    sc_file = os.path.splitext(sc)[0]
    for k in lis:
        if sc_file in k and sc not in k:
            lis_sub_zip.append(k)
    return lis_sub_zip


def decompressionZIP(dirs, sqlPath):
    """
        linux压缩包解压
    :param dirs: 扫描目录
    :param sqlPath: sql文件目录（可以不添加）
    """
    # if not os.path.isdir(sqlPath):
    #     os.system('mkdir ' + sqlPath)
    zip = get_filelist(dirs, 'zip')
    for i in zip:
        new_file_name = i.split('/')[-1]
        old_file_name = i.split('/')[-1]
        for tu in ['(', ')', ' ', '-', '#', ';', '$', '!', '@', '&', '\\', '"']:
            new_file_name = new_file_name.replace(tu, '_')
        new_file_name = i.replace(old_file_name, new_file_name)
        if i != new_file_name:
            os.system('mv ' + "'" + i + "'" + ' ' + new_file_name)
        i = new_file_name
        pathname, filename = os.path.split(i)
        newpath = os.path.join(pathname, filename.split('.')[0], '')
        print(newpath)
        if not os.path.isdir(newpath):
            os.system('mkdir ' + newpath)
        os.system('echo ' + i + ' ... ...')
        if filename.endswith('.gz') or filename.endswith('tar'):
            os.system('tar -xf ' + i + ' -C ' + newpath + ' && rm ' + i)
        elif filename.endswith('zip'):
            lis_sub_zip = getZipSubsection(filename, zip)
            if len(lis_sub_zip) > 0:
                i_pathname, i_filename = os.path.split(i)
                new_i = os.path.join(i_pathname[0], 'all_' + i_filename[-1])
                os.system('mv ' + i + ' ' + new_i)
                for sub_zip in lis_sub_zip:
                    os.system('cat ' + sub_zip + ' > ' + i + ' && rm ' + sub_zip)
                os.system('unzip -O gbk ' + new_i + ' -d ' + newpath + ' && rm ' + new_i)
            else:
                os.system('unzip -O gbk ' + i + ' -d ' + newpath + ' && rm ' + i)
        elif filename.endswith('.rar') and ('.part' not in filename):
            os.system('rar e -o+ -y ' + i + ' -C ' + newpath + ' && rm ' + i)
        print(i)
        os.system('echo ' + i + ' ok')
        # todoList = get_filelist(dirs, fileCondition='sql')
        # for sqldir in todoList:
        #     moveFileToDir(sqldir, sqlPath)
    delDir(dirs)




if __name__ == '__main__':
    # print('葵花解压手')
    # sqlPath = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'sql','')
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
