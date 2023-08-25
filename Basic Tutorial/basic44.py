# ตรวจจับขอบภาพด้วย Laplacian Method
# โดยใช้ฟังก์ชัน cv2.Laplacian()

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:\Python\Python OpenCV\image/coin.png',0)

laplacian=cv2.Laplacian(img,-1) # ตรวจจับขอบภาพด้วย Laplacian Method โดยใช้ฟังก์ชัน cv2.Laplacian() 
#โดยใช้ค่าความเข้มของขอบเป็นค่าเริ่มต้น -1 หรือ ค่าเริ่มต้น 0 หรือ 1

images = [img,laplacian]
titles = ['Original','Laplacian']

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],cmap='gray') # แสดงรูปภาพ แบบ gray scale 
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

