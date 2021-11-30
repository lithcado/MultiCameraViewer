# -*- coding: utf-8 -*-

# 相机类

from PyQt5 import QtCore

import cv2
import time


class UvcCamera(object):
    def __init__(self, cam_name):
        self.state_flag = 1
        self.cam_name = cam_name
        self.cap = cv2.VideoCapture(cam_name)
        if not self.cap.isOpened():
            print("Camera" + self.cam_name + "open failed!")
            self.state_flag = 0
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)

    def get_frame(self):
        ret, self.frame = self.cap.read()
        if ret == False:
            print("Camera" + self.cam_name + "grab frame failed!")
            self.state_flag = 0

    def camera_parameter_renew(self):
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.frame_rate = self.cap.get(cv2.CAP_PROP_FPS)
        if  self.width == -1 or self.height == -1 or self.frame_rate == -1:
            print("Camera" + self.cam_name + "parameter get failed!")
            self.state_flag = 0

    def camera_parameter_set(self, width , height , frame_rate):
        flag1 = self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        flag2 = self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        flag3 = self.cap.set(cv2.CAP_PROP_FPS, frame_rate)
        if not (flag1 and flag2 and flag3):
            print("Camera" + self.cam_name + "parameter set failed!")
            self.state_flag = 0
        self.camera_parameter_renew()

    def camera_close(self):
        if not self.cap.isOpened():
            self.state_flag = 0
        self.cap.release()
        cv2.destroyAllWindows()

    #only for test
    def print_parameter(self):
        print(self.width)
        print(self.height)
        print(self.frame_rate)


if __name__ == '__main__':
    cam1 = UvcCamera(0)
    cam1.print_parameter()
    cam1.camera_parameter_set(800, 600, 30)
    cam1.print_parameter()
    print(cam1.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cam1.state_flag)
    while True:
        time.sleep(0.5)
        frame = cam1.get_frame()
        cv2.imshow("frame", frame)
        if chr(cv2.waitKey(1) & 255) == 'q':
            break
    print(cam1.state_flag)
    cam1.camera_close()


