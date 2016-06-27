import cv2
import numpy as np


def convolve(image, location):
    sobel_converted = cv2.Sobel(image, cv2.CV_16S, 1, 0, ksize=3)
    absolute_sobel = np.absolute(sobel_converted)
    uint8_sobel = np.uint8(absolute_sobel)
    cv2.imwrite(location, uint8_sobel)
