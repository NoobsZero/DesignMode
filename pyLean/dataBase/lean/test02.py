# encoding: utf-8
"""
@file: test02.py
@time: 2021/4/1 16:41
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from PyQt5 import Qt
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from pyLean.dataBase.lean.Ui_MainWindow import Ui_MainWindow


class Car_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # super().__init__()
        # self.setupUi(self)
        # self.pushButton_10
        # 设置播放暂停的标志
        self.FLAG_PLAY = False
        self.videoFullScreen = False  # 判断当前widget是否全屏
        self.wsize = self.widget.size()
        # 定义player
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.widget)  # 视频播放输出的widget，就是上面定义的
        # 这里进行按钮的绑定
        self.pushButton_7.clicked.connect(self.test)
        # self.pushButton_11.clicked.connect(self.test)
        # self.btn_choose.clicked.connect(self.openVideoFile)
        # self.btn_play.clicked.connect(self.playVideo)
        # self.btn_stop.clicked.connect(self.stopVideo)
        # self.widget.doubleClickedItem.connect(self.videoDoubleClicked)

    # 槽函数练习
    @QtCore.pyqtSlot()
    def on_pushButton_10_clicked(self):
        self.label_5.setText("槽函数")

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件

        self.player.play()  # 播放视频
        self.FLAG_PLAY = True

    def playVideo(self):
        # 如果没有播放，则进行播放
        if not self.FLAG_PLAY:
            self.player.play()
            self.FLAG_PLAY = True
        else:
            self.player.pause()
            self.FLAG_PLAY = False

    def stopVideo(self):
        self.player.stop()

    def changeSlide(self, position):
        self.vidoeLength = self.player.duration() + 0.1
        print(self.vidoeLength)
        self.sld_video.setValue(round((position / self.vidoeLength) * 100))
        self.lab_video.setText(str(round((position / self.vidoeLength) * 100, 2)) + '%')

    def videoDoubleClicked(self, text):
        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                # self.player.pause()
                # self.videoFullScreenWidget.hide()
                # self.player.setVideoOutput(self.wgt_video)
                # self.player.play()
                self.videoFullScreen = False
                self.widget.setFullScreen(0)
                self.widget.setMaximumSize(self.wsize)
            else:
                self.wsize = self.widget.size()
                self.widget.setFullScreen(1)
                # self.player.pause()
                # self.videoFullScreenWidget.show()
                # self.player.setVideoOutput(self.videoFullScreenWidget)
                # self.player.play()
                self.videoFullScreen = True

    # 这里进行按钮事件的编写
    def test(self):
        self.label_8.setText("测试按钮")
        self.label_5.setText("测试按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = QMediaPlayer()
    vw = QVideoWidget()  # 定义视频显示的widget
    vw.show()
    player.setVideoOutput(vw)  # 视频播放输出的widget，就是上面定义的
    player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))  # 选取视频文件
    player.play()  # 播放视频
    # player.stop()
    sys.exit(app.exec_())
