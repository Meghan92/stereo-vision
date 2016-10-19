import cv2, os
import numpy as np
import file


def run():
	recognizer = cv2.createLBPHFaceRecognizer()
	print "- Fetching images and labels"
	images, labels = file.get_images_and_labels()
	print "- Running face recognizer"
	recognizer.train(images, np.array(labels))
	print "- Saving output"
	current_path = os.path.dirname(__file__)
	file_name = os.path.join(current_path, "recognizer.xml")
	recognizer.save(file_name)
	