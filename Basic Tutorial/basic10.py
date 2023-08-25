# วาดเส้นตรง โดยใช้ cv2.line() และ cv2.arrowedLine() 
import cv2 

# อ่านภาพจากไฟล์
img= cv2.imread('Python OpenCV\image\cat.jpg') # อ่านภาพจากไฟล์ cat.jpg แล้วเก็บไว้ในตัวแปร img 

# กำหนดขนาด
imgresize = cv2.resize(img,(700,700)) # ปรับขนาดภาพให้กว้าง 700 และสูง 700 แล้วเก็บไว้ในตัวแปร imgresize

# วาดเส้นตรง 
# line (ภาพ, จุดเริ่มต้น(x,y), จุดสิ้นสุด(x,y), สี (BGR), ความหนา)
cv2.arrowedLine(imgresize, (100,100), (200,300), (0,0,255), 5) # วาดเส้นตรงจากจุด (100,100) ไปยังจุด (200,300) สีแดง ความหนา 5 แล้วเก็บไว้ในตัวแปร imgresize 
cv2.arrowedLine(imgresize, (550,500), (300,300), (0,255,0), 5)
cv2.arrowedLine(imgresize, (400,100), (250,350), (255,0,0), 5)
cv2.imshow("Output",imgresize) # แสดงภาพ imgresize ในหน้าต่างชื่อ Output 
cv2.waitKey(0) # รอกดปุ่มใดๆเพื่อปิดหน้าต่าง
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด
