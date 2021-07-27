# encoding: utf-8
"""
@file: ffmpeg.py
@time: 2021/6/24 9:40
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
@introduce: ffmpeg图片转MP4
"""
import os
import glob
from datetime import date, timedelta

fileDir = '/home/ykftp/Camera_Weather/'  # 存放图片路径 192.168.90.10/ykftp/Camera_Weather/
outputfile = '/home/ykftp/qixiang_data/Camera_Weather_out_mp4/'  # 输出mp4视频路径
txt_path = '/home/ykftp/qixiang_data/Camera_Weather_txt_path/'  # 图片路径txt文件


def run_make_file(fileDir, txt_path, outputfile):
    """
    合成固定某天云状图片为mp4,命名规则为机位名加日期
    """
    cmd = ''
    output_img_name = ''
    # timedata = '2020_09_10-2020_09_10'
    # yesterday = '2020_09_10'
    yesterday = (date.today() + timedelta(days=-1)).strftime("%Y_%m_%d")
    timedata = yesterday + "-" + yesterday

    os.makedirs(outputfile + yesterday)
    os.makedirs(txt_path + yesterday)

    for locationDir in glob.glob(fileDir + '*'):
        location_name = os.path.basename(locationDir)
        output_img_name = location_name + '_' + timedata[:10]
        output_img_name_txt = txt_path + "/" + yesterday + "/" + output_img_name + '.txt'
        dir_path = locationDir + '/' + timedata

        print(dir_path)
        if os.path.exists(dir_path):
            print("output_img_name_txt")
            with open(output_img_name_txt, mode='w') as f:
                img_names = os.listdir(dir_path)
                img_names.sort()
                print(img_names)
                for img_name in img_names:
                    img_path = os.path.join(dir_path, img_name)
                    f.write('file ' + "'" + img_path + "'" + '\n')
        # cmd = 'ffmpeg -r 2 -f concat -safe 0 -i ' + output_img_name_txt + '  -s  1920x1080 ' + outputfile+"/"+yesterday+'/'+output_img_name +'.mp4'

        cmd = 'ffmpeg -r 2 -f concat -safe 0 -i ' + output_img_name_txt + ' -s 1920x1080 -b 250k ' + outputfile + '/' + yesterday + '/' + output_img_name + '.mp4'

        os.system(cmd)


if __name__ == "__main__":
    run_make_file(fileDir, txt_path, outputfile)
    print((date.today() + timedelta(days=-1)).strftime("%Y_%m_%d"))
