# Mophological การปรับรูปภาพ
# การปรับรูปภาพด้วยการเปลี่ยนรูปร่างของวัตถุในภาพ

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\Python\Python OpenCV\image/coin.png',0)
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

titles = ['ORIGINAL','THRESH']
images = [img,result]

for i in range(len(images)):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()