def run():
    number_map = []
    input_array = []
    with open("output/bytes.txt", "r") as text:
        for line in text:
            data_val = line.split(";")
            number = data_val[0].split("_")[1]
            array = map(int, line.split("[")[1].split("]")[0].split(","))
            if number_map.__len__() > 0 and number_map.__contains__(number):
                index = number_map.index(number)
                input_array[index] += array
            else:
                input_array.append(array)
                number_map.append(number)
    text.close()
    text = open("output/inputs.txt", "w")
    for array in input_array:
        text.write(str(array))
    text.close()
    return input_array
