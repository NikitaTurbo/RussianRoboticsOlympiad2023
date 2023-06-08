import sys #Импортируем библиотеку sys
import time #Импортируем библиотеку time

m3=brick.motor("M3") #Делаем цифровую индентификацию M3
e3=brick.encoder("E3") #Делаем цифровую индентификацию E3

object={} #Словарь записей объектов и повреждений
object['encoder'] = [] #Запись энкодеров
object['breaken'] = [] #Запись повреждений

encoder=0
coor=0

e3.reset() #Очищаем энкодеры
number=-1

while -encoder <= 1554: #Цикл с условием
    m3.setPower(30) #Движение мотора со скоростью 35
    encoder=e3.read() #Считываем данные с e3    
    script.wait(10) #Ждём    

mailbox.send(2, 20) #Отправляем сообщение

e3.reset()
encoder =  e3.read() #Очищаем энкодеры

while -encoder <= 1554: #Бесконечный цикл
    m3.setPower(30) #Движение мотора со скоростью 35
    encoder=e3.read() #Считываем данные с e3 
    if mailbox.hasMessages() == True: #Если роботу пришло сообщение
        m3.setPower(0) #Останавливаем мотор
        encoder=e3.read()
        #if mailbox.receive() == 0: #Если робот-инспектор нашёл объект
            #brick.led().red() #Включаем диод красным светом
            #object["encoder"].append(e3.read()) #Записываем координаты объекта
            #brick.display().setBackground ("white") #Цвет фона
            #brick.display().setPainterColor ("red") #Цвет шрифта
            #brick.display().setPainterWidth(1000) #Размер шрифта
            #brick.display().redraw() #Перерисовка
            #brick.display().addLabel("Object!", 1, 1) #Выводим сообщение
            #script.wait(10000) #Ждём
          
        if mailbox.receive() == "10": #Если робот-инспектор нашёл повреждение 
            number+=1;
            object['breaken'].append(str(int((170 * -encoder) / 1554)) + ' см') #Записываем координаты повреждения
            script.wait(4000) #Ждём
        
    script.wait(10) #Ждём
    
m3.setPower(0) #Движение мотора со скоростью 0    
brick.display().setBackground ("white") #Цвет фона
brick.display().setPainterColor ("black") #Цвет шрифта
brick.display().setPainterWidth(1000) #Размер шрифта
brick.display().redraw() #Перерисовка
brick.display().addLabel('Результаты:', 1, 1) #Выводим сообщение
brick.display().addLabel('Повреждение(я):', 1, 20) #Выводим сообщение
for i in range(0, number+1):
    brick.display().redraw() #Перерисовка
    brick.display().addLabel(str(object['breaken'][i]), 1, 20 * (i+2)) #Выводим сообщение
    script.wait(1)
script.wait(10000)
  
