# -*- coding: utf-8 -*-

# 相机类

from PyQt5 import QtCore,QtTest
import cv2
import numpy
from error_type import *

resolution_list = [(640, 480), (800, 600), (1024, 768), (1280, 960), (1600, 1200), (2048, 1536), (2592, 1944),
                        (1280, 720), (1920, 1080), (3840, 2160)]
fps_list = [30, 60]
format = [cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), cv2.VideoWriter_fourcc('Y', 'U', 'Y', '2')]


class UvcCamera(QtCore.QObject):
    sig_get_frame_finished = QtCore.pyqtSignal(numpy.ndarray)

    def __init__(self):
        super().__init__()
        self.cam_name = 0
        self._camera_state = 0         # 0: 关闭 1: 开启 2：grab中 -1:未正常关闭

        self._sample_time = 20          # 窗口采样时间
        self._parameter_scanned_flag = 0      # 0: 初次打开未扫描 1：已扫描
        self._parameter_list_read_flag = 0
        self.cap = None
        self.parameter_list = []

    def camera_init(self, cam_name):
        self.cam_name = cam_name
        self.cap = cv2.VideoCapture(cam_name, cv2.CAP_MSMF)
        if self.cap.isOpened():
            self._camera_state = 1
            self.available_parameter_scan()
        else:
            print("Camera " + str(self.cam_name) + " open failed!")      # 补充
            raise InitialError
            self.camera_release()

    def parameter_list_read_get(self):
        return self._parameter_list_read_flag

    def parameter_list_read_set(self, flag):
        self._parameter_list_read_flag = flag

    def available_parameter_scan(self):
        if not self._parameter_scanned_flag:
            for resolution in resolution_list:
                self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
                self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
                QtTest.QTest.qWait(1)
                for fps in fps_list:
                    self.cap.set(cv2.CAP_PROP_FPS, fps)
                    real_width, real_height, real_fps = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), self.cap.get(
                        cv2.CAP_PROP_FRAME_HEIGHT), self.cap.get(cv2.CAP_PROP_FPS)
                    if real_width == resolution[0] and real_height == resolution[1] and real_fps == fps:
                        self.parameter_list.append((real_width, real_height, real_fps))
                    QtTest.QTest.qWait(1)
            self._parameter_scanned_flag = 1
            if not self.parameter_list:
                raise ParameterListError
                self.camera_release()

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Camera " + str(self.cam_name) + " grab frame failed!")
            raise GetFrameError
            self.camera_release()
        return frame

    def start_grab(self):
        self._camera_state = 2
        while self._camera_state == 2:
            frame = self.get_frame()
            self.sig_get_frame_finished.emit(frame)
            QtTest.QTest.qWait(int(self._sample_time))


    def stop_grab(self):
        self._camera_state = 1

    def camera_release(self):
        self.stop_grab()
        self.cap.release()
        if self.cap.isOpened():
            self._camera_state = -1
            raise CameraReleaseError
        else:
            self._camera_state = 0

    def camera_parameter_set(self, width_set, height_set, fps_set):
        flag1 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width_set)
        flag2 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height_set)
        flag3 = self.cap.set(cv2.CAP_PROP_FPS, fps_set)
        if not (flag1 and flag2 and flag3):
            print("Camera " + str(self.cam_name) + " parameter set failed!")
            raise ParameterSetError

    def video_format_set(self, format_id):
        flag = self.cap.set(cv2.CAP_PROP_FOURCC, format[format_id])
        if flag:
            print("Camera " + str(self.cam_name) + " format set OK!")       # for test
            print(decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC)))         # for test
            return True
        else:
            print("Camera " + str(self.cam_name) + " format set failed!")   # for test
            print(decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC)))         # for test
            return False

    def camera_state_get(self):
        return self._camera_state

    def camera_parameter_get(self):
        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        return width, height, fps

    def video_format_get(self):
        video_format = decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC))
        print(video_format)
        return video_format

    # only for test
    def print_parameter(self):
        print(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(self.cap.get(cv2.CAP_PROP_FPS))

    def sample_time_set(self, sample_time):
        self._sample_time = sample_time

def decode_fourcc(cc):
    return "".join([chr((int(cc) >> 8 * i) & 0xFF) for i in range(4)])

# only for test


def print_ok():
    print("OK")

if __name__ == '__main__':
    cam1 = UvcCamera()
    cam1.camera_init(0)
    cam1.start_grab()
    cam1.stop_grab()
    cam1.camera_release()
    cam1.camera_init(0)
    cam1.start_grab()

    print(cam1.camera_state_get())


