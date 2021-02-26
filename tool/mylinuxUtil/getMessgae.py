# -*- encoding:utf-8 -*-
"""
@File   :getMessgae.py
@Time   :2021/2/25 11:52
@Author :Chen
@Software:PyCharm
"""
import os


def Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_File begin')

    cmd = 'C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
        password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
    os.system(cmd)

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_File end')


def Window_to_Linux_Dir(window_path, Linux_path, Linux_ip, username, password):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_Dir begin')

    cmd = 'C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} -r {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
        password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
    os.system(cmd)

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_Dir end')


def Linux_to_Window_File(Linux_path, window_path, Linux_ip, username, password):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Linux_to_Window_File begin')

    cmd = 'C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} {username}@{Linux_ip}:{Linux_path} {window_path}'.format(
        password=password, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path, window_path=window_path)
    os.system(cmd)

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<Linux_to_Window_File end')


def Linux_to_Window_Dir(Linux_path, window_path, Linux_ip, username, password):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Linux_to_Window_Dir begin')

    cmd = 'C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} -r {username}@{Linux_ip}:{Linux_path} {window_path}'.format(
        password=password, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path, window_path=window_path)
    os.system(cmd)

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<Linux_to_Window_Dir end')


def Linux_get_Window_File(Linux_path, window_path):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>Linux_get_Window_File begin')



if __name__ == '__main__':
    password = '*****'
    window_path = r'D:'
    username = '****'
    Linux_ip = '10.**.***.***'
    Linux_path = r'/var/backup'

    Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password)
    # Window_to_Linux_Dir(window_path, Linux_path, Linux_ip, username, password)
    # Linux_to_Window_File(Linux_path, window_path, Linux_ip, username, password))
    # Linux_to_Window_Dir(Linux_path, window_path, Linux_ip, username, password)
