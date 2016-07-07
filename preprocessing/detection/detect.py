import cv2


def run(environment):
    face_cascade = cv2.CascadeClassifier(environment.haar_xml)
    img = cv2.imread(environment.capture)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    i = 0
    for (x, y, w, h) in faces:
        i += 1
        crop_img = img[y:y+h, x:x+w]
        cv2.imwrite(environment.output, crop_img)