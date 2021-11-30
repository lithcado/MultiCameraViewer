# -*- coding: utf-8 -*-

# 相机类

from PyQt5 import QtCore,QtTest

import cv2
import time


class UvcCamera(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.cam_name = 0
        self.state_flag = 0
        self.running_flag = 0
        self.pause_flag = 0
        self.pan_flip_flag = 0
        self.tilt_flip_flag = 0
        self.rotate_degree = 0
        self.width_set = 640
        self.height_set = 480
        self.frame_rate_set = 30
        self.frame = None
        self.cap = None

    def camera_init(self, cam_name):
        self.state_flag = 1
        self.running_flag = 1
        self.cam_name = cam_name
        self.cap = cv2.VideoCapture(cam_name)
        self.camera_parameter_set()
        if not self.cap.isOpened():
            print("Camera " + str(self.cam_name) + " open failed!")
            self.state_flag = 0

    def get_frame(self):
        ret, self.frame = self.cap.read()
        if ret == False:
            print("Camera " + str(self.cam_name) + " grab frame failed!")
            self.state_flag = 0

    def camera_parameter_set(self):
        flag1 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width_set)
        flag2 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height_set)
        flag3 = self.cap.set(cv2.CAP_PROP_FPS, self.frame_rate_set)
        if not (flag1 and flag2 and flag3):
            print("Camera " + str(self.cam_name) + " parameter set failed!")
            self.state_flag = 0

    def camera_close(self):
        if not self.cap.isOpened():
            self.state_flag = 0
        self.cap.release()
        cv2.destroyAllWindows()

    #only for test
    def print_parameter(self):
        print(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(self.cap.get(cv2.CAP_PROP_FPS))



# only for test
def print_ok():
    print("OK")


if __name__ == '__main__':
    cam1 = UvcCamera()
    cam1.camera_init(0)
    while cam1.running_flag == 1:
        #frame = cam1.get_frame()
        cam1.get_frame()
        cv2.namedWindow("frame")
        cv2.imshow("frame", cam1.frame)
        print( cam1.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920))
        cv2.waitKey(0)
        time.sleep(0.5)

    cam1.camera_close()


