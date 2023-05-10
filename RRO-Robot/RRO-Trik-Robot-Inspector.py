import sys #Импортируем библиотеку sys
import time #Импортируем библиотеку time

d1=brick.sensor("D1") #Делаем цифровую индентификацию D1
d2=brick.sensor("D2") #Делаем цифровую индентификацию D2
a1=brick.sensor("A1") #Делаем цифровую индентификацию A1 
s1=brick.motor("S1") #Делаем цифровую индентификацию S1
m4=brick.motor("M4") #Делаем цифровую индентификацию M4

number=0 #Номерация буёв

def hatch(command, number): #Функция для открывания или закрывания люка
    if number == 0: #Если первый буй
        if command == 'open': #Если надо открыть
            for i in range(-90, 0): #Цикл открывания
                s1.setPower(10) #Подаём скорость на сервопривод
                script.wait(10) #Ждём
        elif command == 'close': #Если надо закрыть
            for i in range(0, -90): #Цикл закрывания
                s1.setPower(10) #Подаём скорость на сервопривод
                script.wait(10) #Ждём
     elif number == 1: #Если второй буй
        if command == 'open': #Если надо открыть
            for i in range(-90, 90): #Цикл открывания
                s1.setPower(10) #Подаём скорость на сервопривод
                script.wait(10) #Ждём
        elif command == 'close': #Если надо закрыть
            for i in range(90, -90): #Цикл закрывания
                s1.setPower(10) #Подаём скорость на сервопривод
                script.wait(10) #Ждём         
               
mailbox.connect("192.168.77.213") #Подключение к роботу-диспетчеру

point=0 #Значение флага

while mailbox.hasMessages() == False: #Цикл с условием
    m4.setPower(100) #Включаем вентилятор

m4.stop() #Останавливаем вентилятор

while True: #Бесконечный цикл
    distance_sensor_r=d1.read() #Считываем данные с D1   
    distance_sensor_l=d2.read() #Считываем данные с D2  
    light_sensor=a1.read() #Считываем данные с A1  
    brick.display().setBackground ("white") #Цвет фона
    brick.display().setPainterColor ("black") #Цвет шрифта
    brick.display().setPainterWidth(100) #Размер шрифта
    brick.display().redraw() #Перерисовка
    brick.display().addLabel("Left: " + str(distance_sensor_l), 1, 1) #Выводим данные D1
    brick.display().addLabel("Right: " + str(distance_sensor_r), 1, 20) #Выводим данные D2
    brick.display().addLabel("Light: " + str(light_sensor), 1, 40) #Выводим данные A1
    if distance_sensor_l <= 23 or distance_sensor_r <= 23: #Если видим объект
        mailbox.connect("192.168.77.213") #Подключение к роботу-диспетчеру
        mailbox.send(2, "Stop, found object!") #Отправляем сообщение 
    if light_sensor <= 50: #Если датчик видит повреждение
        if point == 0: #Если флаг опущен
            number+=1 #Переключение номерации
            point=1 #Поднимаем флаг
            hatch('open', number) #Открываем люк
            mailbox.connect("192.168.77.213") #Подключение к роботу-диспетчеру
            mailbox.send(2, "Stop, found breaken!") #Отправляем сообщение
          
    else: #Иначе
        point=0 #Опускаем флаг
        hatch('close') #Закрываем люк
    
    script.wait(10) #Ждём
    