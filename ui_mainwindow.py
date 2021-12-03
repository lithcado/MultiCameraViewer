# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lizx.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Tang: splitter让多个模块平均分布
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        # Tang: 水平布局
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # Tang: 要把splitter套一个Layout才能显示出来
        self.verticalLayout.addWidget(self.splitter)

        # self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.graphicsView.setGeometry(QtCore.QRect(120, 230, 256, 192))
        # self.graphicsView.setObjectName("graphicsView")

        # self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit.setGeometry(QtCore.QRect(180, 100, 113, 20))
        # self.lineEdit.setObjectName("lineEdit")

        # self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # self.textEdit.setGeometry(QtCore.QRect(170, 140, 104, 71))
        # self.textEdit.setObjectName("textEdit")

        # self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        # self.spinBox.setGeometry(QtCore.QRect(340, 170, 42, 22))
        # self.spinBox.setObjectName("spinBox")

        # self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        # self.openGLWidget.setGeometry(QtCore.QRect(420, 230, 300, 200))
        # self.openGLWidget.setObjectName("openGLWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
