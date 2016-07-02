import preprocessing.convolution.output as output


def run():
    face_data = output.get()
    text = open("output/bytes.txt", "w")
    text.close()
    for data in face_data:
        algorithm(data.image, data.name)


def algorithm(data, name):
    height, width, channels = data.shape
    increment_h = int(height / 4)
    increment_w = int(width / 4)
    start_h = 0
    start_w = 0
    fpb_list = []

    while start_h + increment_h <= height:
        count = 0
        for x in range(start_h, start_h + increment_h):
            for y in range(0, width):
                if data[x][y][0] > 0:
                    count += 1
        start_h += increment_h
        fpb_list.append(count)

    while start_w + increment_w <= width:
        count = 0
        for x in range(0, height):
            for y in range(start_w, start_w + increment_w):
                if data[x][y][0] > 0:
                    count += 1
        start_w += increment_w
        fpb_list.append(count)

    text = open("output/bytes.txt", "a")
    text.write("\"" + name + "\"" + "," + str(fpb_list) + "\n")
    text.close()
