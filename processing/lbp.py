import cv2
import preprocessing.convolution.output as output


def run():
    print("- fetching images")
    face_data = output.get()
    for data in face_data:
        algorithm(data)


def algorithm(data):
    print("- using canny detection")
    edged = cv2.Canny(data.image, 500, 100)
    cv2.imwrite("output/" + data.name, edged)
    print("- image written to: output/" + data.name)
