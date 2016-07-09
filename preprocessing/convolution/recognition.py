import cv2
import convolution.base as base
import detection.output as output_detection


def run():
	print("- recognition")
	face_data = output_detection.get()
	for data in face_data:
		convolve(data.name, data.image)


def convolve(name, image):
    filename_length = name.__len__()
    new_name = name[0:filename_length-4]
    b, g, r = cv2.split(image)

    base.convolve(b, "convolution/output/" + new_name + "_blue.jpg")
    base.convolve(g, "convolution/output/" + new_name + "_green.jpg")
    base.convolve(r, "convolution/output/" + new_name + "_red.jpg")



