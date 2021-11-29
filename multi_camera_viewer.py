# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_mainwindow import Ui_MainWindow

class MultiCameraViewer(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        # self.ui.opencamera.clicked.connect(self.open_camera)
        # self.show()
    
    # def open_camera():
    #     camera = 
    #     analyz_thread=QThread()
    #     camera.moveToThread(self.analyz_thread)
    #     self.analyz_thread.started.connect(self.analyze.analyz_work)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWindow = Calc24()
#     mainWindow.show()
#     sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    multi_cam_viewer = MultiCameraViewer()
    multi_cam_viewer.show()
    sys.exit(app.exec_())