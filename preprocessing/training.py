import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import preprocessing.detection.crop as crop
import preprocessing.detection.detect as detect
import preprocessing.convolution.verification as verify
import preprocessing.detection.config as detect_config
import clean

try:
	print("-----Detecting faces in taiwan set-----")
	for i in range(91, 91):
		environment = detect_config.Environment(
			detect_config.Ubuntu("database/taiwan/" + str(i) + "/left.jpg", "left_" + str(i) + ".jpg"))
		detect.run(environment)
		environment = detect_config.Environment(
			detect_config.Ubuntu("database/taiwan/" + str(i) + "/right.jpg", "right_" + str(i) + ".jpg"))
		detect.run(environment)
	print("-----Detecting faces in taiwan spoof set-----")
	for i in range(32, 32):
		environment = detect_config.Environment(
			detect_config.Ubuntu("database/taiwan_spoof/" + str(i) + "/left.jpg", "spoofleft_" + str(i) + ".jpg"))
		detect.run(environment)
		environment = detect_config.Environment(
			detect_config.Ubuntu("database/taiwan_spoof/" + str(i) + "/right.jpg", "spoofright_" + str(i) + ".jpg"))
		detect.run(environment)
	print("-----Cropping faces-----")
	#crop.run(16)
	print("-----Convolving-----")
	verify.run()
except ReferenceError as refError:
	print("A reference occurred: " + refError.message)

