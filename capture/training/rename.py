import os

path = os.path.dirname(os.path.realpath(__file__))
output_path = os.path.join(path, "taiwan")

n = 0
for i in range(8, 91):
    new_path = os.path.join(output_path, str(i))
    for files in os.listdir(new_path):
        if files == "Thumbs.db":
            continue
        if n == 0:
            os.rename(os.path.join(new_path, files), os.path.join(new_path, "left.jpg"))
            n = 1
        elif n == 1:
            n = 0
            os.rename(os.path.join(new_path, files), os.path.join(new_path, "right.jpg"))
