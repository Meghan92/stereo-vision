import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import convolution.base as base
import detection.output as output_detection


def run():
	face_data = output_detection.get()
	length = face_data.__len__()
	if length <= 0:
		raise ReferenceError("No images were found in the detection step. Please try again.")
	for data in face_data:
		convolve(data.name, data.image)


def convolve(name, image):
	filename_length = name.__len__()
	new_name = name[0:filename_length - 4] + "_gray.jpg"
	current_path = os.path.dirname(__file__)
	output_path = os.path.join(current_path, "output")
	new_path = os.path.join(output_path, new_name)
	base.convolve(image, new_path)
