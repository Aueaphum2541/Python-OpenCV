# เปรียบเทียบค่า BlockSize และ C ใน Adaptive Thresholding
# ในการทำ Adaptive Thresholding แบบ Gaussian และ Mean ตามลำดับ

import cv2
import matplotlib.pyplot as plt
img =cv2.imread('C:\Python\Python OpenCV\image/maps.jpg',0)

# กำหนดขนาด Block
size = [3,5,9,17,33]

plt.subplot(231,xticks=[],yticks=[]) # แสดงรูปภาพแบบ 2 แถว 3 คอลัมน์ และตำแหน่งที่ 1 
plt.imshow(img,cmap='gray') # แสดงรูปภาพในแต่ละตำแหน่ง 

for i in range(len(size)): # ใช้คำสั่ง for ในการวนลูปแสดงรูปภาพ โดยใช้คำสั่ง subplot ของ Matplotlib ในการแสดงรูปภาพ 
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,size[i],1) 
    # ใช้คำสั่ง adaptiveThreshold ในการทำ Adaptive Thresholding แบบ Mean
    plt.subplot(232+i,xticks=[],yticks=[]) # แสดงรูปภาพแบบ 2 แถว 3 คอลัมน์ และตำแหน่งที่ 2 ถึง 6 
    plt.title('%d'%size[i]) # แสดงขนาดของ Block 
    plt.imshow(th2,cmap='gray') # แสดงรูปภาพในแต่ละตำแหน่ง
    plt.xticks([]),plt.yticks([]) # ไม่แสดงค่า x และ y

plt.show()