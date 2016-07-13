import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import processing.format as format
import ann.train as train
import numpy as np


inputs = format.run()
input_array = []
output_array = []
for array in inputs:
	temp_array = []
	temp_array.append(array.pop())
	output_array.append(temp_array)
	input_array.append(array)
	
input_array = np.array(input_array)
output_array = np.array(output_array)

print input_array.shape
print output_array.shape

train.run(input_array, output_array)