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
	recognizer.save("recognizer.xml")
	