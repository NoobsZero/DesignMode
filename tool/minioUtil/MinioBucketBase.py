# encoding: utf-8
"""
@file: MinioBucketBase.py
@time: 2021/7/5 15:43
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from minio.error import InvalidResponseError

from tool.minioUtil.MinioConfig import minioClient


class Bucket:
    # 创建桶(调用make_bucket来创建一个存储桶) make_bucket函数
    """
    注：创建桶命名限制：小写字母，句点，连字符和数字是
    唯一允许使用的字符（使用大写字母、下划线等命名会报错），长度至少应为3个字符
    """

    def create_bucket(self, bucket_name):
        try:
            if minioClient.bucket_exists(bucket_name=bucket_name):  # bucket_exists：检查桶是否存在
                print("该存储桶已经存在")
            else:
                minioClient.make_bucket(bucket_name)
                print("存储桶创建成功")
        except InvalidResponseError as err:
            print(err)

    # 列出所有的存储桶 list_buckets函数
    def get_bucket_list(self):
        try:
            buckets = minioClient.list_buckets()
            for bucket in buckets:
                print(bucket.name, bucket.creation_date)  # 获取桶的名称和创建时间
        except InvalidResponseError as err:
            print(err)

    # 删除存储桶
    def get_remove_bucket(self, bucket_name):
        try:
            minioClient.remove_bucket(bucket_name)
            print("删除存储桶成功")
        except InvalidResponseError as err:
            print(err)

    # 列出存储桶中所有对象  或者使用 list_objects_v2也可
    def get_bucket_files(self, bucket_name):
        try:
            objects = minioClient.list_objects(bucket_name, prefix='libin/上海路口配置/',
                                               recursive=True)  # prefix用于过滤的对象名称前缀
            for obj in objects:
                print(obj.bucket_name, obj.object_name, obj.last_modified,
                      obj.etag, obj.size, obj.content_type)
                # 885d2110e48fd0f0d77eccf0358a2325
                # print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
                #       obj.etag, obj.size, obj.content_type)
        except InvalidResponseError as err:
            print(err)

    # 列出存储桶中未完整上传的对象
    def get_list_incomplete_uploads(self, bucket_name):
        try:
            uploads = minioClient.list_incomplete_uploads(bucket_name,
                                                          prefix=None,
                                                          recursive=True)
            for obj in uploads:
                print(obj.bucket_name, obj.object_name, obj.upload_id, obj.size)
        except InvalidResponseError as err:
            print(err)

    # 获取存储桶的当前策略
    def bucket_policy(self, bucket_name):
        try:
            policy = minioClient.get_bucket_policy(bucket_name)
            print(policy)
        except InvalidResponseError as err:
            print(err)

    # # 给指定的存储桶设置存储桶策略
    # def get_set_bucket_policy(self):
    #     try:
    #         minioClient.set_bucket_policy('testfiles', policy.READ_ONLY)
    #     except InvalidResponseError as err:
    #         print(err)

    # 获取存储桶上的通知配置
    def bucket_notification(self):
        try:
            # 获取存储桶的通知配置。
            notification = minioClient.get_bucket_notification('testfiles')
            print(notification)
            # 如果存储桶上没有任何通知：
            # notification  == {}
        except InvalidResponseError as err:
            print(err)

    # 给存储桶设置通知配置
    def set_bucket_notification(bucket_name, notification):
        pass

    # 删除存储桶上配置的所有通知
    def remove_all_bucket_notifications(bucket_name):
        try:
            minioClient.remove_all_bucket_notifications('mybucket')
        except InvalidResponseError as err:
            print(err)

    # 监听存储桶上的通知
    def listen_bucket_notification(bucket_name, prefix, suffix, events):
        pass


if __name__ == '__main__':
    # Bucket().bucket_notification()
    bu = Bucket()
    # print(bu.get_bucket_list())
    bu.get_bucket_files("dataset")
    # Bucket().get_bucket_list()
