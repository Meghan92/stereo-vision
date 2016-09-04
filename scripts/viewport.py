import cv2
import display.viewport as viewport


def show():
	viewport.start()
	cam = cv2.VideoCapture(0)
	show = 1
	while show == 1:
		viewport.loaded()
		ret_val, img = cam.read()
		window_name = 'Image Viewport'
		cv2.imshow(window_name, img)
		cv2.moveWindow(window_name, 100, 0)
		if cv2.waitKey(1) > -1: 
			show = 0
			cv2.destroyAllWindows()
