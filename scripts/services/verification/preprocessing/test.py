import detection.crop as crop
import detection.detect as detect
import detection.config as detect_config
import detection.count as count
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import clean
import common.constants as constants
import common.exception as exception
import convolution.verification as convolution


def run():
	print("- Clean up")
	clean.run()
	config_left = ["output/left.jpg", "left.jpg"]
	config_right = ["output/right.jpg", "right.jpg"]
	left_os = detect_config.Environment(detect_config.Ubuntu(config_left[0], config_left[1]))
	right_os = detect_config.Environment(detect_config.Ubuntu(config_right[0], config_right[1]))
	print("- Detecting faces")
	detect.run(left_os)
	detect.run(right_os)
	print("- Cropping faces")
	crop.run(constants.RESOLUTION)
	print("- Counting faces")
	faces = count.faces()
	if faces > 1:
		raise exception.MultiFaceException("Multiple faces were detected, unable to run verification.")
	print("- Convolving")
	convolution.run()
