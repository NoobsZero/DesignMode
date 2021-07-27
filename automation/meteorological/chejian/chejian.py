# -*- encoding:utf-8 -*-
# coding=utf-8
"""
@File   :chinacarPicture.py
@Time   :2020/12/31 10:40
@Author :Chen
@Software:PyCharm
"""
import os
import shutil
import sys
import threading
import time
import jieba
import re
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import tool
from tool.baseUtil.getBaseUtil import BaseProgressBar, MyCity
from tool.dirUtil.getDirUtil import project_root_path
from tool.dirUtil.mvi import cs_id
from tool.myconfigUtil.JsonConfig import JsonConfig
from tool.mylinuxUtil.getMessgae import LoginLinux
from tool.mytimeUtil.dataTime import get_time_difference, getTime, getTimeToStamp


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


def zip_cj_move(linuxPaths, zipFileName, types):
    execlis = []
    filePath = linuxPaths.getValue('cj_tmp') + '/' + zipFileName + ' '
    beifuPath = linuxPaths.getValue('cj_beifen') + '/' + getTime(timeformat="%Y%m") + '/'
    if 'wupan' == types:
        toPath = linuxPaths.getValue('cj_wupan') + '/' + MyCity().getCityName(zipFileName) + '/raw/' + getTime(
            timeformat="%Y%m") + '/'
        execlis.append('mkdir -p ' + toPath)
        execlis.append('mv ' + filePath + toPath)
    elif 'other' == types:
        toPath = linuxPaths.getValue('cj_other') + '/' + MyCity().getCityName(zipFileName) + '/raw/' + getTime(
            timeformat="%Y%m") + '/'
        execlis.append('mkdir -p ' + toPath)
        execlis.append('cp ' + filePath + ' ' + toPath)
        execlis.append('mkdir -p ' + beifuPath)
        execlis.append('mv ' + filePath + beifuPath)
    elif 'beifen' == types:
        execlis.append('mkdir -p ' + beifuPath)
        execlis.append('mv ' + filePath + beifuPath)
    execlis.append('rm -rf ' + linuxPaths.getValue('cj_tmp') + '/*')
    execlis.append('rm -rf ' + linuxPaths.getValue('cj_todo') + '/*')
    return execlis


def zip_cj_tmp(zipFile):
    client = LoginLinux()
    linuxPaths = tool.myconfigUtil.JsonConfig.JsonConfig().loadConf(
        os.path.join(project_root_path('untitled'),
                     r'automation\meteorological\chejian\conf\linuxpath.conf.json'))

    unzip_command = 'unzip -n -O gbk {} -d {}'.format(
        linuxPaths.getValue('cj_tmp') + '/' + os.path.basename(zipFile),
        linuxPaths.getValue('cj_tmp'))
    print(unzip_command)
    reLis = client.exec(unzip_command)
    rm_lis = []
    for i in reLis:
        if ('tar.gz' in i and '误判' not in os.path.basename(zipFile) and 'emData' in i) or (
                'tar.gz' in i and '误判' in os.path.basename(zipFile) and 'WP' in i):
            print(linuxPaths.getValue('cj_tmp'))
            print(str(i).replace('extracting:', '').strip())
            print(linuxPaths.getValue('cj_todo'))
            mv_command = 'mv ' + linuxPaths.getValue('cj_tmp') + '/' + str(i).replace('extracting:', '').strip() + ' ' \
                         + linuxPaths.getValue('cj_todo')
            print(mv_command)
            sys.exit(1)
            client.exec(mv_command)
        elif 'creating:' in i:
            rm_lis.append(i)
    for r in rm_lis:
        rm_command = 'rm -rf ' + str(r).replace('creating:', '').strip()
        print(rm_command)
        client.exec(rm_command)
    print('sh work.sh')
    start_log = client.exec('ls -l ' + linuxPaths.getValue('cj_log'))[0]
    client.exec('cd ' + linuxPaths.getValue('cj_collect') + ' && sh work.sh')
    while True:
        time.sleep(5)
        end_log = client.exec('ls -l ' + linuxPaths.getValue('cj_log'))[0]
        if start_log != end_log:
            if len(client.exec('ls ' + linuxPaths.getValue('cj_todo'))) == 0 and \
                    len(re.findall(r'True|False|没有 处理结束的压缩文件|the end',
                                   client.exec('cat ' + linuxPaths.getValue('cj_log'))[-1])) > 0:
                break
            else:
                start_log = end_log
    result_log = client.exec('cat ' + linuxPaths.getValue('cj_log'))[-2]
    print(result_log)
    command = ''
    if 'True' in result_log:
        if '误判' in os.path.basename(zipFile):
            command = 'rm ' + zipFile
        else:
            command = zip_cj_move(linuxPaths, os.path.basename(zipFile), 'beifen')
    else:
        if '误判' in os.path.basename(zipFile):
            command = zip_cj_move(linuxPaths, os.path.basename(zipFile), 'wupan')
        else:
            command = zip_cj_move(linuxPaths, os.path.basename(zipFile), 'other')
    print(command)
    client.exec(command)
    return True


def file_winToLinux(zipFile, count):
    linuxFile = os.path.join(r'\\192.168.90.10\vehicle_data\tool\temporary', os.path.basename(zipFile))
    print(linuxFile)
    threading.Thread(target=shutil.move,
                     args=(zipFile, r'\\192.168.90.10\vehicle_data\tool\temporary')).start()
    time.sleep(1)
    handle = BaseProgressBar(count)
    tqdm_re = handle.tqdmBarFlush(linuxFile)
    return tqdm_re


def file_download(key, chejian_dic):
    clickUp = True
    while clickUp:
        upStartLen = len(os.listdir(download))
        action = ActionChains(browser).move_to_element(chejian_dic[key]['data-link'])
        action.context_click(chejian_dic[key]['data-link']).perform()  # 右键点击该元素
        time.sleep(1)
        element = browser.find_element_by_class_name('action-4')
        ActionChains(browser).move_to_element(element).click().perform()
        time.sleep(2)
        upEndLen = len(os.listdir(download))
        if upStartLen != upEndLen:
            clickUp = False
    for filename in os.listdir(download):
        tqdm_re = False
        if key in filename and filename.endswith('.crdownload'):
            handle = BaseProgressBar(chejian_dic[key]['data-size'])
            filepath = os.path.join(download, filename)
            print('https://pan.em-data.com.cn/index.php/apps/files/?dir=%s' % chejian_dic[key]['data-path'])
            tqdm_re = handle.tqdmBarFlush(filepath)
            time.sleep(5)
            zipFile = [os.path.join(download, filename).rstrip('.crdownload') for filename in os.listdir(download) if key in filename][0]
        if tqdm_re and os.path.isfile(zipFile):
            # 移动
            if file_winToLinux(zipFile, chejian_dic[key]['data-size']):
                # 解压
                if zip_cj_tmp(zipFile):
                    action = ActionChains(browser).move_to_element(chejian_dic[key]['data-link'])
                    action.context_click(chejian_dic[key]['data-link']).perform()  # 右键点击该元素
                    element = browser.find_element_by_class_name('action-5')
                    ActionChains(browser).move_to_element(element).click().perform()
                    time.sleep(2)


def getTableLis(browser, datapath='/道路交通本部'):
    browser.get('https://pan.em-data.com.cn/index.php/apps/files/?dir=%s' % datapath)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'fileList')))
    time.sleep(1)
    chejian_dic = {}
    for link in browser.find_element_by_id('fileList').find_elements_by_tag_name('tr'):
        datafile = link.get_attribute('data-file')
        if re.findall(r'车检|查验|误判', datafile) and not re.findall(
                r'东营车检|8000|日志|自动化|7000|.mp4|程序|.rar|.exe|.wmv|违法|镜像|视频|示例|log',
                datafile):
            chejian_dic[datafile] = {'data-type': link.get_attribute('data-type'),
                                     'data-size': link.get_attribute('data-size'),
                                     'data-path': link.get_attribute('data-path') + '/' + datafile,
                                     'data-mtime': link.get_attribute('data-mtime'),
                                     'data-link': link}
            if not getChengshi(datafile) is None and (get_time_difference(chejian_dic[datafile]['data-mtime'],
                                                                          sub='H') > 10 or '完成' in datafile):
                file_download(datafile, chejian_dic)
                print(chejian_dic.pop(datafile))
    for key in chejian_dic:
        if chejian_dic[key]['data-type'] == 'dir' and int(chejian_dic[key]['data-size']) > 0:
            datapath = chejian_dic[key]['data-path']
            if not getChengshi(key) is None and (
                    get_time_difference(chejian_dic[key]['data-mtime'], sub='H') > 10 or '完成' in datafile):
                file_download(key, chejian_dic)
                print(chejian_dic.pop(key))
            else:
                getTableLis(browser, datapath)
    if '/'.join(datapath.split('/')[:-1]) != '/道路交通本部' or len(chejian_dic) == 0:
        time.sleep(2)
        browser.back()


def test():
    client = LoginLinux()
    linuxPaths = tool.myconfigUtil.JsonConfig.JsonConfig().loadConf(
        os.path.join(project_root_path('untitled'),
                     r'automation\meteorological\chejian\conf\linuxpath.conf.json'))
    # print(getTime())
    # client.exec('cd ' + linuxPaths.getValue('cj_collect') + ' && sh work.sh')
    for i in client.exec('cat ' + linuxPaths.getValue('cj_log'))[-5:-1]:
        print(i)
    # print('ok', getTime())


if __name__ == '__main__':
    # test()
    download = r"F:\chejian"
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
    browser.find_element_by_id("user").send_keys("Afakerchen@em-data.com.cn")
    browser.find_element_by_id("password").send_keys("asdf1234?")
    browser.find_element_by_id("submit-form").click()
    new_lis = []
    getTableLis(browser)
    # browser.close()
