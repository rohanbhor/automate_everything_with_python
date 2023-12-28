import cv2

video = cv2.VideoCapture('smile.mp4')

success, frame = video.read()
height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')


output = cv2.VideoWriter('blurred_smile.mp4', cv2.VideoWriter.fourcc(*"DIVX"), 30,
                         (width, height))

while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50, 50)) # 50, 50 is intensity of blurrness

    output.write(frame)
    success, frame = video.read()

output.release()
