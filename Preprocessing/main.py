import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.detection.strategy as strategy

try:
    print("-----Detecting faces-----")
    detect.run()
    print("-----Cropping faces-----")
    crop.run(-1)
    print("-----Running strategy-----")
    strategy.run()
except ReferenceError as refError:
    print("A reference occurred: " + refError.message)

