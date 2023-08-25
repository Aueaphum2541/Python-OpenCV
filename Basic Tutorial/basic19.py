# ตรวจจับกลุ่มวัตถุจากสี (Detecting object by color)
# โดยใช้ฟังก์ชัน cv2.inRange() และ cv2.bitwise_and()
# ซึ่งจะเห็นว่าการตรวจจับสีจะมีความแม่นยำมากกว่าการตรวจจับขอบ
# แต่จะมีข้อจำกัดในการตรวจจับสีเพราะสีจะมีความแตกต่างกันไปตามแสง
# และสีจะมีความแตกต่างกันไปตามสภาพแวดล้อม
# ซึ่งการตรวจจับสีจะมีความแม่นยำมากกว่าการตรวจจับขอบ

import cv2
import numpy 

# อ่านภาพ

while True: # วนซ้ำไปเรื่อยๆ
    img = cv2.imread('C:\Python\Python OpenCV\image/candy.jpg')
    img = cv2.resize(img, (400,400)) # ปรับขนาดภาพ

    # ช่วงสีของสี BGR
    lower = numpy.array([5, 111, 10]) # สีเขียวเข้ม
    upper = numpy.array([124, 255, 133]) # สีเขียวอ่อน

    mask = cv2.inRange(img, lower, upper) # ตรวจจับสี
    result = cv2.bitwise_and(img, img, mask=mask) # แสดงสีที่ตรวจจับได้
    
    if cv2.waitKey(0) & 0xFF == ord('e'): # กดปุ่ม e ในคีย์บอร์ดเพื่อออกจากโปรแกรม
        break # ออกจากการวนซ้ำ
    cv2.imshow('Original', img) # แสดงภาพต้นฉบับ
    cv2.imshow('Mask', mask) # แสดงภาพสีที่ตรวจจับได้
    cv2.imshow('Result', result) # แสดงภาพสีที่ตรวจจับได้

cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด

