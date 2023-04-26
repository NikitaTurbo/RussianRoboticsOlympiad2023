import sys

while True:
    if mailbox.hasMessages() == True:
        brick.display().setBackground ("white")
        brick.display().setPainterColor ("black")
        brick.display().setPainterWidth(100)
        brick.display().redraw()
        brick.display().addLabel(mailbox.receive(), 1, 1)
        script.wait(10000)
    script.wait(50)
