from random import randint # randint คือการสุ่มตัวเลข ในช่วงที่กำหนด ในที่นี้คือ 0-255 ซึ่งเป็นค่าสีของ RGB
import time # คือการเรียกใช้งานโมดูล time ในการทำงานเกี่ยวกับเวลา  

class MyPerson: # สร้าง class ชื่อ MyPerson คือ Object orient programming ที่เราสามารถสร้าง Object ได้
    tracks = [] # สร้าง list ชื่อ tracks
    def __init__(self, i, xi, yi, max_age): # สร้าง method ชื่อ __init__ โดยมี parameter ทั้งหมด 4 ตัว คือ i, xi, yi, max_age
        self.i = i # สร้างตัวแปร i และกำหนดค่าให้เท่ากับ parameter i
        self.x = xi # สร้างตัวแปร x และกำหนดค่าให้เท่ากับ parameter xi
        self.y = yi # สร้างตัวแปร y และกำหนดค่าให้เท่ากับ parameter yi
        self.tracks = [] # สร้างตัวแปร tracks และกำหนดค่าให้เท่ากับ list ชื่อ tracks
        self.R = randint(0,255) # สร้างตัวแปร R และกำหนดค่าให้เท่ากับการสุ่มตัวเลข 0-255
        self.G = randint(0,255) # สร้างตัวแปร G และกำหนดค่าให้เท่ากับการสุ่มตัวเลข 0-255
        self.B = randint(0,255) # สร้างตัวแปร B และกำหนดค่าให้เท่ากับการสุ่มตัวเลข 0-255
        self.done = False # สร้างตัวแปร done และกำหนดค่าให้เท่ากับ False
        self.state = '0' # สร้างตัวแปร state และกำหนดค่าให้เท่ากับ '0'
        self.age = 0 # สร้างตัวแปร age และกำหนดค่าให้เท่ากับ 0
        self.max_age = max_age # สร้างตัวแปร max_age และกำหนดค่าให้เท่ากับ parameter max_age
        self.dir = None # สร้างตัวแปร dir และกำหนดค่าให้เท่ากับ None
    def getRGB(self): # สร้าง method ชื่อ getRGB
        return (self.R,self.G,self.B) # คืนค่ากลับเป็น tuple ที่มีค่าเท่ากับ (self.R,self.G,self.B)
    def getTracks(self): # สร้าง method ชื่อ getTracks
        return self.tracks # คืนค่ากลับเป็น self.tracks
    def getId(self): # สร้าง method ชื่อ getId
        return self.i # คืนค่ากลับเป็น self.i
    def getState(self): # สร้าง method ชื่อ getState
        return self.state # คืนค่ากลับเป็น self.state
    def getDir(self): # สร้าง method ชื่อ getDir
        return self.dir # คืนค่ากลับเป็น self.dir
    def getX(self): # สร้าง method ชื่อ getX
        return self.x # คืนค่ากลับเป็น self.x
    def getY(self): # สร้าง method ชื่อ getY
        return self.y # คืนค่ากลับเป็น self.y
    def updateCoords(self, xn, yn): # สร้าง method ชื่อ updateCoords ที่รับ parameter xn, yn มา 2 ตัว โดยเป็นตัวแปรชนิด int หรือ float 
        self.age = 0  # กำหนดค่า self.age เป็น 0  
        self.tracks.append([self.x,self.y]) # เพิ่มค่า [self.x,self.y] ใน list ชื่อ tracks
        self.x = xn # กำหนดค่า self.x เป็น xn
        self.y = yn # กำหนดค่า self.y เป็น yn
    def setDone(self): # สร้าง method ชื่อ setDone
        self.done = True # กำหนดค่า self.done เป็น True
    def timedOut(self): # สร้าง method ชื่อ timedOut
        return self.done # คืนค่ากลับเป็น self.done
    def going_UP(self,mid_start,mid_end): # สร้าง method ชื่อ going_UP ที่รับ parameter mid_start, mid_end มา 2 ตัว โดยเป็นตัวแปรชนิด int หรือ float
        if len(self.tracks) >= 2: # ถ้าความยาวของ self.tracks มากกว่าหรือเท่ากับ 2
            if self.state == '0': # ถ้า self.state เท่ากับ '0' 
                if self.tracks[-1][1] < mid_end and self.tracks[-2][1] >= mid_end: # ถ้า self.tracks ตำแหน่งที่ -1 และ ตำแหน่งที่ -2 มีค่าน้อยกว่า mid_end
                    state = '1' # กำหนดค่า state เป็น '1'
                    self.dir = 'up' # กำหนดค่า self.dir เป็น 'up'
                    return True # คืนค่ากลับเป็น True
            else: # ถ้าไม่เป็น 
                return False # คืนค่ากลับเป็น False
        else: # ถ้าไม่เป็น
            return False # คืนค่ากลับเป็น False
    def going_DOWN(self,mid_start,mid_end): # สร้าง method ชื่อ going_DOWN ที่รับ parameter mid_start, mid_end มา 2 ตัว โดยเป็นตัวแปรชนิด int หรือ float
        if len(self.tracks) >= 2: # ถ้าความยาวของ self.tracks มากกว่าหรือเท่ากับ 2
            if self.state == '0': # ถ้า self.state เท่ากับ '0'
                if self.tracks[-1][1] > mid_start and self.tracks[-2][1] <= mid_start: # ถ้า self.tracks ตำแหน่งที่ -1 และ ตำแหน่งที่ -2 มีค่ามากกว่า mid_start
                    self.dir = 'down' # กำหนดค่า self.dir เป็น 'down'
                    return True # คืนค่ากลับเป็น True
            else: # ถ้าไม่เป็น
                return False # คืนค่ากลับเป็น False
        else: # ถ้าไม่เป็น 
            return False # คืนค่ากลับเป็น False
    def age_one(self): # สร้าง method ชื่อ age_one
        self.age += 1 # บวกค่า self.age ทีละ 1
        if self.age > self.max_age: # ถ้า self.age มากกว่า self.max_age
            self.done = True # กำหนดค่า self.done เป็น True
        return True # คืนค่ากลับเป็น True
class MultiPerson: # สร้าง class ชื่อ MultiPerson
    def __init__(self, persons, xi, yi): # สร้าง method ชื่อ __init__ ที่รับ parameter persons, xi, yi มา 3 ตัว
        self.persons = persons # กำหนดค่า self.persons เป็น persons
        self.x = xi # กำหนดค่า self.x เป็น xi
        self.y = yi # กำหนดค่า self.y เป็น yi
        self.tracks = [] # กำหนดค่า self.tracks เป็น list ว่าง
        self.R = randint(0,255) # กำหนดค่า self.R เป็นตัวเลขสุ่มจาก 0 ถึง 255
        self.G = randint(0,255) # กำหนดค่า self.G เป็นตัวเลขสุ่มจาก 0 ถึง 255
        self.B = randint(0,255) # กำหนดค่า self.B เป็นตัวเลขสุ่มจาก 0 ถึง 255
        self.done = False # กำหนดค่า self.done เป็น False
        