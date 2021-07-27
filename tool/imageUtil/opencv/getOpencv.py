# encoding: utf-8
"""
@file: getOpencv.py
@time: 2021/7/1 18:14
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import cv2
import aircv as ac
from PIL import Image
import numpy as np


def bijiao(file1, file2):
    """
        判断两张图片是否是一张
    Args:
        file1:
        file2:

    Returns:

    """
    image1 = cv2.imread(file1)
    image2 = cv2.imread(file2)
    difference = cv2.subtract(image1, image2)
    print(difference)
    result = not np.any(difference)

    if result is True:
         print("两张图片一样")
    else:
         cv2.imwrite("result.jpg", difference)
         print ("两张图片不一样")


def matchImg(imgPath1, imgPath2):
    imgs = []

    # 原始图像，用于展示
    sou_img1 = cv2.imread(imgPath1)
    sou_img2 = cv2.imread(imgPath2)

    # 原始图像，灰度
    # 最小阈值100,最大阈值500
    img1 = cv2.imread(imgPath1, 0)
    blur1 = cv2.GaussianBlur(img1, (3, 3), 0)
    canny1 = cv2.Canny(blur1, 100, 500)
    cv2.imwrite('temp1.png', canny1)

    img2 = cv2.imread(imgPath2, 0)
    blur2 = cv2.GaussianBlur(img2, (3, 3), 0)
    canny2 = cv2.Canny(blur2, 100, 500)
    cv2.imwrite('temp2.png', canny2)

    target = cv2.imread('temp1.png')
    template = cv2.imread('temp2.png')

    # 调整显示大小
    target_temp = cv2.resize(sou_img1, (350, 200))
    target_temp = cv2.copyMakeBorder(target_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    template_temp = cv2.resize(sou_img2, (200, 200))
    template_temp = cv2.copyMakeBorder(template_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp)
    imgs.append(template_temp)

    theight, twidth = template.shape[:2]

    # 匹配拼图
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

    # 归一化
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 匹配后结果画圈
    cv2.rectangle(target, max_loc, (max_loc[0] + twidth, max_loc[1] + theight), (0, 0, 255), 2)

    target_temp_n = cv2.resize(target, (350, 200))
    target_temp_n = cv2.copyMakeBorder(target_temp_n, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp_n)

    imstack = np.hstack(imgs)

    cv2.imshow('stack' + str(max_loc), imstack)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


IMAGE_SIZE = 800


# 将图片缩放成短边IMAGE_SIZE
def changeImageSize(inputImage, x, y):
    xymin = min(x, y)
    rates = xymin / IMAGE_SIZE
    outputImage = cv2.resize(inputImage, (int(y / rates), int(x / rates)))
    return outputImage


# 判断短边是否小于IMAGE_SIZE，是的话执行resize
def judgeChangeable(image):
    h, w = image.shape[:2]
    if h > IMAGE_SIZE and w > IMAGE_SIZE:
        img = changeImageSize(image, h, w)
        return img
    else:
        return image


def getSmallPicture(srcPath='../eee.png', objPath='../xiaotu.png'):
    """
     找出图像中最佳匹配位置
    :param srcPath: 目标即背景图
    :param objPath: 模板即需要找到的图
    :return: 返回最佳匹配及其最差匹配和对应的坐标
    """
    srcIm = ac.imread(srcPath)
    objIm = ac.imread(objPath)
    objIm = judgeChangeable(objIm)
    print(objIm.shape)
    match_res = ac.find_template(srcIm, objIm, 0.5)
    print(match_res)
    return match_res['rectangle'][0]
    # if match_res is not None:
    # 如果存在则显示截取图片
    # rect_points = match_res['rectangle']
    # TL = rect_points[0]
    # BR = rect_points[3]
    #
    # img2 = srcIm[TL[1]:BR[1], TL[0]:BR[0]]
    # print(img2.shape)
    # plt.imshow(img2), plt.show()
    # else:
    #     print("Can't find objIm site")


def FindPic(target, template):
    """
    找出图像中最佳匹配位置
    :param target: 目标即背景图
    :param template: 模板即需要找到的图
    :return: 返回最佳匹配及其最差匹配和对应的坐标
    """
    target_rgb = cv2.imread(target)
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    template_rgb = cv2.imread(template, 0)
    # template_rgb = template_rgb[10:50, 10:40]
    # cv2.TM_CCOEFF （系数匹配法）
    # cv2.TM_CCOEFF_NORMED（相关系数匹配法）
    # cv2.TM_CCORR （相关匹配法）
    # cv2.TM_CCORR_NORMED （归一化相关匹配法）
    # cv2.TM_SQDIFF （平方差匹配法）
    # cv2.TM_SQDIFF_NORMED （归一化平方差匹配法）
    # res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF)
    value = cv2.minMaxLoc(res)
    print(value)
    return value[3][0]


def MovePictureToLocation(srcPath, objPath, match_res):
    im = Image.open(srcPath)
    im1 = Image.open(objPath)
    # im1.thumbnail((700, 100))
    im.paste(im1, match_res)
    im.show()


if __name__ == '__main__':
    srcPath = 'b1.png'
    objPath = 'b2.png'
    print(getSmallPicture(srcPath, objPath)[0])
    MovePictureToLocation(srcPath=srcPath, objPath=objPath, match_res=(69, 17))
