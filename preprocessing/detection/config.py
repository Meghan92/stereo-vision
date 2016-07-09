

class Environment(object):
    def __init__(self, env_type):
        self.haar_xml = env_type.haar + "haarcascade_frontalface_default.xml"
        self.capture = env_type.path + "capture/" + env_type.input
        self.output = env_type.path + "preprocessing/detection/output/" + env_type.output


class Windows(object):
    def __init__(self, input_location, output_name):
        self.haar = "C:/Program Files/OpenCV/sources/data/haarcascades/"
        self.path = "C:/Development/stereo-vision/"
        self.input = input_location
        self.output = output_name


class Ubuntu(object):
	def __init__(self, input_location, output_name):
		self.haar = "/usr/share/opencv/haarcascades/"
		self.path = "/home/meghan/Development/stereo-vision/"
		self.input = input_location
		self.output = output_name
