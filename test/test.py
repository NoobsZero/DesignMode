# -*- codeing = utf-8 -*-
# @Time :2020/7/21 13:17
# @Author:Eric
# @File : test.py
# @Software: PyCharm
from tool.ftpUtil.getFtpUtil import FTP_OPS
import os

if __name__ == '__main__':
    ftp = FTP_OPS()
    url = '/jma/hsd/202007/20/'
    localpath = "E:/hsd/202007/20/"

    def get_urlOrlis_download_file(url, localpath):
        try:
            doc_urls = ftp.get_ftp_urls(url)
            print('\033[0;32;40m获取路径:' + url + ',下的列表,成功!\033[0m')
            doc_urls.sort()
            for doc_url in doc_urls:
                print('\033[0;32;40m读取:' + doc_url + ',读取中。。。。。。\033[0m')
                lis_urls = None
                while lis_urls == None:
                    print('\033[0;32;40m读取失败：:' + doc_url + ',重新读取。。。。。。\033[0m')
                    lis_urls = ftp.get_ftp_urls(doc_url, 'FLDK')
                    print(lis_urls)
                print('\033[0;32;40m读取:' + doc_url + '成功！开始写入。。。。。。\033[0m')
                for i in lis_urls:
                    with open(localpath + doc_url.split('/')[-1] + ".txt", 'a+') as fp:
                        fp.write(i + '\n')
                        fp.flush()
                print('\033[0;32;40m执行写入成功！文件名字为:' + doc_url.split('/')[-1] + '\033[0m')
        except Exception:
            get_urlOrlis_download_file(url, localpath)


    ftp.get_url_download_file('E:/hsd/202007/21/url21/00.txt','E:/hsd/202007/21/00')