# encoding: utf-8
"""
@file: fontTTF.py
@time: 2021/6/8 17:26
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import base64
import re
from threading import Thread

import requests
from fontTools.ttLib import TTFont

base_mapping = {
    'seven': 7, 'three': 3, 'five': 5, 'two': 2, 'nine': 9, 'one': 1, 'six': 6, 'zero': 0, 'four': 4, 'eight': 8
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'cookie': '...'
}


def get_cmap(font_text):
    with open('world.ttf', 'wb') as f:
        f.write(font_text)
    font = TTFont('world.ttf')
    font.saveXML('world.xml')
    bestcmap = TTFont("world.ttf")['cmap'].getBestCmap()
    newmap = dict()
    for key in bestcmap.keys():
        value = bestcmap[key] if bestcmap[key] not in list(base_mapping.keys()) else base_mapping[bestcmap[key]]
        if isinstance(value, int):
            newmap[hex(key)] = value
    return newmap


if __name__ == '__main__':
    content = requests.get('https://xiawei518.b2b.huangye88.com/', headers=headers).text
    code_list = re.search("<span class='secret'>(.*?)</span>", content).group(1).replace("&#", "0").split(';')[:-1]
    font_data_after_decode = base64.b64decode(re.search('base64,(.*?)"\)', content).group(1))
    phone_number = "".join([str(get_cmap(font_data_after_decode)[code]) for code in code_list])
    print(phone_number)
#     content.replace(web_word, values)
