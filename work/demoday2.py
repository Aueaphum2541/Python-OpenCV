import cv2  # import OpenCV
import numpy as np  # import numpy
cap = cv2.VideoCapture(0)  # กำหนดให้เปิดกล้อง 0
ret, frame1 = cap.read()  # อ่านภาพจากกล้อง
ret, frame2 = cap.read()  # อ่านภาพจากกล้อง
while cap.isOpened():  # วนลูปเมื่อกล้องเปิดอยู่
    diff = cv2.absdiff(frame1, frame2)  # คำนวณต่าง
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # แปลงเป็นระดับสีเทา
    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # ลบเสียง
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # กำหนดค่าเป้าหมาย
    dilated = cv2.dilate(thresh, None, iterations=3)  # ขยายรูป
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # ค้นหาเส้นรอบวง
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)  # วาดเส้นรอบวง
        if cv2.contourArea(contour) < 900:  # กำหนดขนาด
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)  # วาดเส้นรอบวง
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)  # แสดงข
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)  # วาดเส้นรอบวง
    cv2.imshow("feed", frame1)  # แสดงภาพ
    frame1 = frame2  # กำหนดค่าใหม่
    ret, frame2 = cap.read()  # อ่านภาพจากกล้อง
    if cv2.waitKey(40) == 27:  # กดปุ่ม ESC เพื่อออก
        break