# encoding: utf-8
"""
@file: Presigned.py
@time: 2021/7/5 15:44
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from minio.error import InvalidResponseError
from datetime import timedelta

from tool.minioUtil.MinioConfig import minioClient


class Presigned:

    # 生成一个用于HTTP GET操作的presigned URL
    def presigned_get_object(self):
        # 预先获得的对象名称的获取对象URL，将在2天后过期
        try:
            print(minioClient.presigned_get_object('dataset', 'libin/上海路口配置/8d2e287bf25b4a2f9c7da6cdc6f735f3+冀DS913L+1223+8d2e287bf25b4a2f9c7da6cdc6f735f3++0+@4154@@@2020-12-02=14=24=00+a0+1.jpg', expires=timedelta(days=7)))
            print("Sussess")
        # 由于内部预定位确实会获得存储桶位置，因此仍然可能出现响应错误
        except InvalidResponseError as err:
            print(err)

    # 生成一个用于HTTP PUT操作的presigned URL
    def presigned_put_object(self):
        try:
            print(minioClient.presigned_put_object('testfiles',
                                                   '123.txt',
                                                   expires=timedelta(days=7)))
            print("Sussess")
        except InvalidResponseError as err:
            print(err)

    # 允许给POST操作的presigned URL设置策略条件。这些策略包括比如，
    # 接收对象上传的存储桶名称，名称前缀，过期策略
    def presigned_post_policy(self, PostPolicy):
        pass


if __name__ == '__main__':
    Presigned().presigned_get_object()
