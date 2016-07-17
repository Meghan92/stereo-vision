import count
import cv2
import os


def run(resolution):
    length = count.images()
    if length == 0:
        raise ReferenceError("No jpg files were found")
    if resolution <= 0:
        resolution = 4
    path = os.path.dirname(os.path.realpath(__file__))
    for filename in os.listdir("detection/output"):
        location = os.path.join(os.path.join(path, "output"), filename)
        resize(cv2.imread(location), location, resolution)


def resize(image, path, resolution):
    height, width, channels = image.shape
    remainder_y = height % resolution
    remainder_x = width % resolution
    if (remainder_y > 0) or (remainder_x > 0):
        cropped = image[0:height-remainder_y, 0:width-remainder_y]
        cv2.imwrite(path, cropped)
