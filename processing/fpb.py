import preprocessing.convolution.output as output


def run(resolution=4):
    print("- using resolution size of: " + str(resolution))
    face_data = output.get(resolution)
    print("- clearing bytes.txt")
    text = open("output/bytes.txt", "w")
    text.close()
    print("- getting faces")
    for data in face_data:
        algorithm(data)


def algorithm(face_data):
    height, width, channels = face_data.image.shape
    increment_h = int(height / face_data.resolution)
    increment_w = int(width / face_data.resolution)
    start_h = 0
    start_w = 0
    fpb_list = []
    print("- creating fpb for: " + face_data.name)
    while start_h + increment_h <= height:
        count = 0
        for x in range(start_h, start_h + increment_h):
            for y in range(0, width):
                if face_data.image[x][y][0] > 0:
                    count += 1
        start_h += increment_h
        fpb_list.append(count)

    while start_w + increment_w <= width:
        count = 0
        for x in range(0, height):
            for y in range(start_w, start_w + increment_w):
                if face_data.image[x][y][0] > 0:
                    count += 1
        start_w += increment_w
        fpb_list.append(count)

    text = open("output/bytes.txt", "a")
    text.write("\"" + face_data.name + "\"" + "," + str(fpb_list) + "\n")
    text.close()
