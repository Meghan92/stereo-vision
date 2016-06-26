import preprocessing.detection.count as count
import os


def run():
    length = count.images()

    if length == 0:
        raise ReferenceError("No jpg files were found")
