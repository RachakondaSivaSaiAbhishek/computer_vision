import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Abhishek\PycharmProjects\pythonProject\Resources\car.jpeg")

imgrey =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow(" image",img)
cv2.imshow("grey image",imgrey)

cv2.waitKey(0)