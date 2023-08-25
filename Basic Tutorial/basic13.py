# ใส่ข้อความในภาพ (Text on Image)
# ใช้ฟังก์ชัน putText() ในการใส่ข้อความในภาพ
# putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) → img
# ฟังก์ชัน cv2.putText() ใช้ในการใส่ข้อความในภาพ
# พารามิเตอร์
# img รูปภาพที่จะใส่ข้อความ
# text ข้อความที่จะใส่
# org พิกัดซ้ายบนของข้อความ
# fontFace แบบอักษร
# fontScale ขนาดอักษร
# color สีของอักษร
# thickness ความหนาของข้อความ
# lineType ชนิดของเส้นของอักษร
# bottomLeftOrigin ถ้าเป็น True พิกัดจะเป็นซ้ายล่าง ถ้าเป็น False พิกัดจะเป็นซ้ายบน

import cv2

# อ่านรูปภาพ
img = cv2.imread('Python OpenCV\image\cat.jpg') # รูปภาพจะถูกอ่านเป็นสี (Color) แบบ BGR (Blue-Green-Red)

# กำหนดขนาด
imgresize = cv2.resize(img,(700,700)) # กำหนดขนาดให้รูปภาพ 700x700 pixel

# กำหนดตำแหน่งของข้อความ
cv2.putText(imgresize, 'Cat', (150, 200), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 255), 2, cv2.LINE_AA)
 # ใส่ข้อความ Cat ในภาพ และกำหนดตำแหน่ง 150,200 และกำหนดสีเป็นสีแดง (0,0,255) และกำหนดความหนาของข้อความเป็น 2 pixel 
 # และกำหนดชนิดของเส้นของอักษรเป็น cv2.LINE_AA (Anti-aliased line) 

# แสดงรูปภาพ
cv2.imshow('Cat', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()



