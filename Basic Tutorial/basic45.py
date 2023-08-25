# ตรวจจับขอบภาพด้วย canny edge detection
# โดยใช้ฟังก์ชัน cv2.Canny()  

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:\Python\Python OpenCV\image/coin.png',0)

canny=cv2.Canny(img,50,200) # ตรวจจับขอบภาพด้วย canny edge detection โดยใช้ฟังก์ชัน cv2.Canny()
images = [img,canny]
titles = ['Original','Canny']

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],cmap='gray') # แสดงรูปภาพ แบบ gray scale 
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

