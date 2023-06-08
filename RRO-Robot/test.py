import sys

gyro=[]

while True:
    gyro=brick.gyroscope().read()    
    brick.display().setBackground ("white") #Цвет фона
    brick.display().setPainterColor ("black") #Цвет шрифта
    brick.display().setPainterWidth(1000) #Размер шрифта
    brick.display().redraw() #Перерисовка
    brick.display().addLabel(str(gyro[5]), 1, 1) #Выводим сообщение
    script.wait(10)