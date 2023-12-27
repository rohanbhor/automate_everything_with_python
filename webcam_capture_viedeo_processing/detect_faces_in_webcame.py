import cv2
video = cv2.VideoCapture(0) # 0 for webcam

success, frame = video.read()
height = frame.shape[0]
width = frame.shape[1]

output = cv2.VideoWriter('output.mp4', cv2.VideoWriter.fourcc(*'DIVX'), 30, (width, height))

face_cascade = cv2.CascadeClassifier('faces.xml')

counter = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 4)

    output.write(frame)
    success, frame = video.read()
    counter+=1
    print(counter)

output.release()


