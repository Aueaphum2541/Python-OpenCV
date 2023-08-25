# Opening Morphological 
# การเปิดรูปภาพ

# Erosion Morphological Transformation
# การ Erosion Morphological Transformation
# การย่อรูปภาพ

# การ Dilation Morphological 
# การขยายรูปภาพ

# Closing Morphological
# การปิดรูปภาพ

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:\Python\Python OpenCV\image/coin.png',0)
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
# การขยายรูปภาพ
dilation = cv2.dilate(result,kernel,iterations=3)
# การย่อรูปภาพ
erosion = cv2.erode(result,kernel,iterations=3)
# การเปิดรูปภาพ
opening = cv2.morphologyEx(result,cv2.MORPH_OPEN,kernel)

# การปิดรูปภาพ
closing = cv2.morphologyEx(result,cv2.MORPH_CLOSE,kernel)


titles = ['ORIGINAL','THRESH','DILATION','EROSION','OPENING','CLOSING']
images = [img,result,dilation,erosion,opening,closing]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
