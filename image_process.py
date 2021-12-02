import cv2
from PyQt5 import QtGui, QtTest, QtCore


class ImageProcess(QtCore.QObject):
    sig_image_process_finished = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self):
        super().__init__()
        self._horizontal_flip_flag = 0        # 成员变量私有，通过get函数获取
        self._vertical_flip_flag = 0
        self._rotate_degree = 0
        self._image_scale = 1

    def set_horizontal_flip_flag(self):
        if self._horizontal_flip_flag:
            self._horizontal_flip_flag = 0
        else:
            self._horizontal_flip_flag = 1

    def set_vertical_flip_flag(self):
        if self._vertical_flip_flag:
            self._vertical_flip_flag = 0
        else:
            self._vertical_flip_flag = 1

    def set_rotate_degree(self, degree):
        self._rotate_degree = -degree

    def set_image_scale(self, scale):
        self._image_scale = scale

    def image_flip(self, cvimage):
        image = cvimage
        if self._horizontal_flip_flag:
            cv2.flip(image, 1, image)
        if self._vertical_flip_flag:
            cv2.flip(image, 0, image)
        return image
    # 最后-增加亮度、对比度等调整功能

    # 顺时针旋转
    # 扩展成仿射变换
    def image_rotate(self, cvimage):
        image = cvimage
        (cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
        rotate_mat = cv2.getRotationMatrix2D((cX, cY), self._rotate_degree, self._image_scale)
        image = cv2.warpAffine(image, rotate_mat, (image.shape[1], image.shape[0]))
        return image

    def cvimage_to_qimage(self, cvimage):
        image = None
        image = cv2.cvtColor(cvimage, cv2.COLOR_BGR2RGB, image)
        image = QtGui.QImage(image, image.shape[1], image.shape[0], image.shape[1] * 3, QtGui.QImage.Format_RGB888)
        return image

    def image_process(self, cvimage):
        image = self.image_flip(cvimage)
        image = self.image_rotate(image)

        image = self.cvimage_to_qimage(image)
        self.sig_image_process_finished.emit(image)


if __name__ == '__main__' :
    pic = cv2.imread('test_image.jpg')
    result = ImageProcess()
    result.image_process(pic)
    cv2.waitKey(0)
