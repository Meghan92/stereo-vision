import cv2
import preprocessing.detection.crop as crop

project_path = "C:/Development/stereo-vision/"
haar_location = "C:/Program Files/OpenCV/sources/data/haarcascades/"
raw_capture = project_path + "capture/"
left_output = project_path + "detection/output/left"
right_output = project_path + "detection/output/right"
frontal_face = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(haar_location + frontal_face)
img_left = cv2.imread(raw_capture + "output/left.jpg")
img_right = cv2.imread(raw_capture + "output/right.jpg")

left_faces = face_cascade.detectMultiScale(img_left, 1.3, 5)

i = 0

for (x, y, w, h) in left_faces:
    ++i
    crop_img = img_left[y:y+h, x:x+w]
    cv2.imwrite(left_output + "_" + str(i) + ".jpg", crop_img)

right_faces = face_cascade.detectMultiScale(img_right, 1.3, 5)

i = 0

for (x, y, w, h) in right_faces:
    ++i
    crop_img = img_right[y:y+h, x:x+w]
    cv2.imwrite(right_output + "_" + str(i) + ".jpg", crop_img)

print("Left: ")
print(left_faces)

print("Right: ")
print(right_faces)

crop.run()


