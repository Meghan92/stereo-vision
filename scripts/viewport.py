import cv2


def show():
	#display the viewport
	cam = cv2.VideoCapture(0)
	show = 1
	while show == 1:
		ret_val, img = cam.read()
		cv2.imshow('Image Viewport', img)
		if cv2.waitKey(1) > -1: 
			show = 0
			cv2.destroyAllWindows()
