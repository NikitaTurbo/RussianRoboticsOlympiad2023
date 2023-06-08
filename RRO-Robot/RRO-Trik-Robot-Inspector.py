import sys #Импортируем библиотеку sys
import time #Импортируем библиотеку time

#169,56

d1=brick.sensor("D1") #Делаем цифровую индентификацию D1
d2=brick.sensor("D2") #Делаем цифровую индентификацию D2
a1=brick.sensor("A1") #Делаем цифровую индентификацию A1 
s1=brick.motor("S1") #Делаем цифровую индентификацию S1
m4=brick.motor("M4") #Делаем цифровую индентификацию M4
gyro=brick.gyroscope() #Делаем цифровую индентификацию гироскопа 

number=0 #Номерация буёв
point=0 #Значение флага
n_black=0
gyroscope=[]

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
        if command == 'close': #Если надо открыть
            for i in range(-90, 90): #Цикл открывания
                s1.setPower(10) #Подаём скорость на сервопривод
                script.wait(10) #Ждём
        elif command == 'close': #Если надо закрыть
            for i in range(90, -90): #Цикл закрывания
                s1.setPower(10) #Подаём скорость на сервопривод
                script.wait(10) #Ждём         

while mailbox.hasMessages() == False: #Цикл с условием
    m4.setPower(100) #Включаем вентилятор
    script.wait(1) #Ждём

m4.setPower(0) #Останавливаем вентилятор

while True: #Бесконечный цикл
    #distance_sensor_r=d1.read() #Считываем данные с D1   
    #distance_sensor_l=d2.read() #Считываем данные с D2  
    light_sensor=a1.read() #Считываем данные с A1 
    gyroscope=gyro.read()
    #if distance_sensor_l <= 10 or distance_sensor_r <= 10: #Если видим объект
        #mailbox.connect("192.168.77.213") #Подключение к роботу-диспетчеру
        #mailbox.send(2, 0) #Отправляем сообщение
    if light_sensor <= 10: #Если датчик видит повреждение
            #number+=1 #Переключение номерации
            #hatch('open', number) #Открываем люк
            while light_sensor <= 10:
              light_sensor=a1.read() #Считываем данные с A1 
              n_black+=1;
              script.wait(1)
            if n_black >= 25:
              mailbox.send(0, 10) #Отправляем сообщение
              n_black=0   
    #else: #Иначе
        #hatch('close', number) #Закрываем люк
    script.wait(10) #Ждём
    