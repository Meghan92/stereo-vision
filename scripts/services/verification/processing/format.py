import os


def run(show_output=1):
	path = os.path.dirname(os.path.realpath(__file__))
	output_path = os.path.join(path, "output")
	text_path = os.path.join(output_path, "bytes.txt")
	filename_map = []
	value_map = []
	with open(text_path, "r") as text:
		for line in text:
			filename = line.split(";")[0]
			filecount = line.split("_")[1]
			array = map(float, line.split("[")[1].split("]")[0].split(","))
			image_type = "live"
			if "spoof" in filename:
				image_type = "spoof"
			filecombo = image_type + filecount
			if filename_map.__len__() > 0 and filename_map.__contains__(filecombo):
				index = filename_map.index(filecombo)
				if show_output > 0:
					if "spoof" in filename:
						array.append(-1)
					else:
						array.append(1)
				value_map[index] += array					
			else:
				filename_map.append(filecombo)
				value_map.append(array)
	text.close()
	input_path = os.path.join(output_path, "inputs.txt")
	text = open(input_path, "w")
	for array in value_map:
		text.write(str(array))
		text.write("\n")
	text.close()
	return value_map

	
