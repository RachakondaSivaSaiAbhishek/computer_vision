import cv2
import numpy as np

img = np.zeros((512,512,3))
print(img)
#colouring 
img[200:300,100:200]=0,255,0

#line in image



cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),cv2.FILLED)

cv2.line(img,(0,512),(255,255),(0,255,255),5)

cv2.circle(img,(400,50),30,(0,255,0),2)

cv2.imshow("image",img)


cv2.waitKey(0)



