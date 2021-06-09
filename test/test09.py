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

from untitled.tool.myconfigUtil.JsonConfig import JsonConfig
from PIL import Image


labels = {'banmaxian': [1, '斑马线'], 'tingzhixian': [2, '停止线'], 'zhixing': [3, '直行'], 'zuozhuan': [4, '左转'],
          'youzhuan': [5, '右转'], 'zhixingzuozhuan': [6, '直行加左转'], 'zhixingyouzhuan': [7, '直行加右转'],
          'zuozhuandiaotou': [8, '左转加掉头'], 'shixian': [9, '车道虚线'], 'xuxian': [10, '车道实线'],
          'xiaoche': [11, '小车'], 'dache': [12, '大车'], 'xingren': [13, '行人'], 'daizhuanqu': [14, '待转区'],
          'huangxian': [15, '黄线'], 'zhanyongchedao': [16, '占用车道'], 'bus_road': [17, '公交车道'],
          'zhalan': [18, '栅栏'], 'zhixingdiaotou': [19, '直行掉头'], 'daoliuxian': [20, '导流线'],
          'fanxiangdaoxiangxian': [21, '反向导向线'], 'other': [22, '其他'], 'zuozhuanyouzhuanzhixing': [23, '左转右转直行'],
          'zuozhuanyouzhuan': [24, '左转右转']}
categoriesKeys = ['id', 'name', 'supercategory']


def categories(label):
    categoriesValues = [labels[label][0], labels[label][1], '']
    return dict(zip(categoriesKeys, categoriesValues)), labels[label][0]


imagesKeys = ['id', 'width', 'height', 'file_name', 'license', 'flickr_url', 'coco_url', 'date_captured']


def images(im, imagesIdex, addr):
    imagesValues = [imagesIdex, im.width, im.height, addr, '0', '', '', '0']
    return dict(zip(imagesKeys, imagesValues))


annotationsKeys = ['id', 'image_id', 'category_id', 'segmentation', 'area', 'bbox', 'iscrowd']


def annotations(annotationsId, imagesIndex, categoriesId, polygon):
    annotationsValues = [annotationsId, imagesIndex, categoriesId, polygon, '', [], 0]
    return dict(zip(annotationsKeys, annotationsValues))


def DelRepeat(data, key):
    new_data = [] # 用于存储去重后的list
    values = []   # 用于存储当前已有的值
    for d in data:
        if d[key] not in values:
            new_data.append(d)
            values.append(d[key])
    return new_data


if __name__ == '__main__':
    json_url = r'\\192.168.30.41\0_.算法部\panliuhua\up\路口分割2021-04-26\2-2-2\标注员\test\json'
    local_json_txt = r'F:\chejian\annotations\test_20210513.json'
    imagesId = 1
    annotationsId = 1
    categoriesList, imagesList, annotationsList = [], [], []
    for src_dir, dirs, files in os.walk(json_url):
        for filename in files:
            oldjson = JsonConfig.loadConf(os.path.join(src_dir, filename))
            imagePath = os.path.join('panliuhua/up/路口分割2021-04-26/2-2-2/标注员/test/img/', str(filename).rstrip('.json'))
            im = Image.open(json_url + '\\' + str(filename).rstrip('.json'))
            imagesList.append(images(im, imagesId, imagePath))
            for data in oldjson.getValue('objects'):
                categorie, categoriesId = categories(data['label'])
                categoriesList.append(categorie)
                annotationsList.append(annotations(annotationsId, imagesId, categoriesId, data['polygon']))
                annotationsId += 1
            imagesId += 1
    keys = ['categories', 'images', 'annotations']
    values = [DelRepeat(categoriesList, 'id'), imagesList, annotationsList]
    dictionary = dict(zip(keys, values))
    j = json.dumps(dictionary, ensure_ascii=False)
    print(dictionary)
    # with open(local_json_txt, 'a', encoding='utf-8', errors="ignore") as fo:
    #     fo.write(j)
    #     fo.flush()
