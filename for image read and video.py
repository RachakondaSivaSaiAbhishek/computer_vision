import cv2
import numpy as np
print('hello world')

#code for reading an image using cv2
#using function called imread()
img = cv2.imread(r"C:\Users\Abhishek\PycharmProjects\pythonProject\Resources\car.jpeg")

cv2.imshow('car',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(np.shape(img))

#code for reading an video using cv2
#using function called VideoCapture()
cap = cv2.VideoCapture(r"C:\Users\Abhishek\PycharmProjects\pythonProject\Resources\big.mp4")

while True:
    success, im = cap.read()
    cv2.imshow("VIDEO",im)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

#code for reading from web cam  using cv2
#using function called VideoCapture(0)
# 0 for default web cam