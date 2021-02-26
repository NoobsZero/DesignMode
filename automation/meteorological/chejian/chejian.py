# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :chinacarPicture.py
@Time   :2020/12/31 10:40
@Author :Chen
@Software:PyCharm
"""
import os
import time
import jieba
import re
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from tool.dirUtil.mvi import cs_id
from tool.mytimeUtil.dataTime import get_time_difference


def ModifDocuments(infileName, downLoadDir):
    dirs = [i for i in os.listdir(downLoadDir) if os.path.isdir(os.path.join(downLoadDir, i, ''))]
    lines = []
    with open(infileName, encoding='utf8', errors='ignore') as er:
        for dirname in er.readlines():
            if dirname.strip() not in dirs:
                lines.append(dirname.strip())
    return lines


sheng = [cs_id[i] for i in cs_id if i[-4:] == '0000']
shi = [cs_id[i] for i in cs_id if i[-4:] != '0000' and i[-2:] == '00']
qu = [cs_id[i] for i in cs_id if i[-2:] != '00']


def getChengshi(url):
    """:arg 通过查询城市列表匹配地址中的城市名称并去掉后缀
    """
    jieba.setLogLevel(jieba.logging.INFO)
    seg_list = jieba.lcut(url)
    for i in seg_list:
        cs = [i for k in shi if k.startswith(i)]
        if len(cs) == 0:
            cs = [i for k in qu if k.startswith(i)]
        if len(cs) == 0:
            cs = [i for k in sheng if k.startswith(i)]
        if len(cs) > 0:
            return cs[0]


def getTableLis(browser, datapath='/道路交通本部'):
    browser.get('https://pan.em-data.com.cn/index.php/apps/files/?dir=%s' % datapath)
    print('https://pan.em-data.com.cn/index.php/apps/files/?dir=%s' % datapath)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/table/tbody')))
    time.sleep(1)
    chejian_dic = {}
    for link in browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/table/tbody').find_elements_by_tag_name(
            'tr'):
        datafile = link.get_attribute('data-file')
        if re.findall(r'车检|查验|误判', datafile) and not re.findall(r'8000|日志|自动化|7000|.mp4|程序|.rar|.exe|.wmv|违法|镜像|视频|示例',
                                                                datafile):
            chejian_dic[datafile] = {'data-type': link.get_attribute('data-type'),
                                     'data-size': link.get_attribute('data-size'),
                                     'data-path': link.get_attribute('data-path'),
                                     'data-mtime': link.get_attribute('data-mtime'),
                                     'data-link': link}
    for key in chejian_dic:
        if chejian_dic[key]['data-type'] == 'dir' and int(chejian_dic[key]['data-size']) > 0 and get_time_difference(
                chejian_dic[key]['data-mtime'], sub='H') > 10:
            datapath = chejian_dic[key]['data-path'] + '/' + key
            if not getChengshi(key) is None:
                print(key)
                action = ActionChains(browser).move_to_element(chejian_dic[key]['data-link'])
                action.context_click(chejian_dic[key]['data-link']).perform()  # 右键点击该元素
                element = browser.find_element_by_xpath('/html/body/div[6]/div/ul/li[5]')
                ActionChains(browser).move_to_element(element).click().perform()
                time.sleep(2)
                for filename in os.listdir(download):
                    if key in filename:
                        print(filename)
            else:
                getTableLis(browser, datapath)
        # elif re.findall(r'.tar.gz', key) and chejian_dic[key]['data-type'] == 'file' and chejian_dic[key]['data-size'] > 0:
        #     print(key)
    if '/'.join(datapath.split('/')[:-1]) != '/道路交通本部' or len(chejian_dic) == 0:
        time.sleep(2)
        browser.back()


if __name__ == '__main__':
    download = r"E:\chejian"
    proxy_data = [
        '--proxy=%s' % '61.135.185.152:80',  # 设置的代理ip
        '--proxy-type=http',  # 代理类型
        '--ignore-ssl-errors=true',  # 忽略https错误
    ]
    prefs = {"profile.managed_default_content_settings.images": 2}
    capo = DesiredCapabilities.PHANTOMJS
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", {"download.default_directory": download})
    options.add_argument('--ignore-certificate-errors')
    # taskkill /F /IM java.exe
    # taskkill /F /IM chromedriver.exe
    browser = webdriver.Chrome(desired_capabilities=capo, service_args=proxy_data, chrome_options=options)
    browser.get('https://pan.em-data.com.cn/index.php/login')
    # 输入用户名
    browser.find_element_by_id("user").send_keys("Afakerchen@em-data.com.cn")
    # 输入密码
    browser.find_element_by_id("password").send_keys("asdf1234/")
    # 点击“下一步”
    browser.find_element_by_id("submit-form").click()
    new_lis = []
    getTableLis(browser)
