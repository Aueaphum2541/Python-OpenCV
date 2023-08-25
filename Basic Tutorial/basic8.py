#Viedo GrayScale Mode
import cv2

cap = cv2.VideoCapture("Python OpenCV\image/flower.mp4") # กำหนดตัวแปร cap เพื่อเก็บค่าวิด๊โอที่เปิดด้วย OpenCV 

while(cap.isOpened()): # วนลูปเพื่อแสดงผลวิด๊โอ 
   check , frame = cap.read() # อ่านภาพจากกล้อง  รับภาพจากกล้อง 1 frame ต่อ frame และเก็บไว้ในตัวแปร frame  และเก็บค่า True หรือ False ไว้ในตัวแปร check 
   if check == True: # ถ้า check เป็น True ให้แสดงผลภาพ 
       Gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # แปลงภาพเป็นภาพสีเทา 
       cv2.imshow("Capturing", Gray) # แสดงภาพจากกล้อง  แสดงภาพจากตัวแปร frame  โดยใช้ชื่อหน้าต่างว่า Capturing
       if cv2.waitKey(1) & 0xFF == ord("e"): # รอรับค่าจากคีย์บอร์ด  รอรับค่าจากคีย์บอร์ด 1 วินาที และเก็บค่าที่รับเข้ามาไว้ในตัวแปร key  ถ้าค่า key ที่รับเข้ามาเท่ากับ e ให้หยุดการทำงาน
           break # ออกจาก loop while
   else: # ถ้า check เป็น False ให้แสดงข้อความว่า ไม่สามารถอ่านภาพจากกล้องได้
     break # ออกจาก loop while
print("Cannot read the video file") # แสดงข้อความว่า ไม่สามารถอ่านภาพจากกล้องได้ 
      
cap.release() # ปิดการใช้งานกล้อง 
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด 
