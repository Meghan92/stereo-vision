import cv2
import cmd, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'verification'))
import preprocessing.convolution.base as base
import preprocessing.detection.output as output_detection


def run():
	print "- Clearing old images"
	clean()
	print "- Fetching detected faces"
	face_data = output_detection.get()
	for data in face_data:
		convolve(data.name, data.image)


def convolve(name, image):
	print "- splitting colours " + name
	filename_length = name.__len__()
	new_name = name[0:filename_length-4]
	b, g, r = cv2.split(image)
	
	current_path = os.path.dirname(__file__)
	output_path = os.path.join(current_path, "output")
	
	cv2.imwrite(os.path.join(output_path, new_name + "_blue.jpg"), b)
	cv2.imwrite(os.path.join(output_path, new_name + "_green.jpg"), g)
	cv2.imwrite(os.path.join(output_path, new_name + "_red.jpg"), r)
	

def clean():
	path = os.path.dirname(os.path.realpath(__file__))
	output_path = os.path.join(path, "output")
	for files in os.listdir(output_path):
		os.remove(os.path.join(output_path, files))



