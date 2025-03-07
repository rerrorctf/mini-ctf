#!/usr/bin/env python3

from pwn import *
from Crypto.Cipher import AES

#context.log_level = "debug"
#p = process(["venv/bin/python3", "./server.py"])
p = remote("127.0.0.1", 9001)

flag_enc = bytes.fromhex(p.readline().decode())

chosen_plaintext = b"\xff" * 16
p.sendlineafter(b"> ", chosen_plaintext.hex().encode())

chosen_ciphertext = bytes.fromhex(p.readline().decode())
keystream = xor(chosen_plaintext, chosen_ciphertext)

p.sendlineafter(b"> ", keystream.hex().encode())
nonce = bytes.fromhex(p.readline().decode())[:14]

for i in range(0x10000):
    key = nonce + p16(i)
    flag = AES.new(key, AES.MODE_CTR, nonce=key[:14]).decrypt(flag_enc)
    try:
        print(flag.decode()[:-1])
        break
    except:
        pass
