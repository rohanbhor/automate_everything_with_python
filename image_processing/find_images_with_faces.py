import cv2
import os

cascade = "faces.xml"
input_folder = "input"
output_folder = "output"

def has_face(image_path):
    image = cv2.imread(image_path, 1)

    face_cascade = cv2.CascadeClassifier(cascade)

    faces = face_cascade.detectMultiScale(image, 1.1, 4)

    if len(faces) != 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 4)
        return image


images = os.listdir(input_folder)
for image in images:
    face_image = has_face(f"{input_folder}/{image}")
    if face_image is not None:
        cv2.imwrite(f"{output_folder}/{image}", face_image)

