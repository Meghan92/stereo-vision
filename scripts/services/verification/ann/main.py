import scripts.services.verification.ann.train as train
import numpy as np
import scripts.services.verification.preprocessing.convolution.output as output


def run(resolution):
    images = output.get(resolution)
    image_map = {}
    for image in images:
        image_id = image.name.split("_")[0].replace("left", "").replace("right", "") + image.name.split("_")[1]
        image_pair = [None] * 2
        if image_id in image_map:
            image_pair[1] = image.image
        else:
            image_pair[0] = image.image
        image_map[image_id] = image_pair
    input_array1 = []
    input_array2 = []
    output_array = []
    for key, image_pair in image_map.iteritems():
        input_array1.append(image_pair[0])
        input_array2.append(image_pair[1])
        if "spoof" in key:
            output_array.append(-1)
        else:
            output_array.append(1)

    input_array = np.array([input_array1, input_array1])
    output_array = np.array(output_array)

    train.run(input_array, output_array)


def flatten_rgb(image):
    return image.flatten() / 255.0
