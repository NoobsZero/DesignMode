# -*- encoding:utf-8 -*-
"""
@File   :getMessgae.py
@Time   :2021/2/25 11:52
@Author :Chen
@Software:PyCharm
"""
import os

import paramiko

from tool.dirUtil.getDirUtil import project_root_path
from tool.myconfigUtil.JsonConfig import JsonConfig


class LoginLinux:
    def __init__(self, sshConfPath=None):
        """
            LoginLinux类
            通过SSH连接Linux
        Args:
            sshConfPath: 配置文件地址
        """
        self.SSHConfPath = os.path.join(project_root_path('untitled'),
                                        r'source\linux.conf.json') if sshConfPath is None else sshConfPath
        self.sshConf = JsonConfig().loadConf(self.SSHConfPath)
        self.sys_ip = self.sshConf.getValue('sys_ip')
        self.username = self.sshConf.getValue('username')
        self.password = self.sshConf.getValue('password')
        self.port = self.sshConf.getValue('port')
        self.client = self.loginLinux()

    def setLoginLinuxConf(self, sysIp, port, userName, passWord):
        """
            设置SSH连接参数
        Args:
            sysIp: ip地址
            port: 端口号
            userName: 用户名
            passWord: 密码

        Returns:pass

        """
        self.sys_ip = sysIp
        self.username = userName
        self.password = passWord
        self.port = port

    def loginLinux(self):
        """
            获取Linux连接
        Returns: SSHClient

        """
        try:
            clientSocket = paramiko.SSHClient()
            clientSocket.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            clientSocket.connect(hostname=self.sys_ip, port=self.port, username=self.username, password=self.password,
                                 compress=True, timeout=20)
            return clientSocket
        except Exception as e:
            print(e)

    def exec(self, cmd):
        """
            执行命令
        Args:
            cmd: Linux命令

        Returns:结果

        """
        if isinstance(cmd, list):
            cmd = ' && '.join(cmd)
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            results = stdout.readlines()
            return results
        except Exception as e:
            print(e)

    def __del__(self):
        self.client.close()
        pass


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

    client = LoginLinux()
    client.exec('cd /')
    resultLis = client.exec('ls')
    for i in resultLis:
        print(i)
