# Step 1: Import required libraries. 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 2: We will read the image by using “cv2.imread(image-name)” 
# command & then convert this image into grayscale image using “cv2.cvtColor(image-name, cv2.COLOR_BGR2GRAY)” command.
image = cv2.imread('C:\Python\Python OpenCV\image/coin.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#plt.imshow(gray, cmap='gray')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows

#Step 3: For counting, we have to detect the edges but before detecting the edges 
# we have to make the image blur to avoid the noises. Use “cv2.GaussianBlur(image-name, Kernal size, std. deviation)”. 
blur = cv2.GaussianBlur(gray, (11, 11), 0)
plt.imshow(blur, cmap='gray')

# Step 4:  Now we will detect edges using a canny algorithm, 2nd & 3rd parameters in cv2.canny() 
# function are threshold values. a value between 30 & 150 are consider as an edge for this image.
canny = cv2.Canny(blur, 30, 150, 3)
plt.imshow(canny, cmap='gray')

#Step 5: We can see that edges are not connected. We need to connect the edges, have to make more thiker & visible. 
dilated = cv2.dilate(canny, (1, 1), iterations=0)
plt.imshow(dilated, cmap='gray')

#Step 6: Now we have to calculate the contour in the image & convert the image into RGB from BGR & then draw the contours.
(cnt, hierarchy) = cv2.findContours(
	dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

plt.imshow(rgb)

#Step 7: Printing the result
print("coins in the image : ", len(cnt))

