# -*- coding: utf-8 -*-
"""
@file: Ui_MainWindow.py
@time: 2021/4/2 11:09
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""

# Form implementation generated from reading ui file 'single_car_system.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1182, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame1 = QtWidgets.QFrame(self.frame)
        self.frame1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame1.setStyleSheet("border-style:solid;\n"
                                  "border-width:3px;\n"
                                  "background-color: rgb(94, 94, 94);")
        self.frame1.setObjectName("frame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalFrame = QtWidgets.QFrame(self.frame1)
        self.verticalFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.verticalFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.verticalFrame.setStyleSheet("\n"
                                         "background-color: rgb(43, 43, 43);\n"
                                         "border-style:none")
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setMaximumSize(QtCore.QSize(100, 30))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "text-align:center;\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.horizontalFrame)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 40))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(127, 127, 127);\n"
                                    "\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_7.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_7.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.verticalLayout_2.addWidget(self.verticalFrame)
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border-style:none;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.frame2 = QtWidgets.QFrame(self.frame1)
        self.frame2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame2.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                  "border-style:none;")
        self.frame2.setObjectName("frame2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame2)
        self.pushButton.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame2)
        self.pushButton_2.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.frame2)
        self.scrollArea = QtWidgets.QScrollArea(self.frame1)
        self.scrollArea.setStyleSheet("border-style:none;\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 172, 440))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "border-style:none;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.frame3 = QtWidgets.QFrame(self.frame1)
        self.frame3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame3.setStyleSheet("background-color: rgb(74, 74, 74);border-style:none;\n"
                                  "")
        self.frame3.setObjectName("frame3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame3)
        self.pushButton_3.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame3)
        self.pushButton_4.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame3)
        self.pushButton_5.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame3)
        self.pushButton_6.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame3)
        self.horizontalLayout_5.addWidget(self.frame1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalFrame1 = QtWidgets.QFrame(self.frame)
        self.verticalFrame1.setMaximumSize(QtCore.QSize(1666666, 162))
        self.verticalFrame1.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                          "color: rgb(255, 255, 255);")
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalFrame1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalFrame1)
        self.pushButton_11.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_6.addWidget(self.pushButton_11)
        self.pushButton10 = QtWidgets.QPushButton(self.verticalFrame1)
        self.pushButton10.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton10.setObjectName("pushButton10")
        self.horizontalLayout_6.addWidget(self.pushButton10)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalSlider = QtWidgets.QSlider(self.verticalFrame1)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal {\n"
                                            "border: 1px solid #4A708B;\n"
                                            "background: #C0C0C0;\n"
                                            "height: 5px;\n"
                                            "border-radius: 1px;\n"
                                            "padding-left:-1px;\n"
                                            "padding-right:-1px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::sub-page:horizontal {\n"
                                            "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
                                            "    stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                            "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
                                            "    stop: 0 #5DCCFF, stop: 1 #1874CD);\n"
                                            "border: 1px solid #4A708B;\n"
                                            "height: 10px;\n"
                                            "border-radius: 2px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::add-page:horizontal {\n"
                                            "background: #575757;\n"
                                            "border: 0px solid #777;\n"
                                            "height: 10px;\n"
                                            "border-radius: 2px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::handle:horizontal \n"
                                            "{\n"
                                            "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
                                            "    stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));\n"
                                            "\n"
                                            "    width: 11px;\n"
                                            "    margin-top: -3px;\n"
                                            "    margin-bottom: -3px;\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::handle:horizontal:hover {\n"
                                            "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, \n"
                                            "    stop:0.778409 rgba(255, 255, 255, 255));\n"
                                            "\n"
                                            "    width: 11px;\n"
                                            "    margin-top: -3px;\n"
                                            "    margin-bottom: -3px;\n"
                                            "    border-radius: 5px;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::sub-page:horizontal:disabled {\n"
                                            "background: #00009C;\n"
                                            "border-color: #999;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::add-page:horizontal:disabled {\n"
                                            "background: #eee;\n"
                                            "border-color: #999;\n"
                                            "}\n"
                                            "\n"
                                            "QSlider::handle:horizontal:disabled {\n"
                                            "background: #eee;\n"
                                            "border: 1px solid #aaa;\n"
                                            "border-radius: 4px;\n"
                                            "}")
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_7.addWidget(self.horizontalSlider)
        self.label_7 = QtWidgets.QLabel(self.verticalFrame1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_choose = QtWidgets.QPushButton(self.verticalFrame1)
        self.btn_choose.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_choose.setObjectName("btn_choose")
        self.horizontalLayout_8.addWidget(self.btn_choose)
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalFrame1)
        self.pushButton_13.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_8.addWidget(self.pushButton_13)
        self.pushButton_15 = QtWidgets.QPushButton(self.verticalFrame1)
        self.pushButton_15.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_8.addWidget(self.pushButton_15)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalFrame1)
        self.pushButton_12.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_8.addWidget(self.pushButton_12)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addWidget(self.verticalFrame1)
        # self.widget = myVideoWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5.addWidget(self.widget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                   "color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sld_video = QtWidgets.QSlider(self.frame_2)
        self.sld_video.setStyleSheet("QSlider::groove:horizontal {\n"
                                     "border: 1px solid #4A708B;\n"
                                     "background: #C0C0C0;\n"
                                     "height: 5px;\n"
                                     "border-radius: 1px;\n"
                                     "padding-left:-1px;\n"
                                     "padding-right:-1px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::sub-page:horizontal {\n"
                                     "background: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
                                     "    stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
                                     "background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
                                     "    stop: 0 #5DCCFF, stop: 1 #1874CD);\n"
                                     "border: 1px solid #4A708B;\n"
                                     "height: 10px;\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::add-page:horizontal {\n"
                                     "background: #575757;\n"
                                     "border: 0px solid #777;\n"
                                     "height: 10px;\n"
                                     "border-radius: 2px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal \n"
                                     "{\n"
                                     "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, \n"
                                     "    stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));\n"
                                     "\n"
                                     "    width: 11px;\n"
                                     "    margin-top: -3px;\n"
                                     "    margin-bottom: -3px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal:hover {\n"
                                     "    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, \n"
                                     "    stop:0.778409 rgba(255, 255, 255, 255));\n"
                                     "\n"
                                     "    width: 11px;\n"
                                     "    margin-top: -3px;\n"
                                     "    margin-bottom: -3px;\n"
                                     "    border-radius: 5px;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::sub-page:horizontal:disabled {\n"
                                     "background: #00009C;\n"
                                     "border-color: #999;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::add-page:horizontal:disabled {\n"
                                     "background: #eee;\n"
                                     "border-color: #999;\n"
                                     "}\n"
                                     "\n"
                                     "QSlider::handle:horizontal:disabled {\n"
                                     "background: #eee;\n"
                                     "border: 1px solid #aaa;\n"
                                     "border-radius: 4px;\n"
                                     "}")
        self.sld_video.setPageStep(5)
        self.sld_video.setTracking(True)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.horizontalLayout_10.addWidget(self.sld_video)
        self.lab_video = QtWidgets.QLabel(self.frame_2)
        self.lab_video.setObjectName("lab_video")
        self.horizontalLayout_10.addWidget(self.lab_video)
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_10.addWidget(self.timeEdit)
        self.horizontalLayout_9.addWidget(self.frame_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setStyleSheet("background-color: rgb(43, 43, 43);\n"
                                   "color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_18.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_12.addWidget(self.pushButton_18)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_16.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_12.addWidget(self.pushButton_16)
        self.btn_play = QtWidgets.QPushButton(self.frame_4)
        self.btn_play.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout_12.addWidget(self.btn_play)
        self.btn_stop = QtWidgets.QPushButton(self.frame_4)
        self.btn_stop.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_12.addWidget(self.btn_stop)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_19.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                         "color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_12.addWidget(self.pushButton_19)
        self.horizontalLayout_13.addWidget(self.frame_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addWidget(self.frame)
        self.horizontalFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame1.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalFrame1.setMaximumSize(QtCore.QSize(16777215, 150))
        self.horizontalFrame1.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalFrame1)
        self.pushButton_8.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_10.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalFrame1)
        self.pushButton_9.setStyleSheet("background-color: rgb(129, 129, 129);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_10.addWidget(self.pushButton_9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.horizontalFrame1)
        self.scrollArea_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1052, 146))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.addWidget(self.scrollArea_2)
        self.verticalLayout_8.addWidget(self.horizontalFrame1)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "XX选择"))
        self.comboBox.setItemText(0, _translate("MainWindow", "全部"))
        self.comboBox.setItemText(1, _translate("MainWindow", "选项1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "选项2"))
        self.pushButton_7.setText(_translate("MainWindow", "设置"))
        self.label_2.setText(_translate("MainWindow", "文字"))
        self.pushButton.setText(_translate("MainWindow", "按钮1"))
        self.pushButton_2.setText(_translate("MainWindow", "按钮2"))
        self.label_3.setText(_translate("MainWindow", "可选择文件"))
        self.pushButton_3.setText(_translate("MainWindow", "按钮3"))
        self.pushButton_4.setText(_translate("MainWindow", "按钮4"))
        self.pushButton_5.setText(_translate("MainWindow", "按钮5"))
        self.pushButton_6.setText(_translate("MainWindow", "按钮6"))
        self.label_6.setText(_translate("MainWindow", "文件名"))
        self.pushButton_11.setText(_translate("MainWindow", "按钮9"))
        self.pushButton10.setText(_translate("MainWindow", "按钮10"))
        self.label_7.setText(_translate("MainWindow", "132321321321313"))
        self.btn_choose.setText(_translate("MainWindow", "选择文件"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.lab_video.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.btn_play.setText(_translate("MainWindow", "开始/暂停"))
        self.btn_stop.setText(_translate("MainWindow", "停止"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "按钮7"))
        self.pushButton_9.setText(_translate("MainWindow", "按钮8"))
