#!/usr/bin/env python3

import os
from Crypto.Cipher import AES

with open("flag.txt", "rb") as f:
    FLAG = f.read()

KEY = os.urandom(16)

def enc(k, p):
    return AES.new(k, AES.MODE_CTR, nonce=k[:14]).encrypt(p)

def dec(k, c):
    return AES.new(k, AES.MODE_ECB).decrypt(c)

if __name__ == "__main__":
    print(enc(KEY, FLAG).hex())
    print(enc(KEY, bytes.fromhex(input("> "))).hex())
    print(dec(KEY, bytes.fromhex(input("> "))).hex())
