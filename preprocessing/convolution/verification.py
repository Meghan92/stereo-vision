import cv2
import os


def run():
    path = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir("detection/output"):
        location = os.path.join(os.path.join(path, "output"), filename)
        convolve(location)


def convolve(location):
    gray = cv2.cvtColor(cv2.imread(location), cv2.COLOR_RGB)
    cv2.imwrite("convolution/output/test_gray.jpg", gray)
