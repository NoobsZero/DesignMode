# -*- encoding:utf-8 -*-
"""
@File   :testImage.py
@Time   :2020/12/2 12:27
@Author :Chen
@Software:PyCharm
"""
import cv2 as cv2
import numpy as np
import os
from tqdm import tqdm
import argparse
import shutil


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-image_dir', default=r'E:\toos\test\image', help='imageUtil dir')
    parser.add_argument('-output_dir_1', default=r'E:\toos\test\ok1/',
                        help='output dir')
    parser.add_argument('-output_dir_2', default=r'E:\toos\test\ok2/',
                        help='output dir')
    parser.add_argument('-output_dir_3', default=r'E:\toos\test\ok3/',
                        help='output dir')
    parser.add_argument('-copy_dir', default=r'E:\toos\test/',
                        help='copy dir')
    parser.add_argument('-image_width', default=960)
    parser.add_argument('-image_height', default=540)
    g_args = parser.parse_args()
    return g_args


class ImageNotation():
    def __init__(self, img_filename, g_args):

        self.img_filename = img_filename
        self.img = cv2.imread(self.img_filename)

        self.img = cv2.resize(self.img,
                              (g_args.image_width, int(self.img.shape[0] / self.img.shape[1] * g_args.image_width)))

        self.g_args = g_args

    def on_EVENT_LBUTTONDOWN(self, event, x, y, flags, a):
        if event == cv2.EVENT_LBUTTONDOWN:

            cv2.destroyAllWindows()
            shutil.move(self.img_filename, g_args.output_dir + os.path.split(self.img_filename)[1])

        elif event == cv2.EVENT_MOUSEWHEEL:
            cv2.destroyAllWindows()
            os.remove(self.img_filename)

    def showImg(self):
        cv2.destroyAllWindows()
        cv2.namedWindow("image")
        cv2.imshow("image", self.img)
        cv2.setMouseCallback("image", self.on_EVENT_LBUTTONDOWN)
        cv2.waitKey()


def get_filelist(dir):
    """
            递归获取目录下所有后缀为jpg的路径
        :param dir: 指定URL是目录（'dir'）
        :return: Filelist:list URL集合
        """
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 文件名列表，包含完整路径
            if filename[-3:] == 'jpg':
                Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist


if __name__ == '__main__':
    g_args = parseArgs()  # 解析参数


    def on_EVENT_LBUTTONDOWN(event, x, y, flags, a):
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     cv2.destroyAllWindows()
        #     shutil.move(filename, g_args.output_dir + os.path.split(filename)[1])
        # elif event == cv2.EVENT_RBUTTONDOWN:
        #     cv2.destroyAllWindows()
        if event == cv2.EVENT_MOUSEWHEEL:
            value = cv2.getMouseWheelDelta(flags)
            if value > 0:
                cv2.resize(img, (g_args.image_width, int(img.shape[0] / img.shape[1] * g_args.image_width,0,0)))
        # OpenCV图像缩放使用的函数是：resize
        # void
        # resize(InputArray
        # src, OutputArray
        # dst, Size
        # dsize, double
        # fx = 0, double
        # fy = 0, int
        # interpolation = INTER_LINEAR )
        # 参数含义：
        # InputArray
        # src - 原图像
        # OutputArray
        # dst - 输出图像
        # Size
        # dsize - 目标图像的大小
        # double
        # fx = 0 - 在x轴上的缩放比例
        # double
        # fy = 0 - 在y轴上的缩放比例
        # int
        # interpolation - 插值方式，有以下四种方式
        # INTER_NN - 最近邻插值
        # INTER_LINEAR - 双线性插值(缺省使用)
        # INTER_AREA - 使用象素关系重采样，当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于
        # INTER_NN
        # 方法。
        # INTER_CUBIC - 立方插值。
        # 说明：dsize与fx和fy必须不能同时为零


        k = cv2.waitKey(0)  # 等待并监听键盘活动
        if k == ord('c'):
            shutil.copyfile(filename, g_args.copy_dir + os.path.split(filename)[1])
        if k == ord('1'):
            cv2.destroyAllWindows()
            shutil.move(filename, g_args.output_dir_1 + os.path.split(filename)[1])
        elif k == ord('2'):
            cv2.destroyAllWindows()
            shutil.move(filename, g_args.output_dir_2 + os.path.split(filename)[1])
        elif k == ord('3'):
            cv2.destroyAllWindows()
            shutil.move(filename, g_args.output_dir_3 + os.path.split(filename)[1])
        elif k == ord('d'):
            cv2.destroyAllWindows()
            os.remove(filename)


    Filelist = get_filelist(g_args.image_dir)
    print(len(Filelist))
    print('======== Begin to notate ========')
    print('images located in: {}'.format(g_args.image_dir))
    print('total image: {}'.format(len(Filelist)))
    files = sorted(Filelist)
    if not os.path.exists(g_args.output_dir_1):
        os.mkdir(g_args.output_dir_1)
    if not os.path.exists(g_args.output_dir_2):
        os.mkdir(g_args.output_dir_2)
    if not os.path.exists(g_args.output_dir_3):
        os.mkdir(g_args.output_dir_3)
    for filename in tqdm(files):
        if os.path.exists(filename):
            img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)
            img = cv2.resize(img, (g_args.image_width, int(img.shape[0] / img.shape[1] * g_args.image_width)))
            cv2.namedWindow("image")
            cv2.imshow("image", img)
            print('\nimages located in: {}'.format(filename))
            # cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
            cv2.waitKey()
