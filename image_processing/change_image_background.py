import cv2
import numpy as np

# Load the two images
foreground = cv2.imread('img_background/giraffe.jpeg')
background = cv2.imread('img_background/safari.jpeg')

print(foreground[40, 40]) #[ 28 255  76]

print(foreground.shape) # (480, 852, 3)
width = foreground.shape[1]  # 852
height = foreground.shape[0]  # 480

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any(pixel == [1, 255, 76]):
            foreground[j, i] = resized_background[j, i]

cv2.imwrite('img_background/output.jpeg', foreground)