# -*- encoding:utf-8 -*-
"""
@File   :ch01.py
@Time   :2020/12/11 12:30
@Author :Chen
@Software:PyCharm
"""
import json
import time

import pyautogui as pag
import requests
import selenium
from browsermobproxy import Server
from bs4 import BeautifulSoup
from selenium import webdriver
import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WindyKey(object):

    def mouseAndKeyboard(self):
        server = Server("E:\\JetBrains\\maven\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat", {'port': 8080})
        server.start()
        proxy = server.create_proxy()
        chrome_options = Options()
        chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
        driver = webdriver.Chrome(chrome_options=chrome_options)
        base_url = "http://chinacar.com.cn/search.html"
        proxy.new_har('chinacar', options={'captureHeaders': True, 'captureContent': True})
        driver.get(base_url)

        _dict = {}
        while True:
            time.sleep(10)
            result = proxy.har
            for entry in result['log']['entries']:
                url = entry['request']['url']
                if 'http://chinacar.com.cn/Home/GonggaoSearch/GonggaoSearch/search_json?_dc=' in url:
                    data = entry['response']['content']['text']
                    if '没有查到相关数据，请更改查询条件' not in data:
                        _dict[url] = json.loads(data)
                    else:
                        print(data)
            if len(_dict) >= 5:
                break

        for key, values in _dict.items():
            print(values)
        time.sleep(1000)
        server.stop()
        driver.quit()



if __name__ == '__main__':
    str1 ={"success":"true","totalCount":"46","msg":"ok","topics":[{'pic':'<img src="http://img.chinacar.com.cn/spic/x7t91108360.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x7t91108360.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400Z','clmc':'自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'337','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x2700,2800,2900,3000,3100,3200,3300,3400,3500','edzzl':'31500,31800,32000','ckbj':'','tarid':'OTI1Mjcw',                'tarid_nobase':'925270','invalid':'true','tarpic':'/spic/x7t91108360.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x7u11144680.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x7u11144680.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9402TJZ','clmc':'集装箱运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'337','zs':'3','zj':'7480+1310+1310,7180+1310+1310,6880+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12450x2480,2500,2550x1410,1450,1500,1550,1580,1600,1650','edzzl':'34700,34400,34200','ckbj':'','tarid':'OTI1NTg2',                'tarid_nobase':'925586','invalid':'true','tarpic':'/spic/x7u11144680.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x7u81159940.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x7u81159940.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9380Z','clmc':'自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'337','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2550,2500x3500,3400,3300,3200,3100,3000,2900,2800,2700','edzzl':'29500,29800,30200','ckbj':'','tarid':'OTI1OTQ1',                'tarid_nobase':'925945','invalid':'true','tarpic':'/spic/x7u81159940.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x7x61670140.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x7x61670140.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400ZLS','clmc':'散装粮食运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'337','zs':'3','zj':'3950+1310+1310,3830+1310+1310,3730+1310+1310,3600+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'10000,9500,9000,8500x2500,2550x2950,3150,3350,3550,3750,3950','edzzl':'32250,31900,31500','ckbj':'','tarid':'OTI2MDk5',                'tarid_nobase':'926099','invalid':'true','tarpic':'/spic/x7x61670140.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x6x61669930.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x6x61669930.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9403TJZE','clmc':'集装箱运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'336','zs':'3','zj':'5600+1310+1310,5880+1310+1310,6150+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'9500,9800,10000,10500,10980x2550,2500x1550,1600,1650,1700,1750,1800,1850','edzzl':'35000,34750,34510','ckbj':'','tarid':'OTE1ODEx',                'tarid_nobase':'915811','invalid':'true','tarpic':'/spic/x6x61669930.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x6t91108330.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x6t91108330.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400ZHX','clmc':'自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'336','zs':'3','zj':'4180+1310+1310,4000+1310+1310,3810+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'9000,8500,8000x2500,2550x4000,3800,3700,3600,3500,3400,3200','edzzl':'31500,31900,32200','ckbj':'','tarid':'OTE3Mzk4',                'tarid_nobase':'917398','invalid':'true','tarpic':'/spic/x6t91108330.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x6u11145260.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x6u11145260.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401Z','clmc':'自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'336','zs':'3','zj':'5580+1310+1310,5380+1310+1310,5080+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'11500,11000,10500x2500,2550x2500,2700,2800,2900,3000,3100,3200,3300,3400,3500','edzzl':'32900,33100,33500','ckbj':'','tarid':'OTE3NDgy',                'tarid_nobase':'917482','invalid':'true','tarpic':'/spic/x6u11145260.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x6u51208940.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x6u51208940.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400TDPQX','clmc':'低平板半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'336','zs':'3','zj':'7300+1310+1310,7200+1310+1310,7100+1310+1310,7000+1310+1310,6900+1310+1310,6700+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13740,12990,12500x3000,2800x1750,1700,1600','edzzl':'33500,33700,34000','ckbj':'','tarid':'OTE3ODg2',                'tarid_nobase':'917886','invalid':'true','tarpic':'/spic/x6u51208940.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x4t91100650.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x4t91100650.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400ZQX','clmc':'自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'334','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x2700,2800,2900,3000,3100,3200,3300,3400,3500','edzzl':'32900,32500,32200','ckbj':'','tarid':'ODk3MTUz',                'tarid_nobase':'897153','invalid':'true','tarpic':'/spic/x4t91100650.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x3t91104370.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x3t91104370.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401TJZE','clmc':'集装箱运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'333','zs':'3','zj':'7800+1310+1310,8000+1310+1310,8200+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13950x2550,2500,2480x1460,1550,1600,1650','edzzl':'34700,34200','ckbj':'','tarid':'ODg2OTY0',                'tarid_nobase':'886964','invalid':'true','tarpic':'/spic/x3t91104370.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x3t91114790.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x3t91114790.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400TJZE','clmc':'集装箱运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'333','zs':'3','zj':'8900+1310+1310,8500+1310+1310,8100+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13950x2550,2500,2480x1480,1500,1550,1600,1650','edzzl':'33500,33700,34000','ckbj':'','tarid':'ODg3MDEy',                'tarid_nobase':'887012','invalid':'true','tarpic':'/spic/x3t91114790.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x3t91122900.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x3t91122900.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400TPB','clmc':'平板运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'333','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3100,3000,2900,2800,2700,1700,1650,1600,1550,1500','edzzl':'34000,33800,33410','ckbj':'','tarid':'ODg3MDM2',                'tarid_nobase':'887036','invalid':'true','tarpic':'/spic/x3t91122900.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x3x31570510.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x3x31570510.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9020XLJ','clmc':'旅居挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'333','zs':'1','zj':'3945','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'6012,5999x2370x2500,2750,2610','edzzl':'160','ckbj':'','tarid':'ODkyNjA0',                'tarid_nobase':'892604','invalid':'true','tarpic':'/spic/x3x31570510.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x1w61569360.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x1w61569360.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401ZHX','clmc':'自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'331','zs':'3','zj':'5100+1310+1310,4850+1310+1310,4650+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'10500,10000,9500x2550,2500x4000,3800,3600,3500,3400','edzzl':'31420,31700,32000,32150','ckbj':'','tarid':'ODgwODQ4',                'tarid_nobase':'880848','invalid':'true','tarpic':'/spic/x1w61569360.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/x0x01524760.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/x0x01524760.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP5041XLJ','clmc':'旅居车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'CA1041P40K50L1BE6A84',                'pc':'330','zs':'2','zj':'2800','fdjxh':'Q23-95E60','fdjcs':'安徽全柴动力股份有限公司',                'rlzl':'柴油','wxcc':'5995,5780,5700x2240,2340,2400,2500x2900,3000,3100,3200','edzzl':'','ckbj':'','tarid':'ODczODAx',                'tarid_nobase':'873801','invalid':'true','tarpic':'/spic/x0x01524760.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91101860.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91101860.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400LB','clmc':'栏板半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3100,3000,2900,2800,2700','edzzl':'34200,34000,33700','ckbj':'','tarid':'ODU1MjY2',                'tarid_nobase':'855266','invalid':'true','tarpic':'/spic/w8t91101860.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91106510.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91106510.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400CCYEZX','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3950,3900,3750,3700,3550,3500,3350,3300,3150,3100','edzzl':'31500,31800,32200','ckbj':'','tarid':'ODU1NTk2',                'tarid_nobase':'855596','invalid':'true','tarpic':'/spic/w8t91106510.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91119200.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91119200.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400CCYEQX','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3950,3900,3750,3700,3550,3500,3350,3300,3150,3080','edzzl':'34000,33700,33410','ckbj':'','tarid':'ODU1NjAw',                'tarid_nobase':'855600','invalid':'true','tarpic':'/spic/w8t91119200.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u01142320.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u01142320.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9200TCL','clmc':'车辆运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'2','zj':'7800+1400,7200+1400,7100+1400','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13750,13700x2550,2500x4000,3800,3700,3600,3500,3400,3300','edzzl':'12600,12900,13200','ckbj':'','tarid':'ODU1NjA3',                'tarid_nobase':'855607','invalid':'true','tarpic':'/spic/w8u01142320.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u01124960.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u01124960.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400LBE','clmc':'栏板半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3100,3000,2900,2800,2700','edzzl':'34200,34000,33700','ckbj':'','tarid':'ODU1NjY3',                'tarid_nobase':'855667','invalid':'true','tarpic':'/spic/w8u01124960.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91103650.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91103650.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400TPBE','clmc':'平板运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3100,3000,2900,2800,2700,1650,1600,1550,1500','edzzl':'34000,33800,33410','ckbj':'','tarid':'ODU1ODA4',                'tarid_nobase':'855808','invalid':'true','tarpic':'/spic/w8t91103650.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91108680.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91108680.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400CCYE','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3950,3900,3750,3700,3550,3500,3350,3300,3150,3100','edzzl':'32500,32800,33180','ckbj':'','tarid':'ODU1OTYx',                'tarid_nobase':'855961','invalid':'true','tarpic':'/spic/w8t91108680.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91104480.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91104480.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400CCYZX','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3950,3900,3750,3700,3550,3500,3350,3300','edzzl':'31500,31800,32200','ckbj':'','tarid':'ODU2MDkz',                'tarid_nobase':'856093','invalid':'true','tarpic':'/spic/w8t91104480.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u01134100.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u01134100.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9220TCL','clmc':'车辆运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'2','zj':'7370+1310,7600+1310,8000+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13750x2550,2500x4000,3800,3700,3600,3500,3400,3200','edzzl':'14500,14200,13800','ckbj':'','tarid':'ODU2MzIx',                'tarid_nobase':'856321','invalid':'true','tarpic':'/spic/w8u01134100.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8t91120340.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8t91120340.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400CCY','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3950,3900,3750,3700,3550,3500,3350,3300','edzzl':'32500,32800,33180','ckbj':'','tarid':'ODU2NTI2',                'tarid_nobase':'856526','invalid':'true','tarpic':'/spic/w8t91120340.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u11146510.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u11146510.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9402TJZE','clmc':'集装箱运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,7160+1310+1310,7480+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'12450x2480,2500,2550x1460,1480,1550,1580,1600','edzzl':'34200,34000,33650','ckbj':'','tarid':'ODU2NjI3',                'tarid_nobase':'856627','invalid':'true','tarpic':'/spic/w8u11146510.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u01138790.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u01138790.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400CCYQX','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3950,3900,3750,3700,3550,3500,3350,3300','edzzl':'33410,33700,34000','ckbj':'','tarid':'ODU2Nzg3',                'tarid_nobase':'856787','invalid':'true','tarpic':'/spic/w8u01138790.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u21171410.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u21171410.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401TDP','clmc':'低平板半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'8600+1310+1310,8230+1310+1310,7830+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13750,13000,12500x2800,3000x3850,3650,3450,3300,3150,1700,1650,1600,1550,1500','edzzl':'31500,31000,30700','ckbj':'','tarid':'ODU2ODEz',                'tarid_nobase':'856813','invalid':'true','tarpic':'/spic/w8u21171410.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8v01189720.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8v01189720.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401E','clmc':'栏板半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2550,2500x3500,3300,3100,3000,2900,2800,2700','edzzl':'32000,32500,32700','ckbj':'','tarid':'ODU3NTI1',                'tarid_nobase':'857525','invalid':'true','tarpic':'/spic/w8v01189720.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8u81166570.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8u81166570.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401CCY','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'5680+1310+1310,5580+1310+1310,5480+1310+1310,5380+1310+1310,5280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'11500,11000,10500x2550,2500x3950,3900,3750,3700,3550,3500,3350,3300','edzzl':'33800,34000,34200','ckbj':'','tarid':'ODU4MDM3',                'tarid_nobase':'858037','invalid':'true','tarpic':'/spic/w8u81166570.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8v01206680.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8v01206680.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9402CCY','clmc':'仓栅式运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'5200+1310+1310,5000+1310+1310,4900+1310+1310,4800+1310+1310,4730+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'11000,10500,10000x2550,2500x3950,3900,3750,3700,3550,3500,3350,3300','edzzl':'32000,32500,32700','ckbj':'','tarid':'ODU4Njcw',                'tarid_nobase':'858670','invalid':'true','tarpic':'/spic/w8v01206680.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8v01192620.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8v01192620.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401L','clmc':'栏板半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2550,2500x3500,3300,3100,2900,2700','edzzl':'32000,32500,32700','ckbj':'','tarid':'ODU4Njg3',                'tarid_nobase':'858687','invalid':'true','tarpic':'/spic/w8v01192620.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w8w21477000.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w8w21477000.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400TWY','clmc':'危险品罐箱骨架运输半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'	        ',                'pc':'328','zs':'3','zj':'7480+1310+1310,7160+1310+1310,6880+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12450,12400x2480,2500,2550x1400,1450,1500,1550,1600,1650','edzzl':'34700,34500,34200','ckbj':'','tarid':'ODU5NjMz',                'tarid_nobase':'859633','invalid':'true','tarpic':'/spic/w8w21477000.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w6w61560890.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w6w61560890.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP5040XLJ','clmc':'旅居车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'NJ1045EFC',                'pc':'326','zs':'2','zj':'3300','fdjxh':'F1CE34818','fdjcs':'南京依维柯汽车有限公司',                'rlzl':'柴油','wxcc':'5995x2430,2370,2290x3050,3200,2950,2870,2760','edzzl':'','ckbj':'','tarid':'ODM2MTk0',                'tarid_nobase':'836194','invalid':'true','tarpic':'/spic/w6w61560890.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w1v21233000.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w1v21233000.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9402ZZXPC','clmc':'平板自卸半挂车',                'mz':'否','ry':'是','hb':'是','dpsb':'','dpxh':'',                'pc':'321','zs':'3','zj':'5380+1310+1310,5200+1310+1310,5080+1310+1310,5000+1310+1310,4900+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'11000,10500,10000x2550,2500x3900,3800,3700,3600,3500,3400,3300,3200,3100,3000,2900,2800,2700,2500,1800,1780,1750,1700,1680','edzzl':'33650,33800,34000,34200','ckbj':'','tarid':'NzkxNzMx',                'tarid_nobase':'791731','invalid':'true','tarpic':'/spic/w1v21233000.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/w0u71144450.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/w0u71144450.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400XXYE','clmc':'厢式运输半挂车',                'mz':'否','ry':'是','hb':'是','dpsb':'','dpxh':'',                'pc':'320','zs':'3','zj':'7400+1310+1310,7280+1310+1310,6980+1310+1310,6780+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13750,13590,13000x2550x4000,3800,3600,3400,3200','edzzl':'31500,32000,32200','ckbj':'','tarid':'Nzg0Mjgy',                'tarid_nobase':'784282','invalid':'true','tarpic':'/spic/w0u71144450.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v6u71144210.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v6u71144210.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401ZZXPC','clmc':'平板自卸半挂车',                'mz':'否','ry':'是','hb':'否','dpsb':'','dpxh':'',                'pc':'316','zs':'3','zj':'4630+1310+1310,4380+1310+1310,4230+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'10000,9500,9000x2550,2500x3500,3300,3100,3000,2900,2800,2700,1800,1750,1700,1600,1550,1500','edzzl':'32300,32500,32800','ckbj':'','tarid':'NzU3OTUz',                'tarid_nobase':'757953','invalid':'true','tarpic':'/spic/v6u71144210.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v5u51208910.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v5u51208910.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9350TDP','clmc':'低平板半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'315','zs':'2','zj':'8500+1310,8200+1310,7900+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'12000,11500,11000x3000x1500,1550,1600,1650,1750,3100,3300,3500,3700','edzzl':'26800,27200,27540','ckbj':'','tarid':'NzQ5ODIx',                'tarid_nobase':'749821','invalid':'true','tarpic':'/spic/v5u51208910.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v3u01124860.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v3u01124860.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400ZZXP','clmc':'平板自卸半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'313','zs':'3','zj':'6880+1310+1310,6780+1310+1310,6680+1310+1310,6480+1310+1310,6280+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2500,2550x3500,3300,3100,3000,2900,2800,2700,1800,1750,1700,1650,1600,1550,1500','edzzl':'32200,32500,32900','ckbj':'','tarid':'NzI5MzA1',                'tarid_nobase':'729305','invalid':'true','tarpic':'/spic/v3u01124860.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v3v31253420.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v3v31253420.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401XXY','clmc':'厢式运输半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'313','zs':'3','zj':'5450+1310+1310,5350+1310+1310,5250+1310+1310,5150+1310+1310,5000+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'11000,10500,10000x2550x4000,3800,3600,3400','edzzl':'31500,31800,32000,32200','ckbj':'','tarid':'NzI5ODQw',                'tarid_nobase':'729840','invalid':'true','tarpic':'/spic/v3v31253420.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v3u11159640.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v3u11159640.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401ZZXP','clmc':'平板自卸半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'313','zs':'3','zj':'5580+1310+1310,5400+1310+1310,5280+1310+1310,5100+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'11500,11000,10500x2500,2550x1550,1580,1600,1650,1680,1700,1750,1780,1800,2500,2700,2800,2900,3000,3100,3300,3500','edzzl':'33200,32800,32530','ckbj':'','tarid':'NzMwNTkx',                'tarid_nobase':'730591','invalid':'true','tarpic':'/spic/v3u11159640.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v3u71130320.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v3u71130320.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9380XXY','clmc':'厢式运输半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'313','zs':'3','zj':'7400+1310+1310,7280+1310+1310,6980+1310+1310,6780+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13750,13590,13000x2550,2500x4000,3800,3600,3400','edzzl':'29500,30000,30200','ckbj':'','tarid':'NzMxMTA3',                'tarid_nobase':'731107','invalid':'true','tarpic':'/spic/v3u71130320.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v0u11157030.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v0u11157030.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9402ZZXPHX','clmc':'平板自卸半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'310','zs':'3','zj':'5650+1310+1310,5770+1310+1310,6170+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'10500,11000,11500x2500,2550x3100,3300,3400,3500,3600,3700,3800,3900','edzzl':'32200,31900,31500','ckbj':'','tarid':'NzA1NjQw',                'tarid_nobase':'705640','invalid':'true','tarpic':'/spic/v0u11157030.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/v0u21168530.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/v0u21168530.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9400ZZXPHX','clmc':'平板自卸半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'310','zs':'3','zj':'4100+1310+1310,4300+1310+1310,4500+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'9000,9500,10000x2500,2550x3900,3700,3500,3300,3100','edzzl':'32500,32100,31760','ckbj':'','tarid':'NzA2MjI3',                'tarid_nobase':'706227','invalid':'true','tarpic':'/spic/v0u21168530.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/u9u21180430.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/u9u21180430.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'LXP9401ZZXPHX','clmc':'平板自卸半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'309','zs':'3','zj':'3480+1310+1310,3620+1310+1310,3820+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'7500,8000,8500x2500,2550x3100,3200,3300,3400,3500,3600,3700,3800,3900','edzzl':'33200,32900,32530','ckbj':'','tarid':'Njk4ODY4',                'tarid_nobase':'698868','invalid':'true','tarpic':'/spic/u9u21180430.jpg'},{'pic':'<img src="http://img.chinacar.com.cn/spic/t0t01300600.jpg" width="82" height="62" onMouseOver=toolTip("http://img.chinacar.com.cn/clcppic/t0t01300600.jpg"); onMouseOut="toolTip();"; />','zwpp':'鲁玺牌','clxh':'DHH9400XXY','clmc':'厢式运输半挂车',                'mz':'否','ry':'否','hb':'否','dpsb':'','dpxh':'',                'pc':'290','zs':'3','zj':'6750+1310+1310,6650+1310+1310,6450+1310+1310,6150+1310+1310','fdjxh':'','fdjcs':'',                'rlzl':'','wxcc':'13000,12500,12000x2550x3400,3600,3800,4000','edzzl':'31500,32000','ckbj':'','tarid':'NTY2MDk5',                'tarid_nobase':'566099','invalid':'true','tarpic':'/spic/t0t01300600.jpg'}]}
    print(json.dumps(str1, sort_keys=True, indent=2))
    # WindyKey().mouseAndKeyboard()
    # url = 'http://chinacar.com.cn/Home/GonggaoSearch/GonggaoSearch/search_json?_dc=1607662628578'
    #
    # requests.get(url)
    # print(url)
# driver = webdriver.Chrome()
    # driver.get("https://www.windy.com/zh/-%E5%8D%AB%E6%98%9F%E4%BA%91%E5%9B%BE-satellite?satellite,13.561,114.697,5")
    # try:
    #     time.sleep(20)
    #     pageSource = driver.page_source
    #     # 打印页面源码 html5lib解决获取不全html页面
    #     soup = BeautifulSoup(pageSource.encode("UTF-8", "ignore"), features="html5lib")
    #     print(soup.prettify())
    #
    # except TimeoutException as e:
    #     print('超时！')
    # finally:
    #     driver.quit()