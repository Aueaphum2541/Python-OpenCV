import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')

 
while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        cv2.imshow('frame',b)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()