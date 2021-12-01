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
        
        self.cam = UvcCamera()
        self.window_num = window_num
        self.processor = None   # 帧
        self.cam_viewing_thread = None
        self.sample_time = 20
        self.get_parameter_list_finished = 0                    # 仅第一次初始化要读取相机参数

        self.ui.btn_start.clicked.connect(self.camera_open_thread)
        self.ui.btn_close.clicked.connect(self.camera_close)
        self.ui.btn_pause.clicked.connect(self.camera_pause)
        self.ui.btn_pan_flip.clicked.connect(self.pan_flip)
        self.ui.btn_tilt_flip.clicked.connect(self.tilt_flip)
        self.ui.btn_rotate.clicked.connect(self.rotate)
        self.ui.btn_sample_time.clicked.connect(self.sample_time_set)
        self.ui.btn_information_inquire.clicked.connect(self.imformation_inquire)
        self.ui.camera_parameter.currentIndexChanged.connect(self.cam_parameter_set)
        self.ui.format_list.currentIndexChanged.connect(self.video_format_set)
        # self.ui.btn_parameter_set.clicked.connect(self.resolution_set)


    # 信号和槽
    # uvc_camera里面start_grab()循环getframe，通过emit把图像发送到UiCameraViewer，然后显示到lable

    # 加个拍照功能

    # def updateBtn():
    #     if running:

    # closeEvent有问题啊
    def closeEvent(self, event):
        self.cam.camera_close()

    def camera_open_thread(self):
        self.cam_viewing_thread = QtCore.QThread()
        self.cam.moveToThread(self.cam_viewing_thread)
        self.cam_viewing_thread.started.connect(self.camera_open)
        self.cam_viewing_thread.start()

    def camera_open(self):
        self.cam.camera_init(self.window_num)  # cam_id
        self.ui.btn_start.setEnabled(False)     # 先不做，让孙，用状态标志位做
        if not self.get_parameter_list_finished:            # 第一次初始化读取相机可用参数
            self.cam.available_parameter_scan()
            for parameter in self.cam.parameter_list:
                self.ui.camera_parameter.addItem(str(parameter[0]) + '*' + str(parameter[1]) + '*' + str(parameter[2]))
                QtTest.QTest.qWait(1)
            self.get_parameter_list_finished = 1
        while self.cam.running_flag:
            QtTest.QTest.qWait(1)
            while (not self.cam.pause_flag) and self.cam.running_flag:      # 按下暂停或者停止时跳出这个循环
                self.cam.get_frame()

                self.processor = ImageProcess(self.cam.frame)
                if self.cam.pan_flip_flag:
                    self.processor.image_pan_flip()
                if self.cam.tilt_flip_flag:
                    self.processor.image_tilt_flip()
                self.processor.image_rotate(self.cam.rotate_degree,self.cam.scale_set)
                self.processor.cvimage_to_qimage()
                #self.frame.image_process(self.cam.pan_flip_flag, self.cam.tilt_flip_flag, self.cam.rotate_degree)  可以优化
                self.ui.pic1.setPixmap(QtGui.QPixmap(self.processor.image).scaled(self.ui.pic1.size(), QtCore.Qt.KeepAspectRatio))

                QtTest.QTest.qWait(int(self.sample_time))

    def camera_close(self):
        self.cam.running_flag = 0
        self.cam_viewing_thread.quit()
        self.cam.camera_close()
        self.ui.btn_start.setEnabled(True)

    def camera_pause(self):
        if self.cam.pause_flag:
            self.cam.pause_flag = 0
            self.ui.btn_pause.setFlat(False)
        else:
            self.cam.pause_flag = 1
            self.ui.btn_pause.setFlat(True)
        if self.cam.state_flag == 1:
            self.cam.state_flag = 2
        elif self.cam.state_flag == 2:
            self.cam.state_flag = 1

    # TODO: 新建self.processor执行图像处理操作
    def pan_flip(self):
        if self.cam.pan_flip_flag:
            self.cam.pan_flip_flag = 0
        else:
            self.cam.pan_flip_flag = 1

    def tilt_flip(self):
        if self.cam.tilt_flip_flag:
            self.cam.tilt_flip_flag = 0
        else:
            self.cam.tilt_flip_flag = 1

    def rotate(self):
        self.cam.rotate_degree = float(self.ui.input_degree.text())
        self.cam.scale_set = float(self.ui.input_scale.text())

    def cam_parameter_set(self):
        self.camera_close()
        parameter_id = self.ui.camera_parameter.currentIndex()
        # 改为cam的一个函数
        self.cam.width_set = float(self.cam.parameter_list[parameter_id][0])
        self.cam.height_set = float(self.cam.parameter_list[parameter_id][1])
        self.cam.frame_rate_set = float(self.cam.parameter_list[parameter_id][2])
        self.camera_open_thread()

    def sample_time_set(self):
        self.sample_time = self.ui.input_sample_time.text()

    def video_format_set(self):
        self.camera_close()
        parameter_id = self.ui.format_list.currentIndex()
        self.cam.format_id = int(parameter_id)
        self.camera_open_thread()

    def imformation_inquire(self):
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

