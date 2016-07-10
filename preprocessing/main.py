import detection.crop as crop
import detection.detect as detect
import detection.strategy as strategy
import detection.config as detect_config
import clean

try:
	taiwan = "training/taiwan spoof/1/"
	config_left = ["output/left.jpg", "spoofleft.jpg"]
	config_right = ["output/right.jpg", "spoofright.jpg"]
	left_os = detect_config.Environment(detect_config.Ubuntu(config_left[0], config_left[1]))
	right_os = detect_config.Environment(detect_config.Ubuntu(config_right[0], config_right[1]))
	print("-----Detecting faces-----")
	detect.run(left_os)
	detect.run(right_os)
	print("-----Cropping faces-----")
	resolution = 16
	crop.run(resolution)
	print("-----Running strategy-----")
	convolution = strategy.run()
	print("-----Convolving-----")
	convolution.run()
	print("-----Clean up-----")
	# clean.run()
except ReferenceError as refError:
    print("A reference occurred: " + refError.message)