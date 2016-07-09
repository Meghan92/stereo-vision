import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.convolution.verification as verify
import preprocessing.detection.config as detect_config
import clean

try:
    print("-----Detecting faces in training set-----")
    for i in range(1, 51):
        environment = detect_config.Environment(
            detect_config.Ubuntu("training/taiwan/" + str(i) + "/left.jpg", "left_" + str(i) + ".jpg"))
        print(environment.capture)
        environment = detect_config.Environment(
            detect_config.Ubuntu("training/taiwan/" + str(i) + "/right.jpg", "right_" + str(i) + ".jpg"))
        detect.run(environment)
    print("-----Cropping faces-----")
    crop.run(16)
    print("-----Convolving-----")
    verify.run()
    print("-----Clean up-----")
    # clean.run()
except ReferenceError as refError:
    print("A reference occurred: " + refError.message)

