import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import processing.format as format
import ann.train as train
import numpy as np


inputs = format.run()
input_array = []
input_array = np.array(inputs)

output = [0]
output_array = []
for i in range (0, 90):
	output_array.append(output)
output_array = np.array(output_array)
print input_array[0]


train.run(input_array, output_array)