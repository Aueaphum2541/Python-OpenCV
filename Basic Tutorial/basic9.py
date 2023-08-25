# การอัดวิดีโอ และ บันทึกวิดีโอ ด้วย Python OpenCV ใช้คำสั่ง VideoWriter โดยมีคำสั่งดังนี้ 
# VideoWriter(filename, fourcc, fps, frameSize[, isColor]) -> retval
# filename ชื่อไฟล์ที่ต้องการบันทึก
# fourcc รหัสการเข้ารหัสวิดีโอ ใช้คำสั่ง VideoWriter_fourcc() ในการกำหนด
# fps ความเร็วของวิดีโอ
# frameSize ขนาดของภาพ
# isColor ถ้าเป็น True จะบันทึกวิดีโอสี ถ้าเป็น False จะบันทึกวิดีโอดำ
# retval คืนค่าว่าสามารถเขียนไฟล์ได้หรือไม่
# การกำหนดค่า fourcc ใช้คำสั่ง VideoWriter_fourcc() โดยมีคำสั่งดังนี้
# VideoWriter_fourcc(c1, c2, c3, c4) -> retval
# c1 ตัวอักษรแรก
# c2 ตัวอักษรที่สอง
# c3 ตัวอักษรที่สาม
# c4 ตัวอักษรที่สี่
# retval คืนค่ารหัสการเข้ารหัสวิดีโอ
# ตัวอย่างการกำหนดค่า fourcc ให้กับวิดีโอ
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# หรือ
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

import cv2 # ใช้งาน OpenCV ในการประมวลผลภาพ วิดีโอ และ ระบบคอมพิวเตอร์ตามที่ต้องการ 
cap = cv2.VideoCapture(0) # กำหนดให้ cap เป็นตัวแปรสำหรับเก็บวิดีโอจากกล้อง 0 คือกล้องหน้า 

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') # กำหนดรหัสการเข้ารหัสวิดีโอ 
result = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) # กำหนดค่าการบันทึกวิดีโอ 

while(cap.isOpened()): # วนลูปเพื่อแสดงผลวิด๊โอ 
   check , frame = cap.read() # อ่านภาพจากกล้อง  รับภาพจากกล้อง 1 frame ต่อ frame และเก็บไว้ในตัวแปร frame  และเก็บค่า True หรือ False ไว้ในตัวแปร check 
   
   if check == True: # ถ้า check เป็น True ให้แสดงผลภาพ 
       cv2.imshow("Output", frame) # แสดงภาพจากกล้อง  แสดงภาพจากตัวแปร frame  โดยใช้ชื่อหน้าต่างว่า Capturing
       result.write(frame) # บันทึกวิดีโอ 
       if cv2.waitKey(1) & 0xFF == ord("e"): # รอรับค่าจากคีย์บอร์ด  รอรับค่าจากคีย์บอร์ด 1 วินาที และเก็บค่าที่รับเข้ามาไว้ในตัวแปร key  ถ้าค่า key ที่รับเข้ามาเท่ากับ e ให้หยุดการทำงาน
           break # ออกจาก loop while
   
# Release everything if job is finished
result.release() # ปิดการบันทึกวิดีโอ
cap.release() # ปิดการเชื่อมต่อกล้อง 
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด