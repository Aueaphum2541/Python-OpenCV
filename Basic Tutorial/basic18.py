# สร้างเส้นเชื่อมโยง (Connect point)
# สร้างเส้นเชื่อมโยงระหว่างจุดที่กำหนด
# โดยใช้ฟังก์ชัน cv2.line() และ cv2.polylines()
import cv2
import numpy 
img = numpy.zeros((400,400,3))

points = []


def clickPosition( event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       cv2.circle(img,(x,y),5,(0,0,255),5)
       points.append((x,y)) # สร้างจุดใหม่ และเก็บค่าจุดใหม่ลงใน point list 
       if len(points) >=2: # ถ้าจำนวนจุดมากกว่า 2 จุด ให้เชื่อมโยงจุด 2 จุดล่าสุด 
          cv2.line(img,points[-2],points[-1],(0,255,0),5) # สร้างเส้นเชื่อมโยงระหว่างจุดที่กำหนดโดยใช้ฟังก์ชัน cv2.line() 
          print('point1 = ',points[-2],'point2 = ',points[-1])
       cv2.imshow('Output',img) 

    
# แสดงรูปภาพ
cv2.imshow('Output', img)
# ทำงานกับเม้าส์
cv2.setMouseCallback('Output', clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()