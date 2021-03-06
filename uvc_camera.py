# -*- coding: utf-8 -*-

# 相机类

from PyQt5 import QtCore,QtTest
import cv2
import numpy
from error_type import *
import utils

resolution_list = [(640, 480), (800, 600), (1024, 768), (1280, 960), (1600, 1200), (2048, 1536), (2592, 1944),
                        (1280, 720), (1920, 1080), (3840, 2160)]

format = [cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), cv2.VideoWriter_fourcc('Y', 'U', 'Y', '2')]


class UvcCamera(QtCore.QObject):
    sig_get_frame_finished = QtCore.pyqtSignal(numpy.ndarray)

    def __init__(self):
        super().__init__()
        self.cam_name = 0               # 相机编号 VideoCapture(cam_name)
        self._camera_state = 0         # 0: 关闭 1: 开启 2：grab中 -1:未正常关闭
        self._sample_time = 20          # 窗口采样时间 已废除
        self._parameter_scanned_flag = 0      # 0: 初次打开未扫描 1：已扫描
        self._parameter_list_read_flag = 0      # 1：界面中已经读到相机参数

        self.cap = None                         # 相机流
        self.parameter_list = []                # 可用参数列表

    def camera_init(self, cam_name):
        self.cam_name = cam_name
        self.cap = cv2.VideoCapture(cam_name, cv2.CAP_DSHOW)
        if self.cap.isOpened():
            self._camera_state = 1
            self.available_parameter_scan()
        else:
            print("Camera " + str(self.cam_name) + " open failed!")      # 补充
            #raise InitialError
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
                real_width, real_height = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                if real_width == resolution[0] and real_height == resolution[1]:
                    self.parameter_list.append((real_width, real_height))
                QtTest.QTest.qWait(1)
            self._parameter_scanned_flag = 1
            if not self.parameter_list:
                #raise ParameterListError
                self.camera_release()
            else:
                self.camera_parameter_set(float(self.parameter_list[0][0]),float(self.parameter_list[0][1]), 0)

    def frame_get(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Camera " + str(self.cam_name) + " grab frame failed!")
            #raise GetFrameError
            self.camera_release()
        return frame

    def start_grab(self):
        self._camera_state = 2
        while self._camera_state == 2:
            frame = self.frame_get()
            self.sig_get_frame_finished.emit(frame)
            QtTest.QTest.qWait(int(self._sample_time))

    def stop_grab(self):
        self._camera_state = 1

    def camera_release(self):
        self.stop_grab()
        self.cap.release()
        if self.cap.isOpened():
            self._camera_state = -1
            #raise CameraReleaseError
        else:
            self._camera_state = 0

    def camera_parameter_set(self, width_set, height_set, format_id):
        flag1 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width_set)
        flag2 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height_set)
        flag3 = self.cap.set(cv2.CAP_PROP_FOURCC, format[format_id])
        if not (flag1 and flag2 and flag3):
            print("Camera " + str(self.cam_name) + " parameter set failed!")
            #raise ParameterSetError
        print(utils.decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC)))  # for test

    def camera_state_get(self):
        return self._camera_state

    def camera_parameter_get(self):
        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return width, height

    def video_format_get(self):
        video_format = utils.decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC))
        print(video_format)
        return video_format
    '''
    def sample_time_set(self, sample_time):
        self._sample_time = sample_time
    '''


if __name__ == '__main__':
    cam1 = UvcCamera()
    cam1.camera_init(0)
    cam1.start_grab()
    cam1.stop_grab()
    cam1.camera_release()
    cam1.camera_init(0)
    cam1.start_grab()

    print(cam1.camera_state_get())


