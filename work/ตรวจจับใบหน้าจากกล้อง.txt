# ตรวจจับใบหน้าจากคลิปวิด๊โอ
# โดยใช้ Haar Cascade ในการตรวจจับใบหน้า

import cv2
# อ่านภาพ
cap = cv2.VideoCapture(0)

# อ่านไฟล์ Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier('C:\Python\Python OpenCV\image\haarcascade_frontalface_default.xml') # ใบหน้า (Frontal Face) 

# แสดงผลวิด๊โอ
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # แปลงภาพเป็นสีเทา
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ตรวจจับใบหน้า
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # วาดกล่องรอบใบหน้า
        for (x, y, w, h) in faces:
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




