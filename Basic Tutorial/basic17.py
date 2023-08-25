# แสดงภาพสีจากจุด Pixel ที่เราคลิก
import cv2 
import numpy # สร้างภาพสีดำ และแสดงผล 
img = cv2.imread('C:\Python\Python OpenCV\image/rgb.png')

def clickPosition(event, x, y, flags, param): 
    if event == cv2.EVENT_LBUTTONDOWN: # แสดงค่าสีของจุดที่เราคลิก 
        blue = img[y, x, 0] 
        green = img[y, x, 1]
        red = img[y, x, 2]
        imgcolor=numpy.zeros([300,300,3], numpy.uint8) # สร้างภาพสีดำ และแสดงผล 
        imgcolor[:]=[blue,green,red] # แสดงค่าสีของจุดที่เราคลิก
        print(imgcolor) 
        cv2.imshow('Result', imgcolor) 
       
# แสดงภาพ
cv2.imshow('Output', img)
# ทำงานกับ Mouse 
cv2.setMouseCallback('Output', clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()


