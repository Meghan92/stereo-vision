import processing.output as output
import numpy as np


def run(resolution=4):
	print("- using resolution size of: " + str(resolution))
	face_data = output.get(resolution)
	print("- clearing bytes.txt")
	text = open("output/bytes.txt", "w")
	text.close()
	print("- getting faces")
	for data in face_data:
		algorithm(data)


def algorithm(face_data):
	height, width, channels = face_data.image.shape
	increment_h = int(height / face_data.resolution)
	increment_w = int(width / face_data.resolution)
	print("- creating fpb for: " + face_data.name)
	horizontal_list = loop(increment_h, height, width, face_data.image)
	vertical_list = loop(increment_w, width, height, face_data.image)
	list = horizontal_list + vertical_list
	fpb_list = []
	max = np.amax(list)
	min = np.amin(list)
	for num in list:
		fpb_list.append(normalise(num, min, max))
	write(face_data.name, fpb_list)
	del fpb_list[:]
	

def loop(increment, length, breadth, image):
	start_val = 0
	count = 0
	count_list = []
	min = -1
	max = 0
	while start_val + increment <= length:
		count = 0
		for x in range(start_val, start_val + increment):
			for y in range(0, breadth):
				item = image[x][y][0]
				if item > 0:
					count += 1
		start_val += increment
		count_list.append(count)
	return count_list
	

def normalise(x, min, max):
	return (((x - min) / float(max - min)) * 2) -1
	
	
def write(name, list):
	text = open("output/bytes.txt", "a")
	text.write(name + ";" + str(list) + "\n")
	text.close()
