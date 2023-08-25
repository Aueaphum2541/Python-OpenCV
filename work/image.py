import cv2

# ฟังก์ชันที่จะถูกเรียกเมื่อมีการคลิกที่ภาพ
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked pixel position (x, y):", x, y)

# โหลดภาพ
image = cv2.imread("image000059.jpg")

# สร้างหน้าต่างแสดงภาพ
cv2.namedWindow("Image")
cv2.imshow("Image", image)

# กำหนดฟังก์ชัน callback สำหรับการคลิกเมาส์
cv2.setMouseCallback("Image", mouse_callback)

# รอให้ผู้ใช้คลิกเมาส์
cv2.waitKey(0)

# ปิดหน้าต่างทั้งหมด
cv2.destroyAllWindows()
