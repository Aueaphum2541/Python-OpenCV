# ตรวจจับดวงตาจากวิดีโอ (Eye Detection from Video)

import cv2
# อ่านภาพ
cap = cv2.VideoCapture('C:\Python\Python OpenCV\image/face.mp4')

# อ่านไฟล์ Haar Cascade Classifier
eye_cascade = cv2.CascadeClassifier('C:\Python\Python OpenCV\image\haarcascade_eye_tree_eyeglasses.xml') # ใบหน้า (Frontal Face) 

# แสดงผลวิด๊โอ
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # แปลงภาพเป็นสีเทา
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ตรวจจับดวงตา
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
        # วาดกล่องรอบดวงตา
        for (x, y, w, h) in eyes:
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




