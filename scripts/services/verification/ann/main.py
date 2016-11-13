import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import processing.format as format
import ann.train as train
import numpy as np


def run(resolution):
	inputs = format.run()
	input_array = []
	output_array = []
	array_count = 0
	line = "\n------------------------------------------------------------------------------------------\n"
	input_nodes= resolution * 2 * 2
	for array in inputs:
		array_count += 1
		if array.__len__() >= input_nodes:
			temp_array = []
			temp_array.append(array.pop())
			output_array.append(temp_array)
			input_array.append(array)
		else:
			print "%sArray length for image %s is too short, discarded.%s" % (line, array_count, line)
		
	input_array = np.array(input_array)
	output_array = np.array(output_array)

	train.run(input_array, output_array, input_nodes)
