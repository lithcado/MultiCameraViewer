# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 1036)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(350, 200, 111, 91))
        self.btn_pause.setObjectName("btn_pause")
        self.pic1 = QtWidgets.QLabel(self.centralwidget)
        self.pic1.setGeometry(QtCore.QRect(140, 390, 781, 491))
        self.pic1.setScaledContents(True)
        self.pic1.setObjectName("pic1")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(90, 200, 101, 81))
        self.btn_start.setObjectName("btn_start")
        self.btn_resolution_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resolution_set.setGeometry(QtCore.QRect(540, 310, 93, 28))
        self.btn_resolution_set.setObjectName("btn_resolution_set")
        self.btn_pan_flip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pan_flip.setGeometry(QtCore.QRect(860, 130, 101, 61))
        self.btn_pan_flip.setObjectName("btn_pan_flip")
        self.btn_rotate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rotate.setGeometry(QtCore.QRect(920, 290, 91, 71))
        self.btn_rotate.setObjectName("btn_rotate")
        self.input_width = QtWidgets.QLineEdit(self.centralwidget)
        self.input_width.setGeometry(QtCore.QRect(550, 179, 131, 31))
        self.input_width.setObjectName("input_width")
        self.input_height = QtWidgets.QLineEdit(self.centralwidget)
        self.input_height.setGeometry(QtCore.QRect(550, 219, 131, 31))
        self.input_height.setObjectName("input_height")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 190, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 230, 54, 12))
        self.label_2.setObjectName("label_2")
        self.input_degree = QtWidgets.QLineEdit(self.centralwidget)
        self.input_degree.setGeometry(QtCore.QRect(770, 310, 131, 41))
        self.input_degree.setObjectName("input_degree")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 270, 54, 12))
        self.label_3.setObjectName("label_3")
        self.input_fps = QtWidgets.QLineEdit(self.centralwidget)
        self.input_fps.setGeometry(QtCore.QRect(550, 260, 131, 31))
        self.input_fps.setObjectName("input_fps")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(220, 200, 101, 81))
        self.btn_close.setObjectName("btn_close")
        self.btn_tilt_flip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tilt_flip.setGeometry(QtCore.QRect(860, 210, 101, 61))
        self.btn_tilt_flip.setObjectName("btn_tilt_flip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_pause.setText(_translate("MainWindow", "暂停"))
        self.pic1.setText(_translate("MainWindow", "相机1画面"))
        self.btn_start.setText(_translate("MainWindow", "启动"))
        self.btn_resolution_set.setText(_translate("MainWindow", "设置分辨率"))
        self.btn_pan_flip.setText(_translate("MainWindow", "水平镜像"))
        self.btn_rotate.setText(_translate("MainWindow", "旋转"))
        self.label.setText(_translate("MainWindow", "宽"))
        self.label_2.setText(_translate("MainWindow", "高"))
        self.label_3.setText(_translate("MainWindow", "FPS"))
        self.btn_close.setText(_translate("MainWindow", "停止"))
        self.btn_tilt_flip.setText(_translate("MainWindow", "垂直镜像"))

