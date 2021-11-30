# -*- coding: utf-8 -*-

# 相机类

from PyQt5 import QtCore

import cv2
import time


class UvcCamera(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.state_flag = 0
        self.running_flag = 0
        self.cam_name = 0
        self.width = 640
        self.height = 480
        self.frame_rate = 30
        self.frame = None
        self.cap = None

    def camera_init(self, cam_name):
        self.state_flag = 1
        self.running_flag = 1
        self.cam_name = cam_name
        self.cap = cv2.VideoCapture(cam_name)
        if not self.cap.isOpened():
            print("Camera " + str(self.cam_name) + " open failed!")
            self.state_flag = 0
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)


    def get_frame(self):
        ret, self.frame = self.cap.read()
        if ret == False:
            print("Camera " + str(self.cam_name) + " grab frame failed!")
            self.state_flag = 0

    def camera_parameter_renew(self):
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)
        if  self.width == -1 or self.height == -1 or self.frame_rate == -1:
            print("Camera " + str(self.cam_name) + " parameter get failed!")
            self.state_flag = 0

    def camera_parameter_set(self, width, height, frame_rate):
        flag1 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        flag2 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        flag3 = self.cap.set(cv2.CAP_PROP_FPS, frame_rate)
        if not (flag1 and flag2 and flag3):
            print("Camera " + str(self.cam_name) + " parameter set failed!")
            self.state_flag = 0
        self.camera_parameter_renew()

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
        self.end_flag=1;


# only for test
def print_ok():
    print("OK")


if __name__ == '__main__':
    cam1 = UvcCamera()

    cam1.camera_init(0)


    while cam1.running_flag == 1:
        time.sleep(0.1)
        #frame = cam1.get_frame()
        cam1.get_frame()
        cv2.namedWindow("frame")
        cv2.imshow("frame", cam1.frame)

        if chr(cv2.waitKey(1) & 255) == 'q':
            break
    print(cam1.state_flag)
    cam1.camera_close()


