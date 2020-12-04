#打开文件
import h5py
import cv2
import argparse
import os
import shutil
import numpy as np


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-image_dir', default = 'E:/toos/test/image', help='imageUtil dir')
    parser.add_argument('-output_dir', default='E:/toos/test/ok',
                        help='output dir')
    parser.add_argument('-image_width', default=960)
    parser.add_argument('-image_height', default=540)
    g_args = parser.parse_args()
    return g_args

def get_filelist(dir):
    Filelist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 文件名列表，包含完整路径
            if filename[-3:] == 'jpg':
                Filelist.append(os.path.join(home, filename))
            # # 文件名列表，只包含文件名
            # Filelist.append( filename)
    return Filelist

g_args = parseArgs()

# 创建目录
if os.path.exists(g_args.output_dir) == False:
    os.mkdir(g_args.output_dir)
# 遍历获取文件下所有文件地址
Filelist = get_filelist(g_args.image_dir)

print(len(Filelist))
num = 0
for file in Filelist:
    num = num + 1
    print(num)
    print(file)
    # 解决中文路径
    img = cv2.imdecode(np.fromfile(file, dtype=np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (g_args.image_width, int(img.shape[0]/img.shape[1]*g_args.image_width)))
    cv2.imshow(file, img)
    cv2.waitKey()
    # print('======== Begin to notate ========')
    # print('images located in: {}'.format(g_args.image_dir))
    # print('total imageUtil: {}'.format(len(Filelist)))

#     # files = [os.path.join(g_args.image_dir, filename) for filename in files]
#     for filename in tqdm(files):
#         if os.path.exists(filename):