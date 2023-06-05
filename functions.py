import cv2
import numpy as np

# Read the image from the specified path
img = cv2.imread(r"C:\Users\Abhishek\PycharmProjects\pythonProject\Resources\car.jpeg")

# Create a kernel of size 5x5 with all ones
kernal = np.ones((5, 5))

# Convert the image to grayscale
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur with a kernel size of (7, 7) to the grayscale image
imgblur = cv2.GaussianBlur(imgGrey, (7, 7), 0)

# Perform edge detection on the original image using Canny edge detection algorithm
imgCanny = cv2.Canny(img, 150, 200)

# Dilate the original image using the defined kernel and 1 iteration
imgDilation = cv2.dilate(img, kernal, iterations=1)

# Erode the original image using the defined kernel and 1 iteration
imgEroded = cv2.erode(img, kernal, iterations=1)

# Display the original image
cv2.imshow("image", img)

# Display the grayscale image
cv2.imshow("grey image", imgGrey)

# Display the blurred image
cv2.imshow("Blur image", imgblur)

# Display the edge-detected image
cv2.imshow("Edge detect - image", imgCanny)

# Display the dilated image
cv2.imshow("dilated image", imgDilation)

# Display the eroded image
cv2.imshow("Eroded image", imgEroded)

# Wait for a key press to exit
cv2.waitKey(0)
