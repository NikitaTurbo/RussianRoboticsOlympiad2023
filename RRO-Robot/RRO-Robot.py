import sys #Импортируем нужные модули

d1=brick.sensor("D1") #Делаем цифровую индентификацию D1
d2=brick.sensor("D2") #Делаем цифровую индентификацию D2
a1=brick.sensor("A1") #Делаем цифровую индентификацию A1 

mailbox.connect("192.168.77.225") #Подключение к роботу диспетчеру

point=0 #Значение флага

while True: #Цикл бесконечности
    distance_sensor_r=d1.read()    
    distance_sensor_l=d2.read()
    light_sensor=d1.read() 
    brick.display().setBackground ("white")
    brick.display().setPainterColor ("black")
    brick.display().setPainterWidth(100)
    brick.display().redraw()
    brick.display().addLabel("Left: " + str(distance_sensor_l), 1, 1)
    brick.display().addLabel("Right: " + str(distance_sensor_r), 1, 20)
    brick.display().addLabel("Light " + str(distance_sensor_l), 1, 40)
    if distance_sensor_l <= 23 or distance_sensor_r <= 23:
        mailbox.connect("192.168.77.1")
        mailbox.send(1, "Stop, found object!")
    if light_sensor <= 50:
        if point = 0:
          point=1
          mailbox.connect("192.168.77.1")
          mailbox.send(1, "Stop, found breaken!")
          #Work servo
    else:
      point=0
    
    script.wait(10)


    