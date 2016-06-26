import cv2
import os
import preprocessing.convolution.base as base


def run():
    path = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir("detection/output"):
        convolve(path, filename)


def convolve(path, filename):
    location = os.path.join(os.path.join(path, "output"), filename)
    l = filename.__len__()
    new_name = filename[0:l - 4] + "_gray.jpg"

    gray = cv2.cvtColor(cv2.imread(location), cv2.COLOR_RGB2GRAY)
    cv2.imwrite("convolution/output/" + new_name, gray)

    base.convolve(gray, "convolution/output/" + new_name)
