import cv2, os
import numpy as np


def convolve(image, file_name):
	blur = cv2.GaussianBlur(image, ksize=(3,3), sigmaX=0, sigmaY=0)
	sobel_x = cv2.Sobel(blur, cv2.CV_16S, 1, 0, ksize=3)
	sobel_y = cv2.Sobel(blur, cv2.CV_16S, 0, 1, ksize=3)
	abs_sobel_x = cv2.convertScaleAbs(sobel_x)
	abs_sobel_y = cv2.convertScaleAbs(sobel_y)
	weighted = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, gamma=0)
	directory = os.path.dirname(os.path.abspath(__file__))
	location = os.path.join(directory, "output", file_name)
	#print "- Writing to " + location
	cv2.imwrite(location, weighted)
