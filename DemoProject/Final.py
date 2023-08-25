from tkinter import *
from tkinter import ttk
import os
import cv2
import random
import time
import tkinter.messagebox
import datetime
from tkinter.filedialog import* 
import matplotlib.pyplot as plt
import numpy as np

# บรรทัดที่ 3 เพิ่มคำสั่ง import ImageTk
from PIL import ImageTk, Image 

root = Tk()
root.option_add("*font", ("verdana", 20, "bold")) # กำหนด font ให้กับ widget ทั้งหมด ใน root นี้
root.title("โปรแกรมตรวจจับการเคลื่อนไหว")
root.geometry("800x600")
root.resizable(width=False, height=False) # กำหนดขนาดหน้าต่างไม่สามารถปรับขนาดได้


# บรรทัดที่ 9-14 เพิ่มรูปภาพ
#background_image = PhotoImage(file='C:\Users\admin\Desktop\GUI\project.py/Walking.mp4')
#background_label = Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

img = Image.open("C:\Python\Python OpenCV\image/maps.jpg") 
img = img.resize((700, 400))
photo = ImageTk.PhotoImage(img) # แปลงรูปภาพให้เป็นข้อมูลที่สามารถแสดงผลได้บน GUI
label = Label(root, image=photo)
label.pack()
Label(root, text="โปรแกรมตรวจจับการเคลื่อนไหว").place(x=220, y=420)

def ExitProgram ():
    exit=tkinter.messagebox.askquestion("ยืนยันการออกจากโปรแกรม","คุณต้องการปิดโปรแกรมหรือไม่?")
    if exit == "yes":
        root.destroy()
    else:
        pass

def openwindow():
    mywindow=Tk()
    mywindow.title("โปรแกรมการแสดงผลภาพ")
    mywindow.geometry("1000x700")
    
    def newwindow():
        newwindow=Tk()
        newwindow.title("วิดีโอ")
        newwindow.geometry("1000x800")
        newwindow.withdraw()
    mywindow.option_add("*font", ("verdana", 20, "bold"))
    Label(mywindow, text="โปรแกรมตรวจจับการเคลื่อนไหว").place(x=320, y=10)
    Label(mywindow, text="จับภาพวิดีโอจากกล้อง กดปุ่ม Spacebar",font=15,background='#CCFFFF').place(x=10,y=600)
    Label(mywindow, text="กดปุ่ม Esc เพื่อออกจากโปรแกรมกล้อง",font=15,background='#CCFFFF').place(x=10,y=650)
    mywindow.configure(background='#CCFFFF')
    pgb1 = ttk.Progressbar(mywindow, mode="determinate",length=200) # สร้าง progressbar แบบ determinate ขนาด 200 pixel และเก็บไว้ในตัวแปร pgb1 
    pgb1.place(x=700, y=600) # วาง progressbar ในตำแหน่ง x=10, y=650
    pgb1.start()
    Fcanvas = Canvas( height=400, width=800) 
    root.withdraw() #ทำการซ่อนหน้าต่างหลัก
    
    def snd1():
       import numpy as np
       import cv2 as cv
       import Person # คือไฟล์ที่เขียนไว้ในโฟลเดอร์เดียวกัน ใช้เพื่อเก็บข้อมูลของคนที่ติดตาม และคำนวณความเร็ว และความเร็วเฉลี่ย ของคน โดยใช้ค่า x และ y ของคน และเวลาที่ผ่านมา จากนั้นคำนวณความเร็วเฉลี่ย และความเร็วของคน
       import time # ใช้เพื่อเก็บเวลาที่ผ่านมา และคำนวณความเร็วของคน โดยใช้ค่า x และ y ของคน และเวลาที่ผ่านมา จากนั้นคำนวณความเร็วเฉลี่ย และความเร็วของคน

       try: # ใช้เพื่อเช็คว่ามีไฟล์ที่เรียกใช้หรือไม่ ถ้าไม่มีจะขึ้น error
           log = open('log.txt',"w") # สร้างไฟล์ log.txt ใหม่ หรือเขียนทับไฟล์เดิมที่มีอยู่แล้ว
       except:
           print( "can't create log file" ) # ถ้าไม่สามารถสร้างไฟล์ log.txt ได้ จะขึ้น error

       cnt_up   = 0 # ใช้เก็บจำนวนคนที่เข้า
       cnt_down = 0 # ใช้เก็บจำนวนคนที่ออก
       cap = cv.VideoCapture('C:\Python\Python OpenCV\image/TestVideo.avi')
       # Print คุณสมบัติการจับภาพไปยังเทอร์มินอล
       for i in range(19): # วนลูป 19 ครั้ง เพื่อแสดงคุณสมบัติของกล้อง 19 คุณสมบัติ โดยใช้คำสั่ง cap.get(i) ในการแสดงคุณสมบัติ โดย i คือ ตัวเลข 0-18 และ cap.get(i) คือ ค่าของคุณสมบัติที่ i นั้นๆ  โดยคุณสมบัติที่ 3 คือความกว้างของภาพ และคุณสมบัติที่ 4 คือความสูงของภาพ และคุณสมบัติที่ 5 คือความถี่ของการถ่ายภาพ และคุณสมบัติที่ 6 คือความเร็วของการถ่ายภาพ  
           print( i, cap.get(i)) # คือการดูค่าของค่าต่างๆ ที่เก็บไว้ใน cap โดยใช้ cap.get(i) โดย i คือตัวเลขที่เรียกค่าต่างๆ ออกมา โดย 0-18 คือค่าต่างๆ ที่เก็บไว้ใน cap และ 19 คือค่าที่เก็บไว้ใน cap.get(19) คือค่าของความกว้างของภาพ และ 20 คือค่าของความสูงของภาพ และ 21 คือค่าของความเร็วของภาพ และ 22 คือค่าของความเร็วของภาพที่เรากำหนดไว้ 
        
       h = 480 # กำหนดความสูงของภาพ 480 พิกเซล
       w = 640 # กำหนดความกว้างของภาพ 640 พิกเซล
       frameArea = h*w # คำนวณพื้นที่ของภาพ 
       areaTH = frameArea/250 # คือการกำหนดพื้นที่ของภาพที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ โดยใช้ frameArea/250 คือการหารพื้นที่ของภาพ โดยใช้ค่าของความกว้างและความสูงของภาพ และนำค่าที่ได้มาหาร 250 คือค่าที่กำหนดไว้ว่า ถ้าพื้นที่ของภาพน้อยกว่า 250 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าพื้นที่ของภาพมากกว่า 250 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ
       print( 'Area Threshold', areaTH) # คือการแสดงค่าของพื้นที่ที่กำหนดไว้ใน areaTH  

        #อินพุต/เอาต์พุต
       line_up = int(2*(h/5)) # คือการกำหนดค่าของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ โดยใช้ int(2*(h/5)) คือการหารความสูงของภาพ โดยใช้ค่าของความสูงของภาพ และนำค่าที่ได้มาหาร 5 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 5 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 5 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ และนำค่าที่ได้มาคูณ 2 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 2 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 2 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ
       line_down   = int(3*(h/5)) # คือการกำหนดค่าของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ โดยใช้ int(3*(h/5)) คือการหารความสูงของภาพ โดยใช้ค่าของความสูงของภาพ และนำค่าที่ได้มาหาร 5 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 5 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 5 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ และนำค่าที่ได้มาคูณ 3 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 3 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 3 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ

       up_limit =   int(1*(h/5)) # คือการกำหนดค่าของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ โดยใช้ int(1*(h/5)) คือการหารความสูงของภาพ โดยใช้ค่าของความสูงของภาพ และนำค่าที่ได้มาหาร 5 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 5 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 5 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ และนำค่าที่ได้มาคูณ 1 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 1 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 1 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ
       down_limit = int(4*(h/5)) # คือการกำหนดค่าของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ โดยใช้ int(4*(h/5)) คือการหารความสูงของภาพ โดยใช้ค่าของความสูงของภาพ และนำค่าที่ได้มาหาร 5 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 5 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 5 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ และนำค่าที่ได้มาคูณ 4 คือค่าที่กำหนดไว้ว่า ถ้าความสูงของภาพน้อยกว่า 4 คือจะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ และถ้าความสูงของภาพมากกว่า 4 คือจะนับว่าไม่มีคนเข้ามาในพื้นที่นั้นๆ

       print( "Red line y:",str(line_down)) # คือการแสดงค่าของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       print( "Blue line y:", str(line_up)) # คือการแสดงค่าของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       line_down_color = (255,0,0) # คือการกำหนดสีของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       line_up_color = (0,0,255) # คือการกำหนดสีของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt1 =  [0, line_down]; # คือการกำหนดจุดเริ่มต้นของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt2 =  [w, line_down]; # คือการกำหนดจุดสิ้นสุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L1 = np.array([pt1,pt2], np.int32) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L1 = pts_L1.reshape((-1,1,2)) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ 
       pt3 =  [0, line_up]; # คือการกำหนดจุดเริ่มต้นของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt4 =  [w, line_up]; # คือการกำหนดจุดสิ้นสุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L2 = np.array([pt3,pt4], np.int32) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L2 = pts_L2.reshape((-1,1,2)) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt5 =  [0, up_limit]; # คือการกำหนดจุดเริ่มต้นของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt6 =  [w, up_limit]; # คือการกำหนดจุดสิ้นสุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L3 = np.array([pt5,pt6], np.int32) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L3 = pts_L3.reshape((-1,1,2)) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt7 =  [0, down_limit]; # คือการกำหนดจุดเริ่มต้นของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pt8 =  [w, down_limit]; # คือการกำหนดจุดสิ้นสุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L4 = np.array([pt7,pt8], np.int32) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       pts_L4 = pts_L4.reshape((-1,1,2)) # คือการกำหนดจุดของเส้นที่จะนับว่ามีคนเข้ามาในพื้นที่นั้นๆ
       import cv2 as cv
       fgbg = cv.createBackgroundSubtractorMOG2(detectShadows = True) # คือการกำหนดพื้นหลังให้กับภาพ โดยใช้ฟังก์ชั่น createBackgroundSubtractorMOG2 โดยมีการตั้งค่า detectShadows = True คือการตั้งค่าให้มีเงา 
 
       #องค์ประกอบโครงสร้างสำหรับตัวกรองทาง Morphologycal
       kernelOp = np.ones((3,3),np.uint8) # คือการกำหนดค่าของ kernelOp โดยใช้ฟังก์ชั่น np.ones โดยมีการกำหนดค่าของ kernelOp ให้เป็น 3x3 และมีค่าเป็น 1 โดยมีการกำหนดค่าให้เป็น np.uint8
       kernelOp2 = np.ones((5,5),np.uint8) # คือการกำหนดค่าของ kernelOp2 โดยใช้ฟังก์ชั่น np.ones โดยมีการกำหนดค่าของ kernelOp2 ให้เป็น 5x5 และมีค่าเป็น 1 โดยมีการกำหนดค่าให้เป็น np.uint8
       kernelCl = np.ones((11,11),np.uint8) # คือการกำหนดค่าของ kernelCl โดยใช้ฟังก์ชั่น np.ones โดยมีการกำหนดค่าของ kernelCl ให้เป็น 11x11 และมีค่าเป็น 1 โดยมีการกำหนดค่าให้เป็น np.uint8

       #Variables
       font = cv.FONT_HERSHEY_SIMPLEX # คือการกำหนดตัวอักษรที่จะแสดงผลบนภาพ
       persons = [] # คือการกำหนดตัวแปร persons ให้เป็น list
       max_p_age = 5 # คือการกำหนดค่า max_p_age ให้เป็น 5
       pid = 1 # คือการกำหนดค่า pid ให้เป็น 1
       
       while(cap.isOpened()):
       ##for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): # คือการกำหนดการทำงานของการเก็บภาพจากกล้อง โดยใช้ฟังก์ชั่น capture_continuous โดยมีการกำหนดค่าให้เป็น rawCapture และ format="bgr" และ use_video_port=True ซึ่งจะทำการเก็บภาพเป็นรูปแบบ BGR และใช้ port ของกล้อง 
       #อ่านภาพจากแหล่งวิดีโอ
          ret, frame = cap.read() # คือการกำหนดการทำงานของการอ่านภาพจากกล้อง โดยใช้ฟังก์ชั่น read โดยมีการกำหนดค่าให้เป็น ret และ frame ซึ่งจะทำการอ่านภาพจากกล้องและเก็บไว้ในตัวแปร frame และเก็บค่าการทำงานของการอ่านภาพไว้ในตัวแปร ret ซึ่งถ้า ret มีค่าเป็น True แสดงว่าการอ่านภาพสำเร็จ แต่ถ้า ret มีค่าเป็น False แสดงว่าการอ่านภาพไม่สำเร็จ 
       ##    frame = image.array # คือการกำหนดการทำงานของการเก็บภาพจากกล้อง โดยใช้ฟังก์ชั่น array โดยมีการกำหนดค่าให้เป็น frame ซึ่งจะทำการเก็บภาพจากกล้องไว้ในตัวแปร frame 

          for i in persons: # คือการกำหนดการทำงานของการวนลูปของตัวแปร persons โดยใช้ฟังก์ชั่น for โดยมีการกำหนดค่าให้เป็น i ซึ่งจะทำการวนลูปตัวแปร persons และเก็บค่าในตัวแปร i
                i.age_one() #age every person one frame
    #########################
    #  การประมวลผลล่วงหน้า  #
    #########################
    
    #ใช้การลบพื้นหลัง
          fgmask = fgbg.apply(frame) # คือการกำหนดการทำงานของการลบพื้นหลัง โดยใช้ฟังก์ชั่น apply โดยมีการกำหนดค่าให้เป็น fgmask ซึ่งจะทำการลบพื้นหลังจากภาพที่อยู่ในตัวแปร frame และเก็บไว้ในตัวแปร fgmask
          fgmask2 = fgbg.apply(frame) # คือการกำหนดการทำงานของการลบพื้นหลัง โดยใช้ฟังก์ชั่น apply โดยมีการกำหนดค่าให้เป็น fgmask2 ซึ่งจะทำการลบพื้นหลังจากภาพที่อยู่ในตัวแปร frame และเก็บไว้ในตัวแปร fgmask2

    #ไบนารีเพื่อลบเงา (สีเทา)
          try: # คือการกำหนดการทำงานของการลบเงา โดยใช้ฟังก์ชั่น try โดยมีการกำหนดค่าให้เป็น try ซึ่งจะทำการลบเงาจากภาพที่อยู่ในตัวแปร fgmask และเก็บไว้ในตัวแปร fgmask2
             ret,imBin= cv.threshold(fgmask,200,255,cv.THRESH_BINARY)  # คือการกำหนดการทำงานของการเปลี่ยนภาพเป็นภาพไบนารี โดยใช้ฟังก์ชั่น threshold โดยมีการกำหนดค่าให้เป็น imBin ซึ่งจะทำการเปลี่ยนภาพที่อยู่ในตัวแปร fgmask ให้เป็นภาพไบนารี และเก็บไว้ในตัวแปร imBin
             ret,imBin2 = cv.threshold(fgmask2,200,255,cv.THRESH_BINARY) # คือการกำหนดการทำงานของการเปลี่ยนภาพเป็นภาพไบนารี โดยใช้ฟังก์ชั่น threshold โดยมีการกำหนดค่าให้เป็น imBin2 ซึ่งจะทำการเปลี่ยนภาพที่อยู่ในตัวแปร fgmask2 ให้เป็นภาพไบนารี และเก็บไว้ในตัวแปร imBin2
        #เปิด (กัดกร่อน->ขยาย) เพื่อลบเสียงรบกวน
             mask = cv.morphologyEx(imBin, cv.MORPH_OPEN, kernelOp) # คือการกำหนดการทำงานของการกัดกร่อน โดยใช้ฟังก์ชั่น morphologyEx โดยมีการกำหนดค่าให้เป็น mask ซึ่งจะทำการกัดกร่อนภาพที่อยู่ในตัวแปร imBin และเก็บไว้ในตัวแปร mask
             mask2 = cv.morphologyEx(imBin2, cv.MORPH_OPEN, kernelOp) # คือการกำหนดการทำงานของการกัดกร่อน โดยใช้ฟังก์ชั่น morphologyEx โดยมีการกำหนดค่าให้เป็น mask2 ซึ่งจะทำการกัดกร่อนภาพที่อยู่ในตัวแปร imBin2 และเก็บไว้ในตัวแปร mask2
      #Closing (ขยาย -> กัดเซาะ) เพื่อปิดพื้นที่สีขาวเข้าด้วยกัน
             mask =  cv.morphologyEx(mask , cv.MORPH_CLOSE, kernelCl) # คือการกำหนดการทำงานของการขยาย โดยใช้ฟังก์ชั่น morphologyEx โดยมีการกำหนดค่าให้เป็น mask ซึ่งจะทำการขยายภาพที่อยู่ในตัวแปร mask และเก็บไว้ในตัวแปร mask
             mask2 = cv.morphologyEx(mask2, cv.MORPH_CLOSE, kernelCl) # คือการกำหนดการทำงานของการขยาย โดยใช้ฟังก์ชั่น morphologyEx โดยมีการกำหนดค่าให้เป็น mask2 ซึ่งจะทำการขยายภาพที่อยู่ในตัวแปร mask2 และเก็บไว้ในตัวแปร mask2
          except: # คือการกำหนดการทำงานของ except โดยจะทำงานเมื่อเกิดข้อผิดพลาด
             print('EOF') # คือการแสดงข้อความ EOF
             print( 'UP:',cnt_up) # คือการแสดงข้อความ UP: และจำนวนครั้งที่มีการเคลื่อนไหวขึ้น
             print ('DOWN:',cnt_down) # คือการแสดงข้อความ DOWN: และจำนวนครั้งที่มีการเคลื่อนไหวลง
             break # คือการหยุดการทำงาน
    #################
    #   การหาเส้นเค้าโครงของภาพ (Contours)   #
    #################
    
   #  ส่งคืนค่าสถานะภายนอกสุดเท่านั้น รูปร่างทั้งหมดถูกทิ้งไว้ข้างหลัง
          contours0, hierarchy = cv.findContours(mask2,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) # คือการกำหนดการทำงานของการหาเส้นเค้าโครงของภาพ โดยใช้ฟังก์ชั่น findContours โดยมีการกำหนดค่าให้เป็น mask2 ซึ่งจะทำการหาเส้นเค้าโครงของภาพที่อยู่ในตัวแปร mask2 และเก็บไว้ในตัวแปร contours0 และ hierarchy
          for cnt in contours0: # คือการกำหนดการทำงานของ for โดยจะทำงานเมื่อมีการเกิดการเคลื่อนไหวขึ้น
             area = cv.contourArea(cnt) # คือการกำหนดการทำงานของการหาพื้นที่ของภาพ โดยใช้ฟังก์ชั่น contourArea โดยมีการกำหนดค่าให้เป็น cnt ซึ่งจะทำการหาพื้นที่ของภาพที่อยู่ในตัวแปร cnt และเก็บไว้ในตัวแปร area
             if area > areaTH: # คือการกำหนดการทำงานของ if โดยจะทำงานเมื่อพื้นที่ของภาพมากกว่า areaTH
            #################
            #   การติดตาม TRACKING    #
            #################
            
            # เพิ่มเงื่อนไขสำหรับหลายคน ออก และคัดกรองทางเข้า
            
              M = cv.moments(cnt) # คือการกำหนดการทำงานของการหาจุดกึ่งกลางของภาพ โดยใช้ฟังก์ชั่น moments โดยมีการกำหนดค่าให้เป็น cnt ซึ่งจะทำการหาจุดกึ่งกลางของภาพที่อยู่ในตัวแปร cnt และเก็บไว้ในตัวแปร M
              cx = int(M['m10']/M['m00']) # คือการกำหนดการทำงานของการหาจุดกึ่งกลางของภาพ โดยใช้ฟังก์ชั่น moments โดยมีการกำหนดค่าให้เป็น cnt ซึ่งจะทำการหาจุดกึ่งกลางของภาพที่อยู่ในตัวแปร cnt และเก็บไว้ในตัวแปร M
              cy = int(M['m01']/M['m00']) # คือการกำหนดการทำงานของการหาจุดกึ่งกลางของภาพ โดยใช้ฟังก์ชั่น moments โดยมีการกำหนดค่าให้เป็น cnt ซึ่งจะทำการหาจุดกึ่งกลางของภาพที่อยู่ในตัวแปร cnt และเก็บไว้ในตัวแปร M
              x,y,w,h = cv.boundingRect(cnt) # คือการกำหนดการทำงานของการหาจุดขอบของภาพ โดยใช้ฟังก์ชั่น boundingRect โดยมีการกำหนดค่าให้เป็น cnt ซึ่งจะทำการหาจุดขอบของภาพที่อยู่ในตัวแปร cnt และเก็บไว้ในตัวแปร x,y,w,h

              new = True # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
              if cy in range(up_limit,down_limit): # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                for i in persons: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                    if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                        # วัตถุอยู่ใกล้กับวัตถุที่ตรวจพบก่อนหน้านี้
                        new = False # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                        i.updateCoords(cx,cy)   #updates พิกัดบนวัตถุและรีเซ็ตอายุ
                        if i.going_UP(line_down,line_up) == True: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            cnt_up += 1; # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            print( "ID:",i.getId(),'crossed going up at',time.strftime("%c")) # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            log.write("ID: "+str(i.getId())+' crossed going up at ' + time.strftime("%c") + '\n') # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                        elif i.going_DOWN(line_down,line_up) == True: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            cnt_down += 1; # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            print( "ID:",i.getId(),'crossed going down at',time.strftime("%c")) # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            log.write("ID: " + str(i.getId()) + ' crossed going down at ' + time.strftime("%c") + '\n') # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                    if i.getState() == '1': # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                        if i.getDir() == 'down' and i.getY() > down_limit: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            i.setDone() # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                        elif i.getDir() == 'up' and i.getY() < up_limit: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                            i.setDone() # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                    if i.timedOut(): # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                      
                        index = persons.index(i) # คือการกำหนดค่าให้ตัวแปร index มีค่าเท่ากับ persons.index(i)
                        persons.pop(index) # คือการกำหนดค่าให้ตัวแปร persons มีค่าเท่ากับ persons.pop(index)
                        del i    
                if new == True: # คือการกำหนดการทำงานของการเปลี่ยนแปลงของภาพ โดยมีการกำหนดค่าให้เป็น True ซึ่งจะทำการเปลี่ยนแปลงของภาพที่อยู่ในตัวแปร new
                    p = Person.MyPerson(pid,cx,cy, max_p_age) # คือการกำหนดค่าให้ตัวแปร p มีค่าเท่ากับ Person.MyPerson(pid,cx,cy, max_p_age)
                    persons.append(p) # คือการกำหนดค่าให้ตัวแปร persons มีค่าเท่ากับ persons.append(p)
                    pid += 1  # คือการกำหนดค่าให้ตัวแปร pid มีค่าเท่ากับ pid += 1  
            #################
            #  ภาพวาด     #
            #################
              cv.circle(frame,(cx,cy), 5, (0,0,255), -1) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.circle(frame,(cx,cy), 5, (0,0,255), -1)
              img = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)  # คือการกำหนดค่าให้ตัวแปร img มีค่าเท่ากับ cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)         
            #cv.drawContours(frame, cnt, -1, (0,255,0), 3) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.drawContours(frame, cnt, -1, (0,255,0), 3)
            
    #สิ้นสุดสำหรับ cnt ใน contours0
            
    #########################
    # DRAW TRAJECTORIES #
    #########################
       for i in persons: # คือการกำหนดค่าให้ตัวแปร i มีค่าเท่ากับ persons
##        if len(i.getTracks()) >= 2: # คือการกำหนดค่าให้ตัวแปร i.getTracks() มีค่าเท่ากับ 2
##            pts = np.array(i.getTracks(), np.int32) # คือการกำหนดค่าให้ตัวแปร pts มีค่าเท่ากับ np.array(i.getTracks(), np.int32)
##            pts = pts.reshape((-1,1,2)) # คือการกำหนดค่าให้ตัวแปร pts มีค่าเท่ากับ pts.reshape((-1,1,2))
##            frame = cv.polylines(frame,[pts],False,i.getRGB()) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.polylines(frame,[pts],False,i.getRGB())
##        if i.getId() == 9: # คือการกำหนดค่าให้ตัวแปร i.getId() มีค่าเท่ากับ 9
##            print str(i.getX()), ',', str(i.getY()) # คือการกำหนดค่าให้ตัวแปร i.getX() มีค่าเท่ากับ i.getY()
        cv.putText(frame, str(i.getId()),(i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv.LINE_AA) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.putText(frame, str(i.getId()),(i.getX(),i.getY()),font,0.3,i.getRGB(),1,cv.LINE_AA)
        
    #################
    #   รูปภาพ    #
    #################
       str_up = 'UP: '+ str(cnt_up) # คือการกำหนดค่าให้ตัวแปร str_up มีค่าเท่ากับ 'UP: '+ str(cnt_up)  
       str_down = 'DOWN: '+ str(cnt_down) # คือการกำหนดค่าให้ตัวแปร str_down มีค่าเท่ากับ 'DOWN: '+ str(cnt_down)
       frame = cv.polylines(frame,[pts_L1],False,line_down_color,thickness=2) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.polylines(frame,[pts_L1],False,line_down_color,thickness=2)
       frame = cv.polylines(frame,[pts_L2],False,line_up_color,thickness=2) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.polylines(frame,[pts_L2],False,line_up_color,thickness=2)  
       frame = cv.polylines(frame,[pts_L3],False,(255,255,255),thickness=1) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.polylines(frame,[pts_L3],False,(255,255,255),thickness=1)
       frame = cv.polylines(frame,[pts_L4],False,(255,255,255),thickness=1) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.polylines(frame,[pts_L4],False,(255,255,255),thickness=1)
       cv.putText(frame, str_up ,(10,40),font,0.5,(255,255,255),2,cv.LINE_AA) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.putText(frame, str_up ,(10,40),font,0.5,(255,255,255),2,cv.LINE_AA)
       cv.putText(frame, str_up ,(10,40),font,0.5,(0,0,255),1,cv.LINE_AA) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.putText(frame, str_up ,(10,40),font,0.5,(0,0,255),1,cv.LINE_AA)
       cv.putText(frame, str_down ,(10,90),font,0.5,(255,255,255),2,cv.LINE_AA) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.putText(frame, str_down ,(10,90),font,0.5,(255,255,255),2,cv.LINE_AA)
       cv.putText(frame, str_down ,(10,90),font,0.5,(255,0,0),1,cv.LINE_AA) # คือการกำหนดค่าให้ตัวแปร frame มีค่าเท่ากับ cv.putText(frame, str_down ,(10,90),font,0.5,(255,0,0),1,cv.LINE_AA)

       cv.imshow('Frame',frame) # คือการแสดงผลรูปภาพ frame ที่มีค่าเท่ากับ cv.imshow('Frame',frame)
       cv.imshow('Mask',mask)   # คือการแสดงผลรูปภาพ mask ที่มีค่าเท่ากับ cv.imshow('Mask',mask)   
    

##    rawCapture.truncate(0) # คือการกำหนดค่าให้ตัวแปร rawCapture มีค่าเท่ากับ rawCapture.truncate(0) 
    #กด ESC เพื่อออก
       k = cv.waitKey(30) & 0xff # คือการกำหนดค่าให้ตัวแปร k มีค่าเท่ากับ cv.waitKey(30) & 0xff
       if k == 27: # คือการกำหนดค่าให้ตัวแปร k มีค่าเท่ากับ 27
          pass # คือการออกจากการทำงานของโปรแกรม
       
       log.flush() # คือการกำหนดค่าให้ตัวแปร log มีค่าเท่ากับ log.flush()
       log.close()
       cap.release() # คือการกำหนดค่าให้ตัวแปร cap มีค่าเท่ากับ cap.release() 
       cv.destroyAllWindows() # คือการกำหนดค่าให้ตัวแปร cv มีค่าเท่ากับ cv.destroyAllWindows()
   
              
    def snd2():
       os.system('C:\Python/output.avi')
       
    var = IntVar()
    def snd3():
       nwindow=Tk()
       nwindow.title("โปรแกรมการแสดงผลภาพ")
       nwindow.geometry("800x600")
       cap=cv2.VideoCapture("image/Leonidas - This is Sparta.mp4")
       fourcc = cv2.VideoWriter_fourcc(*'XVID')

       result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
       while (cap.isOpened()):
            check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
                
            if check == True :
                cv2.imshow("output",frame)
                result.write(frame)
            if cv2.waitKey(1) & 0xFF == ord("x"):
                break
       result.release()            
       cap.release()
       cv2.destroyAllWindows()
    rb1 = Radiobutton(mywindow, text= "เปิดโปรแกรมวิดีโอ", variable = var, value=1, command=snd3)
    rb1.place(x=400,y=420)
    
    
    def exits():
        exit=tkinter.messagebox.askquestion("ยืนยันการออกจากโปรแกรม","คุณต้องการปิดโปรแกรมหรือไม่?")
        if exit == "yes":
            mywindow.destroy()
        else:
            pass
    def selectFile():
        file = askopenfilename()
        print(file)
        fileContent = open(file,encoding="utf8")
        myLabel = Label(mywindow, text = file).pack()
        myLabel = Label(mywindow, text = fileContent.read(),font=12).pack()

    def selectSave ():
        save = asksaveasfilename()
        print(save)
       
    
    def graph():
        fig=plt.figure()
        ax=fig.add_subplot()
        fig.show()
        x=[]
        n=100

        for i in range(n):
            x.append(random.randint(0,20))
            ax.plot(x,color="red")
            fig.canvas.draw()
            ax.set_xlim(left=max(0,i-30),right=i+5)
            time.sleep(0.1)
        plt.show()

    
    
        
   
    btne=Button(mywindow,text="exit",fg="black",command=exits).place(x=475,y=570)
    btnp=Button(mywindow,text="เปิดกล้อง",fg="black",command=snd1).place(x=500,y=490)
    btn1=Button(root,text="exit",fg="black",command = ExitProgram).place(x=180,y=500)   
    btn2=Button(root,text="start",fg="black",command= openwindow).place(x=520,y=500)
    btn3= Button(mywindow,text="เลือกไฟล์", command=selectFile).place(x=330,y=490)
    btn4= Button(mywindow,text="บันทึกไฟล์", command=selectSave).place(x=670,y=490)
    btn5= Button(mywindow,text="กราฟ", command=graph).place(x=200,y=490)
    root.mainloop()
    mywindow.mainloop()
    
  
btn1=Button(root,text="exit",fg="black",command = ExitProgram).place(x=180,y=500)   
btn2=Button(root,text="start",fg="black",command= openwindow).place(x=520,y=500)
root.mainloop()




