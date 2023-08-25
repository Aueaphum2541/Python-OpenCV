# ปรับค่า threshold ด้วย trackbar

import cv2

def display(value):
    pass

cv2.namedWindow('Output')
cv2.createTrackbar('value','Output',0,255,display)

while True :
    gray_img=cv2.imread('C:\Python\Python OpenCV\image/children.jpg',0)
    Thresh_value = cv2.getTrackbarPos('value','Output')
    cv2.threshold(gray_img,Thresh_value,255,cv2.THRESH_BINARY,gray_img)
    if cv2.waitKey(1) == 0xFF & ord('e'):
        break
    cv2.imshow('Output',gray_img)
    

cv2.destroyAllWindows()