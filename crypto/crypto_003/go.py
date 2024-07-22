#!/usr/bin/env python3

from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from string import ascii_lowercase

#context.log_level = "debug"
p = remote("127.0.0.1", 9001)

p.readuntil(b"your password is: ")
admin_password = p.readline().decode().strip("\n")

log.success(f"admin password: {admin_password}")

def crack_email():
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    email = a + b + c + d + "@example.com"
                    p.sendlineafter(b"> ", b"1")
                    p.sendlineafter(b"email:", email.encode())
                    p.readuntil(b"your password is: ")
                    password = p.readline().decode().strip("\n")
                    if password == admin_password:
                        return email

email = crack_email()

log.success(f"email: {email}")

p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"email: ", email.encode())
p.sendlineafter(b"password: ", admin_password.encode())

log.success(p.readline().decode()) # flag{...}

