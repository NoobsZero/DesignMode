# encoding: utf-8
"""
@file: InsertionSort.py
@time: 2021/7/8 14:39
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""


def insertionSort(A):
    """
        插入排序
    Args:
        A: 数组

    Returns:升序数组

    """
    # 初始化：第一次循环迭代之前（当j=2时），循环不变式成立
    # j[1,2,...,N-1]
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        # 保持：证明每次迭代保持循环不变式
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    # 终止：在循环终止时，不变式为我们提供一个有用的性质，该性质有助于证明算法是正确的。
    return A


def selectA(A, x):
    # for j in range(len(A)):
    if x in A:
        print(x)
    else:
        print(None)


def selectB(A, x):
    for j in range(len(A)):
        print(j)


if __name__ == '__main__':
    x = 6
    A = [5, 2, 4, 6, 1, 3]
    # print(insertionSort(A))
    selectB(A, x)
