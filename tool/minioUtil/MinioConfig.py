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
minioClient = Minio("192.168.50.75:9000", access_key="minio", secret_key="minioadmin", secure=False)

