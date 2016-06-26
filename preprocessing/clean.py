import os


def run():
    path = os.path.dirname(os.path.realpath("convolution/output"))
    for files in os.listdir("convolution/output"):
        os.remove(os.path.join(os.path.join(path, "output"), files))
