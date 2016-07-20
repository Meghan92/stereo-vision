import cv2, os


def run(student):
	recognizer = cv2.createLBPHFaceRecognizer()
	current_path = os.path.dirname(__file__)
	image_name = "left_1_blue.jpg"
	output_location = os.path.join(current_path, "output")
	image_location = os.path.join(output_location, image_name)
	file_name = os.path.join(current_path, "recognizer.xml")
	recognizer.load(file_name)
	
	image = cv2.imread(image_location, 0)
	nbr_predicted, conf = recognizer.predict(image)
	nbr_actual = int(student)
	if nbr_actual == nbr_predicted:
		return 1
	else:
		return 0