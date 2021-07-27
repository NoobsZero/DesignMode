# -*- encoding:utf-8 -*-
"""
@File   :wc.py
@Time   :2020/10/23 8:35
@Author :Chen
@Software:PyCharm
"""
import re


def wordcount(file):
    chars = 0
    word = [] # 单词列表
    lines = 0
    for line in file:
        chars += len(line)
        # 正则表达式替代非英文、汉字、非数字
        lb = re.sub("[^0-9a-zA-Z\\u4e00-\\u9fff]", " ", line).strip().split(" ")
        word.extend(lb)
        words = len(word)
        lines += 1
        return chars, words, lines


if __name__ == '__main__':
    str1 = "wordcount wordcount wordcount wordcount wordcount ip ss"
    chars, words, lines = wordcount(str1)
    print(chars)
    print(words)
    print(lines)
