import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from ui_camera_viewer import Ui_Widget
from uvc_camera import UvcCamera
from image_process import ImageProcess
import cv2


class UiCameraViewer(QtWidgets.QMainWindow):
    def __init__(self, window_num) -> None:
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(MainWindow)
        self.ui.retranslateUi(MainWindow)


        self.window_num = window_num
        self.cam = UvcCamera()
        self.processor = ImageProcess()
        self.cam_viewing_thread = None

        self.cam.sig_get_frame_finished.connect(self.processor.image_process)
        self.processor.sig_image_process_finished.connect(self.image_show)

        self.ui.btn_open_camera.clicked.connect(self.camera_open)
        self.ui.btn_start_grab.clicked.connect(self.camera_grab_thread)
        self.ui.btn_close.clicked.connect(self.camera_close)
        self.ui.btn_stop_grab.clicked.connect(self.cam.stop_grab)
        #self.ui.btn_restart.clicked.connect(self.)
        self.ui.btn_pan_flip.clicked.connect(self.processor.set_horizontal_flip_flag)
        self.ui.btn_tilt_flip.clicked.connect(self.processor.set_vertical_flip_flag)
        self.ui.btn_rotate.clicked.connect(self.rotate)
        self.ui.btn_sample_time.clicked.connect(self.sample_time_set)
        #self.ui.btn_information_inquire.clicked.connect(self.information_inquire)
        self.ui.camera_parameter.currentIndexChanged.connect(self.cam_parameter_set)
        self.ui.format_list.currentIndexChanged.connect(self.video_format_set)


    # 信号和槽
    # uvc_camera里面start_grab()循环getframe，通过emit把图像发送到UiCameraViewer，然后显示到label      # from li: uvc_camera->image_process->uvc_camera->camera_widget

    # 加个拍照功能

    # def updateBtn():
    #     if running:
    def camera_grab_thread(self):
        self.cam_viewing_thread = QtCore.QThread()
        print(self.cam.moveToThread(self.cam_viewing_thread))
        print(self.cam_viewing_thread.started.connect(self.cam.start_grab))
        self.cam_viewing_thread.start()


    def camera_open(self):
        self.cam.camera_init(self.window_num)  # cam_id
        self.ui.btn_open_camera.setEnabled(False)     # 先不做，让孙，用状态标志位做
        if not self.cam.parameter_list_read_get():            # 第一次初始化读取相机可用参数
            for parameter in self.cam.parameter_list:
                self.ui.camera_parameter.addItem(str(parameter[0]) + '*' + str(parameter[1]) + '*' + str(parameter[2]))
                QtTest.QTest.qWait(1)
            self.cam.parameter_list_read_set(1)

    def image_show(self, qimage):
        self.ui.pic1.setPixmap(QtGui.QPixmap(qimage).scaled(self.ui.pic1.size(), QtCore.Qt.KeepAspectRatio))

    def camera_close(self):
        self.cam.stop_grab()

        self.cam_viewing_thread.quit()
        self.cam_viewing_thread.wait()

        QtTest.QTest.qWait(1000)
        print(self.cam_viewing_thread.isRunning())
        self.cam.camera_release()
        self.ui.btn_open_camera.setEnabled(True)

    def camera_pause(self):
        self.cam.stop_grab()

    def rotate(self):
        self.processor.set_rotate_degree(float(self.ui.input_degree.text()))
        self.processor.set_image_scale(float(self.ui.input_scale.text()))

    def sample_time_set(self):
        self.cam.sample_time_set(int(self.ui.input_sample_time.text()))

    def cam_parameter_set(self):
        self.camera_close()
        self.camera_open()
        parameter_id = self.ui.camera_parameter.currentIndex()-1
        self.cam.camera_parameter_set(float(self.cam.parameter_list[parameter_id][0]),
                                      float(self.cam.parameter_list[parameter_id][1]),
                                      float(self.cam.parameter_list[parameter_id][2]))
        self.cam.print_parameter()
        self.camera_grab_thread()

    def video_format_set(self):
        self.camera_close()
        self.camera_open()
        format_id = self.ui.format_list.currentIndex()
        self.cam.video_format_set(format_id)
        self.cam.video_format_get()
        self.camera_grab_thread()

    def information_inquire(self):
        text = self.cam.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.ui.information_output.setText(text)
        text = self.cam.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.ui.information_output.setText(text)

# only for test
def print_ok():
    print("OK")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiCameraViewer(0)
    MainWindow.show()
    sys.exit(app.exec_())

