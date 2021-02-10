# -*- encoding:utf-8 -*-
"""
@File   :alarm.py
@Time   :2021/1/20 8:54
@Author :Chen
@Software:PyCharm
"""
import datetime
import time
import requests


def get_time_stamp13(datetime_obj):
    # 生成13时间戳   eg:1557842280000
    datetime_obj = datetime.datetime.strptime(datetime_obj, '%Y-%m-%d %H:%M:%S.%f')
    # datetime_str = datetime.datetime.strftime(datetime_obj, '%Y-%m-%d %H:%M:%S.%f')
    # # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(datetime_obj.timetuple())))
    # # 3位，微秒
    data_microsecond = str("%06d" % datetime_obj.microsecond)[0:3]
    date_stamp = date_stamp + data_microsecond
    return int(date_stamp)


def get_stamp13_time(date_stamp):
    d = datetime.datetime.fromtimestamp(date_stamp / 1000)
    date_str = d.strftime("%Y-%m-%d %H:%M:%S.%f")
    return date_str


def get_stamp13():
    t = time.time()
    return int(round(t * 1000))


if __name__ == '__main__':
    yesterday_time = datetime.datetime.strptime(
        (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d 00:00:00"), '%Y-%m-%d %H:%M:%S')
    url = 'http://product.weather.com.cn/alarm/grepalarm_cn.php?_=%d' % get_stamp13()
    reponse = requests.get(url=url)
    reponse.encoding = 'utf-8'
    alarm_url_lis = eval(reponse.text.lstrip('var alarminfo = ').rstrip(';'))['data']
    for data in alarm_url_lis:
        try:
            datetime_str = datetime.datetime.strptime(str(data[1]).split('-')[1], '%Y%m%d%H%M%S')
            if datetime_str > yesterday_time:
                alarm_data_re = requests.get(
                    url='http://product.weather.com.cn/alarm/webdata/%s?_=%d' % (data[1], get_stamp13()))
                alarm_data_re.encoding = 'utf-8'
                alarm_data = eval(alarm_data_re.text.lstrip('var alarminfo = '))
                alarm_data_qi = requests.get(
                    url='http://www.weather.com.cn/data/alarminfo/%s.html?_=%d' % (
                        alarm_data['TYPECODE'] + alarm_data['LEVELCODE'], get_stamp13()))
                alarm_data_qi.encoding = 'utf-8'
                if '404' not in alarm_data_qi.text:
                    alarm_data['alarmfyzn_id'] = eval(alarm_data_qi.text.lstrip('var alarmfyzn='))[0]
                    alarm_data['alarmfyzn_type'] = eval(alarm_data_qi.text.lstrip('var alarmfyzn='))[1]
                    alarm_data['alarmfyzn_bz'] = eval(alarm_data_qi.text.lstrip('var alarmfyzn='))[2]
                    alarm_data['alarmfyzn_fyzn'] = eval(alarm_data_qi.text.lstrip('var alarmfyzn='))[3]
                    alarm_data['alarmfyzn_gif'] = 'http://www.weather.com.cn/m2/i/about/alarmpic/%s.gif' % (
                                alarm_data['TYPECODE'] + alarm_data['LEVELCODE'])
                alarm_data['url'] = data[1]
                print(alarm_data)
                requests.post(url='http://192.168.50.75:5001/api/v1/weather/yujing', data=alarm_data)
                time.sleep(2)
        except Exception:
            continue