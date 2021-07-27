# encoding= utf-8
"""
@file: sendPost.py
@time: 2021/6/11 17:15
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""

import requests

url = 'http://192.168.50.100:8000/up'
files = {'files': open(r'F:\chejian\smart_city_images_ele_20210603_1mp4000004.jpg', 'rb')}
# data = {'xxx':xxx,'xxx':xxx}

# response = requests.post(url, files=files)
# json = response.json()
# print(response.text)

# if __name__ == '__main__':
#     urls = ['https://so.huangye88.com/?kw=%E7%BB%B4%E4%BF%AEE&page=2']
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "zh-CN,zh;q=0.9",
#         "Cache-Control": "max-age=0",
#         "Connection": "keep-alive",
#         "Cookie": "hy88showeditems=a%3A3%3A%7Bi%3A107767918%3Ba%3A3%3A%7Bs%3A7%3A%22subject%22%3Bs%3A87%3A%22%E8%9C%80%E5%B1%B1%E5%8C%BA%E9%A9%AC%E6%A1%B6%E7%96%8F%E9%80%9A%EF%BC%8C%E9%A9%AC%E6%A1%B6%E6%BC%8F%E6%B0%B4%E7%BB%B4%E4%BF%AE%E3%80%81%E5%8E%A8%E6%88%BF%E7%AE%A1%E9%81%93%E7%96%8F%E9%80%9A%E3%80%81%E5%90%88%E8%82%A5%E7%96%8F%E9%80%9A%E4%B8%8B%E6%B0%B4%E9%81%93%22%3Bs%3A3%3A%22url%22%3Bs%3A53%3A%22https%3A%2F%2Fhefei.huangye88.com%2Fxinxi%2F9465_107767918.html%22%3Bs%3A3%3A%22img%22%3Bs%3A68%3A%22http%3A%2F%2Foss.huangye88.net%2Flive%2Fuser%2F1159920%2F1456116345072966700-2.jpg%22%3B%7Di%3A115494615%3Ba%3A3%3A%7Bs%3A7%3A%22subject%22%3Bs%3A69%3A%22%E8%8B%8F%E5%B7%9E%E7%9C%9F%E7%A9%BA%E6%B3%B5%E7%BB%B4%E4%BF%AE%EF%BD%9C%E6%99%AE%E6%97%AD%E7%9C%9F%E7%A9%BA%E6%B3%B5%E7%BB%B4%E4%BF%AE%EF%BD%9C%E8%B4%9D%E5%85%8B%E7%9C%9F%E7%A9%BA%E6%B3%B5%E7%BB%B4%E4%BF%AE%22%3Bs%3A3%3A%22url%22%3Bs%3A48%3A%22https%3A%2F%2Fjixie.huangye88.com%2Fxinxi%2F115494615.html%22%3Bs%3A3%3A%22img%22%3Bs%3A67%3A%22http%3A%2F%2Foss.huangye88.net%2Flive%2Fuser%2F215678%2F1493967387060352500-0.jpg%22%3B%7Di%3A119016041%3Ba%3A3%3A%7Bs%3A7%3A%22subject%22%3Bs%3A42%3A%22%E5%AE%A4%E5%86%85%E8%87%AA%E6%9D%A5%E6%B0%B4%E7%AE%A1%E6%B8%97%E6%BC%8F%E7%BB%B4%E4%BF%AE%E7%96%8F%E9%80%9A%E7%AD%89%E7%AD%89%22%3Bs%3A3%3A%22url%22%3Bs%3A55%3A%22https%3A%2F%2Fnanjing.huangye88.com%2Fxinxi%2F9465_119016041.html%22%3Bs%3A3%3A%22img%22%3Bs%3A67%3A%22http%3A%2F%2Foss.huangye88.net%2Flive%2Fuser%2F416485%2F1496445398000561500-0.jpg%22%3B%7D%7D; PHPSESSID=16237273931629-f05711375b9383e74411b243c88aa3ea44b0838d; hy88loginid=3427140; hy88username=u3427140; hy88usergroup=12; hy88mobile=15174506817; showcj=1;",
#         "Host": "so.huangye88.com",
#         "Referer": "https://so.huangye88.com/?kw=%E7%BB%B4%E4%BF%AEE&type=sale",
#         "Sec-Fetch-Dest": "document",
#         "Sec-Fetch-Mode": "navigate",
#         "Sec-Fetch-Site": "same-origin",
#         "Sec-Fetch-User": "?1",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
#     }
#     for url in urls:
#         res = requests.get(url=url, headers=headers)
#         print(res.text)

if __name__ == '__main__':
    url = "http://192.168.50.100:8000/transform?data_type=json&imgpath=/6t/1.共享/7.workspace/collect_transformation/img"
    response = requests.get(url)
    print(response.text)
