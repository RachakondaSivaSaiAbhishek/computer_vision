import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while True:
    success, im = cap.read()
    cv2.imshow("VIDEO",im)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break