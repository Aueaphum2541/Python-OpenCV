# เปรียบเทียบค่า Threshold value 

import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:\Python\Python OpenCV\image/children.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh_value = [50,100,130,200,230]
plt.subplot(231,xticks=[],yticks=[])
plt.title('Original')
plt.imshow(gray_img,cmap='gray')

for i in range(len(thresh_value)):
    ret,thresh = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY)
    plt.subplot(232+i,xticks=[],yticks=[])
    plt.title("%d"%thresh_value[i])
    plt.imshow(thresh,cmap='gray')

plt.show()