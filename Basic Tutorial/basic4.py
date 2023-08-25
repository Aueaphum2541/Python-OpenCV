# กำหนดรูปแบบของภาพ
# กำหนดค่าสีของภาพ
# กำหนดขนาดของภาพ
# กำหนดชื่อของหน้าต่าง
# แสดงภาพ
# รอการกดปุ่ม
# ปิดหน้าต่าง

# รูปแบบของภาพ
import cv2  # โหลด OpenCV เข้ามาใช้งาน โดยตั้งชื่อว่า cv2 
# กำหนดค่าสีของภาพ 
img= cv2.imread('Python OpenCV\image\cat.jpg',0)  # อ่านภาพ cat.jpg และกำหนดให้เป็นภาพดำ-ขาว โดยตั้งชื่อว่า img  
img1= cv2.imread('Python OpenCV\image\cat.jpg',1)  # อ่านภาพ cat.jpg และกำหนดให้เป็นภาพสี โดยตั้งชื่อว่า img1  
img2 = cv2.imread('Python OpenCV\image\cat.jpg',-1)  # อ่านภาพ cat.jpg และกำหนดให้เป็นภาพสี โดยระบุค่าสีแบบเต็ม และเก็บค่าในตัวแปร img2 

# แสดงภาพ
cv2.imshow('image',img)  # แสดงภาพที่อ่านมา
cv2.imshow('image1',img1)  # แสดงภาพที่อ่านมา
cv2.imshow('image2',img2)  # แสดงภาพที่อ่านมา 
cv2.waitKey(0)  # รอการกดปุ่ม
cv2.destroyAllWindows()  # ปิดหน้าต่าง 
