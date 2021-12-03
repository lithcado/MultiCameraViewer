# -*- coding: utf-8 -*- 
# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from first import Ui_First
from second import Ui_Second
 
class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(800, 600)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
    self.horizontalLayout.setObjectName("horizontalLayout")
    self.splitter = QtWidgets.QSplitter(self.centralwidget)
    self.splitter.setOrientation(QtCore.Qt.Horizontal)
    self.splitter.setObjectName("splitter")
    self.frame = QtWidgets.QFrame(self.splitter)
    self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
    self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame.setObjectName("frame")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
    self.verticalLayout.setObjectName("verticalLayout")
    self.pushButton = QtWidgets.QPushButton(self.frame)
    self.pushButton.setObjectName("pushButton")
    self.verticalLayout.addWidget(self.pushButton)
    self.pushButton_2 = QtWidgets.QPushButton(self.frame)
    self.pushButton_2.setObjectName("pushButton_2")
    self.verticalLayout.addWidget(self.pushButton_2)
 
    # 这里注释掉，因为不需要frame2。当初在qt 里面设计这个frame2的原因是为了占位，不至于到时候布局出现错乱。
    # self.frame_2 = QtWidgets.QFrame(self.splitter)
    # self.frame_2.setStyleSheet("background-color:white;")
    # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    # self.frame_2.setObjectName("frame_2")
 
    self.horizontalLayout.addWidget(self.splitter)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
    self.menubar.setObjectName("menubar")
    MainWindow.setMenuBar(self.menubar)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)
 
    # 初始化两个对象，并把 first对象 加入到 splitter 中
    self.first = First()
    self.second = Second()
    self.splitter.addWidget(self.first)
 
    self.pushButton.clicked.connect(lambda :self.change(self.pushButton.objectName()))
    self.pushButton_2.clicked.connect(lambda :self.change(self.pushButton_2.objectName()))
 
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
 
  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.pushButton.setText(_translate("MainWindow", "界面1"))
    self.pushButton_2.setText(_translate("MainWindow", "界面2"))
 
  def change(self,name):
    if name == "pushButton":
      self.splitter.widget(1).setParent(None)
      self.splitter.insertWidget(1, self.first)
 
    if name == "pushButton_2":
      self.splitter.widget(1).setParent(None)
      self.splitter.insertWidget(1, self.second)
 
class First(QWidget, Ui_First):
  def __init__(self):
    super(First,self).__init__()
    # 子窗口初始化时实现子窗口布局
    self.setupUi(self)
 
    # 设置子窗体最小尺寸
    self.setMinimumWidth(30)
    self.setMinimumHeight(30)
 
class Second(QWidget, Ui_Second):
  def __init__(self):
    super(Second,self).__init__()
    self.setupUi(self)
    self.setMinimumWidth(30)
    self.setMinimumHeight(30)
 
if __name__ == '__main__':
  import sys
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  ui = Ui_MainWindow()
  ui.setupUi(MainWindow)
  MainWindow.show()
  sys.exit(app.exec_())