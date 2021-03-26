# encoding: utf-8
"""
@file: csdn.py
@time: 2021/3/11 14:55
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import random
import time

import requests
from bs4 import SoupStrainer, BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

city = {"name": "阿拉善盟", "url": "http://poi.mapbar.com/alashanmeng/", "remaker": "alashanmeng"}, {"name": "安阳市",
                                                                                                 "url": "http://poi.mapbar.com/anyang/",
                                                                                                 "remaker": "anyang"}, {
           "name": "鞍山市", "url": "http://poi.mapbar.com/anshan/", "remaker": "anshan"}, {"name": "阿坝藏族羌族自治州",
                                                                                         "url": "http://poi.mapbar.com/aba/",
                                                                                         "remaker": "aba"}, {
           "name": "安顺市", "url": "http://poi.mapbar.com/anshun/", "remaker": "anshun"}, {"name": "阿里地区",
                                                                                         "url": "http://poi.mapbar.com/ali/",
                                                                                         "remaker": "ali"}, {
           "name": "阿勒泰地区", "url": "http://poi.mapbar.com/aletai/", "remaker": "aletai"}, {"name": "阿克苏地区",
                                                                                           "url": "http://poi.mapbar.com/akesu/",
                                                                                           "remaker": "akesu"}, {
           "name": "阿拉尔市", "url": "http://poi.mapbar.com/alaer/", "remaker": "alaer"}, {"name": "安康市",
                                                                                        "url": "http://poi.mapbar.com/ankang/",
                                                                                        "remaker": "ankang"}, {
           "name": "安庆市", "url": "http://poi.mapbar.com/anqing/", "remaker": "anqing"}, {"name": "北京市",
                                                                                         "url": "http://poi.mapbar.com/beijing/",
                                                                                         "remaker": "beijing"}, {
           "name": "保定市", "url": "http://poi.mapbar.com/baoding/", "remaker": "baoding"}, {"name": "包头市",
                                                                                           "url": "http://poi.mapbar.com/baotou/",
                                                                                           "remaker": "baotou"}, {
           "name": "巴彦淖尔市", "url": "http://poi.mapbar.com/bayannaoer/", "remaker": "bayannaoer"}, {"name": "白城市",
                                                                                                   "url": "http://poi.mapbar.com/baicheng/",
                                                                                                   "remaker": "baicheng"}, {
           "name": "白山市", "url": "http://poi.mapbar.com/baishan/", "remaker": "baishan"}, {"name": "本溪市",
                                                                                           "url": "http://poi.mapbar.com/benxi/",
                                                                                           "remaker": "benxi"}, {
           "name": "巴中市", "url": "http://poi.mapbar.com/bazhong/", "remaker": "bazhong"}, {"name": "保山市",
                                                                                           "url": "http://poi.mapbar.com/baoshan/",
                                                                                           "remaker": "baoshan"}, {
           "name": "毕节市", "url": "http://poi.mapbar.com/bijie/", "remaker": "bijie"}, {"name": "巴音郭楞蒙古自治州",
                                                                                       "url": "http://poi.mapbar.com/bayinguole/",
                                                                                       "remaker": "bayinguole"}, {
           "name": "博尔塔拉蒙古自治州", "url": "http://poi.mapbar.com/boertala/", "remaker": "boertala"}, {"name": "北屯市",
                                                                                                   "url": "http://poi.mapbar.com/beitun/",
                                                                                                   "remaker": "beitun"}, {
           "name": "宝鸡市", "url": "http://poi.mapbar.com/baoji/", "remaker": "baoji"}, {"name": "白银市",
                                                                                       "url": "http://poi.mapbar.com/baiyin/",
                                                                                       "remaker": "baiyin"}, {
           "name": "百色市", "url": "http://poi.mapbar.com/baise/", "remaker": "baise"}, {"name": "北海市",
                                                                                       "url": "http://poi.mapbar.com/beihai/",
                                                                                       "remaker": "beihai"}, {
           "name": "白沙黎族自治县", "url": "http://poi.mapbar.com/baisha/", "remaker": "baisha"}, {"name": "保亭黎族苗族自治县",
                                                                                             "url": "http://poi.mapbar.com/baoting/",
                                                                                             "remaker": "baoting"}, {
           "name": "滨州市", "url": "http://poi.mapbar.com/binzhou/", "remaker": "binzhou"}, {"name": "蚌埠市",
                                                                                           "url": "http://poi.mapbar.com/bengbu/",
                                                                                           "remaker": "bengbu"}, {
           "name": "亳州市", "url": "http://poi.mapbar.com/bozhou/", "remaker": "bozhou"}, {"name": "承德市",
                                                                                         "url": "http://poi.mapbar.com/chengde/",
                                                                                         "remaker": "chengde"}, {
           "name": "沧州市", "url": "http://poi.mapbar.com/cangzhou/", "remaker": "cangzhou"}, {"name": "长治市",
                                                                                             "url": "http://poi.mapbar.com/changzhi/",
                                                                                             "remaker": "changzhi"}, {
           "name": "赤峰市", "url": "http://poi.mapbar.com/chifeng/", "remaker": "chifeng"}, {"name": "长沙市",
                                                                                           "url": "http://poi.mapbar.com/changsha/",
                                                                                           "remaker": "changsha"}, {
           "name": "常德市", "url": "http://poi.mapbar.com/changde/", "remaker": "changde"}, {"name": "郴州市",
                                                                                           "url": "http://poi.mapbar.com/chenzhou/",
                                                                                           "remaker": "chenzhou"}, {
           "name": "长春市", "url": "http://poi.mapbar.com/changchun/", "remaker": "changchun"}, {"name": "朝阳市",
                                                                                               "url": "http://poi.mapbar.com/chaoyang/",
                                                                                               "remaker": "chaoyang"}, {
           "name": "成都市", "url": "http://poi.mapbar.com/chengdu/", "remaker": "chengdu"}, {"name": "楚雄彝族自治州",
                                                                                           "url": "http://poi.mapbar.com/chuxiong/",
                                                                                           "remaker": "chuxiong"}, {
           "name": "重庆市", "url": "http://poi.mapbar.com/chongqing/", "remaker": "chongqing"}, {"name": "昌都市",
                                                                                               "url": "http://poi.mapbar.com/changdu/",
                                                                                               "remaker": "changdu"}, {
           "name": "昌吉回族自治州", "url": "http://poi.mapbar.com/changji/", "remaker": "changji"}, {"name": "潮州市",
                                                                                               "url": "http://poi.mapbar.com/chaozhou/",
                                                                                               "remaker": "chaozhou"}, {
           "name": "崇左市", "url": "http://poi.mapbar.com/chongzuo/", "remaker": "chongzuo"}, {"name": "昌江黎族自治县",
                                                                                             "url": "http://poi.mapbar.com/changjiang/",
                                                                                             "remaker": "changjiang"}, {
           "name": "澄迈县", "url": "http://poi.mapbar.com/chengmai/", "remaker": "chengmai"}, {"name": "常州市",
                                                                                             "url": "http://poi.mapbar.com/changzhou/",
                                                                                             "remaker": "changzhou"}, {
           "name": "池州市", "url": "http://poi.mapbar.com/chizhou/", "remaker": "chizhou"}, {"name": "滁州市",
                                                                                           "url": "http://poi.mapbar.com/chuzhou/",
                                                                                           "remaker": "chuzhou"}, {
           "name": "大同市", "url": "http://poi.mapbar.com/datong/", "remaker": "datong"}, {"name": "大庆市",
                                                                                         "url": "http://poi.mapbar.com/daqing/",
                                                                                         "remaker": "daqing"}, {
           "name": "大兴安岭地区", "url": "http://poi.mapbar.com/daxinganling/", "remaker": "daxinganling"}, {"name": "丹东市",
                                                                                                        "url": "http://poi.mapbar.com/dandong/",
                                                                                                        "remaker": "dandong"}, {
           "name": "大连市", "url": "http://poi.mapbar.com/dalian/", "remaker": "dalian"}, {"name": "德阳市",
                                                                                         "url": "http://poi.mapbar.com/deyang/",
                                                                                         "remaker": "deyang"}, {
           "name": "达州市", "url": "http://poi.mapbar.com/dazhou/", "remaker": "dazhou"}, {"name": "德宏傣族景颇族自治州",
                                                                                         "url": "http://poi.mapbar.com/dehong/",
                                                                                         "remaker": "dehong"}, {
           "name": "迪庆藏族自治州", "url": "http://poi.mapbar.com/diqing/", "remaker": "diqing"}, {"name": "大理白族自治州",
                                                                                             "url": "http://poi.mapbar.com/dali/",
                                                                                             "remaker": "dali"}, {
           "name": "定西市", "url": "http://poi.mapbar.com/dingxi/", "remaker": "dingxi"}, {"name": "东莞市",
                                                                                         "url": "http://poi.mapbar.com/dongguan/",
                                                                                         "remaker": "dongguan"}, {
           "name": "儋州市", "url": "http://poi.mapbar.com/danzhou/", "remaker": "danzhou"}, {"name": "东方市",
                                                                                           "url": "http://poi.mapbar.com/dongfang/",
                                                                                           "remaker": "dongfang"}, {
           "name": "定安县", "url": "http://poi.mapbar.com/dingan/", "remaker": "dingan"}, {"name": "德州市",
                                                                                         "url": "http://poi.mapbar.com/dezhou/",
                                                                                         "remaker": "dezhou"}, {
           "name": "东营市", "url": "http://poi.mapbar.com/dongying/", "remaker": "dongying"}, {"name": "鄂尔多斯市",
                                                                                             "url": "http://poi.mapbar.com/eerduosi/",
                                                                                             "remaker": "eerduosi"}, {
           "name": "鄂州市", "url": "http://poi.mapbar.com/ezhou/", "remaker": "ezhou"}, {"name": "恩施土家族苗族自治州",
                                                                                       "url": "http://poi.mapbar.com/enshi/",
                                                                                       "remaker": "enshi"}, {
           "name": "阜新市", "url": "http://poi.mapbar.com/fuxin/", "remaker": "fuxin"}, {"name": "抚顺市",
                                                                                       "url": "http://poi.mapbar.com/fushun/",
                                                                                       "remaker": "fushun"}, {
           "name": "佛山市", "url": "http://poi.mapbar.com/foshan/", "remaker": "foshan"}, {"name": "防城港市",
                                                                                         "url": "http://poi.mapbar.com/fangchenggang/",
                                                                                         "remaker": "fangchenggang"}, {
           "name": "福州市", "url": "http://poi.mapbar.com/fuzhou1/", "remaker": "fuzhou1"}, {"name": "抚州市",
                                                                                           "url": "http://poi.mapbar.com/fuzhou2/",
                                                                                           "remaker": "fuzhou2"}, {
           "name": "阜阳市", "url": "http://poi.mapbar.com/fuyang/", "remaker": "fuyang"}, {"name": "广元市",
                                                                                         "url": "http://poi.mapbar.com/guangyuan/",
                                                                                         "remaker": "guangyuan"}, {
           "name": "广安市", "url": "http://poi.mapbar.com/guangan/", "remaker": "guangan"}, {"name": "甘孜藏族自治州",
                                                                                           "url": "http://poi.mapbar.com/ganzi/",
                                                                                           "remaker": "ganzi"}, {
           "name": "贵阳市", "url": "http://poi.mapbar.com/guiyang/", "remaker": "guiyang"}, {"name": "甘南藏族自治州",
                                                                                           "url": "http://poi.mapbar.com/gannan/",
                                                                                           "remaker": "gannan"}, {
           "name": "固原市", "url": "http://poi.mapbar.com/guyuan/", "remaker": "guyuan"}, {"name": "果洛藏族自治州",
                                                                                         "url": "http://poi.mapbar.com/guoluo/",
                                                                                         "remaker": "guoluo"}, {
           "name": "广州市", "url": "http://poi.mapbar.com/guangzhou/", "remaker": "guangzhou"}, {"name": "桂林市",
                                                                                               "url": "http://poi.mapbar.com/guilin/",
                                                                                               "remaker": "guilin"}, {
           "name": "贵港市", "url": "http://poi.mapbar.com/guigang/", "remaker": "guigang"}, {"name": "赣州市",
                                                                                           "url": "http://poi.mapbar.com/ganzhou/",
                                                                                           "remaker": "ganzhou"}, {
           "name": "衡水市", "url": "http://poi.mapbar.com/hengshui/", "remaker": "hengshui"}, {"name": "邯郸市",
                                                                                             "url": "http://poi.mapbar.com/handan/",
                                                                                             "remaker": "handan"}, {
           "name": "呼和浩特市", "url": "http://poi.mapbar.com/huhehaote/", "remaker": "huhehaote"}, {"name": "呼伦贝尔市",
                                                                                                 "url": "http://poi.mapbar.com/hulunbeier/",
                                                                                                 "remaker": "hulunbeier"}, {
           "name": "鹤壁市", "url": "http://poi.mapbar.com/hebi/", "remaker": "hebi"}, {"name": "衡阳市",
                                                                                     "url": "http://poi.mapbar.com/hengyang/",
                                                                                     "remaker": "hengyang"}, {
           "name": "怀化市", "url": "http://poi.mapbar.com/huaihua/", "remaker": "huaihua"}, {"name": "黄石市",
                                                                                           "url": "http://poi.mapbar.com/huangshi/",
                                                                                           "remaker": "huangshi"}, {
           "name": "黄冈市", "url": "http://poi.mapbar.com/huanggang/", "remaker": "huanggang"}, {"name": "哈尔滨市",
                                                                                               "url": "http://poi.mapbar.com/haerbin/",
                                                                                               "remaker": "haerbin"}, {
           "name": "黑河市", "url": "http://poi.mapbar.com/heihe/", "remaker": "heihe"}, {"name": "鹤岗市",
                                                                                       "url": "http://poi.mapbar.com/hegang/",
                                                                                       "remaker": "hegang"}, {
           "name": "葫芦岛市", "url": "http://poi.mapbar.com/huludao/", "remaker": "huludao"}, {"name": "红河哈尼族彝族自治州",
                                                                                            "url": "http://poi.mapbar.com/honghe/",
                                                                                            "remaker": "honghe"}, {
           "name": "哈密市", "url": "http://poi.mapbar.com/hami/", "remaker": "hami"}, {"name": "和田地区",
                                                                                     "url": "http://poi.mapbar.com/hetian/",
                                                                                     "remaker": "hetian"}, {
           "name": "胡杨河市", "url": "http://poi.mapbar.com/huyanghe/", "remaker": "huyanghe"}, {"name": "汉中市",
                                                                                              "url": "http://poi.mapbar.com/hanzhong/",
                                                                                              "remaker": "hanzhong"}, {
           "name": "海北藏族自治州", "url": "http://poi.mapbar.com/haibei/", "remaker": "haibei"}, {"name": "海东市",
                                                                                             "url": "http://poi.mapbar.com/haidong/",
                                                                                             "remaker": "haidong"}, {
           "name": "海南藏族自治州", "url": "http://poi.mapbar.com/hainan/", "remaker": "hainan"}, {"name": "海西蒙古族藏族自治州",
                                                                                             "url": "http://poi.mapbar.com/haixi/",
                                                                                             "remaker": "haixi"}, {
           "name": "黄南藏族自治州", "url": "http://poi.mapbar.com/huangnan/", "remaker": "huangnan"}, {"name": "香港特别行政区",
                                                                                                 "url": "http://poi.mapbar.com/hongkong/",
                                                                                                 "remaker": "hongkong"}, {
           "name": "河源市", "url": "http://poi.mapbar.com/heyuan/", "remaker": "heyuan"}, {"name": "惠州市",
                                                                                         "url": "http://poi.mapbar.com/huizhou/",
                                                                                         "remaker": "huizhou"}, {
           "name": "河池市", "url": "http://poi.mapbar.com/hechi/", "remaker": "hechi"}, {"name": "贺州市",
                                                                                       "url": "http://poi.mapbar.com/hezhou/",
                                                                                       "remaker": "hezhou"}, {
           "name": "海口市", "url": "http://poi.mapbar.com/haikou/", "remaker": "haikou"}, {"name": "淮安市",
                                                                                         "url": "http://poi.mapbar.com/huaian/",
                                                                                         "remaker": "huaian"}, {
           "name": "杭州市", "url": "http://poi.mapbar.com/hangzhou/", "remaker": "hangzhou"}, {"name": "湖州市",
                                                                                             "url": "http://poi.mapbar.com/huzhou/",
                                                                                             "remaker": "huzhou"}, {
           "name": "菏泽市", "url": "http://poi.mapbar.com/heze/", "remaker": "heze"}, {"name": "合肥市",
                                                                                     "url": "http://poi.mapbar.com/hefei/",
                                                                                     "remaker": "hefei"}, {
           "name": "黄山市", "url": "http://poi.mapbar.com/huangshan/", "remaker": "huangshan"}, {"name": "淮北市",
                                                                                               "url": "http://poi.mapbar.com/huaibei/",
                                                                                               "remaker": "huaibei"}, {
           "name": "淮南市", "url": "http://poi.mapbar.com/huainan/", "remaker": "huainan"}, {"name": "晋城市",
                                                                                           "url": "http://poi.mapbar.com/jincheng/",
                                                                                           "remaker": "jincheng"}, {
           "name": "晋中市", "url": "http://poi.mapbar.com/jinzhong/", "remaker": "jinzhong"}, {"name": "焦作市",
                                                                                             "url": "http://poi.mapbar.com/jiaozuo/",
                                                                                             "remaker": "jiaozuo"}, {
           "name": "济源市", "url": "http://poi.mapbar.com/jiyuan/", "remaker": "jiyuan"}, {"name": "荆门市",
                                                                                         "url": "http://poi.mapbar.com/jingmen/",
                                                                                         "remaker": "jingmen"}, {
           "name": "荆州市", "url": "http://poi.mapbar.com/jingzhou/", "remaker": "jingzhou"}, {"name": "佳木斯市",
                                                                                             "url": "http://poi.mapbar.com/jiamusi/",
                                                                                             "remaker": "jiamusi"}, {
           "name": "鸡西市", "url": "http://poi.mapbar.com/jixi/", "remaker": "jixi"}, {"name": "吉林市",
                                                                                     "url": "http://poi.mapbar.com/jilin/",
                                                                                     "remaker": "jilin"}, {
           "name": "锦州市", "url": "http://poi.mapbar.com/jinzhou/", "remaker": "jinzhou"}, {"name": "酒泉市",
                                                                                           "url": "http://poi.mapbar.com/jiuquan/",
                                                                                           "remaker": "jiuquan"}, {
           "name": "嘉峪关市", "url": "http://poi.mapbar.com/jiayuguan/", "remaker": "jiayuguan"}, {"name": "金昌市",
                                                                                                "url": "http://poi.mapbar.com/jinchang/",
                                                                                                "remaker": "jinchang"}, {
           "name": "揭阳市", "url": "http://poi.mapbar.com/jieyang/", "remaker": "jieyang"}, {"name": "江门市",
                                                                                           "url": "http://poi.mapbar.com/jiangmen/",
                                                                                           "remaker": "jiangmen"}, {
           "name": "嘉兴市", "url": "http://poi.mapbar.com/jiaxing/", "remaker": "jiaxing"}, {"name": "金华市",
                                                                                           "url": "http://poi.mapbar.com/jinhua/",
                                                                                           "remaker": "jinhua"}, {
           "name": "济南市", "url": "http://poi.mapbar.com/jinan/", "remaker": "jinan"}, {"name": "济宁市",
                                                                                       "url": "http://poi.mapbar.com/jining/",
                                                                                       "remaker": "jining"}, {
           "name": "九江市", "url": "http://poi.mapbar.com/jiujiang/", "remaker": "jiujiang"}, {"name": "景德镇市",
                                                                                             "url": "http://poi.mapbar.com/jingdezhen/",
                                                                                             "remaker": "jingdezhen"}, {
           "name": "吉安市", "url": "http://poi.mapbar.com/jian/", "remaker": "jian"}, {"name": "开封市",
                                                                                     "url": "http://poi.mapbar.com/kaifeng/",
                                                                                     "remaker": "kaifeng"}, {
           "name": "昆明市", "url": "http://poi.mapbar.com/kunming/", "remaker": "kunming"}, {"name": "克拉玛依市",
                                                                                           "url": "http://poi.mapbar.com/kelamayi/",
                                                                                           "remaker": "kelamayi"}, {
           "name": "克孜勒苏柯尔克孜自治州", "url": "http://poi.mapbar.com/kezilesu/", "remaker": "kezilesu"}, {"name": "喀什地区",
                                                                                                     "url": "http://poi.mapbar.com/kashen/",
                                                                                                     "remaker": "kashen"}, {
           "name": "可克达拉市", "url": "http://poi.mapbar.com/kekedala/", "remaker": "kekedala"}, {"name": "昆玉市",
                                                                                               "url": "http://poi.mapbar.com/kunyu/",
                                                                                               "remaker": "kunyu"}, {
           "name": "廊坊市", "url": "http://poi.mapbar.com/langfang/", "remaker": "langfang"}, {"name": "临汾市",
                                                                                             "url": "http://poi.mapbar.com/linfen/",
                                                                                             "remaker": "linfen"}, {
           "name": "吕梁市", "url": "http://poi.mapbar.com/lvliang/", "remaker": "lvliang"}, {"name": "洛阳市",
                                                                                           "url": "http://poi.mapbar.com/luoyang/",
                                                                                           "remaker": "luoyang"}, {
           "name": "漯河市", "url": "http://poi.mapbar.com/luohe/", "remaker": "luohe"}, {"name": "娄底市",
                                                                                       "url": "http://poi.mapbar.com/loudi/",
                                                                                       "remaker": "loudi"}, {
           "name": "辽源市", "url": "http://poi.mapbar.com/liaoyuan/", "remaker": "liaoyuan"}, {"name": "辽阳市",
                                                                                             "url": "http://poi.mapbar.com/liaoyang/",
                                                                                             "remaker": "liaoyang"}, {
           "name": "乐山市", "url": "http://poi.mapbar.com/leshan/", "remaker": "leshan"}, {"name": "泸州市",
                                                                                         "url": "http://poi.mapbar.com/luzhou/",
                                                                                         "remaker": "luzhou"}, {
           "name": "凉山彝族自治州", "url": "http://poi.mapbar.com/liangshan/", "remaker": "liangshan"}, {"name": "丽江市",
                                                                                                   "url": "http://poi.mapbar.com/lijiang/",
                                                                                                   "remaker": "lijiang"}, {
           "name": "临沧市", "url": "http://poi.mapbar.com/lincang/", "remaker": "lincang"}, {"name": "六盘水市",
                                                                                           "url": "http://poi.mapbar.com/liupanshui/",
                                                                                           "remaker": "liupanshui"}, {
           "name": "拉萨市", "url": "http://poi.mapbar.com/lasa/", "remaker": "lasa"}, {"name": "林芝市",
                                                                                     "url": "http://poi.mapbar.com/linzhi/",
                                                                                     "remaker": "linzhi"}, {
           "name": "兰州市", "url": "http://poi.mapbar.com/lanzhou/", "remaker": "lanzhou"}, {"name": "临夏回族自治州",
                                                                                           "url": "http://poi.mapbar.com/linxia/",
                                                                                           "remaker": "linxia"}, {
           "name": "陇南市", "url": "http://poi.mapbar.com/longnan/", "remaker": "longnan"}, {"name": "柳州市",
                                                                                           "url": "http://poi.mapbar.com/liuzhou/",
                                                                                           "remaker": "liuzhou"}, {
           "name": "来宾市", "url": "http://poi.mapbar.com/laibin/", "remaker": "laibin"}, {"name": "乐东黎族自治县",
                                                                                         "url": "http://poi.mapbar.com/ledong/",
                                                                                         "remaker": "ledong"}, {
           "name": "临高县", "url": "http://poi.mapbar.com/lingao/", "remaker": "lingao"}, {"name": "陵水黎族自治县",
                                                                                         "url": "http://poi.mapbar.com/lingshui/",
                                                                                         "remaker": "lingshui"}, {
           "name": "连云港市", "url": "http://poi.mapbar.com/lianyungang/", "remaker": "lianyungang"}, {"name": "丽水市",
                                                                                                    "url": "http://poi.mapbar.com/lishui/",
                                                                                                    "remaker": "lishui"}, {
           "name": "龙岩市", "url": "http://poi.mapbar.com/longyan/", "remaker": "longyan"}, {"name": "聊城市",
                                                                                           "url": "http://poi.mapbar.com/liaocheng/",
                                                                                           "remaker": "liaocheng"}, {
           "name": "临沂市", "url": "http://poi.mapbar.com/linyi/", "remaker": "linyi"}, {"name": "六安市",
                                                                                       "url": "http://poi.mapbar.com/liuan/",
                                                                                       "remaker": "liuan"}, {
           "name": "牡丹江市", "url": "http://poi.mapbar.com/mudanjiang/", "remaker": "mudanjiang"}, {"name": "绵阳市",
                                                                                                  "url": "http://poi.mapbar.com/mianyang/",
                                                                                                  "remaker": "mianyang"}, {
           "name": "眉山市", "url": "http://poi.mapbar.com/meishan/", "remaker": "meishan"}, {"name": "澳门特别行政区",
                                                                                           "url": "http://poi.mapbar.com/macau/",
                                                                                           "remaker": "macau"}, {
           "name": "梅州市", "url": "http://poi.mapbar.com/meizhou/", "remaker": "meizhou"}, {"name": "茂名市",
                                                                                           "url": "http://poi.mapbar.com/maoming/",
                                                                                           "remaker": "maoming"}, {
           "name": "马鞍山市", "url": "http://poi.mapbar.com/maanshan/", "remaker": "maanshan"}, {"name": "南阳市",
                                                                                              "url": "http://poi.mapbar.com/nanyang/",
                                                                                              "remaker": "nanyang"}, {
           "name": "南充市", "url": "http://poi.mapbar.com/nanchong/", "remaker": "nanchong"}, {"name": "内江市",
                                                                                             "url": "http://poi.mapbar.com/neijiang/",
                                                                                             "remaker": "neijiang"}, {
           "name": "怒江傈僳族自治州", "url": "http://poi.mapbar.com/nujiang/", "remaker": "nujiang"}, {"name": "那曲市",
                                                                                                "url": "http://poi.mapbar.com/naqu/",
                                                                                                "remaker": "naqu"}, {
           "name": "南宁市", "url": "http://poi.mapbar.com/nanning/", "remaker": "nanning"}, {"name": "南京市",
                                                                                           "url": "http://poi.mapbar.com/nanjing/",
                                                                                           "remaker": "nanjing"}, {
           "name": "南通市", "url": "http://poi.mapbar.com/nantong/", "remaker": "nantong"}, {"name": "宁波市",
                                                                                           "url": "http://poi.mapbar.com/ningbo/",
                                                                                           "remaker": "ningbo"}, {
           "name": "南平市", "url": "http://poi.mapbar.com/nanping/", "remaker": "nanping"}, {"name": "宁德市",
                                                                                           "url": "http://poi.mapbar.com/ningde/",
                                                                                           "remaker": "ningde"}, {
           "name": "南昌市", "url": "http://poi.mapbar.com/nanchang/", "remaker": "nanchang"}, {"name": "濮阳市",
                                                                                             "url": "http://poi.mapbar.com/puyang/",
                                                                                             "remaker": "puyang"}, {
           "name": "平顶山市", "url": "http://poi.mapbar.com/pingdingshan/", "remaker": "pingdingshan"}, {"name": "盘锦市",
                                                                                                      "url": "http://poi.mapbar.com/panjin/",
                                                                                                      "remaker": "panjin"}, {
           "name": "攀枝花市", "url": "http://poi.mapbar.com/panzhihua/", "remaker": "panzhihua"}, {"name": "普洱市",
                                                                                                "url": "http://poi.mapbar.com/puer/",
                                                                                                "remaker": "puer"}, {
           "name": "平凉市", "url": "http://poi.mapbar.com/pingliang/", "remaker": "pingliang"}, {"name": "莆田市",
                                                                                               "url": "http://poi.mapbar.com/putian/",
                                                                                               "remaker": "putian"}, {
           "name": "萍乡市", "url": "http://poi.mapbar.com/pingxiang/", "remaker": "pingxiang"}, {"name": "秦皇岛市",
                                                                                               "url": "http://poi.mapbar.com/qinhuangdao/",
                                                                                               "remaker": "qinhuangdao"}, {
           "name": "潜江市", "url": "http://poi.mapbar.com/qianjiang/", "remaker": "qianjiang"}, {"name": "齐齐哈尔市",
                                                                                               "url": "http://poi.mapbar.com/qiqihaer/",
                                                                                               "remaker": "qiqihaer"}, {
           "name": "七台河市", "url": "http://poi.mapbar.com/qitaihe/", "remaker": "qitaihe"}, {"name": "曲靖市",
                                                                                            "url": "http://poi.mapbar.com/qujing/",
                                                                                            "remaker": "qujing"}, {
           "name": "黔东南苗族侗族自治州", "url": "http://poi.mapbar.com/qiandongnan/", "remaker": "qiandongnan"}, {
           "name": "黔南布依族苗族自治州", "url": "http://poi.mapbar.com/qiannan/", "remaker": "qiannan"}, {"name": "黔西南布依族苗族自治州",
                                                                                                  "url": "http://poi.mapbar.com/qianxinan/",
                                                                                                  "remaker": "qianxinan"}, {
           "name": "庆阳市", "url": "http://poi.mapbar.com/qingyang/", "remaker": "qingyang"}, {"name": "清远市",
                                                                                             "url": "http://poi.mapbar.com/qingyuan/",
                                                                                             "remaker": "qingyuan"}, {
           "name": "钦州市", "url": "http://poi.mapbar.com/qinzhou/", "remaker": "qinzhou"}, {"name": "琼海市",
                                                                                           "url": "http://poi.mapbar.com/qionghai/",
                                                                                           "remaker": "qionghai"}, {
           "name": "琼中黎族苗族自治县", "url": "http://poi.mapbar.com/qiongzhong/", "remaker": "qiongzhong"}, {"name": "衢州市",
                                                                                                       "url": "http://poi.mapbar.com/quzhou/",
                                                                                                       "remaker": "quzhou"}, {
           "name": "泉州市", "url": "http://poi.mapbar.com/quanzhou/", "remaker": "quanzhou"}, {"name": "青岛市",
                                                                                             "url": "http://poi.mapbar.com/qingdao/",
                                                                                             "remaker": "qingdao"}, {
           "name": "日喀则市", "url": "http://poi.mapbar.com/rikaze/", "remaker": "rikaze"}, {"name": "日照市",
                                                                                          "url": "http://poi.mapbar.com/rizhao/",
                                                                                          "remaker": "rizhao"}, {
           "name": "石家庄市", "url": "http://poi.mapbar.com/shijiazhuang/", "remaker": "shijiazhuang"}, {"name": "朔州市",
                                                                                                      "url": "http://poi.mapbar.com/shuozhou/",
                                                                                                      "remaker": "shuozhou"}, {
           "name": "三门峡市", "url": "http://poi.mapbar.com/sanmenxia/", "remaker": "sanmenxia"}, {"name": "商丘市",
                                                                                                "url": "http://poi.mapbar.com/shangqiu/",
                                                                                                "remaker": "shangqiu"}, {
           "name": "邵阳市", "url": "http://poi.mapbar.com/shaoyang/", "remaker": "shaoyang"}, {"name": "十堰市",
                                                                                             "url": "http://poi.mapbar.com/shiyan/",
                                                                                             "remaker": "shiyan"}, {
           "name": "随州市", "url": "http://poi.mapbar.com/suizhou/", "remaker": "suizhou"}, {"name": "神农架林区",
                                                                                           "url": "http://poi.mapbar.com/shennongjia/",
                                                                                           "remaker": "shennongjia"}, {
           "name": "双鸭山市", "url": "http://poi.mapbar.com/shuangyashan/", "remaker": "shuangyashan"}, {"name": "绥化市",
                                                                                                      "url": "http://poi.mapbar.com/suihua/",
                                                                                                      "remaker": "suihua"}, {
           "name": "松原市", "url": "http://poi.mapbar.com/songyuan/", "remaker": "songyuan"}, {"name": "四平市",
                                                                                             "url": "http://poi.mapbar.com/siping/",
                                                                                             "remaker": "siping"}, {
           "name": "沈阳市", "url": "http://poi.mapbar.com/shenyang/", "remaker": "shenyang"}, {"name": "遂宁市",
                                                                                             "url": "http://poi.mapbar.com/suining/",
                                                                                             "remaker": "suining"}, {
           "name": "山南市", "url": "http://poi.mapbar.com/shannan/", "remaker": "shannan"}, {"name": "石河子市",
                                                                                           "url": "http://poi.mapbar.com/shihezi/",
                                                                                           "remaker": "shihezi"}, {
           "name": "双河市", "url": "http://poi.mapbar.com/shuanghe/", "remaker": "shuanghe"}, {"name": "商洛市",
                                                                                             "url": "http://poi.mapbar.com/shangluo/",
                                                                                             "remaker": "shangluo"}, {
           "name": "石嘴山市", "url": "http://poi.mapbar.com/shizuishan/", "remaker": "shizuishan"}, {"name": "韶关市",
                                                                                                  "url": "http://poi.mapbar.com/shaoguan/",
                                                                                                  "remaker": "shaoguan"}, {
           "name": "汕头市", "url": "http://poi.mapbar.com/shantou/", "remaker": "shantou"}, {"name": "汕尾市",
                                                                                           "url": "http://poi.mapbar.com/shanwei/",
                                                                                           "remaker": "shanwei"}, {
           "name": "深圳市", "url": "http://poi.mapbar.com/shenzhen/", "remaker": "shenzhen"}, {"name": "三亚市",
                                                                                             "url": "http://poi.mapbar.com/sanya/",
                                                                                             "remaker": "sanya"}, {
           "name": "三沙市", "url": "http://poi.mapbar.com/sansha/", "remaker": "sansha"}, {"name": "上海市",
                                                                                         "url": "http://poi.mapbar.com/shanghai/",
                                                                                         "remaker": "shanghai"}, {
           "name": "苏州市", "url": "http://poi.mapbar.com/suzhou1/", "remaker": "suzhou1"}, {"name": "宿迁市",
                                                                                           "url": "http://poi.mapbar.com/suqian/",
                                                                                           "remaker": "suqian"}, {
           "name": "绍兴市", "url": "http://poi.mapbar.com/shaoxing/", "remaker": "shaoxing"}, {"name": "三明市",
                                                                                             "url": "http://poi.mapbar.com/sanming/",
                                                                                             "remaker": "sanming"}, {
           "name": "上饶市", "url": "http://poi.mapbar.com/shangrao/", "remaker": "shangrao"}, {"name": "宿州市",
                                                                                             "url": "http://poi.mapbar.com/suzhou2/",
                                                                                             "remaker": "suzhou2"}, {
           "name": "天津市", "url": "http://poi.mapbar.com/tianjin/", "remaker": "tianjin"}, {"name": "唐山市",
                                                                                           "url": "http://poi.mapbar.com/tangshan/",
                                                                                           "remaker": "tangshan"}, {
           "name": "太原市", "url": "http://poi.mapbar.com/taiyuan/", "remaker": "taiyuan"}, {"name": "通辽市",
                                                                                           "url": "http://poi.mapbar.com/tongliao/",
                                                                                           "remaker": "tongliao"}, {
           "name": "天门市", "url": "http://poi.mapbar.com/tianmen/", "remaker": "tianmen"}, {"name": "通化市",
                                                                                           "url": "http://poi.mapbar.com/tonghua/",
                                                                                           "remaker": "tonghua"}, {
           "name": "铁岭市", "url": "http://poi.mapbar.com/tieling/", "remaker": "tieling"}, {"name": "铜仁市",
                                                                                           "url": "http://poi.mapbar.com/tongren/",
                                                                                           "remaker": "tongren"}, {
           "name": "吐鲁番市", "url": "http://poi.mapbar.com/tulufan/", "remaker": "tulufan"}, {"name": "塔城地区",
                                                                                            "url": "http://poi.mapbar.com/tacheng/",
                                                                                            "remaker": "tacheng"}, {
           "name": "图木舒克市", "url": "http://poi.mapbar.com/tumushuke/", "remaker": "tumushuke"}, {"name": "铁门关市",
                                                                                                 "url": "http://poi.mapbar.com/tiemenguan/",
                                                                                                 "remaker": "tiemenguan"}, {
           "name": "铜川市", "url": "http://poi.mapbar.com/tongchuan/", "remaker": "tongchuan"}, {"name": "天水市",
                                                                                               "url": "http://poi.mapbar.com/tianshui/",
                                                                                               "remaker": "tianshui"}, {
           "name": "屯昌县", "url": "http://poi.mapbar.com/tunchang/", "remaker": "tunchang"}, {"name": "泰州市",
                                                                                             "url": "http://poi.mapbar.com/taizhou1/",
                                                                                             "remaker": "taizhou1"}, {
           "name": "台州市", "url": "http://poi.mapbar.com/taizhou2/", "remaker": "taizhou2"}, {"name": "泰安市",
                                                                                             "url": "http://poi.mapbar.com/taian/",
                                                                                             "remaker": "taian"}, {
           "name": "铜陵市", "url": "http://poi.mapbar.com/tongling/", "remaker": "tongling"}, {"name": "乌海市",
                                                                                             "url": "http://poi.mapbar.com/wuhai/",
                                                                                             "remaker": "wuhai"}, {
           "name": "乌兰察布市", "url": "http://poi.mapbar.com/wulanchabu/", "remaker": "wulanchabu"}, {"name": "武汉市",
                                                                                                   "url": "http://poi.mapbar.com/wuhan/",
                                                                                                   "remaker": "wuhan"}, {
           "name": "文山壮族苗族自治州", "url": "http://poi.mapbar.com/wenshan/", "remaker": "wenshan"}, {"name": "乌鲁木齐市",
                                                                                                 "url": "http://poi.mapbar.com/wulumuqi/",
                                                                                                 "remaker": "wulumuqi"}, {
           "name": "五家渠市", "url": "http://poi.mapbar.com/wujiaqu/", "remaker": "wujiaqu"}, {"name": "渭南市",
                                                                                            "url": "http://poi.mapbar.com/weinan/",
                                                                                            "remaker": "weinan"}, {
           "name": "武威市", "url": "http://poi.mapbar.com/wuwei/", "remaker": "wuwei"}, {"name": "吴忠市",
                                                                                       "url": "http://poi.mapbar.com/wuzhong/",
                                                                                       "remaker": "wuzhong"}, {
           "name": "梧州市", "url": "http://poi.mapbar.com/wuzhou/", "remaker": "wuzhou"}, {"name": "万宁市",
                                                                                         "url": "http://poi.mapbar.com/wanning/",
                                                                                         "remaker": "wanning"}, {
           "name": "文昌市", "url": "http://poi.mapbar.com/wenchang/", "remaker": "wenchang"}, {"name": "五指山市",
                                                                                             "url": "http://poi.mapbar.com/wuzhishan/",
                                                                                             "remaker": "wuzhishan"}, {
           "name": "无锡市", "url": "http://poi.mapbar.com/wuxi/", "remaker": "wuxi"}, {"name": "温州市",
                                                                                     "url": "http://poi.mapbar.com/wenzhou/",
                                                                                     "remaker": "wenzhou"}, {
           "name": "威海市", "url": "http://poi.mapbar.com/weihai/", "remaker": "weihai"}, {"name": "潍坊市",
                                                                                         "url": "http://poi.mapbar.com/weifang/",
                                                                                         "remaker": "weifang"}, {
           "name": "芜湖市", "url": "http://poi.mapbar.com/wuhu/", "remaker": "wuhu"}, {"name": "邢台市",
                                                                                     "url": "http://poi.mapbar.com/xingtai/",
                                                                                     "remaker": "xingtai"}, {
           "name": "忻州市", "url": "http://poi.mapbar.com/xinzhou/", "remaker": "xinzhou"}, {"name": "兴安盟",
                                                                                           "url": "http://poi.mapbar.com/xinganmeng/",
                                                                                           "remaker": "xinganmeng"}, {
           "name": "锡林郭勒盟", "url": "http://poi.mapbar.com/xilinguolemeng/", "remaker": "xilinguolemeng"}, {
           "name": "新乡市", "url": "http://poi.mapbar.com/xinxiang/", "remaker": "xinxiang"}, {"name": "许昌市",
                                                                                             "url": "http://poi.mapbar.com/xuchang/",
                                                                                             "remaker": "xuchang"}, {
           "name": "信阳市", "url": "http://poi.mapbar.com/xinyang/", "remaker": "xinyang"}, {"name": "湘潭市",
                                                                                           "url": "http://poi.mapbar.com/xiangtan/",
                                                                                           "remaker": "xiangtan"}, {
           "name": "湘西土家族苗族自治州", "url": "http://poi.mapbar.com/xiangxi/", "remaker": "xiangxi"}, {"name": "襄阳市",
                                                                                                  "url": "http://poi.mapbar.com/xiangyang/",
                                                                                                  "remaker": "xiangyang"}, {
           "name": "孝感市", "url": "http://poi.mapbar.com/xiaogan/", "remaker": "xiaogan"}, {"name": "咸宁市",
                                                                                           "url": "http://poi.mapbar.com/xianning/",
                                                                                           "remaker": "xianning"}, {
           "name": "仙桃市", "url": "http://poi.mapbar.com/xiantao/", "remaker": "xiantao"}, {"name": "西双版纳傣族自治州",
                                                                                           "url": "http://poi.mapbar.com/xishuangbanna/",
                                                                                           "remaker": "xishuangbanna"}, {
           "name": "西安市", "url": "http://poi.mapbar.com/xian/", "remaker": "xian"}, {"name": "咸阳市",
                                                                                     "url": "http://poi.mapbar.com/xianyang/",
                                                                                     "remaker": "xianyang"}, {
           "name": "西宁市", "url": "http://poi.mapbar.com/xining/", "remaker": "xining"}, {"name": "徐州市",
                                                                                         "url": "http://poi.mapbar.com/xuzhou/",
                                                                                         "remaker": "xuzhou"}, {
           "name": "厦门市", "url": "http://poi.mapbar.com/xiamen/", "remaker": "xiamen"}, {"name": "新余市",
                                                                                         "url": "http://poi.mapbar.com/xinyu/",
                                                                                         "remaker": "xinyu"}, {
           "name": "宣城市", "url": "http://poi.mapbar.com/xuancheng/", "remaker": "xuancheng"}, {"name": "阳泉市",
                                                                                               "url": "http://poi.mapbar.com/yangquan/",
                                                                                               "remaker": "yangquan"}, {
           "name": "运城市", "url": "http://poi.mapbar.com/yuncheng/", "remaker": "yuncheng"}, {"name": "益阳市",
                                                                                             "url": "http://poi.mapbar.com/yiyang/",
                                                                                             "remaker": "yiyang"}, {
           "name": "岳阳市", "url": "http://poi.mapbar.com/yueyang/", "remaker": "yueyang"}, {"name": "永州市",
                                                                                           "url": "http://poi.mapbar.com/yongzhou/",
                                                                                           "remaker": "yongzhou"}, {
           "name": "宜昌市", "url": "http://poi.mapbar.com/yichang/", "remaker": "yichang"}, {"name": "伊春市",
                                                                                           "url": "http://poi.mapbar.com/yichun1/",
                                                                                           "remaker": "yichun1"}, {
           "name": "延边朝鲜族自治州", "url": "http://poi.mapbar.com/yanbian/", "remaker": "yanbian"}, {"name": "营口市",
                                                                                                "url": "http://poi.mapbar.com/yingkou/",
                                                                                                "remaker": "yingkou"}, {
           "name": "宜宾市", "url": "http://poi.mapbar.com/yibin/", "remaker": "yibin"}, {"name": "雅安市",
                                                                                       "url": "http://poi.mapbar.com/yaan/",
                                                                                       "remaker": "yaan"}, {
           "name": "玉溪市", "url": "http://poi.mapbar.com/yuxi/", "remaker": "yuxi"}, {"name": "伊犁哈萨克自治州",
                                                                                     "url": "http://poi.mapbar.com/yili/",
                                                                                     "remaker": "yili"}, {"name": "延安市",
                                                                                                          "url": "http://poi.mapbar.com/yanan/",
                                                                                                          "remaker": "yanan"}, {
           "name": "榆林市", "url": "http://poi.mapbar.com/yulin1/", "remaker": "yulin1"}, {"name": "银川市",
                                                                                         "url": "http://poi.mapbar.com/yinchuan/",
                                                                                         "remaker": "yinchuan"}, {
           "name": "玉树藏族自治州", "url": "http://poi.mapbar.com/yushu/", "remaker": "yushu"}, {"name": "云浮市",
                                                                                           "url": "http://poi.mapbar.com/yunfu/",
                                                                                           "remaker": "yunfu"}, {
           "name": "阳江市", "url": "http://poi.mapbar.com/yangjiang/", "remaker": "yangjiang"}, {"name": "玉林市",
                                                                                               "url": "http://poi.mapbar.com/yulin2/",
                                                                                               "remaker": "yulin2"}, {
           "name": "盐城市", "url": "http://poi.mapbar.com/yancheng/", "remaker": "yancheng"}, {"name": "扬州市",
                                                                                             "url": "http://poi.mapbar.com/yangzhou/",
                                                                                             "remaker": "yangzhou"}, {
           "name": "烟台市", "url": "http://poi.mapbar.com/yantai/", "remaker": "yantai"}, {"name": "鹰潭市",
                                                                                         "url": "http://poi.mapbar.com/yingtan/",
                                                                                         "remaker": "yingtan"}, {
           "name": "宜春市", "url": "http://poi.mapbar.com/yichun2/", "remaker": "yichun2"}, {"name": "张家口市",
                                                                                           "url": "http://poi.mapbar.com/zhangjiakou/",
                                                                                           "remaker": "zhangjiakou"}, {
           "name": "郑州市", "url": "http://poi.mapbar.com/zhengzhou/", "remaker": "zhengzhou"}, {"name": "周口市",
                                                                                               "url": "http://poi.mapbar.com/zhoukou/",
                                                                                               "remaker": "zhoukou"}, {
           "name": "驻马店市", "url": "http://poi.mapbar.com/zhumadian/", "remaker": "zhumadian"}, {"name": "张家界市",
                                                                                                "url": "http://poi.mapbar.com/zhangjiajie/",
                                                                                                "remaker": "zhangjiajie"}, {
           "name": "株洲市", "url": "http://poi.mapbar.com/zhuzhou/", "remaker": "zhuzhou"}, {"name": "自贡市",
                                                                                           "url": "http://poi.mapbar.com/zigong/",
                                                                                           "remaker": "zigong"}, {
           "name": "资阳市", "url": "http://poi.mapbar.com/ziyang/", "remaker": "ziyang"}, {"name": "昭通市",
                                                                                         "url": "http://poi.mapbar.com/zhaotong/",
                                                                                         "remaker": "zhaotong"}, {
           "name": "遵义市", "url": "http://poi.mapbar.com/zunyi/", "remaker": "zunyi"}, {"name": "张掖市",
                                                                                       "url": "http://poi.mapbar.com/zhangye/",
                                                                                       "remaker": "zhangye"}, {
           "name": "中卫市", "url": "http://poi.mapbar.com/zhongwei/", "remaker": "zhongwei"}, {"name": "珠海市",
                                                                                             "url": "http://poi.mapbar.com/zhuhai/",
                                                                                             "remaker": "zhuhai"}, {
           "name": "中山市", "url": "http://poi.mapbar.com/zhongshan/", "remaker": "zhongshan"}, {"name": "肇庆市",
                                                                                               "url": "http://poi.mapbar.com/zhaoqing/",
                                                                                               "remaker": "zhaoqing"}, {
           "name": "湛江市", "url": "http://poi.mapbar.com/zhanjiang/", "remaker": "zhanjiang"}, {"name": "镇江市",
                                                                                               "url": "http://poi.mapbar.com/zhenjiang/",
                                                                                               "remaker": "zhenjiang"}, {
           "name": "舟山市", "url": "http://poi.mapbar.com/zhoushan/", "remaker": "zhoushan"}, {"name": "漳州市",
                                                                                             "url": "http://poi.mapbar.com/zhangzhou/",
                                                                                             "remaker": "zhangzhou"}, {
           "name": "淄博市", "url": "http://poi.mapbar.com/zibo/", "remaker": "zibo"}, {"name": "枣庄市",
                                                                                     "url": "http://poi.mapbar.com/zaozhuang/",
                                                                                     "remaker": "zaozhuang"}


def get_url_lis(name='六盘水市', url='https://poi.mapbar.com/liupanshui/GA0/'):
    global allroads
    # 61.135.185.152:80
    proxy_data = [
        '--proxy=%s' % '91.205.174.26:80',  # 设置的代理ip
        '--proxy-type=http',  # 代理类型
        '--ignore-ssl-errors=true',  # 忽略https错误
    ]
    capa = DesiredCapabilities.PHANTOMJS
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument(
        'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
    # options.add_argument('--headless')
    # 模拟浏览器发送HTTP请求
    browser = webdriver.Chrome(desired_capabilities=capa, service_args=proxy_data, chrome_options=options)
    browser.get('https://whatleaks.com/')
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located(
    #     (By.XPATH, '//*[@id="body_h"]/div[2]/div[3]/div[4]/div/div[3]/ul/li[1]/font[3]')))
    # only_a_tags = SoupStrainer('div', attrs={"class": "sortC"})
    # p_x_list = BeautifulSoup(reponse.text, 'html.parser', parse_only=only_a_tags)
    # return [{'city_name': name, 'type': 'address', 'address': a.text, 'hash': a['href']} for a in
    #         p_x_list.find_all('a')]


if __name__ == '__main__':
    get_url_lis(name='保定市', url='https://poi.mapbar.com/baoding/GA0/')
    # cityCrossing = []
    # cs = ["保定市", "北屯市", "长沙市", "长春市", "儋州市", "佛山市", "广州市", "哈尔滨市", "哈密市", "胡杨河市", "香港特别行政区", "惠州市", "淮安市", "杭州市", "合肥市",
    #       "金华市", "昆明市", "可克达拉市", "昆玉市", "林芝市", "那曲市", "南通市", "宁波市", "南昌市", "沈阳市", "山南市", "双河市", "上海市", "苏州市", "宿迁市",
    #       "绍兴市", "天津市", "太原市", "吐鲁番市", "铁门关市", "台州市", "乌鲁木齐市", "无锡市", "温州市", "潍坊市", "厦门市", "扬州市", "烟台市", "郑州市", "镇江市"]
    # for i in city:
    #     ename = i['remaker']
    #     name = i['name']
    #     if name in cs:
    #         try:
    #             for n in range(5):
    #                 url = f'https://poi.mapbar.com/{ename}/GA0_{n}/'
    #                 for i in get_url_lis(name=name, url=url):
    #                     print(i)
    #                     # requests.post(url='http://192.168.50.75:5001/map/city', data=i)
    #         except Exception as e:
    #             pass
    # time.sleep(2)
