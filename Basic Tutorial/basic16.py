# ตรวจจับค่าสีด้วย Mouse (Event)
# โดยใช้ฟังก์ชัน cv2.setMouseCallback()
# ฟังก์ชัน cv2.setMouseCallback() จะเรียกฟังก์ชันที่เรากำหนดเมื่อเกิด Event ขึ้น
# ฟังก์ชัน cv2.setMouseCallback() จะรับพารามิเตอร์ 3 ตัว คือ ชื่อ Window, ฟังก์ชันที่เราต้องการให้เรียก, และข้อมูลเพิ่มเติม
# ฟังก์ชันที่เราต้องการให้เรียก จะต้องมีพารามิเตอร์ 3 ตัว คือ Event, x, y
# ฟังก์ชันที่เราต้องการให้เรียก จะต้องมีการ return ค่า True หรือ False กลับไป
# ถ้า return True จะทำให้ Event นั้นเกิดซ้ำๆ ถ้า return False จะทำให้ Event นั้นเกิดครั้งเดียว

import cv2

img = cv2.imread('C:\Python\Python OpenCV\image\maxresdefault.jpg')

def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        text = str(blue) + ', ' + str(green) + ', ' + str(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x,y), font, 1, (255, 255, 0), 2)
        cv2.imshow('image', img)
        print(text)

cv2.imshow('image', img)
cv2.setMouseCallback('image', clickPosition)

cv2.waitKey(0)
cv2.destroyAllWindows()


