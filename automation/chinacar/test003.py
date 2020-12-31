# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :getJs.py
@Time   :2020/12/7 18:19
@Author :Chen
@Software:PyCharm
"""
import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

lis_str = []


def getEngineparameters(soup, id):
    engine = list(a.string for a in
                  soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(35) > td:nth-child(1)').contents if
                  a.string is not None)
    Enginemanufacturer = list(a.string for a in
                              soup.select_one(
                                  '#con_two_p1 > table > tbody > tr:nth-child(35) > td:nth-child(2)').contents
                              if a.string is not None)
    Displacement = list(a.string for a in
                        soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(35) > td:nth-child(3)').contents if
                        a.string is not None)
    Power = list(a.string for a in
                 soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(35) > td:nth-child(4)').contents if
                 a.string is not None)
    Engineparameters = []
    for i in range(len(engine)):
        parameters = {}
        parameters['fdj'] = engine[i]
        parameters['fdjscqy'] = Enginemanufacturer[i]
        parameters['pl'] = Displacement[i]
        parameters['gl'] = Power[i]
        parameters['ids'] = id
        Engineparameters.append(parameters)
    return Engineparameters


def getProductioninformation(soup):
    Productioninformation = {}
    Vehiclename = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > a').text
    Productioninformation['field_1'] = Vehiclename
    Vehicletype = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(2) > td:nth-child(4)').text
    Productioninformation['field_2'] = Vehicletype
    Placeofmanufacture = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(3) > td:nth-child(2)').text
    Productioninformation['field_3'] = Placeofmanufacture
    Typeoflicence = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(3) > td:nth-child(4) > span > a').text
    Productioninformation['field_4'] = Typeoflicence
    Announcementbatch = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(4) > td:nth-child(2)').text
    Productioninformation['field_5'] = Announcementbatch
    Dateofissue = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(4) > td:nth-child(4)').text
    Productioninformation['field_6'] = Dateofissue
    Productnumber = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > span').text
    Productioninformation['field_7'] = Productnumber
    Catalognumber = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(5) > td:nth-child(4)').text
    Productioninformation['field_8'] = Catalognumber
    Chinesebrand = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(6) > td:nth-child(2)').text
    Productioninformation['field_9'] = Chinesebrand
    Englishbrand = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(6) > td:nth-child(4)').text
    Productioninformation['field_10'] = Englishbrand
    Announcementmodel = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(7) > td:nth-child(2)').text
    Productioninformation['field_11'] = Announcementbatch
    Exemption = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(7) > td:nth-child(4)').text
    Productioninformation['field_12'] = Exemption
    Enterprisename = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(8) > td:nth-child(2)').text
    Productioninformation['field_13'] = Enterprisename
    Fuel = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(8) > td:nth-child(4)').text
    Productioninformation['field_14'] = Fuel
    Businessaddress = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(9) > td:nth-child(2)').text
    Productioninformation['field_15'] = Businessaddress
    environmentprotection = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(9) > td:nth-child(4)').text
    Productioninformation['field_16'] = environmentprotection
    Exemptionfrominspection = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(11) > td:nth-child(2)').text
    Productioninformation['field_17'] = Exemptionfrominspection
    Expirydate = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(11) > td:nth-child(4)').text
    Productioninformation['field_18'] = Expirydate
    Announcementstatus = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(13) > td:nth-child(2)').text
    Productioninformation['field_19'] = Announcementstatus
    effectivedate = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(13) > td:nth-child(4)').text
    Productioninformation['field_20'] = effectivedate
    Statedescription = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(14) > td:nth-child(2)').text
    Productioninformation['field_21'] = Statedescription
    Changerecord = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(14) > td:nth-child(4)').text
    Productioninformation['field_22'] = Changerecord
    Dimensions = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(16) > td:nth-child(2) > span').text
    Productioninformation['field_23'] = Dimensions
    Cargoboxsize = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(16) > td:nth-child(4) > span').text
    Productioninformation['field_24'] = Cargoboxsize
    Totalmass = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(17) > td:nth-child(2)').text
    Productioninformation['field_25'] = Totalmass
    Utilizationcoefficient = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(17) > td:nth-child(4)').text
    Productioninformation['field_26'] = Utilizationcoefficient
    curbweight = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(18) > td:nth-child(2) > span').text
    Productioninformation['field_27'] = curbweight
    Ratedloadcapacity = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(18) > td:nth-child(4) > span').text
    Productioninformation['field_28'] = Ratedloadcapacity
    Trailermass = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(19) > td:nth-child(2)').text
    Productioninformation['field_29'] = Trailermass
    Semihangingsaddle = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(19) > td:nth-child(4)').text
    Productioninformation['field_30'] = Semihangingsaddle
    cab = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(20) > td:nth-child(2)').text
    Productioninformation['field_31'] = cab
    Frontrowpassengers = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(20) > td:nth-child(4)').text
    Productioninformation['field_32'] = Frontrowpassengers
    carrypassenger = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(21) > td:nth-child(2)').text
    Productioninformation['field_33'] = carrypassenger
    Antilocksystem = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(21) > td:nth-child(4)').text
    Productioninformation['field_34'] = Antilocksystem
    Approachangle = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(22) > td:nth-child(2)').text
    Productioninformation['field_35'] = Approachangle
    suspension = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(22) > td:nth-child(4) > span').text
    Productioninformation['field_36'] = suspension
    Axleload = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(23) > td:nth-child(2)').text
    Productioninformation['field_37'] = Axleload
    wheelbase = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(23) > td:nth-child(4) > span').text
    Productioninformation['field_38'] = wheelbase
    Numberofaxes = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(24) > td:nth-child(2)').text
    Productioninformation['field_39'] = Numberofaxes
    Maximumspeed = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(24) > td:nth-child(4)').text
    Productioninformation['field_40'] = Maximumspeed
    oilconsumption = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(25) > td:nth-child(2)').text
    Productioninformation['field_41'] = oilconsumption
    Numberofsprings = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(25) > td:nth-child(4)').text
    Productioninformation['field_42'] = Numberofsprings
    Numberoftires = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(26) > td:nth-child(2)').text
    Productioninformation['field_43'] = Numberoftires
    Tiresize = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(26) > td:nth-child(4)').text
    Productioninformation['field_44'] = Tiresize
    Fronttrackwidth = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(27) > td:nth-child(2)').text
    Productioninformation['field_45'] = Fronttrackwidth
    Reartrackwidth = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(27) > td:nth-child(4) > span').text
    Productioninformation['field_46'] = Reartrackwidth
    Beforebraking = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(28) > td:nth-child(2)').text
    Productioninformation['field_47'] = Beforebraking
    Afterbraking = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(28) > td:nth-child(4)').text
    Productioninformation['field_48'] = Afterbraking
    Beforecontroloperation = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(29) > td:nth-child(2)').text
    Productioninformation['field_49'] = Beforecontroloperation
    Aftercontroloperation = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(29) > td:nth-child(4)').text
    Productioninformation['field_50'] = Aftercontroloperation
    Turningform = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(30) > td:nth-child(2)').text
    Productioninformation['field_51'] = Turningform
    Startingmode = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(30) > td:nth-child(4)').text
    Productioninformation['field_52'] = Startingmode
    drivesystem = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(31) > td:nth-child(2)').text
    Productioninformation['field_53'] = drivesystem
    oilconsumptionL100km = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(31) > td:nth-child(4)').text
    Productioninformation['field_54'] = oilconsumptionL100km
    Vin = list(a.string for a in
               soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(32) > td:nth-child(2)').contents if
               a.string is not None)
    vinList = []
    for i in Vin:
        vinList.append(i)
    Productioninformation['field_55'] = ','.join(vinList)
    Fueltype = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(37) > td:nth-child(2)').text
    Productioninformation['field_56'] = Fueltype
    Accordingtothestandard = soup.select_one(
        '#con_two_p1 > table > tbody > tr:nth-child(37) > td:nth-child(4) > span').text
    Productioninformation['field_57'] = Accordingtothestandard
    Chassisemissionstandard = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(38) > td:nth-child(2)').text
    Productioninformation['field_58'] = Chassisemissionstandard
    other = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(40) > td').text
    Productioninformation['field_59'] = other
    Identifytheenterprise = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(42) > td:nth-child(2)').text
    Productioninformation['field_60'] = Identifytheenterprise
    Logotrademark = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(42) > td:nth-child(4)').text
    Productioninformation['field_61'] = Logotrademark
    Identificationmodel = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(43) > td:nth-child(2)').text
    Productioninformation['field_62'] = Identificationmodel
    # Vehiclename = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(2) > td:nth-child(2) > a').text
    # Productioninformation['车辆名称'] = Vehiclename
    # Vehicletype = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(2) > td:nth-child(4)').text
    # Productioninformation['车辆类型'] = Vehicletype
    # Placeofmanufacture = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(3) > td:nth-child(2)').text
    # Productioninformation['制造地'] = Placeofmanufacture
    # Typeoflicence = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(3) > td:nth-child(4) > span > a').text
    # Productioninformation['牌照类型'] = Typeoflicence
    # Announcementbatch = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(4) > td:nth-child(2)').text
    # Productioninformation['公告批次'] = Announcementbatch
    # Dateofissue = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(4) > td:nth-child(4)').text
    # Productioninformation['发布日期'] = Dateofissue
    # Productnumber = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(5) > td:nth-child(2) > span').text
    # Productioninformation['产品号'] = Productnumber
    # Catalognumber = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(5) > td:nth-child(4)').text
    # Productioninformation['目录序号'] = Catalognumber
    # Chinesebrand = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(6) > td:nth-child(2)').text
    # Productioninformation['中文品牌'] = Chinesebrand
    # Englishbrand = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(6) > td:nth-child(4)').text
    # Productioninformation['英文品牌'] = Englishbrand
    # Announcementmodel = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(7) > td:nth-child(2)').text
    # Productioninformation['公告型号'] = Announcementbatch
    # Exemption = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(7) > td:nth-child(4)').text
    # Productioninformation['免征'] = Exemption
    # Enterprisename = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(8) > td:nth-child(2)').text
    # Productioninformation['企业名称'] = Enterprisename
    # Fuel = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(8) > td:nth-child(4)').text
    # Productioninformation['燃油'] = Fuel
    # Businessaddress = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(9) > td:nth-child(2)').text
    # Productioninformation['企业地址'] = Businessaddress
    # environmentprotection = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(9) > td:nth-child(4)').text
    # Productioninformation['环保'] = environmentprotection
    # Exemptionfrominspection = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(11) > td:nth-child(2)').text
    # Productioninformation['免检'] = Exemptionfrominspection
    # Expirydate = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(11) > td:nth-child(4)').text
    # Productioninformation['免检有效期止'] = Expirydate
    # Announcementstatus = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(13) > td:nth-child(2)').text
    # Productioninformation['公告状态'] = Announcementstatus
    # effectivedate = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(13) > td:nth-child(4)').text
    # Productioninformation['公告生效日期'] = effectivedate
    # Statedescription = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(14) > td:nth-child(2)').text
    # Productioninformation['公告状态描述'] = Statedescription
    # Changerecord = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(14) > td:nth-child(4)').text
    # Productioninformation['变更(扩展)记录'] = Changerecord
    # Dimensions = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(16) > td:nth-child(2) > span').text
    # Productioninformation['外形尺寸'] = Dimensions
    # Cargoboxsize = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(16) > td:nth-child(4) > span').text
    # Productioninformation['货厢尺寸'] = Cargoboxsize
    # Totalmass = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(17) > td:nth-child(2)').text
    # Productioninformation['总质量'] = Totalmass
    # Utilizationcoefficient = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(17) > td:nth-child(4)').text
    # Productioninformation['载质量利用系数'] = Utilizationcoefficient
    # curbweight = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(18) > td:nth-child(2) > span').text
    # Productioninformation['整备质量'] = curbweight
    # Ratedloadcapacity = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(18) > td:nth-child(4) > span').text
    # Productioninformation['额定载质量'] = Ratedloadcapacity
    # Trailermass = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(19) > td:nth-child(2)').text
    # Productioninformation['挂车质量'] = Trailermass
    # Semihangingsaddle = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(19) > td:nth-child(4)').text
    # Productioninformation['半挂鞍座'] = Semihangingsaddle
    # cab = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(20) > td:nth-child(2)').text
    # Productioninformation['驾驶室'] = cab
    # Frontrowpassengers = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(20) > td:nth-child(4)').text
    # Productioninformation['前排乘客'] = Frontrowpassengers
    # carrypassenger = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(21) > td:nth-child(2)').text
    # Productioninformation['额定载客'] = carrypassenger
    # Antilocksystem = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(21) > td:nth-child(4)').text
    # Productioninformation['防抱死系统'] = Antilocksystem
    # Approachangle = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(22) > td:nth-child(2)').text
    # Productioninformation['接近角/离去角'] = Approachangle
    # suspension = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(22) > td:nth-child(4) > span').text
    # Productioninformation['前悬/后悬'] = suspension
    # Axleload = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(23) > td:nth-child(2)').text
    # Productioninformation['轴荷'] = Axleload
    # wheelbase = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(23) > td:nth-child(4) > span').text
    # Productioninformation['轴距'] = wheelbase
    # Numberofaxes = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(24) > td:nth-child(2)').text
    # Productioninformation['轴数'] = Numberofaxes
    # Maximumspeed = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(24) > td:nth-child(4)').text
    # Productioninformation['最高车速'] = Maximumspeed
    # oilconsumption = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(25) > td:nth-child(2)').text
    # Productioninformation['油耗'] = oilconsumption
    # Numberofsprings = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(25) > td:nth-child(4)').text
    # Productioninformation['弹簧片数'] = Numberofsprings
    # Numberoftires = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(26) > td:nth-child(2)').text
    # Productioninformation['轮胎数'] = Numberoftires
    # Tiresize = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(26) > td:nth-child(4)').text
    # Productioninformation['轮胎规格'] = Tiresize
    # Fronttrackwidth = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(27) > td:nth-child(2)').text
    # Productioninformation['前轮距'] = Fronttrackwidth
    # Reartrackwidth = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(27) > td:nth-child(4) > span').text
    # Productioninformation['后轮距'] = Reartrackwidth
    # Beforebraking = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(28) > td:nth-child(2)').text
    # Productioninformation['制动前'] = Beforebraking
    # Afterbraking = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(28) > td:nth-child(4)').text
    # Productioninformation['制动后'] = Afterbraking
    # Beforecontroloperation = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(29) > td:nth-child(2)').text
    # Productioninformation['制操前'] = Beforecontroloperation
    # Aftercontroloperation = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(29) > td:nth-child(4)').text
    # Productioninformation['制操后'] = Aftercontroloperation
    # Turningform = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(30) > td:nth-child(2)').text
    # Productioninformation['转向形式'] = Turningform
    # Startingmode = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(30) > td:nth-child(4)').text
    # Productioninformation['起动方式'] = Startingmode
    # drivesystem = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(31) > td:nth-child(2)').text
    # Productioninformation['传动型式'] = drivesystem
    # oilconsumptionL100km = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(31) > td:nth-child(4)').text
    # Productioninformation['油耗(L/100Km)'] = oilconsumptionL100km
    # Vin = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(32) > td:nth-child(2)').text
    # Productioninformation['Vin车辆识别代码'] = Vin
    # Fueltype = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(37) > td:nth-child(2)').text
    # Productioninformation['燃料种类'] = Fueltype
    # Accordingtothestandard = soup.select_one(
    #     '#con_two_p1 > table > tbody > tr:nth-child(37) > td:nth-child(4) > span').text
    # Productioninformation['依据标准'] = Accordingtothestandard
    # Chassisemissionstandard = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(38) > td:nth-child(2)').text
    # Productioninformation['底盘排放标准'] = Chassisemissionstandard
    # other = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(40) > td').text
    # Productioninformation['其他'] = other
    # Identifytheenterprise = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(42) > td:nth-child(2)').text
    # Productioninformation['标识企业'] = Identifytheenterprise
    # Logotrademark = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(42) > td:nth-child(4)').text
    # Productioninformation['标识商标'] = Logotrademark
    # Identificationmodel = soup.select_one('#con_two_p1 > table > tbody > tr:nth-child(43) > td:nth-child(2)').text
    # Productioninformation['标识型号'] = Identificationmodel
    return Productioninformation


def for_list(list_x):
    for x in list_x:
        if len(x) > 1:
            for_list(x)
        else:
            # 过滤所有标签
            pattern = re.compile("<(.*?)>")
            sub_str = re.sub(pattern, "", str(x))
            if bool(re.compile(u'[\u4e00-\u9fa5]').search(sub_str)) or bool(re.search(r'\d', sub_str)):
                lis_str.append(sub_str)

def getjson(file):
    fo = open(file, encoding='utf8', errors='ignore')
    fileList = fo.readlines()
    matches = (x for x in fileList if ('tarid' in x and 'tarid_nobase' not in x) or ('img' in x))
    urlList = {}
    for i in matches:
        if 'img' in i:
            url = re.sub('clcppic', "spic", re.findall(r'(https?://\S*?jpg|\S*?JPG)+', str(i))[1])
        else:
            result = re.sub('\W+', '', i.split(':')[1]).replace("_", '')
            urlList[url] = ['http://chinacar.com.cn/ggcx_new/search_view.html?id=' + result, result]
    return urlList

if __name__ == '__main__':
    # urlList = getjson('dongfeng.txt')
    # with open("baoma.json", "w") as f:
    #     json.dump(urlList, f)
    fo = open('dongfeng.txt', encoding='utf8', errors='ignore')
    fileList = fo.readlines()
    matches = (x for x in fileList if ('tarid' in x and 'tarid_nobase' not in x) or ('img' in x))
    urlList = {}
    for i in matches:
        if 'img' in i:
            url = re.sub('clcppic', "spic", re.findall(r'(https?://\S*?jpg|\S*?JPG)+', str(i))[1])
        else:
            result = re.sub('\W+', '', i.split(':')[1]).replace("_", '')
            urlList[url] = ['http://chinacar.com.cn/ggcx_new/search_view.html?id=' + result, result]

    proxy_data = [
        '--proxy=%s' % '61.135.185.152:80',  # 设置的代理ip
        '--proxy-type=http',  # 代理类型
        '--ignore-ssl-errors=true',  # 忽略https错误
    ]
    capa = DesiredCapabilities.PHANTOMJS
    url1 = 'http://192.168.50.100:3018/api/v1/chinacar'
    url2 = 'http://192.168.50.100:3018/api/v1/chinacar/fdj'

    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument('--headless')
    for key in urlList:
        browser = webdriver.Chrome(desired_capabilities=capa, service_args=proxy_data, chrome_options=options)
        browser.get(urlList[key][0])
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="con_two_p1"]/table')))
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        browser.close()
        productioninformation = getProductioninformation(soup)
        productioninformation['field_63'] = key
        productioninformation['ids'] = urlList[key][1]
        print(productioninformation)
        prJson = json.dumps(productioninformation, ensure_ascii=False).encode('utf-8')
        requests.post(url=url1, data=prJson)
        engineparameters = getEngineparameters(soup, urlList[key][1])
        for i in engineparameters:
            print(i)
            enJson = json.dumps(i, ensure_ascii=False).encode('utf-8')
            requests.post(url=url2, data=enJson)

        lis_str.clear()
