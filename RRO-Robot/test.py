import sys

mailbox.connect("192.168.77.204")
mailbox.send(2, "Hello")
 
script.wait(10000)