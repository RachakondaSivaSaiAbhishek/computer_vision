import cv2
import numpy as np

# Load the image
img = cv2.imread("Rsources/leans.png")

# Perform horizontal concatenation
imgHor = np.hstack((img, img))

# Display the horizontally concatenated image
cv2.imshow("Horizontal", imgHor)

# Perform vertical concatenation
imgVer = np.vstack((img, img))

# Display the vertically concatenated image
cv2.imshow("Vertical", imgVer)

# Wait for a key press to exit
cv2.waitKey(0)
