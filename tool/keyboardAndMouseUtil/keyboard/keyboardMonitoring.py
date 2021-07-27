# encoding: utf-8
"""
@file: keyboardMonitoring.py
@time: 2021/6/16 9:46
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from pynput.keyboard import Controller, Key, Listener


def on_press(key):
    """监听按压"""
    try:
        print("正在按压:", format(key.char))
    except AttributeError:
        print("正在按压:", format(key))


def on_release(key):
    """监听释放"""
    print("已经释放:", format(key))

    if key == Key.esc:
            # 停止监听
        return False


def start_listen():
    """开始监听"""
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
        # 实例化键盘
        kb = Controller()

        # 使用键盘输入一个字母
        # kb.press('a')
        # kb.release('a')

        # 使用键盘输入字符串,注意当前键盘调成英文
        # kb.type("hello world")

        # 使用Key.xxx输入
        kb.press(Key.space)

        # 开始监听,按esc退出监听
        start_listen()
