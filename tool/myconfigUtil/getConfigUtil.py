# -*- codeing = utf-8 -*-
# @Time :2020/7/23 8:50
# @Author:Eric
# @File : getConfig.py
# @Software: PyCharm
import configparser

ftp_config_path = '/source/config.ini'


# 获取ftp配置信息（如果不指定section会获取所有section
def get_ftp_config(sections=None, config_file=ftp_config_path):
    # 创建配置文件对象
    con = configparser.ConfigParser()

    # 读取文件
    con.read(config_file, encoding='utf-8')

    # 获取所有section
    if sections is None:
        sections = con.sections()
        # ['url', 'email']
        param = []
        for section in sections:
            param.append(dict(con.items(section)))
        return param

    # 获取特定section
    else:
        items = con.items(sections)  # 返回结果为元组
        # [('baidu','http://www.baidu.com'),('port', '80')] 	# 数字也默认读取为字符串
        # 可以通过dict方法转换为字典，並且返回
        return dict(items)
