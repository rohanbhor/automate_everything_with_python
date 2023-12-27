import cv2


video = cv2.VideoCapture("video.mp4")
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) #90
fps = video.get(cv2.CAP_PROP_FPS) #30

print(fps, nr_frames)

timestamp = "00:00:02.75"
timestamp_list = timestamp.split(":")
hours, minutes, seconds = [float(x) for x in timestamp_list]

frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps

video.set(1, frame_nr) #set start of the video at frame frame_nr

success, frame = video.read()

cv2.imwrite(f"frame_at_{hours}_{minutes}_{seconds}.jpeg", frame)


