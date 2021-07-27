# encoding: utf-8
"""
@file: test01.py
@time: 2021/7/2 13:07
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import io
import time
from io import BytesIO
from PIL import Image
import random, base64
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from matplotlib import pyplot as plt
import cv2
import pyautogui as pag


class CrackGeetest():
    # def __init__(self, url, proxy, str_xpath):
    def __init__(self, url, str_xpath):
        self.url = url
        # self.proxy = proxy
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # chrome_options.add_argument('--proxy-server=%s' % self.proxy) # 添加代理
        # self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='添加chromedriver插件路径或者添加环境变量') # 创建浏览器对象
        self.browser = webdriver.Chrome(chrome_options=chrome_options)  # 创建浏览器对象
        self.wait = WebDriverWait(self.browser, 80)  # 构造函数，获取一个webdriver实例，并以秒为单位超时。
        self.browser.set_page_load_timeout(20)  # 设置在引发错误之前等待页面加载完成的时间
        self.xpath = str_xpath  # 点击按钮的ID，用于定位
        self.threshold = 60  # 验证码图片对比中RGB的差值，可调
        self.left = 60  # 验证码图片的对比中的起始坐标，即拖动模块的右边线位置
        self.deviation = 7  # 误差值，这个值是多次测试得出的经验值

    def open(self):
        """
        # 打开浏览器,并输入查询内容
        """
        # 最大化正在使用的当前窗口
        self.browser.maximize_window()
        self.browser.get(self.url)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/span[1]/span/input')))
        self.browser.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/div[1]/div[1]/div/span[1]/span/input').send_keys(
            '12346785351')
        time.sleep(0.5)

        if '无法访问此网站' in self.browser.page_source or '未连接到互联网' in self.browser.page_source or '该网页无法正常运作' in self.browser.page_source:
            self.browser.quit()
        bowton = self.wait.until(EC.presence_of_element_located((By.XPATH, self.xpath)))
        try:
            bowton.send_keys(Keys.ENTER)
        except:
            bowton.send_keys(Keys.ENTER)

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'slider')))
        return slider

    def get_image(self):
        """
        从网页的网站截图中，截取验证码图片
        :return: 验证码图片对象
        """
        times = random.uniform(3, 5)
        times = round(times, 2)
        time.sleep(times)  # canvasBg block
        # bg_js = 'return document.getElementsByClassName("block")[0].toDataURL("image/png");'
        fullbg_js = 'return document.getElementsByClassName("canvasBg")[0].toDataURL("image/png");'
        # slice 执行 JS 代码并拿到图片 base64 数据
        # bg_info = self.browser.execute_script(bg_js)  # 执行js文件得到带图片信息的图片数据
        # bg_base64 = bg_info.split(',')[1]  # 拿到base64编码的图片信息
        # bg_bytes = base64.b64decode(bg_base64)  # 转为bytes类型
        # bg_image = Image.open(BytesIO(bg_bytes)).convert('RGBA') # image读取图片信息
        # print(bg_image)
        # bg_image.show()

        fullbg_info = self.browser.execute_script(fullbg_js)  # 执行js文件得到带图片信息的图片数据
        fullbg_base64 = fullbg_info.split(',')[1]  # 拿到base64编码的图片信息
        fullbg_bytes = base64.b64decode(fullbg_base64)  # 转为bytes类型
        fullbg_image = Image.open(BytesIO(fullbg_bytes))  # image读取图片信息
        a_path = 'a.png'
        b_path = 'b.png'
        fullbg_image.save(a_path)

        all_img = cv2.imread(a_path)
        cv2.imwrite(b_path, all_img)
        all_img = Image.open(b_path).convert('RGBA')
        print(all_img)
        return fullbg_image, all_img

    def get_distance(self, image1, image2):
        """
        拿到滑动验证码需要移动的距离
        :param image1: 没有缺口的图片对象
        :param image2: 带缺口的图片对象
        :return: 需要移动的距离
        """
        i = 0
        for i in range(self.left, image1.size[0]):
            for j in range(image1.size[1]):
                rgb1 = image1.load()[i, j]
                rgb2 = image2.load()[i, j]
                res1 = abs(rgb1[0] - rgb2[0])
                res2 = abs(rgb1[1] - rgb2[1])
                res3 = abs(rgb1[2] - rgb2[2])
                res4 = abs(rgb1[3] - rgb2[3])
                # 如果rgb差值大于self.threshold，滑动的距离会等于i-误差
                if not (res1 < self.threshold and res2 < self.threshold and res4 < self.threshold):
                    # distance = i - self.deviation
                    distance = i + 10
                    return distance
        print('未识别出验证码中的不同位置，或图片定位出现异常')
        return i  # 如果没有识别出不同位置，则象征性的滑动，以刷新下一张验证码

    def get_track(self, distance):
        """
        :param distance:需要的滑动距离
        :return: 滑动轨迹
        """
        track = []
        current = 0  # 当前移动距离
        mid = int(distance * round(random.uniform(0.6, 0.7), 2))  # 需要加速的距离
        jiansu = distance - mid  # 需要减速的距离
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            # 设置加速度动态变化
            if current < mid:
                ap = random.uniform(3, 5)
                times = round(ap, 2)
                a = times  # 加速度a
                v0 = v  # 初速度v0
                v = v0 + a * t
                move = v0 * t + 1 / 2 * a * t * t + 0.5
                current += move  # 当前位移
                track.append(round(move))  # 加入轨迹
            # 设置减速度动态变化
            else:
                a = -1 * (v * v) / (2 * jiansu)
                v0 = v
                v = v0 + a * t
                if distance > 120:
                    move = v0 * t + 1 / 2 * a * t * t - 1.5
                elif distance <= 120 and distance >= 60:
                    move = v0 * t + 1 / 2 * a * t * t - 1
                else:
                    move = v0 * t + 1 / 2 * a * t * t - 0.5
                if move < 1:
                    move = 1
                current += move
                track.append(round(move))
        return track

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        # 点击并按住滑块
        ActionChains(self.browser).click_and_hold(slider).perform()
        time.sleep(0.5)
        # 移动
        for x in track:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
            # 代码滑动太快，为了更好的模拟人的行为，滑动每次停0.02秒可以提高成功率
            time.sleep(0.02)
        time.sleep(0.3)
        # 误差
        ActionChains(self.browser).move_by_offset(xoffset=3, yoffset=0).perform()
        # 释放滑块
        ActionChains(self.browser).release().perform()

    def check_html(self, html):
        if '验证成功' in html or '用户不存在' in html:
            return True
        else:
            return False

    def crack(self, button='', verification='first'):
        """
        程序运行流程
        :return:
        """
        if verification == 'first':
            self.open()
            button = self.get_slider()
        button.click()
        image1, image2 = self.get_image()
        distance = self.get_distance(image1, image2)
        print('需要移动的距离：', distance)
        track = self.get_track(distance)
        print('移动轨迹：', track)
        slider = self.get_slider()
        self.move_to_gap(slider, track)
        times = random.uniform(2, 3)
        times = round(times, 1)
        time.sleep(times)
        html = self.browser.page_source
        res = self.check_html(html)
        print('检测html是否滑动成功：', res)
        while not res:
            Crack.crack(button=button, verification='no first')


if __name__ == '__main__':
    url = 'https://sso.ahzwfw.gov.cn/uccp-user/resources/forgetPsd/forgetPsd-phone?callback='
    str_xpath = '//*[@id="forget-step1"]/div[2]/button[1]'
    # Crack = CrackGeetest(url, proxy='http://xxx', str_xpath=str_xpath)
    Crack = CrackGeetest(url, str_xpath=str_xpath)
    Crack.crack()
