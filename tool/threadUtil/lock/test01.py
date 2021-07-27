# encoding: utf-8
"""
@file: test01.py
@time: 2021/6/30 10:15
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import threading
import time

mutex = threading.Lock()  # 创建锁


def test_xc():
    # semaphore.acquire()
    mutex.acquire()  # 取得锁
    # f = open("test.txt", "a")
    # f.write("当前时间" + str(time.ctime()) + '\n')
    print("当前时间" + str(time.ctime()))
    time.sleep(1)
    # f.close()
    mutex.release()  # 释放锁
    # semaphore.release()


def test1(n):
    mutex.acquire()
    print(n, "当前时间" + str(time.ctime()))
    time.sleep(1)
    mutex.release()


def test(n):
    print(n, "当前时间" + str(time.ctime()))
    time.sleep(1)


def main():
    for i in range(10):
        t = threading.Thread(target=test1, args=(i, ))
        t.start()


if __name__ == '__main__':
    main()
    # # semaphore = threading.BoundedSemaphore(2)
    # # lst_record_threads = []
    # for i in range(0, 10):
    #     # t = threading.Thread(target=test_xc)
    #     t = threading.Thread(target=test1, args=(i, ))
    #     # lst_record_threads.append(t)
    #     t.start()
    # # for rt in lst_record_threads:
    # #     rt.join()
