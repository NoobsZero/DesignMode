import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fontTools.ttLib import TTFont


# 抓取文本内容
class AutoSpider:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument(
            'Accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"')
        self.chrome_options.add_argument('Accept-Encoding="gzip, deflate, br"')
        self.chrome_options.add_argument('Accept-Language="zh-CN,zh;q=0.9,en;q=0.8"')
        self.chrome_options.add_argument('Cache-Control="max-age=0"')
        self.chrome_options.add_argument('Connection="keep-alive"')
        self.chrome_options.add_argument('Upgrade-Insecure-Requests="1"')
        self.chrome_options.add_argument(
            'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"')

    def getNote(self):
        url = "https://club.autohome.com.cn/bbs/thread/1032f3a3926a4aaa/95816107-1.html"
        self.chrome_options.add_argument('Host="club.autohome.com.cn"')

        driver = webdriver.Chrome(chrome_options=self.chrome_options)
        driver.get(url)

        # 获取页面内容
        text = driver.find_element_by_tag_name('html').get_attribute('outerHTML')
        driver.quit()
        return text
        # # 匹配ttf font
        # cmp = re.compile("url\('(//.*.ttf)'\) format\('woff'\)")
        # rst = cmp.findall(text)
        # ttf = requests.get("http:" + rst[0], stream=True)
        # with open("autohome.ttf", "wb") as pdf:
        #     for chunk in ttf.iter_content(chunk_size=1024):
        #         if chunk:
        #             pdf.write(chunk)
        # # 解析字体库font文件
        # font = TTFont('autohome.ttf')
        # uniList = font['cmap'].tables[0].ttFont.getGlyphOrder()
        # utf8List = [eval("'\\u" + uni[3:] + "'").encode("utf-8") for uni in uniList[1:]]


if __name__ == '__main__':
    font = TTFont('ChcCQ1sUz0yANyKDAABj8LPX4oE56..ttf')
    uniList = font['cmap'].tables[0].ttFont.getGlyphOrder()
    utf8List = [eval("'\\u" + uni[3:] + "'").encode("utf-8") for uni in uniList[1:]]
    wordList = ['大', '七', '三', '上', '下', '不', '中', '档', '比', '油', '泥', '灯', '九', '了', '二', '五', '低', '保', '光',
                '八', '公', '六', '养', '内', '冷', '副', '加', '动', '十', '电', '的', '皮', '盘', '真', '着', '路', '身', '软',
                '过', '近', '远', '里', '量', '长', '门', '问', '只', '右', '启', '呢', '味', '和', '响', '四', '地', '坏', '坐',
                '外', '多', '大', '好', '孩', '实', '小', '少', '短', '矮', '硬', '空', '级', '耗', '雨', '音', '高', '左', '开',
                '当', '很', '得', '性', '自', '手', '排', '控', '无', '是', '更', '有', '机', '来', ]
    # 获取文本内容
    note = AutoSpider().getNote()
    # print('---------------after-----------------')
    for i in range(len(utf8List)):
        note = note.encode("utf-8").replace(utf8List[i], wordList[i].encode("utf-8")).decode("utf-8")
    print(note)
    # print('---------------after-----------------')
    # for i in range(len(utf8List)):
    #     note = note.encode("utf-8").replace(utf8List[i], wordList[i].encode("utf-8")).decode("utf-8")
    # print(note)
    # driver.quit()
    # print(uniList)
