# -*- coding: utf-8 -*-

# 相机类

from PyQt5 import QtCore,QtTest

import cv2
import time

resolution_list = [(640, 480), (800, 600), (1024, 768), (1280, 960), (1600, 1200), (2048, 1536), (2592, 1944),
                        (1280, 720), (1920, 1080), (3840, 2160)]
fps_list = [30, 60]
format = [cv2.VideoWriter_fourcc('Y', 'U', 'Y', '2'),cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')]


class UvcCamera(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.cam_name = 0
        self.state_flag = 0         # 0: 停止 1: 工作 2: 暂停
        self.running_flag = 0
        self.pause_flag = 0
        self.pan_flip_flag = 0
        self.tilt_flip_flag = 0
        self.rotate_degree = 0
        self.scale_set = 1          # not used
        self.width_set = 640
        self.height_set = 480
        self.frame_rate_set = 30
        self.format_id = 0
        self.frame = None
        self.cap = None
        self.parameter_list = []

    def camera_init(self, cam_name):
        self.state_flag = 1
        self.running_flag = 1
        self.cam_name = cam_name
        self.cap = cv2.VideoCapture(cam_name, cv2.CAP_MSMF)
        self.camera_parameter_set()
        self.video_format_set()
        if not self.cap.isOpened():
            print("Camera " + str(self.cam_name) + " open failed!")
            self.state_flag = 0

    def available_parameter_scan(self):
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

    def get_frame(self):
        ret, self.frame = self.cap.read()
        if not ret:
            print("Camera " + str(self.cam_name) + " grab frame failed!")
            self.state_flag = 0

    def camera_parameter_set(self):
        flag1 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width_set)
        flag2 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height_set)
        flag3 = self.cap.set(cv2.CAP_PROP_FPS, self.frame_rate_set)
        if not (flag1 and flag2 and flag3):
            print("Camera " + str(self.cam_name) + " parameter set failed!")
            self.state_flag = 0

    def video_format_set(self):
        flag = self.cap.set(cv2.CAP_PROP_FOURCC, format[self.format_id])
        if not flag:
            print("Camera " + str(self.cam_name) + " format set failed!")
            print(decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC)))
            self.state_flag = 0
        else:
            print("Camera " + str(self.cam_name) + " format set OK!")
            print(decode_fourcc(self.cap.get(cv2.CAP_PROP_FOURCC)))

    def camera_close(self):
        if not self.cap.isOpened():
            self.state_flag = 0
        self.cap.release()
        cv2.destroyAllWindows()

    # only for test
    def print_parameter(self):
        print(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(self.cap.get(cv2.CAP_PROP_FPS))

# only for test


def print_ok():
    print("OK")


def decode_fourcc(cc):
    return "".join([chr((int(cc) >> 8 * i) & 0xFF) for i in range(4)])


if __name__ == '__main__':
    cam1 = UvcCamera()
    cam1.camera_init(0)
    #print(cam1.cap.set(cv2.CAP_PROP_FOURCC, format[1]))
    print(decode_fourcc(cam1.cap.get(cv2.CAP_PROP_FOURCC)))
    cam1.camera_close()


