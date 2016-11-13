import preprocessing.convolution.output as output
import numpy as np
import os


#variables
current_path = os.path.join(os.path.dirname(__file__))
output_path = os.path.join(current_path, "output")
byte_path = os.path.join(output_path, "bytes.txt")


def run(resolution):
	print("- using resolution size of: " + str(resolution))
	print("- getting faces")
	face_data = output.get(resolution)
	length = face_data.__len__()
	if length <= 0:
		raise ReferenceError("Missing faces from convolution step. Unable to process. Please try again.")
	print("- clearing bytes.txt")
	text = open(byte_path, "w")
	text.close()
	
	for data in face_data:
		algorithm(data)


def algorithm(face_data):
	height, width, channels = face_data.image.shape
	increment_h = int(height / face_data.resolution)
	increment_w = int(width / face_data.resolution)
	print("- creating fpb for: " + face_data.name)
	horizontal_list = loop_horizontal(increment_h, width, face_data.resolution, face_data.image)
	vertical_list = loop_vertical(increment_w, height, face_data.resolution, face_data.image) 
	list = horizontal_list + vertical_list
	fpb_list = []
	max = np.amax(list)
	min = np.amin(list)
	for num in list:
		fpb_list.append(normalise(num, min, max))
	write(face_data.name, fpb_list)
	del fpb_list[:]
	

def loop_horizontal(increment, width, resolution, image):
	start_val = 0
	count = 0
	count_list = []
	min = -1
	max = 0
	
	for value in range (0, resolution):
		for y in range(0, width):
			for x in range(start_val, start_val + increment):
				item = int(image[x,y,0] + image[x,y,1] + image[x,y,2]) 
				count += item
		count_list.append(count)
		start_val += increment
	return count_list
	

def loop_vertical(increment, height, resolution, image):
	start_val = 0
	count = 0
	count_list = []
	min = -1
	max = 0
	
	for value in range (0, resolution):
		for x in range(0, height):
			for y in range(start_val, start_val + increment):
				item = int(image[x,y,0] + image[x,y,1] + image[x,y,2])
				count += item
		count_list.append(count)
		start_val += increment
	return count_list
	
	

def normalise(x, min, max):
	return (x - min) / float(max - min)
	
	
def write(name, list):
	text = open(byte_path, "a")
	text.write(name + ";" + str(list) + "\n")
	text.close()
