# การใช้งาน Adaptive Thresholding แบบ Gaussian และ Mean โดยใช้ฟังก์ชัน cv2.adaptiveThreshold() และ cv2.adaptiveThreshold() 
# ในการทำ Adaptive Thresholding แบบ Gaussian และ Mean ตามลำดับ 
import cv2
import matplotlib.pyplot as plt
img =cv2.imread('C:\Python\Python OpenCV\image/maps.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh,th1 = cv2.threshold(imgGray,128,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

'''
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
'''

images = [imgGray,th1,th2,th3] # สร้าง list ของรูปภาพ 6 รูป โดยใช้คำสั่ง imshow ของ OpenCV
titles = ['Original','Binary','Thresh Mean','Thresh Gaussian'] # กำหนดชื่อของรูปภาพ 6 รูปภาพ โดยใช้ list ของ Python 

for i in range(len(images)): # ใช้คำสั่ง for ในการวนลูปแสดงรูปภาพ โดยใช้คำสั่ง subplot ของ Matplotlib ในการแสดงรูปภาพ  
    plt.subplot(2,2,i+1) # แสดงรูปภาพแบบ 2 แถว 3 คอลัมน์ และตำแหน่งที่ i+1 
    plt.imshow(images[i],'gray') # แสดงรูปภาพในแต่ละตำแหน่ง 
    plt.title(titles[i]) # แสดงชื่อรูปภาพในแต่ละตำแหน่ง
    plt.xticks([]),plt.yticks([]) # ไม่แสดงค่าแกน x และค่าแกน y 
plt.show() # แสดงรูปภาพทั้งหมด

cv2.waitKey(0)
cv2.destroyAllWindows()