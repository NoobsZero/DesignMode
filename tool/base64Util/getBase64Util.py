# -*- codeing = utf-8 -*-
# @Time :2020/7/29 8:43
# @Author:Eric
# @File : getBase64Util.py
# @Software: PyCharm
import base64  # 想将字符串转编码成base64,要先将字符串转换成二进制数据
# 自定义加密解密方式

def get_encode_base64(k, v=None):
    try:
        if v != None:
            data = k + '/' + v
        else:
            data = k
        clearBytesData = data.encode('utf-8')
        encodeData = base64.b64encode(clearBytesData)  # 被编码的参数必须是二进制数据
    except ValueError:
        print('无效参数！')
    else:
        print('加密成功！')
    return encodeData


def get_decode_base64(v):
    decodeData = base64.b64decode(v).decode('utf-8')
    return str(decodeData).split('/')[-1]
