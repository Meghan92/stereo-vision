import detection.output as detection
import convolution.output as convolution


def run():
	print "- Cleaning out the detection and convolution folders"
	detection.clean()
	convolution.clean()

