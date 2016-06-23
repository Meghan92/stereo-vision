import cv2

haar_location = "C:/Program Files/OpenCV/sources/data/haarcascades/"
raw_capture = "../ImageCapture/"
left_output = "output/left.jpg"
right_output = "output/right.jpg"
frontal_face = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(haar_location + frontal_face)
img_left = cv2.imread(raw_capture + left_output)
img_right = cv2.imread(raw_capture + right_output)
gray_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
gray_right = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)

left_faces = face_cascade.detectMultiScale(gray_left, 1.3, 5)

for (x, y, w, h) in left_faces:
    crop_img = img_left[y:y+h, x:x+w]
    cv2.imwrite(left_output, crop_img)

right_faces = face_cascade.detectMultiScale(gray_right, 1.3, 5)

for (x, y, w, h) in right_faces:
    crop_img = img_right[y:y+h, x:x+w]
    cv2.imwrite(right_output, crop_img)



