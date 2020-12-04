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
import threading  # Python主要通过标准库中的threading包来实现多线程
import time
import os


def doChore():  # 作为间隔  每次调用间隔0.5s
    time.sleep(0.5)


def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()  # 得到一个锁，锁定
        if i != 0:
            i = i - 1  # 售票 售出一张减少一张
            print(tid, ':now left:', i)  # 剩下的票数
            doChore()
        else:
            print("Thread_id", tid, " No more tickets")
            os._exit(0)  # 票售完   退出程序
        lock.release()  # 释放锁
        doChore()


if __name__ == '__main__':
    # Start of the main function
    i = 100  # 初始化票数
    lock = threading.Lock()  # 创建锁

    # 总共设置了10个线程
    for k in range(10):
        new_thread = threading.Thread(target=booth, args=(k,))  # 创建线程; Python使用threading.Thread对象来代表线程
        new_thread.start()  # 调用start()方法启动线程
    # indir = r'\\192.168.90.10\data\chejian\chejian\东营\zip\1231-东营车检-赵群-正在上传\5\2019-12-31'
    # todir = r'\\192.168.90.10\data\chejian\chejian\东营\zip\2019\2019-12-31'
    # file1 = get_filelist(indir)
    # file2 = os.listdir(todir)
    # for i in file1:
    #     newSql = os.path.split(i)[1]
    #     if newSql not in file2:
    #             shutil.move(i, todir)
    #     else:
    #         os.remove(i)