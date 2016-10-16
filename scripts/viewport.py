import cv2
import display.viewport as viewport


def show():
	viewport.start()
	cam = cv2.VideoCapture(0)
	show = 1
	window_name = 'Image Viewport'
	while show == 1:
		ret_val, img = cam.read()
		cv2.imshow(window_name, img)
		cv2.moveWindow(window_name, 100, 0)
		viewport.loaded()
		if cv2.waitKey(1) > 0: 
			show = 0
			cv2.destroyWindow(window_name)
			cv2.waitKey(1)
			cv2.waitKey(1)
			cv2.waitKey(1)
			cv2.waitKey(1)
