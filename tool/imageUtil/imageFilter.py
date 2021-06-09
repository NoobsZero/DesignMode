# encoding: utf-8
"""
@file: imageFilter.py
@time: 2021/4/28 16:08
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from hashlib import md5
import os


def main(path):
    f = open(r'F:\tupian\md5.txt', 'w')

    list = []

    list1 = []

#得到所有图片的路径，加到列表list1中
    root, _, files = next(os.walk(path))
    for i in range(len(files)):
        line = path + '/' + str(files[i])
        list1.append(line)

#计算每张图片的md5值，并将图片路径与其md5值整合到列表list中
    for n in range(len(list1)):
        hash = md5()
        img = open(list1[n], 'rb')
        hash.update(img.read())
        img.close()
        list2 = [list1[n], hash.hexdigest()]
        f.write(str(list2)+'\n')
        list.append(list2)

#两两比较md5值，若相同，则删去一张图片
    m = 0
    while m < len(list):
        t = m + 1
        while t < len(list):
            if list[m][1] == list[t][1]:
                os.remove(list[t][0])
                del list[t]
            else:
                t += 1
        m += 1


if __name__ == '__main__':
    path = r'F:\tupian\rain'
    main(path)
