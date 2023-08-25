# เปิดวิด๊โอด้วย OpenCV และแสดงผล โดยใช้ฟังก์ชัน cv2.VideoCapture() และ cv2.imshow() 
# พร้อมกับการกำหนดความกว้าง และความสูงของวิด๊โอ และกำหนดค่า FPS (Frame Per Second) ของวิด๊โอ และกำหนดชื่อของหน้าต่างที่แสดงผล 
# พร้อมกับการกำหนดค่าสีของหน้าต่างที่แสดงผล และการกำหนดค่าสีของตัวอักษรที่แสดงผล 
# พร้อมกับการกำหนดค่าสีของตัวอักษรที่แสดงผล และการกำหนดค่าสีของตัวอักษรที่แสดงผล
import cv2  # ใช้งาน OpenCV ใน Python 

cap = cv2.VideoCapture("Python OpenCV\image/flower.mp4") # กำหนดตัวแปร cap เพื่อเก็บค่าวิด๊โอที่เปิดด้วย OpenCV 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # กำหนดความกว้างของวิด๊โอ
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # กำหนดความสูงของวิด๊โอ
cap.set(cv2.CAP_PROP_FPS, 30) # กำหนดค่า FPS (Frame Per Second) ของวิด๊โอ

while(cap.isOpened()): # วนลูปเพื่อแสดงผลวิด๊โอ 
   check , frame = cap.read() # อ่านภาพจากกล้อง  รับภาพจากกล้อง 1 frame ต่อ frame และเก็บไว้ในตัวแปร frame  และเก็บค่า True หรือ False ไว้ในตัวแปร check 
   if check == True: # ถ้า check เป็น True ให้แสดงผลภาพ 
       cv2.imshow("Capturing", frame) # แสดงภาพจากกล้อง  แสดงภาพจากตัวแปร frame  โดยใช้ชื่อหน้าต่างว่า Capturing
       print(check) # แสดงค่า check ที่เก็บไว้ในตัวแปร check
       print(frame) # แสดงค่า frame ที่เก็บไว้ ในตัวแปร frame
       if cv2.waitKey(1) & 0xFF == ord("e"): # รอรับค่าจากคีย์บอร์ด  รอรับค่าจากคีย์บอร์ด 1 วินาที และเก็บค่าที่รับเข้ามาไว้ในตัวแปร key  ถ้าค่า key ที่รับเข้ามาเท่ากับ e ให้หยุดการทำงาน
           break # ออกจาก loop while
   else: # ถ้า check เป็น False ให้แสดงข้อความว่า ไม่สามารถอ่านภาพจากกล้องได้
     break # ออกจาก loop while
print("Cannot read the video file") # แสดงข้อความว่า ไม่สามารถอ่านภาพจากกล้องได้ 
      
cap.release() # ปิดการใช้งานกล้อง 
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด 


