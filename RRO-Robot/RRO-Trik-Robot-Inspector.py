import sys 
import time

brick.motor("S1").setPower(0)

d1=brick.sensor("D1")
d2=brick.sensor("D2")
a1=brick.sensor("A1")
s1=brick.motor("S1")
m4=brick.motor("M4")

number=0 
point=0 
flag=0
n_black=0

gyroscope=[]

def hatch(command, number): 
    if number == 1: 
        if command == 'open': 
            s1.setPower(50)
        if command == 'close':
            s1.setPower(0)
    elif number == 2: 
        if command == 'open': 
            s1.setPower(-70)
        if command == 'close': 
            s1.setPower(0)
            

while mailbox.hasMessages() == False:
    m4.setPower(100) 
    script.wait(1) 

m4.setPower(0)

brick.gyroscope().calibrate(20000) 
script.wait(20000)

while True: 
    light_sensor=a1.read() 
    distance_sensor_r=d1.read() 
    gyroscope=brick.gyroscope().read()
    if 140 >= gyroscope[6] // 1000 and gyroscope[6] // 1000 >= 25 and distance_sensor_r < 11:
       if point == 0:
          mailbox.send(0, 20) 
          point=1
    else:
       point=0
    if light_sensor <= 10: 
        if n_black >= 8:
            if flag == 0:
                hatch('close', number)
                flag=1
                number+=1 
                mailbox.send(0, 10) 
                pic = getPhoto()
                n_black=0
        else:
            n_black+=1
    else:
        flag=0
        n_black=0 
    if mailbox.hasMessages() == True: 
        message = mailbox.receive()
        if message == "30":
            script.wait(1200)
            hatch('open', number) 
            
    script.wait(1) 
    