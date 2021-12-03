# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_camera_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):

    def setupUi(self, CameraWidget):
        CameraWidget.setObjectName("Form")
        CameraWidget.resize(561, 380)
        self.btn_open_camera = QtWidgets.QPushButton(CameraWidget)
        self.btn_open_camera.setGeometry(QtCore.QRect(440, 130, 81, 41))
        self.btn_open_camera.setObjectName("btn_open_camera")
        self.btn_stop_grab = QtWidgets.QPushButton(CameraWidget)
        self.btn_stop_grab.setGeometry(QtCore.QRect(440, 310, 81, 41))
        self.btn_stop_grab.setObjectName("btn_stop_grab")
        self.format_list = QtWidgets.QComboBox(CameraWidget)
        self.format_list.setGeometry(QtCore.QRect(90, 10, 71, 31))
        self.format_list.setObjectName("format_list")
        self.format_list.addItem("")
        self.format_list.addItem("")
        self.image_window = QtWidgets.QLabel(CameraWidget)
        self.image_window.setGeometry(QtCore.QRect(80, 120, 321, 241))
        self.image_window.setScaledContents(False)
        self.image_window.setObjectName("image_window")
        self.label_2 = QtWidgets.QLabel(CameraWidget)
        self.label_2.setGeometry(QtCore.QRect(11, 9, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_close_camera = QtWidgets.QPushButton(CameraWidget)
        self.btn_close_camera.setGeometry(QtCore.QRect(440, 190, 81, 41))
        self.btn_close_camera.setObjectName("btn_close_camera")
        self.btn_start_grab = QtWidgets.QPushButton(CameraWidget)
        self.btn_start_grab.setGeometry(QtCore.QRect(440, 250, 81, 41))
        self.btn_start_grab.setObjectName("btn_start_grab")
        self.label = QtWidgets.QLabel(CameraWidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.camera_parameter = QtWidgets.QComboBox(CameraWidget)
        self.camera_parameter.setGeometry(QtCore.QRect(280, 10, 141, 31))
        self.camera_parameter.setObjectName("camera_parameter")
        self.camera_parameter.addItem("")
        self.btn_parameter_set = QtWidgets.QPushButton(CameraWidget)
        self.btn_parameter_set.setGeometry(QtCore.QRect(440, 10, 81, 41))
        self.btn_parameter_set.setObjectName("btn_parameter_set")
        self.btn_counterclockwise_90 = QtWidgets.QPushButton(CameraWidget)
        self.btn_counterclockwise_90.setGeometry(QtCore.QRect(30, 70, 71, 31))
        self.btn_counterclockwise_90.setObjectName("btn_counterclockwise_90")
        self.btn_clockwise_90 = QtWidgets.QPushButton(CameraWidget)
        self.btn_clockwise_90.setGeometry(QtCore.QRect(140, 70, 71, 31))
        self.btn_clockwise_90.setObjectName("btn_clockwise_90")
        self.btn_horizontal_flip = QtWidgets.QPushButton(CameraWidget)
        self.btn_horizontal_flip.setGeometry(QtCore.QRect(260, 70, 71, 31))
        self.btn_horizontal_flip.setObjectName("btn_horizontal_flip")
        self.btn_vertical_flip = QtWidgets.QPushButton(CameraWidget)
        self.btn_vertical_flip.setGeometry(QtCore.QRect(370, 70, 71, 31))
        self.btn_vertical_flip.setObjectName("btn_vertical_flip")
        self.retranslateUi(CameraWidget)
        QtCore.QMetaObject.connectSlotsByName(CameraWidget)

    def retranslateUi(self, CameraWidget):
        _translate = QtCore.QCoreApplication.translate
        CameraWidget.setWindowTitle(_translate("Form", "Form"))
        self.btn_open_camera.setText(_translate("Form", "启动"))
        self.btn_stop_grab.setText(_translate("Form", "暂停"))
        self.format_list.setItemText(0, _translate("Form", "MJPG"))
        self.format_list.setItemText(1, _translate("Form", "YUY2"))
        self.image_window.setText(_translate("Form", "相机1画面"))
        self.label_2.setText(_translate("Form", "传输格式"))
        self.btn_close_camera.setText(_translate("Form", "停止"))
        self.btn_start_grab.setText(_translate("Form", "开始抓取"))
        self.label.setText(_translate("Form", "宽*高*FPS"))
        self.camera_parameter.setItemText(0, _translate("Form", "当前为默认参数"))
        self.btn_parameter_set.setText(_translate("Form", "设置参数"))
        self.btn_counterclockwise_90.setText(_translate("Form", "左转90度"))
        self.btn_clockwise_90.setText(_translate("Form", "右转90度"))
        self.btn_horizontal_flip.setText(_translate("Form", "水平镜像"))
        self.btn_vertical_flip.setText(_translate("Form", "垂直镜像"))

