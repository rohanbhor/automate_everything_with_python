import cv2

video = cv2.VideoCapture("video.mp4")
success, frame = video.read()

count = 1
nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

while success:
    cv2.imwrite(f"images/{count}.jpeg", frame)
    success, frame = video.read()
    count+=1

