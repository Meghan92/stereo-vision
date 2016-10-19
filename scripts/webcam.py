import subprocess
import os, base64
from shutil import copyfile


#variables
file_path = os.path.dirname(os.path.realpath(__file__))
output_path = os.path.join(file_path, "output")
preload = "LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libv4l/v4l1compat.so "
application = "fswebcam "
settings = "-r 544x288 -d "
left_capture = preload + application + settings + "/dev/video0 " + output_path + "/left.jpg &"
right_capture = preload + application + settings + "/dev/video1 " + output_path + "/right.jpg &"


def capture():
	try:
		clean()
		message_log_name = os.path.join(file_path, "Log.txt")
		message_log = open(message_log_name, 'w')
		FNULL = open(os.devnull, 'w')
		result = subprocess.check_call(left_capture + "\n" + right_capture + "\n" + "wait", shell=True, stdout=FNULL, stderr=message_log)
		message_log.close()
		FNULL.close()
		return (count() == 2)
	except CalledProcessError:
		return 0


def clean():
    path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(path, "output")
    for files in os.listdir(output_path):
        os.remove(os.path.join(output_path, files))


def count():
	counter = 0
	for files in os.listdir(output_path):
		counter += 1
	return counter


def get_blobs():
	#return blobs in an array
	blob_array = []
	path = os.path.dirname(os.path.realpath(__file__))
	output_path = os.path.join(path, "output")
	for files in os.listdir(output_path):
		file_name = os.path.join(output_path, files)
		blob_array.append(base64.b64encode(open(file_name, 'rb').read()))
	return blob_array
	

def save_to_database(location):
	file_path = os.path.dirname(os.path.realpath(__file__))
	output_path = os.path.join(file_path, "output")
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
	
