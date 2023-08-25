# ตรวจจับขอบภาพ (Edge Detection)
# sobel Method

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:\Python\Python OpenCV\image/coin.png',0)

# Sobel Method's Edge Detection
# ตรวจจับขอบแนวนอน # ค่า ksize ควรเป็นคู่ 3,5,7,9,11 หรือ 1 
#ถ้าไม่ต้องการใช้ ksize ให้ใส่ 0 แทน ค่า ksize มีผลต่อความละเอียดของขอบ และเวลาที่ใช้ในการคำนวณ ค่า ksize มาก จะใช้เวลานาน และมีความละเอียดขอบสูง 
#แต่ถ้าค่า ksize น้อย จะใช้เวลาน้อย และมีความละเอียดขอบต่ำ แต่ถ้าค่า ksize เป็น 0 จะใช้ค่า ksize ที่เหมาะสมตามตัวอักษร 
# ซึ่งค่า ksize ที่เหมาะสมตามตัวอักษร จะมีค่าเท่ากับ 3 หรือ 5 และมีความละเอียดขอบสูง และใช้เวลานาน แต่ถ้าค่า ksize เป็น 1 จะใช้เวลาน้อย 
# #และมีความละเอียดขอบต่ำ แต่ถ้าค่า ksize เป็น 3 หรือ 5 จะใช้เวลานาน และมีความละเอียดขอบสูง แต่ถ้าค่า ksize เป็น 7 หรือ 9 จะใช้เวลานาน
#  และมีความละเอียดขอบสูง แต่ถ้าค่า ksize เป็น 11 จะใช้เวลานาน และมีความละเอียดขอบสูง 
sobelx=cv2.Sobel(img,-1,1,0,ksize=5) # cv2.CV_64F คือ ค่าที่เก็บได้ 64 bit #  sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(img,-1,0,1,ksize=5) 
sobelxy=cv2.bitwise_or(sobelx,sobely) # รวมขอบแนวนอนและแนวตั้ง ด้วย bitwise_or หรือ bitwise_and หรือ bitwise_xor หรือ bitwise_not 


'''
cv2.imshow('Output',img)
cv2.imshow('Sobel X',sobelx)
cv2.imshow('Sobel Y',sobely)
cv2.imshow('Sobel XY',sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
images = [img,sobelx,sobely,sobelxy]
titles = ['Original','Sobel X','Sobel Y','Sobel XY']

for i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],cmap='gray') # แสดงรูปภาพ แบบ gray scale 
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
