# ตัวกรอง Convolution ด้วย Filter 2D
# การใช้งาน 2D Convolution (Image Filtering) ด้วย cv.filter2D()
# คือการใช้งานการกรองภาพด้วยการคำนวณผลรวมของค่า Pixel ในรูปภาพ โดยใช้ Kernel ที่กำหนดไว้

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Original
img = cv2.imread('C:\Python\Python OpenCV\image/noise.png')
#kernel = np.ones((3,3),np.float32)/9 # กำหนด Kernel 5x5 ที่มีค่าเท่ากัน 25 ค่า และแปลงเป็น float32 ก่อน จากนั้นหารด้วย 25 ค่า หรือ 5x5 ค่า
#convo1 = cv2.filter2D(img,-1,kernel) # ใช้ cv.filter2D() ในการกรองภาพ โดยกำหนด Kernel ที่กำหนดไว้ และแปลงเป็นภาพแบบ Gray Scale ก่อน 
#และแสดงผลลัพธ์ ด้วย cv.imshow() และ cv.imwrite() ตามลำดับ และแสดงผลลัพธ์ด้วย plt.imshow() และ plt.show() ตามลำดับ ดังนี้  
convo1 = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
convol2 = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

titles = ['Original Image', 'Convolution 3x3', 'Convolution 5x5']
images = [img, convo1, convol2]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()