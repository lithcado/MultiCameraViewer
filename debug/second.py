# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets 
class Ui_Second(object):
  def setupUi(self, Ui_Second):
    Ui_Second.setObjectName("MainWindow")
    Ui_Second.resize(800, 600)
    # self.centralwidget = QtWidgets.QWidget(Ui_Second)
    # self.centralwidget.setObjectName("centralwidget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(Ui_Second)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.frame_2 = QtWidgets.QFrame(Ui_Second)
    self.frame_2.setStyleSheet("background-color:green;")
    self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame_2.setObjectName("frame_2")
    self.label = QtWidgets.QLabel(self.frame_2)
    self.label.setGeometry(QtCore.QRect(300, 180, 181, 81))
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setObjectName("label")
    self.horizontalLayout.addWidget(self.frame_2)
    # Ui_Second.setCentralWidget(self.centralwidget)
    # self.menubar = QtWidgets.QMenuBar(Ui_Second)
    # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
    # self.menubar.setObjectName("menubar")
    # Ui_Second.setMenuBar(self.menubar)
    # self.statusbar = QtWidgets.QStatusBar(Ui_Second)
    # self.statusbar.setObjectName("statusbar")
    # Ui_Second.setStatusBar(self.statusbar)
 
    self.retranslateUi(Ui_Second)
    QtCore.QMetaObject.connectSlotsByName(Ui_Second) 
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.label.setText(_translate("MainWindow", "这是界面2"))
 