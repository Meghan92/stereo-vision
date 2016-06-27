import os
import cv2


# returns an array of images in the output folder
def get():
    path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(path, "output")
    images = []

    for filename in os.listdir(output_path):
        if filename.endswith(".jpg"):
            location = os.path.join(output_path, filename)
            output = cv2.imread(location)
            images.append(FaceData(filename, output))

    return images


class FaceData(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, image=None):
        self.name = name
        self.image = image
