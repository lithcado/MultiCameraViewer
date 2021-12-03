# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_mainwindow import Ui_MainWindow

from camera_widget import UiCameraViewer


class MultiCameraViewer(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # Tang: 加入第一个窗口
        self.left_camera = UiCameraViewer(0)
        self.ui.splitter.addWidget(self.left_camera)

        # Tang: 点击增加相机按钮后加入第二个窗口，按钮待实现
        self.right_camra = UiCameraViewer(0)
        self.ui.splitter.addWidget(self.right_camra)
        
        # self.show()
    
    # def open_camera():
    #     camera = uvc_camera()
    #     camera.analyze_thread=QThread()
    #     camera.moveToThread(self.analyze_thread)
    #     self.analyze_thread.started.connect(self.analyze.analyze_work)




# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = Calc24()
#     mainWindow.show()
#     sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    multi_cam_viewer = MultiCameraViewer()
    multi_cam_viewer.show()
    sys.exit(app.exec_())