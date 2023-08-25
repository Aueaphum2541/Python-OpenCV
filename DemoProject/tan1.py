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
       cap = cv2.VideoCapture(0)
       
       while(cap.isOpened()): 
          check , frame = cap.read() 
          font = cv2.FONT_HERSHEY_SIMPLEX # กำหนดแบบอักษร 
          text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4)) # กำหนดข้อความ และ ค่าของความกว้าง และ ความสูง 
          datet = str(datetime.datetime.now()) # อ่านวันที่ และเวลา จากระบบ และ กำหนดให้ datet เก็บข้อมูล
          frame = cv2.putText(frame, datet, (10,50), font, 1,(255,0,0), 2, cv2.LINE_AA) # แสดงวันเวลาบนภาพ 
          
          if check == True: 
            cv2.imshow("Output", frame) 
         
          k = cv2.waitKey(1)
          if k%256 == 27: # กด esc ในการออกจากการทำงาน
        # ESC pressed
             print("Escape hit, closing...")
             break
          elif k%256 == 32: # กด space bar ในการบันทึกภาพ 
        # SPACE pressed
            img_counter = 0
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
       cap.release()
       cv2.destroyAllWindows()
              
    
         
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




