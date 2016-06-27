import cv2
import preprocessing.convolution.output as output


def run():
    face_data = output.get()
    for data in face_data:
        algorithm(data)


def algorithm(data):
    edged = cv2.Canny(data.image, 500, 100)
    cv2.imwrite("output/" + data.name, edged)
