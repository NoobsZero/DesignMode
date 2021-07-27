# encoding: utf-8
"""
@file: testjson.py
@time: 2021/5/13 15:34
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import json
import os
from datetime import datetime

from PIL import Image, ImageDraw
import sys
import traceback
import json
import numpy as np
import time


class ReadConfigure:
    def __init__(self):
        self.str = ""
        pass

    def read(self, filePath):
        try:
            fd = open(filePath, 'rb')
        except Exception as ex:
            print(ex)
            msg = traceback.format_exc()
            # print(msg)
            sys.exit(1)
        self.str = fd.read()
        # print "conf_content:", self.str
        return True

    def getReadData(self):
        return self.str


def parseInputParameter(filePath):
    rc = ReadConfigure()
    if not rc.read(filePath):
        sys.exit(1)
    return json.loads(rc.getReadData())


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


class JsonConfig:
    def __init__(self):
        self.objMap = {}

    @classmethod
    def loadConf(cls, filePath):
        self = cls.__new__(cls)
        self.objMap = parseInputParameter(filePath)
        return self

    def getKeys(self):
        return self.objMap.keys()

    def getValue(self, keyName):
        return self.objMap[keyName]


def mask2box(mask):
    '''从mask反算出其边框
    mask：[h,w]  0、1组成的图片
    1对应对象，只需计算1对应的行列号（左上角行列号，右下角行列号，就可以算出其边框）
    '''
    # np.where(mask==1)
    index = np.argwhere(mask == 1)
    rows = index[:, 0]
    clos = index[:, 1]
    # 解析左上角行列号
    left_top_r = np.min(rows)  # y
    left_top_c = np.min(clos)  # x

    # 解析右下角行列号
    right_bottom_r = np.max(rows)
    right_bottom_c = np.max(clos)

    # return [(left_top_r,left_top_c),(right_bottom_r,right_bottom_c)]
    # return [(left_top_c, left_top_r), (right_bottom_c, right_bottom_r)]
    # return [left_top_c, left_top_r, right_bottom_c, right_bottom_r]  # [x1,y1,x2,y2]
    return [left_top_c, left_top_r, right_bottom_c - left_top_c,
            right_bottom_r - left_top_r]  # [x1,y1,w,h] 对应COCO的bbox格式


def polygons_to_mask(img_shape, polygons):
    mask = np.zeros(img_shape, dtype=np.uint8)
    mask = Image.fromarray(mask)
    if len(polygons):
        xy = list(map(tuple, polygons))
        ImageDraw.Draw(mask).polygon(xy=xy, outline=1, fill=1)
    mask = np.array(mask, dtype=bool)
    return mask


def get_stamp13(datetime_obj=None):
    """

    Args:
        datetime_obj:

    Returns:

    """
    if datetime_obj is None:
        t = time.time()
        return int(round(t * 1000))
    # 生成13时间戳   eg:1557842280000
    datetime_obj = datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M:%S.%f')
    # datetime_str = datetime.datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:%S.%f')
    # # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_obj.timetuple())))
    # # 3位，微秒
    data_microsecond = str("%06d" % datetime_obj.microsecond)[0:3]
    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


# labels = {'banmaxian': [1, '斑马线'], 'tingzhixian': [2, '停止线'], 'zhixing': [3, '直行'], 'zuozhuan': [4, '左转'],
#           'youzhuan': [5, '右转'], 'zhixingzuozhuan': [6, '直行加左转'], 'zhixingyouzhuan': [7, '直行加右转'],
#           'zuozhuandiaotou': [8, '左转加掉头'], 'shixian': [9, '车道虚线'], 'xuxian': [10, '车道实线'],
#           'xiaoche': [11, '小车'], 'dache': [12, '大车'], 'xingren': [13, '行人'], 'daizhuanqu': [14, '待转区'],
#           'huangxian': [15, '黄线'], 'zhanyongchedao': [16, '占用车道'], 'bus_road': [17, '公交车道'],
#           'zhalan': [18, '栅栏'], 'zhixingdiaotou': [19, '直行掉头'], 'daoliuxian': [20, '导流线'],
#           'fanxiangdaoxiangxian': [21, '反向导向线'], 'other': [22, '其他'], 'zuozhuanyouzhuanzhixing': [23, '左转右转直行'],
#           'zuozhuanyouzhuan': [24, '左转右转']}

labels = {'cellphone': [1, 'cellphone'], 'people': [2, 'people'], 'Sticker': [3, 'Sticker']}
categoriesKeys = ['id', 'name', 'supercategory']


def categories(label):
    categoriesValues = [labels[label][0], labels[label][1], '']
    return dict(zip(categoriesKeys, categoriesValues))


imagesKeys = ['id', 'width', 'height', 'file_name', 'license', 'flickr_url', 'coco_url', 'date_captured']


def images(im, imagesIdex, addr):
    imagesValues = [imagesIdex, im.width, im.height, addr, '0', '', '', '0']
    return dict(zip(imagesKeys, imagesValues))


def annotations(annotationsId, imagesIndex, categoriesId, polygon=None, bbox=None):
    if bbox is None and polygon is None:
        annotationsValues = [annotationsId, imagesIndex, categoriesId, '', 0]
        return dict(zip(['id', 'image_id', 'category_id', 'area', 'iscrowd'], annotationsValues))
    else:
        annotationsValues = [annotationsId, imagesIndex, categoriesId, polygon, '', bbox, 0]
        return dict(
            zip(['id', 'image_id', 'category_id', 'segmentation', 'area', 'bbox', 'iscrowd'], annotationsValues))


def toPolygons(polygon):
    polygons = []
    if len(polygon):
        for po in polygon:
            polygons.append(po[0])
            polygons.append(po[1])
    return polygons


if __name__ == '__main__':
    json_path = r'F:\chejian\img\file\src\json'
    img_path = r'F:\chejian\img\file\src\mark'
    # local_json_txt = '/old_disk/data/suanfa/panliuhua/up/路口分割2021-04-26/2-2-2/标注员/test/test_20210513.json'
    local_json_txt = r'F:\chejian\img\file\src\test_20210702.json'
    annotationsId = 1
    categoriesList, imagesList, annotationsList = [], [], []
    for key in labels:
        categoriesList.append(categories(key))
    for src_dir, dirs, files in os.walk(json_path):
        for filename in files:
            try:
                oldjson = JsonConfig.loadConf(os.path.join(src_dir, filename))
                imagePath = os.path.join(img_path, str(filename).rstrip('.json'))
                im = Image.open(imagePath)
                imagesId = get_stamp13()
                imagesList.append(images(im, imagesId, imagePath.lstrip('/old_disk/data/suanfa/')))
                for data in oldjson.getValue('objects'):
                    categoriesId = labels[data['label']][0]
                    if 'polygons' in data:
                        polygon = data['polygon']
                        annotationsList.append(annotations(annotationsId, imagesId, categoriesId, [toPolygons(polygon)],
                                                           mask2box(polygons_to_mask([im.height, im.width], polygon))))
                    else:
                        annotationsList.append(annotations(annotationsId, imagesId, categoriesId))
                    annotationsId += 1
            except FileNotFoundError as e:
                print(e)
                pass
    keys = ['categories', 'images', 'annotations']
    values = [categoriesList, imagesList, annotationsList]
    dictionary = dict(zip(keys, values))
    j = json.dumps(dictionary, ensure_ascii=False, cls=NpEncoder, indent=4, sort_keys=True)
    with open(local_json_txt, 'a', encoding='utf-8', errors="ignore") as fo:
        fo.write(j)
        fo.flush()
