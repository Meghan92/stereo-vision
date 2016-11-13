import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import processing.format as format
import ann.train as train
import numpy as np
import preprocessing.convolution.output as output


def run(resolution):
	images = output.get(resolution)
	image_map = {}
	for image in images:
		id = image.name.split("_")[0] + image.name.split("_")[1]
		if id in image_map:
			image_map[id] += image.image
		else:
			image_map[id] = image.image
	input_array = []
	output_array = []
	for key, image in image_map.iteritems():
		input_array.append(flatten_rgb(image))
		if "spoof" in key:
			output_array.append(-1)
		else:
			output_array.append(1)
		
	input_array = np.array(input_array)
	output_array = np.array(output_array)

	train.run(input_array, output_array)


def flatten_rgb(image):
	return image.flatten()/255.0
		
		
