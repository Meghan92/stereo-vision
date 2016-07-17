import subprocess
import os
from shutil import copyfile


#variables
file_path = os.path.dirname(os.path.realpath(__file__))
output_path = os.path.join(file_path, "output")


def capture():
	preload = "LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libv4l/v4l1compat.so "
	application = "fswebcam "
	settings = "-r 544x288 -d "
	left_capture = preload + application + settings + "/dev/video0 " + output_path + "/left.jpg &"
	right_capture = preload + application + settings + "/dev/video1 " + output_path + "/right.jpg &"
	subprocess.call(left_capture + "\n" + right_capture + "\n" + "wait", shell=True)


def save_to_database(location):
	databases_location = os.path.join(file_path, "database")
	database_location = os.path.join(databases_location, location)
	data_num = 1
	for images in os.listdir(database_location):
		if data_num < int(images):
			data_num = int(images)
	data_num += 1
	new_path = os.path.join(database_location, str(data_num))
	os.makedirs(new_path)
	for images in os.listdir(output_path):
		copyfile(os.path.join(output_path, images), os.path.join(new_path, images))
	return data_num
	