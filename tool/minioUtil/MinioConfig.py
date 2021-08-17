# encoding: utf-8
"""
@file: MinioConfig.py
@time: 2021/7/5 15:43
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""

from minio import Minio

# warnings.filterwarnings('ignore')
minioClient = Minio("192.168.41.69:8000", access_key="Afakerchen@em-data.com.cn", secret_key="asdf1234?", secure=False)
