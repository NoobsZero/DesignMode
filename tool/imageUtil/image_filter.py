# coding: utf-8
import cv2 as cv2
import numpy as np
import os
from tqdm import tqdm
import argparse
import shutil


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-image_dir', default=r'//192.168.30.41/0_.算法部/pengshanzhen/up/11-4/all_img/聊城-安全带/60110',
                        help='imageUtil dir')
    parser.add_argument('-output_dir', default='//192.168.30.41/0_.算法部/pengshanzhen/up/11-4/all_img/抽烟cxw/',
                        help='output dir')
    parser.add_argument('-image_width', default=960)
    parser.add_argument('-image_height', default=540)
    g_args = parser.parse_args()
    return g_args


class ImageNotation():
    def __init__(self, img_filename, g_args):

        self.img_filename = img_filename
        self.img = cv2.imread(self.img_filename)

        self.img = cv2.resize(self.img,
                              (g_args.image_width, int(self.img.shape[0] / self.img.shape[1] * g_args.image_width)))

        self.g_args = g_args

    def on_EVENT_LBUTTONDOWN(self, event, x, y, flags, a):
        if event == cv2.EVENT_LBUTTONDOWN:

            cv2.destroyAllWindows()
            shutil.move(self.img_filename, g_args.output_dir + os.path.split(self.img_filename)[1])

        elif event == cv2.EVENT_MOUSEWHEEL:
            cv2.destroyAllWindows()
            os.remove(self.img_filename)

    def showImg(self):
        cv2.destroyAllWindows()
        cv2.namedWindow("image")
        cv2.imshow("image", self.img)
        cv2.setMouseCallback("image", self.on_EVENT_LBUTTONDOWN)
        cv2.waitKey()


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


if __name__ == '__main__':
    g_args = parseArgs()
    Filelist = get_filelist(g_args.image_dir)
    print(len(Filelist))
    # files = os.listdir(g_args.image_dir)
    print('======== Begin to notate ========')
    print('images located in: {}'.format(g_args.image_dir))
    print('total image: {}'.format(len(Filelist)))

    files = sorted(Filelist)
    # files = [os.path.join(g_args.image_dir, filename) for filename in files]
    if os.path.exists(g_args.output_dir) == False:
        os.mkdir(g_args.output_dir)
    for filename in tqdm(files):
        if os.path.exists(filename):
            def on_EVENT_LBUTTONDOWN(event, x, y, flags, a):
                if event == cv2.EVENT_LBUTTONDOWN:
                    cv2.destroyAllWindows()
                    shutil.move(filename, g_args.output_dir + os.path.split(filename)[1])
                elif event == cv2.EVENT_RBUTTONDOWN:
                    cv2.destroyAllWindows()
                print('images located in: {}'.format(filename))
            img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)
            img = cv2.resize(img, (g_args.image_width+1000, int(img.shape[0]/img.shape[1]*g_args.image_width)+300))
            cv2.destroyAllWindows()
            cv2.namedWindow("image")
            cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("image", img)
            cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
            cv2.waitKey()
