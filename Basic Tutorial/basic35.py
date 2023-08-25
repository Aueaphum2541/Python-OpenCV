# การ Dilation Morphological 
# การขยายรูปภาพ

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\Python\Python OpenCV\image/coin.png',0)
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(result,kernel,iterations=2)


titles = ['ORIGINAL','THRESH','DILATION']
images = [img,result,dilation]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
