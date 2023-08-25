# แสดงวันเวลาในกล้อง/วิดีโอ
# โดยใช้ฟังก์ชัน cv2.putText() แสดงข้อความ
import cv2 # ใช้งาน OpenCV ใน Python 
import datetime # ใช้งาน datetime ใน Python

cap = cv2.VideoCapture("Python OpenCV\image/flower.mp4") # อ่านวิดีโอ มาเก็บในตัวแปร cap 
while (cap.isOpened()): # วนลูปเรื่อยๆ จนกว่าจะกดปุ่ม e
    check , frame = cap.read() # รับภาพจากกล้อง/วิดีโอ frame ต่อ frame

    if check == True:
        currentDate = str(datetime.datetime.now()) # อ่านวันเวลาปัจจุบัน มาเก็บในตัวแปร currentDate
        cv2.putText(frame,currentDate,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2) 
        # แสดงข้อความ OpenCV ในภาพ ตำแหน่ง (10,50) ขนาด 1 สีดำ ความหนา 2 พิกเซล 
        cv2.imshow("My Video",frame) # แสดงภาพจากกล้อง/วิดีโอ
        if cv2.waitKey(1) & 0xFF == ord('e'): # รอกดปุ่ม e ถ้ากด e ให้หยุด
            break
    else:
        break

cap.release() # ปิดกล้อง/วิดีโอ
cv2.destroyAllWindows() # ปิดหน้าต่างทั้งหมด
