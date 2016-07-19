import cv2
import cmd, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'verification'))
import preprocessing.convolution.base as base
import preprocessing.detection.output as output_detection


def run():
	print "- fetching detected faces"
	face_data = output_detection.get()
	for data in face_data:
		convolve(data.name, data.image)


def convolve(name, image):
	print "- convolving " + name
	filename_length = name.__len__()
	new_name = name[0:filename_length-4]
	b, g, r = cv2.split(image)
	
	current_path = os.path.dirname(__file__)
	output_path = os.path.join(current_path, "output")
	convolution_path = os.path.join(output_path, "convolution")	

	base.convolve(b, os.path.join(convolution_path, new_name + "_blue.jpg"))
	base.convolve(g, os.path.join(convolution_path, new_name + "_green.jpg"))
	base.convolve(r, os.path.join(convolution_path, new_name + "_red.jpg"))



