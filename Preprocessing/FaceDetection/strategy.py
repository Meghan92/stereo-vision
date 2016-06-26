import glob
import os
import Preprocessing.ImageConvolution.recognition as recognition
import Preprocessing.ImageConvolution.verification as verification


def run():
    os.chdir("C:/Development/stereo-vision/Preprocessing/FaceDetection/output")
    images = glob.glob("*.jpg")
    count = images.__len__()

    people = count / 2

    if people > 1:
        recognition.run()
    else:
        verification.run()
