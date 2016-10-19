import os, sys, cv2
from shutil import copyfile


def clean_and_move(student):
	database_path = os.path.join(os.path.dirname(__file__), "database")
	output_path = os.path.join(os.path.dirname(__file__), "output")
	student_path = os.path.join(database_path, student)
	for files in os.listdir(student_path):
		os.remove(os.path.join(student_path, files))
	for files in os.listdir(output_path):
		copyfile(os.path.join(output_path, files), os.path.join(student_path, files))
		

def get_images_and_labels():
	database_path = os.path.join(os.path.dirname(__file__), "database")
	images = []
	labels = []
	for students in os.listdir(database_path):
		student_path = os.path.join(database_path, students)
		for faces in os.listdir(student_path):
			image_path = os.path.join(student_path, faces)
			image = cv2.imread(image_path, 0)
			images.append(image)
			label = int(students)
			labels.append(label)
	return images, labels