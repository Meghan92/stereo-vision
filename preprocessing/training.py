import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.convolution.verification as verify
import preprocessing.detection.config as detect_config
import clean

try:
    print("-----Detecting faces in training set-----")
    for i in range(1, 91):
        environment = detect_config.Environment(
            detect_config.Windows("training/taiwan/" + str(i) + "/left.jpg", "left" + str(i) + ".jpg"))
        detect.run(environment)
        print(environment.capture)
        environment = detect_config.Environment(
            detect_config.Windows("training/taiwan/" + str(i) + "/right.jpg", "right" + str(i) + ".jpg"))
        detect.run(environment)
        print(environment.capture)
    print("-----Cropping faces-----")
    crop.run(16)
    print("-----Convolving-----")
    verify.run()
    print("-----Clean up-----")
    # clean.run()
except ReferenceError as refError:
    print("A reference occurred: " + refError.message)

