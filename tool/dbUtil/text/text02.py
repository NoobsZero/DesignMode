# encoding: utf-8
from pyspark.sql import SparkSession


def CreateSparkContext():
    # 构建SparkSession实例对象
    spark = SparkSession.builder \
        .appName("SparkSessionExample") \
        .master("local") \
        .getOrCreate()
    # 获取SparkContext实例对象
    sc = spark.sparkContext
    return sc


def save_rdd_to_file(rdd, path):
    # 保存RDD数据，这里指定的路径tmp2文件夹必须是不存在的，否则会报错，因为创建的时候会自动创建
    return rdd.saveAsTextFile(path)


def read_file_to_RDD(sc, files_path):
    return sc.textFile(files_path)


def transform_rdd_to_DF(rdd, columns_list):
    df = rdd.toDF(columns_list)
    return df


if __name__ == '__main__':
    sc = CreateSparkContext()
    raw_ratings_rdd = read_file_to_RDD(sc, r'E:\dbsql\test\2019-08-19.sql')
    print(type(raw_ratings_rdd))
