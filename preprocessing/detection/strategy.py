import glob
import os
import preprocessing.convolution.recognition as recognition
import preprocessing.convolution.verification as verification


def run():
    os.path.expanduser("./output")
    images = glob.glob("*.jpg")
    count = images.__len__()

    people = count / 2

    if people > 1:
        recognition.run()
    else:
        verification.run()
