import preprocessing.convolution.base as base
import preprocessing.detection.output as output_detection


def run():
    face_data = output_detection.get()
    for data in face_data:
        convolve(data.name, data.image)


def convolve(name, image):
    filename_length = name.__len__()
    new_name = name[0:filename_length - 4] + "_gray.jpg"
    base.convolve(image, "convolution/output/" + new_name)
