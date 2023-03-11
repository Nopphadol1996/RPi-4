import time
import threading

def Shower():
    for i in range(10):
        print('กำลังอาบน้ำ',i)
        time.sleep(0.5)


def Toothbrush():
    for i in range(10):
        print('กำลังแปลงฟัน',i)
        time.sleep(0.2)

task1 = threading.Thread(target=Toothbrush)
task2 = threading.Thread(target=Shower)

t1 = time.time()
task1.start()
task2.start()
# .join( ) คือถ้า Function ไหนเสร็จก่อนจะต้องรอให้เสร็จพร้อมกัน
task1.join() # ถ้าเป็นการวิ่งแข่ง  task1 วิ่งไวกว่า เมื่อถึงเส้นชัยต้องรอ task2 แล้วเข้าพร้อมกัน
task2.join() # ถ้่าใน GUI ให้สร้างแค่ task เดียวเพราะ task2 คือ GUI.mainloop run ตอดลเวลา
t2 = time.time()
print('Time:',t2-t1)



'''
t1 = time.time()
Toothbrush()
Shower()
t2 = time.time()
print('Time:',t2-t1)
# โปรแกรมจะรันแปลงฟันก่อนอาบน้ำใช้เวลา 10 วินาที
'''