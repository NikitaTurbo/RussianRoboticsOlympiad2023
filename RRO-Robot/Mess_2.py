import sys
import time

pi = 3.14159265358979
__interpretation_started_timestamp__ = time.time() * 1000
a1 = brick.sensor(A1)
r1 = brick.sensor(D1)

def Mess_2():
  flag1 = 0
  flag = 0
  while  mailbox.hasMessages() == False:
    script.wait(10)
    
  while True:
    flag1 = 0
    flag = 0
    script.wait(10)
    s1 = a1.read()
    r1 = d1.read()
    if s1 < 10:
      if flag == 0:
        mailbox.send(1, "20")
        flag = 1
    else:      
     flag = 0
    if r1 < 5:
      if flag1 == 0:
        mailbox.send(1, "10")
        flag1 = 1
    else:
      flag1 = 0
     


if __name__ == '__main__':
  Mess_2()