# ติดตามการเคลื่อนไหว (Motion Tracker)
# Motion Detection and Tracking
import cv2  
import datetime
cap = cv2.VideoCapture('C:\Python\Python OpenCV\image\demo4.mp4')
check, frame1 = cap.read()
check, frame2 = cap.read()

while (cap.isOpened()):
 # แสดงวันเวลา
 font = cv2.FONT_HERSHEY_SIMPLEX # กำหนดแบบอักษร 
 text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) # กำหนดข้อความ และ ค่าของความกว้าง และ ความสูง 
 datet = str(datetime.datetime.now()) # อ่านวันที่ และเวลา จากระบบ และ กำหนดให้ datet เก็บข้อมูล
 #frame = cv2.putText(frame1, datet, (10,50), font, 1,(255,0,0), 2, cv2.LINE_AA) # แสดงวันเวลาบนภาพ 
 if check == True:
        motiondiff=cv2.absdiff(frame1, frame2) # หาค่าต่างของภาพ 2 ภาพ แล้วเก็บไว้ในตัวแปร motiondiff ซึ่งเป็นภาพแบบ grayscale 
        #และเป็นภาพแบบ binary ค่าสี 0 คือ สีดำ ค่าสี 255 คือ สีขาว ค่าสีอื่นๆ คือ สีเทา โดยค่าสีเทาจะมาจากค่าต่างของภาพ 2 ภาพ 
        #โดยค่าสีเทามาก คือ ค่าต่างของภาพ 2 ภาพมาก และค่าสีเทาน้อย คือ ค่าต่างของภาพ 2 ภาพน้อย ซึ่งค่าต่างของภาพ 2 ภาพนั้นจะมาจากการเปลี่ยนแปลงของภาพ
        #ซึ่งเปลี่ยนแปลงของภาพจะมาจากการเคลื่อนไหวของวัตถุ ซึ่งวัตถุที่เคลื่อนไหวจะมีค่าต่างของภาพ 2 ภาพมากกว่าวัตถุที่ไม่เคลื่อนไหว 
        #ซึ่งวัตถุที่เคลื่อนไหวจะมีค่าสีเทามากกว่าวัตถุที่ไม่เคลื่อนไหว 
        gray = cv2.cvtColor(motiondiff, cv2.COLOR_BGR2GRAY) # แปลงเป็นภาพเทา 0-255 แล้วเก็บใน gray 
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        thresh,result = cv2.threshold(blur, 15, 255, cv2.THRESH_BINARY)
        dilation=cv2.dilate(result, None, iterations=3) # ทำการขยายค่าสีเทา โดยการเพิ่มค่าสีเทาให้กับค่าสีเทาที่มีค่าน้อยกว่า 3 ครั้ง
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # วาดสี่เหลี่ยมในวัตถุที่กำลังเคลื่อนที่
        for contour in contours:
            (x,y,w,h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 5000:
                continue
            cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
       
        cv2.imshow('Result', frame1)
        frame1=frame2
        check, frame2 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 else:
         cv2.putText(frame1, "Status: {}".format('None'), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

cap.release()
cv2.destroyAllWindows()