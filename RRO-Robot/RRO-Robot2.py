import sys
import sys
import time

m3=brick.motor("M3")
e3=brick.encoder("E3")

object={"encoder"}

e3.reset()

while True:
    m3.setPower(35)
    encoder=e3.read()
    if -encoder >= 1550:
        encoder=e3.reset()
        m3.setPower(0)
    if mailbox.hasMessages() == True:
        m3.setPower(0)
        if mailbox.receive() == "Stop, found object":
          object["encoder"]=e3.read()
          brick.display().setBackground ("white")
          brick.display().setPainterColor ("black")
          brick.display().setPainterWidth(100)
          brick.display().redraw()
          brick.display().addLabel("Object:" + str(object), 1, 1)
          script.wait(10000)
          
        elif mailbox.receive() == "Stop, found breaken":
          object=e3.read()
          brick.display().setBackground ("white")
          brick.display().setPainterColor ("red")
          brick.display().setPainterWidth(1000)
          brick.display().redraw()
          brick.display().addLabel("Breaken!!!", 1, 1)
          script.wait(10000)
        
    script.wait(10)
