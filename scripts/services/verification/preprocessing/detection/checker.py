import os


output_path = os.path.join(os.path.dirname(__file__), "output")
image_name_array = []
current_name_array = []
invalid_array = []

def clean_duplicates():
	for images in os.listdir(output_path):
		split_array = images.split("_")
		unique_split = split_array[0] + split_array[1]
		actual_split = unique_split.replace("left","").replace("right","")
		image_name_array.append(actual_split)
		current_name_array.append(images)
	
	index = 0

	for images in image_name_array:
		count = image_name_array.count(images)
		if count != 2:
			name = current_name_array[index]
			invalid_array.append(name)
			print "Missing image for ID {} with count {}.".format(name, count)
		index+=1
	
	for images in invalid_array:
		image_path = os.path.join(output_path, images)
		os.remove(image_path)
		print "Deleted {}".format(images)
	
