# -*- codeing = utf-8 -*-
# @Time :2020/7/27 12:32
# @Author:Eric
# @File : getIoUtil.py
# @Software: PyCharm
import os
import platform
import ctypes
import sys
import math

# 获取磁盘剩余空间
def get_free_space_mb(folder):
    """
    :param folder: 磁盘路径 例如 D:\\
    :return: 剩余空间 单位 G
    """
    # Windows获取方式
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 // 1024
    # Linux获取方式
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 // 1024

# 用于车检修改名字
def prefix_subfolders(files='C:\\Users\\标注\\Desktop\\test\\1'):
    old_names = os.listdir(files)
    for old_name in old_names:
        if os.path.isfile(files + '\\' + old_name):
            try:
                lis_old_name = old_name.split('_')
                lis_old_name[-1] = lis_old_name[-1].replace('.'.join(lis_old_name[-1].split('.')[0:-1]), lis_old_name[-2])
                new_name = '_'.join(lis_old_name)
                os.rename(files + '\\' + old_name, files + '\\' + new_name)
                print('\33[0;32;40m'+ new_name + '\033[0m')
            except Exception:
                print('\n\n\n')
                print('\033[31m修改失败，文件名为：' + old_name + '\33[0m')
                print("\n\n\n")

# 进度条
def processBar(cur, total):
    """
          进度条显示
          cur表示当前的数值，total表示总的数值。
        :param cur:
        :param total:
        :return:
        """
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    sys.stdout.write('[%-50s] %s' %
                     ('\033[0;32;40m=\033[0m' * int(math.floor(cur * 50 / total)), percent))
    sys.stdout.flush()
    if cur == total:
        sys.stdout.write('\n')
