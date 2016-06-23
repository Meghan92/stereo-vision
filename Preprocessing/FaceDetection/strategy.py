import glob
import os
import imp

os.chdir("C:/Development/stereo-vision/Preprocessing/FaceDetection/output")
images = glob.glob("*.jpg")

count = 0
for faces in images:
    count += 1

people = count / 2

if people > 1:
    imp.load_source('recognition', '../../ImageConvolution/recognition.py')
else:
    imp.load_source('verification', '../../ImageConvolution/verification.py')
