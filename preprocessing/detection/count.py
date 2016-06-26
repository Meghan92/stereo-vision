import os


def images():
    output = [name for name in os.listdir('detection/output')]
    length = output.__len__()
    return length


def faces():
    return images() / 2
