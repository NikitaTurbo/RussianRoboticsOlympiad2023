import sys

d1=brick.sensor("D1")
d2=brick.sensor("D2")

while True:
    distance_sensor_r=d1.read()   
    distance_sensor_l=d2.read()
    brick.display().setBackground ("white")
    brick.display().setPainterColor ("black")
    brick.display().setPainterWidth(100)
    brick.display().redraw()
    brick.display().addLabel("Left: " + str(distance_sensor_l), 1, 1)
    brick.display().addLabel("Right: " + str(distance_sensor_r), 1, 20)
    script.wait(100)
    
if mailbox.hasMessages() == True:
    brick.display().setBackground ("white")
    brick.display().setPainterColor ("black")
    brick.display().setPainterWidth(100)
    brick.display().redraw()
    brick.display().addLabel(mailbox.receive(), 1, 1)
    