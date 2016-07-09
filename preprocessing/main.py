import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.detection.strategy as strategy
import preprocessing.detection.config as detect_config
import clean

try:
    print("-----Detecting faces-----")
    environment = detect_config.Environment(detect_config.Windows("output/left.jpg", "left.jpg"))
    detect.run(environment)
    environment = detect_config.Environment(detect_config.Windows("output/right.jpg", "right.jpg"))
    detect.run(environment)
    print("-----Cropping faces-----")
    crop.run(16)
    print("-----Running strategy-----")
    convolution = strategy.run()
    print("-----Convolving-----")
    convolution.run()
    print("-----Clean up-----")
    # clean.run()
except ReferenceError as refError:
    print("A reference occurred: " + refError.message)

