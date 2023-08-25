# วาดสี่เหลี่ยม (Draw Rectangle)

import cv2
# อ่านภาพจากไฟล์
img= cv2.imread('Python OpenCV\image\cat.jpg') # อ่านภาพจากไฟล์ cat.jpg แล้วเก็บไว้ในตัวแปร img

# กำหนดขนาด
imgresize = cv2.resize(img,(700,700)) # ปรับขนาดภาพให้กว้าง 700 และสูง 700 แล้วเก็บไว้ในตัวแปร imgresize

# วาดสี่เหลี่ยม
# rectangle (ภาพ, จุดเริ่มต้น(x,y), จุดสิ้นสุด(x,y), สี (BGR), ความหนา)
cv2.rectangle(imgresize, (0,0), (200,200), (0,0,255), 5) # วาดสี่เหลี่ยมจากจุด (0,0) ไปยังจุด (200,200) สีแดง ความหนา 5 แล้วเก็บไว้ในตัวแปร imgresize 
cv2.rectangle(imgresize, (500,500), (600,600), (0,0,255), -1) # วาดสี่เหลี่ยมจากจุด (500,500) ไปยังจุด (600,600) สีแดง ความหนา -1 แล้วเก็บไว้ในตัวแปร imgresize
cv2.imshow("Output",imgresize) # แสดงภาพ imgresize ในหน้าต่างชื่อ Output
cv2.waitKey(0) # รอกดปุ่มใดๆเพื่อปิดหน้าต่าง
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด

