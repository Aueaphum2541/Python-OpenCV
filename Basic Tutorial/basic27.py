# แสดงภาพด้วย Matplotlib
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:\Python\Python OpenCV\image/cat.jpg')
cv2.imshow('cat',img)

# แสดงภาพด้วย Matplotlib
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()