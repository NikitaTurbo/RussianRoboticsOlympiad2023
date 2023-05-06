import sys #Импортируем библиотеку sys
import time #Импортируем библиотеку time

m3=brick.motor("M3") #Делаем цифровую индентификацию M3
e3=brick.encoder("E3") #Делаем цифровую индентификацию E3

object={} #Словарь записей объектов и повреждений
object['encoder'] = [] #Запись энкодеров
object['breaken'] = [] #Запись повреждений

mailbox.connect("192.168.77.1") #Подключение к роботу-инспектору

e3.reset() #Очищаем энкодеры

while True: #Бесконечный цикл
    m3.setPower(35) #Движение мотора со скоростью 35
    encoder=e3.read() #Считываем данные с D2 
    if -encoder >= 1550: #Если робот сделал полный круг
        encoder=e3.reset() #Очищаем энкодеры
        m3.setPower(0) #Останавливаем мотор
    if mailbox.hasMessages() == True: #Если роботу пришло сообщение
        m3.setPower(0) #Останавливаем мотор
        if mailbox.receive() == "Stop, found object": #Если робот-инспектор нашёл объект
            brick.led().red() #Включаем диод красным светом
            object["encoder"].append(e3.read()) #Записываем координаты объекта
            brick.display().setBackground ("white") #Цвет фона
            brick.display().setPainterColor ("red") #Цвет шрифта
            brick.display().setPainterWidth(100) #Размер шрифта
            brick.display().redraw() #Перерисовка
            brick.display().addLabel("Object!", 1, 1) #Выводим сообщение
            script.wait(3000) #Ждём
          
        elif mailbox.receive() == "Stop, found breaken": #Если робот-инспектор нашёл повреждение 
            brick.led().red() #Включаем диод красным светом
            object['breaken'].append(e3.read()) #Записываем координаты повреждения
            brick.display().setBackground ("white") #Цвет фона
            brick.display().setPainterColor ("red") #Цвет шрифта
            brick.display().setPainterWidth(1000) #Размер шрифта
            brick.display().redraw() #Перерисовка
            brick.display().addLabel("Breaken!!!", 1, 1) #Выводим сообщение
            script.wait(3000) #Ждём
        
    script.wait(10) #Ждём
