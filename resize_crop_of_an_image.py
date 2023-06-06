import cv2
import numpy as np

# Resizing the image
img = cv2.imread(r"C:\Users\Abhishek\PycharmProjects\pythonProject\Resources\car.jpeg")

print(img.shape)

imgResize = cv2.resize(img, (150, 90))

cv2.imshow("Original Image", img)
cv2.imshow("Resized Image", imgResize)

print(imgResize.shape)

cv2.waitKey(0)

# Cropping the image
imgCrop = img[60:150, 30:220]

print(imgCrop.shape)

cv2.imshow("Cropped Image", imgCrop)

cv2.waitKey(0)
