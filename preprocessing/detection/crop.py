import glob


def run():
    images = glob.glob("*.jpg")
    count = images.__len__()

    if count == 0:
        raise ReferenceError("No jpg files were found")
