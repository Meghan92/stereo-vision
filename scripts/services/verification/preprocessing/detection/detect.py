import cv2, sys, os


def run(environment):
	print "\t- " + environment.capture
	face_cascade = cv2.CascadeClassifier(environment.haar_xml)
	img = cv2.imread(environment.capture)
	faces = face_cascade.detectMultiScale(img, 1.3, 5)
	
	length = faces.__len__()
	if length <= 0:
		faces = face_cascade.detectMultiScale(img, 1.3, 1)
		length = faces.__len__()
		if length <= 0:
			raise ValueError("A face could not be detected. Please try again")
	print "\t- %s" % (faces)
	i = 0
	padding=50
	height, width, channels = img.shape
	for (x, y, w, h) in faces:
		i += 1
		output_length = environment.output.__len__()
		output_name = environment.output[0:output_length-4] + "_" + str(i) + ".jpg"
		crop_img = img[minval(y,padding):maxval(y+h,padding,height), minval(x, padding):maxval(x+w, padding, width)]
		cv2.imwrite(output_name, crop_img)
		
		
def minval(val, adjustment):
	val = val - adjustment
	if (val < 0):
		val = 0
	return val
	

def maxval(val, adjustment, maxlength):
	val = val + adjustment
	if (val >= maxlength):
		val = maxlength - 1
	return val
