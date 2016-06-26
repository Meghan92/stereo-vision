import preprocessing.detection.count as count


def run():
    length = count.images()

    if length == 0:
        raise ReferenceError("No jpg files were found")

