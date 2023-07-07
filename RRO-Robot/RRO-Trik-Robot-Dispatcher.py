import sys
import time

m4 = brick.motor("M4")
e4 = brick.encoder("E4")

object = []
breaken = []

encoder = 0
coor = 0
number = 0

e4.reset()
encoder = e4.read()

while encoder <= 3077:
    m4.setPower(45) 
    encoder = e4.read()  
    script.wait(1)  

mailbox.send(2, 20)

m4.setPower(0)
script.wait(20000)

e4.reset()
encoder =  e4.read()

while encoder <= 3077:
    m4.setPower(40)
    encoder = e4.read()
    if mailbox.hasMessages() == True:
        encoder = e4.read()
        message = mailbox.receive()
        if message == "20":
            coor += 1
            object.append(str(int((170 * encoder) / 3077)) + ' см')
            script.writeToFile("object.txt", object[coor - 1] + "\n")
            script.wait(10)
          
        if message == "10":
            m4.setPower(0)
            number += 1
            breaken.append(str(int((170 * encoder) / 3077)) + ' см')
            script.writeToFile("breake.txt", breaken[number - 1] + "\n")
            script.wait(4000)
            m4.setPower(40)
            encoder = e4.read()
            mailbox.send(2, 30)
        
    script.wait(10)
    
m4.setPower(0)

brick.display().setBackground ("white")
brick.display().setPainterColor ("black")
brick.display().setPainterWidth(1000)
brick.display().redraw()

brick.display().addLabel('Результаты:', 1, 1)
brick.display().addLabel('Повреждение(я):', 1, 20) 

for i in range(2, number + 2):
    brick.display().redraw()
    brick.display().addLabel(breaken[i - 2], 1, 20 * i)
    script.wait(1)
    
brick.display().addLabel('Объект(ы):', 1, 20 * (number + 2))

for i in range(number + 3, coor + number + 3):
    brick.display().redraw() #Перерисовка
    brick.display().addLabel(object[i - (number + 3)], 1, 20 * (i))
    script.wait(1)
    
script.wait(300000)
  
