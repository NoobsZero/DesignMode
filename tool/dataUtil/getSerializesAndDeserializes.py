# -*- encoding:utf-8 -*-
"""
@File   :getSerializesAndDeserializes.py
@Time   :2020/12/3 8:34
@Author :Chen
@Software:PyCharm
"""
from importlib import import_module

# Serializes and de-serializes


def obj2dict(obj):
    dic = {'__class__': obj.__class__.__name__, '__module__': obj.__module__}
    dic.update(obj.__dict__)
    return dic


def dict2obj(dic):
    if '__class__' in dic:
        class_name = dic.pop('__class__')
        module_name = dic.pop('__module__')
        module = import_module(module_name)
        class_ = getattr(module, class_name)
        args = dict((key, value) for key, value in dic.items())
        instance = class_(**args)
    else:
        instance = dic
    return instance