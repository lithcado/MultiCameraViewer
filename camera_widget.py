import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from ui_camera_viewer import Ui_Widget
from uvc_camera import UvcCamera
from image_process import ImageProcess
import cv2


class UiCameraViewer(QtWidgets.QWidget):
    def __init__(self, window_num) -> None:
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.window_num = window_num             # 窗口名字
        self.cam = UvcCamera()
        self.processor = ImageProcess()
        self.cam_grab_thread = None             # 图像抓取线程

        self.cam.sig_get_frame_finished.connect(self.processor.image_process)
        self.processor.sig_image_process_finished.connect(self.image_show)

        self.ui.btn_open_camera.clicked.connect(self.btn_camera_open)
        self.ui.btn_start_grab.clicked.connect(self.btn_start_grab)
        self.ui.btn_close_camera.clicked.connect(self.btn_camera_close)
        self.ui.btn_stop_grab.clicked.connect(self.btn_stop_grab)
        self.ui.btn_horizontal_flip.clicked.connect(self.btn_horizontal_flip)
        self.ui.btn_vertical_flip.clicked.connect(self.btn_vertical_flip)
        self.ui.btn_clockwise_90.clicked.connect(self.btn_clockwise_rotate)
        self.ui.btn_counterclockwise_90.clicked.connect(self.btn_counterclockwise_rotate)
        # self.ui.btn_sample_time.clicked.connect(self.sample_time_set)
        self.ui.btn_parameter_set.clicked.connect(self.btn_cam_parameter_set)

    # 信号和槽
    # uvc_camera里面start_grab()循环getframe，通过emit把图像发送到UiCameraViewer，然后显示到label
    # from li: uvc_camera->image_process->uvc_camera->camera_widget
    # 加个拍照功能
    # def updateBtn():
    #     if running:

    def btn_start_grab(self):
        if not self.cam_grab_thread:
            self.cam_grab_thread = QtCore.QThread()
        elif self.cam_grab_thread.isRunning():
            self.cam_grab_thread.quit()
            self.cam_grab_thread.wait()
        self.cam.moveToThread(self.cam_grab_thread)
        self.cam_grab_thread.started.connect(self.cam.start_grab)
        self.cam_grab_thread.start()
        self.ui.btn_start_grab.setEnabled(False)

    def btn_camera_open(self):
        self.cam.camera_init(self.window_num)  # cam_id
        if self.cam.camera_state_get():
            self.ui.btn_open_camera.setEnabled(False)     # 先不做，让孙，用状态标志位做
            if not self.cam.parameter_list_read_get():            # 第一次初始化读取相机可用参数
                for parameter in self.cam.parameter_list:
                    self.ui.camera_parameter.addItem(str(parameter[0]) + ' * ' + str(parameter[1]))
                    QtTest.QTest.qWait(1)
                self.cam.parameter_list_read_set(1)

    def image_show(self, qimage):
        self.ui.image_window.setPixmap(QtGui.QPixmap(qimage).scaled(self.ui.image_window.size(), QtCore.Qt.KeepAspectRatio))

    def btn_camera_close(self):
        self.cam.stop_grab()
        self.cam_grab_thread.quit()
        while self.cam_grab_thread.isRunning():
            QtTest.QTest.qWait(1)
            self.cam.stop_grab()
        self.cam_grab_thread.wait()
        self.cam.camera_release()
        self.ui.btn_open_camera.setEnabled(True)
        self.ui.btn_start_grab.setEnabled(True)

    def btn_stop_grab(self):
        self.cam.stop_grab()
        self.cam_grab_thread.quit()
        while self.cam_grab_thread.isRunning():
            QtTest.QTest.qWait(1)
            self.cam.stop_grab()
        self.ui.btn_start_grab.setEnabled(True)

    def btn_horizontal_flip(self):
        self.processor.horizontal_flip_flag_set()

    def btn_vertical_flip(self):
        self.processor.vertical_flip_flag_set()

    def btn_clockwise_rotate(self):
        self.processor.degree_plus_90()

    def btn_counterclockwise_rotate(self):
        self.processor.degree_minus_90()

    # self.processor.set_image_scale(float(self.ui.input_scale.text()))

    '''
    def sample_time_set(self):
        self.cam.sample_time_set(int(self.ui.input_sample_time.text()))
    '''
    def btn_cam_parameter_set(self):
        self.btn_camera_close()
        self.btn_camera_open()
        parameter_id = self.ui.camera_parameter.currentIndex()-1
        format_id = self.ui.format_list.currentIndex()
        self.cam.camera_parameter_set(float(self.cam.parameter_list[parameter_id][0]),
                                      float(self.cam.parameter_list[parameter_id][1]), format_id)
        self.btn_start_grab()

    '''
    def information_inquire(self):
        text = self.cam.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.ui.information_output.setText(text)
        text = self.cam.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.ui.information_output.setText(text)
    '''


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = UiCameraViewer(0)
    ui.show()
    sys.exit(app.exec_())

