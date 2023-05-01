# RRO-Project-2023
*На меня с Шимой была поставлена цель: **"Связать роботов"**, чтобы мы могли передавать данные с самого робота инспектора на нашего диспетчера.*

___Как это сделать?___ *Мы нашли ответ :arrow_right: [здесь](https://help.trikset.com/trik/wi-fi/interaction) и [здесь](https://help.trikset.com/trik/programming-code/object-mailbox).*

## Подключение блоков

- *Подключение по сети **WI-FI** к самим контроллерам.*
- *На ноутбуке или смартфоне заходим в веб интерфейс, по **IP-адресу** в поисковой строке.*
- *Затем выбераем ведущего робота.*
- *В веб-интерфейсе ведущего контроллера в поле **«Взаимодействие роботов»** указываем его бортовой номер и его **IP-адрес**.*
 
  ![Alt-текст](https://624002469-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-9YMGCK0ySSnTAiseS%2F-M0CXXrWPAO3MBKAVjU4%2F-M0D4Rjqy97JZNqiT0qE%2Fconfigurator-main.png?alt=media&token=c29b258d-66fb-4c5b-8740-ae5f152637be "Вот так")

- *Подключаем втоой контроллер к этой же **Wi-Fi-сети** в режиме **Клиента**.*
- *Указываем для второго контроллера в его веб-интерфейсе, в поле **«Взаимодействие роботов»** его бортовой номер и **IP-адрес** ведущего контроллера.*

  ![Alt-текст](https://624002469-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-9YMGCK0ySSnTAiseS%2F-M0CXXrWPAO3MBKAVjU4%2F-M0D55tDPjl4U9l56Dl1%2Fconfigurator-other.png?alt=media&token=bfc1fdfc-8c57-480a-9e98-ab1db82cbdf9 "Вот так")
  
- *На всех контроллерах зайдём в пункт меню **Взаимодействие** и нажмём кнопку **«Подключиться»**. В правом верхнем углу на экранах контроллеров должна появиться иконка :envelope:.*

  ![Alt-текст](https://624002469-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-M-9YMGCK0ySSnTAiseS%2F-M0CXXrWPAO3MBKAVjU4%2F-M0D6cM_CcVb1hpP3pR7%2Ftrik-connected.png?alt=media&token=53878604-b7ab-4992-a378-757e71fe0e5a "Вот так")
  
## Программный код

*В :arrow_up: [первом абзаце](https://github.com/NikitaTurbo/RRO-Project-2023/edit/Robot/README.md#rro-project-2023), по второй ссылке мы нашли описание объекта **«mailbox»**.* 
*И написали код для обоих роботов.*

### `Робот-инспектор`
```Python
import sys 

d1=brick.sensor("D1")
d2=brick.sensor("D2") 

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
```

### `Робот-диспетчер`

```Python
import sys
import time

m3=brick.motor("M3")
e3=brick.encoder("E3")

object=0

e3.reset()

while True:
    m3.setPower(35)
    encoder=e3.read()
    if -encoder >= 1550:
        encoder=e3.reset()
        m3.setPower(0)
    if mailbox.hasMessages() == True:
        m3.setPower(0)
        object=e3.read()
        brick.display().setBackground ("white")
        brick.display().setPainterColor ("black")
        brick.display().setPainterWidth(100)
        brick.display().redraw()
        brick.display().addLabel("Object " + str(object), 1, 1)
        script.wait(10000)
        
    script.wait(10)
```
