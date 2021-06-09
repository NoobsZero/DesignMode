# encoding: utf-8
"""
@file: testjson.py
@time: 2021/5/13 15:34
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import os
import sys
import time
import untangle
import json
import numpy as np
from PIL import Image, ImageDraw


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


labels = {'Non-motorVehicles': [1, '非机动车'], 'people': [2, '人'], 'bigCar': [3, '大车'],
          'RideBikePeople': [4, '骑自行车的人'], 'smallCar': [5, '小车'], 'jtd': [6, '交通灯']}


imagesKeys = ['id', 'width', 'height', 'file_name', 'license', 'flickr_url', 'coco_url', 'date_captured']
categoriesKeys = ['id', 'name', 'supercategory']


def categories(label):
    categoriesValues = [labels[label][0], labels[label][1], '']
    return dict(zip(categoriesKeys, categoriesValues))


def images(im, imagesIdex, addr):
    imagesValues = [imagesIdex, im.width, im.height, addr, '0', '', '', '0']
    return dict(zip(imagesKeys, imagesValues))


annotationsKeys = ['id', 'image_id', 'category_id', 'segmentation', 'area', 'bbox', 'iscrowd']


def annotations(annotationsId, imagesIndex, categoriesId, polygon=[], area='', bbox=[], iscrowd=0):
    annotationsValues = [annotationsId, imagesIndex, categoriesId, polygon, area, bbox, iscrowd]
    return dict(zip(annotationsKeys, annotationsValues))


if __name__ == '__main__':
    json_path = '/old_disk/data/suanfa/panliuhua/up/路口分割2021-04-26/2-2-2/标注员/test/xml'
    img_path = '/old_disk/data/suanfa/panliuhua/up/路口分割2021-04-26/2-2-2/标注员/test/img1'
    local_json_txt = '/old_disk/data/suanfa/panliuhua/up/路口分割2021-04-26/2-2-2/标注员/test/xml_20210514.json'
    annotationsId = 1
    categoriesList, imagesList, annotationsList = [], [], []
    for key in labels:
        categoriesList.append(categories(key))
    for src_dir, dirs, files in os.walk(json_path):
        for filename in files:
            try:
                imagePath = os.path.join(img_path, str(filename).replace('.xml', '.jpg'))
                im = Image.open(imagePath)
                imagesId = get_stamp13()
                imagesList.append(images(im, imagesId, imagePath.lstrip('/old_disk/data/suanfa/')))
                for data in untangle.parse(os.path.join(src_dir, filename)).annotation.object:
                    name = data.name.__dict__['cdata']
                    categoriesId = labels[name][0]
                    xmin = int(data.bndbox.xmin.__dict__['cdata']) - 1
                    ymin = int(data.bndbox.ymin.__dict__['cdata']) - 1
                    xmax = int(data.bndbox.xmax.__dict__['cdata'])
                    ymax = int(data.bndbox.ymax.__dict__['cdata'])
                    assert (xmax > xmin)
                    assert (ymax > ymin)
                    o_width = abs(xmax - xmin)
                    o_height = abs(ymax - ymin)
                    bbox = [xmin, ymin, o_width, o_height]
                    annotationsList.append(annotations(annotationsId=annotationsId, imagesIndex=imagesId,
                                                       categoriesId=categoriesId, bbox=bbox))
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
