# เปิดกล้องด้วย OpenCV
# แสดงภาพจากกล้อง
# กดปุ่ม q เพื่อออกจากโปรแกรม
import cv2  # ใช้งาน OpenCV ใน Python 

cap = cv2.VideoCapture(0) # กำหนดให้เปิดกล้อง 0 หรือ 1 หรือ 2 ตามต้องการ ถ้ามีหลายกล้อง 0 คือกล้องหลัก 1 คือกล้องรอง 2 คือกล้องรองรอง และตามลำดับ 

while(True): # วนซ้ำไปเรื่อยๆ 
   check , frame = cap.read() # อ่านภาพจากกล้อง  รับภาพจากกล้อง 1 frame ต่อ frame และเก็บไว้ในตัวแปร frame  และเก็บค่า True หรือ False ไว้ในตัวแปร check 
   cv2.imshow("Capturing", frame) # แสดงภาพจากกล้อง  แสดงภาพจากตัวแปร frame  โดยใช้ชื่อหน้าต่างว่า Capturing
   print(check) # แสดงค่า check ที่เก็บไว้
   print(frame) # แสดงค่า frame ที่เก็บไว้

   if cv2.waitKey(1) & 0xFF == ord("e"): # รอรับค่าจากคีย์บอร์ด  รอรับค่าจากคีย์บอร์ด 1 วินาที และเก็บค่าที่รับเข้ามาไว้ในตัวแปร key  ถ้าค่า key ที่รับเข้ามาเท่ากับ e ให้หยุดการทำงาน
      break # ออกจาก loop while

cap.release() # ปิดการใช้งานกล้อง
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด
