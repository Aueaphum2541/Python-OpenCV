# ตัวกรองค่ามัธยฐาน (Median Filter)
# ในการกรองภาพด้วยการคำนวณค่า Pixel ในรูปภาพ โดยใช้ Kernel ที่กำหนดไว้ และแปลงเป็นภาพแบบ Gray Scale ก่อน
# และแสดงผลลัพธ์ ด้วย cv.imshow() และ cv.imwrite() ตามลำดับ ดังนี้

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Original
img = cv2.imread('C:\Python\Python OpenCV\image/noise.png')

# Filter
filter2D = cv2.filter2D(img, -1, np.ones((5,5),np.float32)/25)

# Blur
mean = cv2.blur(img,(5,5))

# Median
median = cv2.medianBlur(img,5)

titles = ['Original Image', 'Filter 2D', 'Mean', 'Median']
images = [img, filter2D, mean, median]

for i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()