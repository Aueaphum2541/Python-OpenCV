# ฟังก์ชัน Threshold ใน OpenCV
import cv2
gray_img = cv2.imread('C:\Python\Python OpenCV\image/bw grad.png')

thresh,result1 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY) 
# ฟังก์ชัน Threshold ใน OpenCV ที่ใช้ในการแปลงรูปภาพเป็นรูปภาพแบบเท็นเซล 
#โดยใช้ค่าเกณฑ์ 128 และค่าสูงสุด 255 และเลือกใช้เท็นเซล 2 ค่า คือ 0 และ 255 โดย 0 คือสีดำ และ 255 คือสีขาว 
# และเก็บผลลัพธ์ไว้ในตัวแปร result และเก็บค่าเกณฑ์ที่ใช้ไว้ในตัวแปร thresh และแสดงผลลัพธ์ โดยใช้ฟังก์ชัน imshow ของ OpenCV
#  และใช้คำสั่ง waitKey 0 ในการรอการกดปุ่มใดๆ จากคีย์บอร์ด เพื่อปิดหน้าต่าง และทำการลบหน้าต่างที่เปิดออกจากหน่วยความจำ 
# โดยใช้คำสั่ง destroyAllWindows ของ OpenCV ดังตัวอย่างด้านล่าง ซึ่งจะแสดงผลลัพธ์ดังรูปภาพด้านล่าง 
thresh,result2 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY_INV) 
thresh,result3 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TRUNC)
thresh,result4 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO)
thresh,result5 = cv2.threshold(gray_img, 128, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Original', gray_img)
cv2.imshow('Binary', result1)
cv2.imshow('Binary Inverse', result2)
cv2.imshow('Truncate', result3)
cv2.imshow('To Zero', result4)
cv2.imshow('To Zero Inverse', result5)
cv2.waitKey(0)
cv2.destroyAllWindows()


