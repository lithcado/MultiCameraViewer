
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from ui_camera_viewer import Ui_Widget
from uvc_camera import UvcCamera
import cv2
import time
from image_process import ImageProcess


class UiCameraViewer(QtWidgets.QMainWindow):
    def __init__(self, window_num) -> None:
        super().__init__()
        self.frame = None
        self.window_num = window_num
        self.ui = Ui_Widget()
        self.ui.setupUi(MainWindow)
        self.ui.retranslateUi(MainWindow)
        self.cam = UvcCamera()
        self.cam_viewing_thread = None
        self.ui.btn_resolution_set.clicked.connect(self.resolution_set)
        self.ui.btn_start.clicked.connect(self.camera_open_thread)
        self.ui.btn_close.clicked.connect(self.camera_close)


    def camera_open_thread(self):
        self.cam_viewing_thread = QtCore.QThread()
        self.cam.moveToThread(self.cam_viewing_thread)
        self.cam_viewing_thread.started.connect(self.camera_open)
        self.cam_viewing_thread.start()


    def test(self):
        while True:
            img = cv2.imread('./test_image.jpg')
            frame=ImageProcess(img)
            frame.cvimage_to_qimage()
            self.ui.pic1.setPixmap(QtGui.QPixmap(frame.image))
            time.sleep(.1)


    def camera_open(self):
        self.cam.camera_init(self.window_num)
        while self.cam.running_flag == 1:
            # frame = cam1.get_frame()
            self.cam.get_frame()
            self.frame = ImageProcess(self.cam.frame)
            self.frame.cvimage_to_qimage()
            self.ui.pic1.setPixmap(QtGui.QPixmap(self.frame.image))
            QtTest.QTest.qWait(100)

    def camera_close(self):
        self.cam.running_flag = 0
        self.cam_viewing_thread.quit()
        self.cam.camera_close()

    def resolution_set(self):
        self.cam.camera_parameter_set(float(self.ui.input_width.text()), float(self.ui.input_height.text()), float(self.ui.input_fps.text()))


'''
    def init_camera(self):
        self.cam_initial_thread = QtCore.QThread()
        self.cam.moveToThread(self.cam_initial_thread)
        self.cam_initial_thread.started.connect(self.cam.print_parameter)
        self.cam_initial_thread.start()
'''



# only for test
def print_ok():
    print("OK")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiCameraViewer(0)
    MainWindow.show()
    sys.exit(app.exec_())

