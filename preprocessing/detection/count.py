import os


def images():
	current_path =  os.path.dirname(os.path.realpath(__file__))
	detect_output = os.path.join(current_path, 'output')
	output = [name for name in os.listdir(detect_output) if name.endswith(".jpg")]
	length = output.__len__()
	return length


def faces():
    return images() / 2
