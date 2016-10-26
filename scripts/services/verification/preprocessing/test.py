import sys
import os
import clean
import detection.crop as crop
import detection.detect as detect
import detection.config
import detection.count
import convolution.verification as convolution


def run(resolution):
	print("- Clean up")
	clean.run()
	image_left = ["output/left.jpg", "left.jpg"]
	image_right = ["output/right.jpg", "right.jpg"]
	path_left = detection.config.Ubuntu(image_left[0], image_left[1])
	path_right = detection.config.Ubuntu(image_right[0], image_right[1])
	environment_path_left = detection.config.Environment(path_left)
	environment_path_right = detection.config.Environment(path_right)
	print("- Detecting faces")
	detect.run(environment_path_left)
	detect.run(environment_path_right)
	print("- Cropping faces")
	crop.run(resolution)
	print("- Counting faces")
	faces = detection.count.faces()
	if faces > 1:
		raise ValueError("Multiple faces were detected, unable to run verification.")
	print("- Convolving")
	convolution.run()
