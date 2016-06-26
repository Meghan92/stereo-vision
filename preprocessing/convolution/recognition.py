import cv2
import os
import preprocessing.convolution.base as base


def run():
    path = os.path.dirname(os.path.realpath("detection/output"))

    for filename in os.listdir("detection/output"):
        convolve(path, filename)


def convolve(path, filename):
    location = os.path.join(os.path.join(path, "output"), filename)
    l = filename.__len__()
    new_name = filename[0:l-4]
    image = cv2.imread(location)

    b, g, r = cv2.split(image)

    base.convolve(b, "convolution/output/" + new_name + "_blue.jpg")
    base.convolve(g, "convolution/output/" + new_name + "_green.jpg")
    base.convolve(r, "convolution/output/" + new_name + "_red.jpg")





