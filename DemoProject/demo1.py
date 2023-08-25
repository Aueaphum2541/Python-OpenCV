# ตรวจจับรถยนต์ และ จำนวนรถยนต์ที่ผ่าน
# โดยใช้วิธีการตรวจจับรูปแบบรถยนต์


import cv2
# อ่านภาพ
cap = cv2.VideoCapture('C:\Python\Python OpenCV\image/Car running.mp4')

# อ่านไฟล์ Haar Cascade Classifier
car_cascade = cv2.CascadeClassifier('C:\Python\Python OpenCV\image\cars.xml') # รถยนต์ (Cars) 

# แสดงผลวิด๊โอ
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # แปลงภาพเป็นสีเทา
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        # ตรวจจับใบหน้า
        cars = car_cascade.detectMultiScale(gray, 1.1, 4) 
        # วาดกล่องรอบใบหน้า
        for (x, y, w, h) in cars: 
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), thickness=2) 
        # แสดงผล
        cv2.imshow('frame', frame)
        # กด q เพื่อออกจากการทำงาน
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()




