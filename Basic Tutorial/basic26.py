# การสร้าง Color Trackbar
# สร้าง Trackbar เบื้องต้น สำหรับการปรับค่าสี

import cv2
import numpy as np

img = np.zeros((200,250,3), np.uint8) # สร้างรูปภาพขาวดำ ขนาด 200x250 และ 3 ช่องสี 
cv2.namedWindow('Color Trackbar') # สร้างหน้าต่าง Color Trackbar 

def display(value): # ฟังก์ชันสำหรับแสดงผล ตามค่าที่ปรับ Trackbar ได้ โดยจะแสดงผลในหน้าต่าง Color Trackbar ที่สร้างไว้ และแสดงผลในรูปภาพ img ด้วย 
     pass
    #โดยใช้ค่าที่ปรับได้จาก Trackbar มากำหนดค่าสีให้กับ img ด้วย ซึ่งจะแสดงผลในหน้าต่าง Color Trackbar ที่สร้างไว้ ดังรูป ด้านล่าง 
    

# เรื่มต้นสร้าง Trackbar สำหรับการปรับค่าสี
cv2.createTrackbar('B', 'Color Trackbar', 0, 255, display) # สีน้ำเงิน 0-255 ค่าเริ่มต้น 0 
cv2.createTrackbar('G', 'Color Trackbar', 0, 255, display) # สีเขียว 0-255 ค่าเริ่มต้น 0 
cv2.createTrackbar('R', 'Color Trackbar', 0, 255, display) # สีแดง 0-255 ค่าเริ่มต้น 0

while True:
    cv2.imshow('Color Trackbar', img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

    # ดึงค่าจาก Trackbar มาใช้งาน
    b = cv2.getTrackbarPos('B', 'Color Trackbar') # ดึงค่าสีน้ำเงิน (Blue) มาใช้งาน 
    g = cv2.getTrackbarPos('G', 'Color Trackbar') # ดึงค่าสีเขียว (Green) มาใช้งาน
    r = cv2.getTrackbarPos('R', 'Color Trackbar') # ดึงค่าสีแดง (Red) มาใช้งาน
    
    img[:] = [b,g,r] # กำหนดค่าสีให้กับ img ด้วยค่าที่ได้จาก Trackbar แต่ละช่อง โดยใช้ค่าสีในรูปแบบ BGR
    # แสดงค่าสีที่ปรับได้
    print(b, g, r)


cv2.waitKey(0)
cv2.destroyAllWindows()