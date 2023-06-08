import sys
import time

pi = 3.14159265358979 
__interpretation_started_timestamp__ = time.time() * 1000

m4 = brick.motor(M4)
e3 = brick.encoder(E3)
def Mess_1():
  end_d = 0
  e3.reset()
  m4.setPower(50)
  while end_d < 1550:#1круг
    end_d = e3.read()
    script.wait(5)
  m4.setPower(0)
  e3.reset()
      
  while True:#2круг
   m4.setPower(50)
   
   script.wait(10)
   brick.display().clear()
   if mailbox.hasMessages() == True:
      brick.display().clear
      message = mailbox.receive()
      if message == "10":
        brick.display().setBackground("black")
        brick .display().setPainterColor("white")
        brick.display().setPainterWidth(100)
        brick.display().redraw()
        brick.display().addLabel(message,1,1)
      if message == "20":
        m4.setPower(0)#
        end_d = e3.read()#перевод в длинну дуги трубы
        
        brick.display().setBackground("white")
        brick .display().setPainterColor("black")
        brick.display().setPainterWidth(100)
        brick.display().redraw()
        brick.display().addLabel(message,1,1)#вивести в см
      script.wait(10000)
 
   


if __name__ == '__main__':
  Mess_1()