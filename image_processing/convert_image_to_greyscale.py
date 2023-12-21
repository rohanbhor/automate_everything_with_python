import cv2

color = cv2.imread('galaxy.png', 1) # 1 = color, 0 = grayscale

print(type(color)) #<class 'numpy.ndarray'>

cv2.imwrite('galaxy_greyscale.png', color) # convert numpy array to image

print(color)