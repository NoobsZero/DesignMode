# encoding: utf-8
"""
@file: video.py
@time: 2021/4/22 8:56
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import re
import sys
from datetime import datetime
import time
from dateutil.parser import parse


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_FileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return TimeStampToTime(t).split(' ')[0]


def getDate(time_dst_dir):
    """
    判断字符串中是否有符合时间规范的数据
    Args:
        time_dst_dir: 字符串或url

    Returns:字符串或url

    """
    time_dst = time_dst_dir.split('/')[-1]
    time_t1 = re.search(r'(\d{4}-\d{2}-\d{2})$', time_dst)
    time_t2 = re.search(r'(\d{4}\d{2}\d{2})$', str(time_dst))
    time_t4 = re.search(r'^(\d{4}\d{2}\d{2})', str(time_dst))
    time_t5 = re.search(r'^(d{2}\d{2})', str(time_dst))
    time_t6 = re.search(r'(d{2}\d{2})$', str(time_dst))
    time_t3 = re.search(r'(\d{4}年\d{2}月\d{2}日)$', str(time_dst))
    if time_t1:
        return time_t1.group(1)
    elif time_t2:
        return parse(time_t2.group(1)).strftime('%Y-%m-%d')
    elif time_t4:
        return parse(time_t4.group(1)).strftime('%Y-%m-%d')
    elif time_t3:
        return parse(re.sub(r'\D', "", time_t3.group(1))).strftime('%Y-%m-%d')
    # elif time_t5:
    #
    # elif time_t6:
    else:
        return get_FileCreateTime(time_dst_dir)


def validate(date_text, timeworn='%Y-%m-%d'):
    """
        时间检验，注意文件时间要符合日期规则超出无效！
    :param timeworn:
    :param date_text: 字符串
    :return: boolean
    """
    try:
        datetime.strptime(date_text, timeworn)
        retie = True
    except ValueError:
        retie = False
    return retie


def modifyTime(paths, numb):
    for home, dirs, files in os.walk(paths):
        if len(home.split('/')) == numb + 1:
            print(home)
        # for file in files:
        #     if len(home.split('/')) == numb:
        #         print(home)


def path_remake(path):
    return path.replace(' ', '\ ').replace('(', '\(').replace(')', '\)')


def demoteVideo(path, videoType, originalVideoPath='Raw', compressVideoPath='Compress'):
    """
    视频降频和截图
    Args:
        path: 视频文件路径
        videoType: 视频格式 []
        originalVideoPath: 原始视频存放路径
        compressVideoPath: 压缩后 + 截图

    Returns:

    """
    sizeMB = 25
    videoList = [os.path.join(home, file) for home, dirs, files in os.walk(path) for file in files if
                 file.split('.')[-1] in videoType and originalVideoPath not in home and compressVideoPath not in home]
    for path in videoList:
        videoPath, videoName = os.path.split(path)
        originalVideoPath = os.path.join(videoPath, originalVideoPath)
        compressVideoPath = os.path.join(videoPath, compressVideoPath)
        if not os.path.isdir(originalVideoPath):
            os.makedirs(originalVideoPath)
        if not os.path.isdir(compressVideoPath):
            os.makedirs(compressVideoPath)
        fileSizeMB = round(os.path.getsize(path) / float(1024 * 1024))
        originalFilePath = path_remake(path)
        frequencyFilePath = path_remake(os.path.join(compressVideoPath, videoName))
        pictureFilePath = os.path.splitext(path_remake(os.path.join(compressVideoPath, videoName)))[0] + ".jpg"
        if fileSizeMB >= sizeMB:
            os.system("ffmpeg -i " + originalFilePath + " -vf scale=iw*0.3:ih*0.3 " + frequencyFilePath)
        else:
            os.system("ffmpeg -i " + originalFilePath + " " + frequencyFilePath)
        os.system("ffmpeg -i " + originalFilePath + " -ss 0.500 -vframes 1 " + pictureFilePath)
        os.system("mv " + originalFilePath + " " + path_remake(os.path.join(originalVideoPath, videoName)))


if __name__ == '__main__':
    path = '/media/ubuntu/5591da6a-473f-4528-ba60-f14db431794c/违法原始数据备份20200422/0.视频'
    videoType = ['avi', 'mkv', 'mp4', 'MP4', 'ts']
    demoteVideo(path, videoType)
    # print(round(189314176 / float(1024 * 1024)))
    # modifyTime(paths, 7)
