import sys #Импортируем нужные модули

d1=brick.sensor("D1") #Делаем цифровую индентификацию
d2=brick.sensor("D2") #Делаем цифровую индентификацию

mailbox.connect("192.168.77.225")

while True:
    distance_sensor_r=d1.read()   
    distance_sensor_l=d2.read()
    brick.display().setBackground ("white")
    brick.display().setPainterColor ("black")
    brick.display().setPainterWidth(100)
    brick.display().redraw()
    brick.display().addLabel("Left: " + str(distance_sensor_l), 1, 1)
    brick.display().addLabel("Right: " + str(distance_sensor_r), 1, 20)
    if distance_sensor_l < 23 or distance_sensor_r < 23:
        brick.say("I")
        mailbox.connect("192.168.77.1")
        mailbox.send(1, "Stop, found!")
    script.wait(10)

    