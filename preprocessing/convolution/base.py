import cv2
import numpy as np


def convolve(image, location):
    print("Doing the final convolving for: " + location)
    kernel = [[1, 1, 1],
              [0, 4, 0],
              [-1, -2, -1]]
    height, width = image.shape
    blank_image = np.zeros((height, width, 1), np.uint8)
    count = 0

    for x in range(0, height):
        for y in range(0, width):
            for i in range(0, 3):
                for j in range(0, 3):
                    if (x - 1 >= 0) and (y - 1 >= 0):
                        count += (image[x-1][y-1] * kernel[i][j])
            blank_image[x][y] += count
            count = 0

    cv2.imwrite(location, blank_image)
