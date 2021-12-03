# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets 
class Ui_First(object):
  def setupUi(self, Ui_First):
    Ui_First.setObjectName("MainWindow")
    Ui_First.resize(800, 600)
    # self.centralwidget = QtWidgets.QWidget(Ui_First)
    # self.centralwidget.setObjectName("centralwidget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(Ui_First)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.frame_2 = QtWidgets.QFrame(Ui_First)
    self.frame_2.setStyleSheet("background-color:white;")
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
    # Ui_First.setCentralWidget(self.centralwidget)
    # self.menubar = QtWidgets.QMenuBar(Ui_First)
    # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
    # self.menubar.setObjectName("menubar")
    # Ui_First.setMenuBar(self.menubar)
    # self.statusbar = QtWidgets.QStatusBar(Ui_First)
    # self.statusbar.setObjectName("statusbar")
    # Ui_First.setStatusBar(self.statusbar)
 
    self.retranslateUi(Ui_First)
    QtCore.QMetaObject.connectSlotsByName(Ui_First)
 
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.label.setText(_translate("MainWindow", "这是界面1"))
 