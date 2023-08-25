# แสดงผลภาพ
import cv2  # โหลด OpenCV เข้ามาใช้งาน โดยตั้งชื่อว่า cv2 
img= cv2.imread('Python OpenCV\image\cat.jpg')  # อ่านภาพ cat.jpg

# แสดงภาพ 
cv2.imshow('Output',img) # แสดงภาพ โดยใช้ชื่อ 'Output' แสดงผล และใช้ img แสดงผล 
cv2.waitKey(delay=5000) # รอ 5 วินาที ก่อนปิด หรือกดปุ่มใดก็ได้ ในระหว่างรอ จะทำงานต่อไปได้ 
cv2.destroyAllWindows() # ปิดหน้าต่าง และ ปิดโปรแกรม  (ถ้ามีหลายหน้าต่าง ให้ปิดทั้งหมด) 