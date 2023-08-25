# ตัวกรองค่าเฉลี่ย (Average Filter)
# ในการกรองภาพด้วยการคำนวณผลรวมของค่า Pixel ในรูปภาพ โดยใช้ Kernel ที่กำหนดไว้ และแปลงเป็นภาพแบบ Gray Scale ก่อน 
# และแสดงผลลัพธ์ ด้วย cv.imshow() และ cv.imwrite() ตามลำดับ ดังนี้

import cv2
from cv2 import filter2D
from cv2 import mean
import numpy as np
import matplotlib.pyplot as plt

# Original
img = cv2.imread('C:\Python\Python OpenCV\image/noise.png')

# Filter
filter2D = cv2.filter2D(img, -1, np.ones((5,5),np.float32)/25)

# Blur
mean = cv2.blur(img,(5,5))

titles = ['Original Image', 'Filter 2D', 'Mean']
images = [img, filter2D, mean]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()