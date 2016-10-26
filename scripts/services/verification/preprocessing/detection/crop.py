import count
import cv2
import os
import sys


def run(resolution):
    length = count.images()
    if length == 0:
        raise ReferenceError("No jpg files were found")
    if resolution <= 0:
        resolution = constants.RESOLUTION
    path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(path, "output")
    for filename in os.listdir(output_path):
        location = os.path.join(output_path, filename)
        resize(cv2.imread(location), location, resolution)


def resize(image, path, resolution):
    height, width, channels = image.shape
    remainder_y = height % resolution
    remainder_x = width % resolution
    if (remainder_y > 0) or (remainder_x > 0):
        cropped = image[0:height-remainder_y, 0:width-remainder_y]
        cv2.imwrite(path, cropped)
