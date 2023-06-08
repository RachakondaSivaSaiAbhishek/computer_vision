import cv2
import numpy as np

img = cv2.imread("Rsources/leans.png")

imgHor = np.hstack((img,img))

cv2.imshow("horizontal",imgHor)

imgVer = np.vstack((img,img))

cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)



