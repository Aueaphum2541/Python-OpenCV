# หาเส้นเค้าโครงของภาพ และวาดเส้นเค้าโครงขึ้นบนภาพ โดยใช้ฟังก์ชัน cv2.findContours() และ cv2.drawContours() 
# ฟังก์ชัน cv2.findContours() จะส่งค่ากลับมา 2 ค่า คือ ค่า contours และ ค่า hierarchy
# ฟังก์ชัน cv2.drawContours() จะส่งค่ากลับมา 1 ค่า คือ ค่า img
# ฟังก์ชัน cv2.findContours() จะส่งค่า contours กลับมาเป็น list ของ array ที่มีขนาดเท่ากับจำนวนเส้นเค้าโครงที่พบ และมีค่าเป็น [Next, Previous, First_Child, Parent]
#  และแต่ละ array จะมีขนาดเท่ากับจำนวนจุดของเส้นเค้าโครงนั้นๆ โดยแต่ละจุดจะมีค่า x และ y อยู่ 2 ค่า
# ดังนั้น array ของ contours จะมีขนาดเท่ากับ (จำนวนจุดของเส้นเค้าโครง, 1, 2) ซึ่งเราสามารถใช้คำสั่ง contours[0].shape เพื่อดูขนาดของ array ของ contours ได้ 
# ฟังก์ชัน cv2.drawContours() จะส่งค่า img กลับมาเป็นภาพที่มีเส้นเค้าโครงที่วาดขึ้นบนภาพแล้ว
# ฟังก์ชัน cv2.drawContours() จะมีพารามิเตอร์ 4 ตัว คือ ภาพ, ค่า contours, ค่า index ของ contours, ค่าสีของเส้นเค้าโครง, ความหนาของเส้นเค้าโครง
# ฟังก์ชัน cv2.drawContours() จะมีพารามิเตอร์ index ของ contours ที่เป็น -1 หมายถึงวาดเส้นเค้าโครงทั้งหมดที่พบ 
# หรือ สามารถใช้ค่า index ของ contours ที่ต้องการวาดเส้นเค้าโครงได้ โดย index ของ contours จะเริ่มต้นที่ 0 จนถึงจำนวนเส้นเค้าโครงที่พบ - 1  
# ซึ่งในที่นี้คือ 0 ถึง 2 หรือ 3 เส้นเค้าโครง ซึ่งเราสามารถใช้คำสั่ง len(contours) เพื่อดูจำนวนเส้นเค้าโครงที่พบได้ 

import cv2
from matplotlib.pyplot import contour

img = cv2.imread('C:\Python\Python OpenCV\image/Ant.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh,result = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
Dcon=cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
cv2.imshow('contours', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

