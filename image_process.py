import cv2
from PyQt5 import QtGui


class ImageProcess:
    def __init__(self, image):
        self.image = image

    def image_tilt_mirror(self):
        cv2.flip(self.image, 0, self.image)

    def image_pan_mirror(self):
        cv2.flip(self.image, 1, self.image)

    # 顺时针旋转
    def image_rotate(self, degree=0, scale=1):
        (cX, cY) = (self.image.shape[1] // 2, self.image.shape[0] // 2)
        rotate_mat = cv2.getRotationMatrix2D((cX, cY), -degree, scale)
        self.image = cv2.warpAffine(self.image, rotate_mat, (self.image.shape[1], self.image.shape[0]))

    def cvimage_to_qimage(self):
        self.image = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.shape[1] * 3,
                                  QtGui.QImage.Format_RGB888)


if __name__ == '__main__' :
    pic = cv2.imread('test_image.jpg')
    result = ImageProcess(pic)
    result.image_rotate(20, 0.5)
    cv2.namedWindow('test')
    cv2.imshow('test', result.image)
    cv2.waitKey(0)
