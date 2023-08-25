# วาดวงกลม (Draw Circle)
# วาดวงกลมด้วยฟังก์ชัน cv2.circle() โดยระบุพิกัดศูนย์กลาง และรัศมี
# พิกัดศูนย์กลาง (x,y) และรัศมี (r) ของวงกลม

import cv2

# อ่านรูปภาพ 
img = cv2.imread('Python OpenCV\image\cat.jpg') # รูปภาพจะถูกอ่านเป็นสี (Color) แบบ BGR (Blue-Green-Red) 

# กำหนดขนาด 
imgresize = cv2.resize(img,(700,700)) # กำหนดขนาดให้รูปภาพ 700x700 pixel 

# วาดวงกลม
cv2.circle(imgresize,(350,350), 100, (0,0,255), 5) # วาดวงกลม พิกัดศูนย์กลาง (350,350) รัศมี 100 สีแดง (0,0,255) และความหนา 5 pixel

# แสดงรูปภาพ
cv2.imshow('img',imgresize) # แสดงรูปภาพ
cv2.waitKey(0) # รอกดปุ่มใดๆเพื่อปิดหน้าต่าง
cv2.destroyAllWindows() # ปิดหน้าต่าง