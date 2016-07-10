import os


def run():
	number_map = []
	input_array = []
	path = os.path.dirname(os.path.realpath(__file__))
	output_path = os.path.join(path, "output")
	text_path = os.path.join(output_path, "bytes.txt")
	with open(text_path, "r") as text:
		for line in text:
			data_val = line.split(";")
			number = data_val[0].split("_")[1]
			array = map(float, line.split("[")[1].split("]")[0].split(","))
			if number_map.__len__() > 0 and number_map.__contains__(number):
				index = number_map.index(number)
				input_array[index] += array
			else:
				input_array.append(array)
				number_map.append(number)
	text.close()
	input_path = os.path.join(output_path, "inputs.txt")
	text = open(input_path, "w")
	for array in input_array:
		text.write(str(array))
		text.write("\n")
	text.close()
	return input_array
