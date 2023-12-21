import cv2
import os
import numpy as np

columns = 3
rows = 2

images = os.listdir("collage")
image_objects = [cv2.imread(f'collage/{image}') for image in images]
print(images)

horizontal_margin = 40
vertical_margin = 20

shape = cv2.imread("collage/1.jpeg").shape

print(shape) # (768, 1024, 3)

big_image = np.zeros(((shape[0] * rows) + horizontal_margin * (rows+1),
                     (shape[1] * columns) + vertical_margin * (columns+1),
                     shape[2]), np.uint8)
big_image.fill(255)

positions = [(x, y) for x in range(columns) for y in range(rows)]
print(positions)

for (pos_x, pos_y), image in zip(positions, image_objects):
    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pos_y * (shape[0] + horizontal_margin) + horizontal_margin
    big_image[y:y+shape[0], x:x+shape[1]] = image

cv2.imwrite("collage/big_image.jpeg", big_image)


