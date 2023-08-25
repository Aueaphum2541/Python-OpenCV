# ตรวจจับใบหน้าจากภาพ (Face Detection)
# โดยใช้ Haar Cascade Classifier ที่เตรียมไว้ให้
# โดยใช้ภาพที่มีใบหน้ามากกว่า 1 ใบ
# และใช้ภาพที่มีใบหน้าที่มีขนาดต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีตำแหน่งต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีหมุนต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีแสงต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีเงาต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีเส้นตาต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีเส้นปากต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีเส้นคิ้วต่างกัน
# และใช้ภาพที่มีใบหน้าที่มีเส้นคางต่างกัน

import cv2

# อ่านภาพ
img = cv2.imread('C:\Python\Python OpenCV\image/boy.jpg')
img = cv2.resize(img, (500,500)) 

# อ่านไฟล์ Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier('C:\Python\Python OpenCV\image\haarcascade_frontalface_default.xml') # ใบหน้า (Frontal Face) 

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# จำแนกใบหน้า
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.30, minNeighbors=3) 
 # scaleFactor=1.20 คือ ขนาดของรูปภาพที่จะตรวจจับ 1.20 เท่าของรูปภาพเดิม 
 # minNeighbors=3 คือ จำนวนของเส้นที่ตรงกันที่จะตรวจจับใบหน้า 3 เส้นขึ้นไป การกำหนดค่า Threshholding ตรวจสอบ Gray Scale ของภาพ 
 # ค่าเริ่มต้น 1.1 และ 3 คือค่าที่ดีที่สุด แต่ถ้าใบหน้ามีขนาดเล็ก ให้เปลี่ยนเป็น 1.05 และ 5 แทน และถ้าใบหน้ามีขนาดใหญ่ ให้เปลี่ยนเป็น 1.15 และ 1 แทน 

# แสดงตำแหน่งใบหน้าที่ตรวจจับได้
for x,y,w,h in faces: # วนลูปตามจำนวนใบหน้าที่ตรวจจับได้  (x,y) คือตำแหน่งซ้ายบน และ (w,h) คือความกว้างและความสูง
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) # วาดสี่เหลี่ยม สีเขียว หนา 5 pixel 

# แสดงภาพ
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


