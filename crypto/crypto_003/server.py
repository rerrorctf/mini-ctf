#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from os import urandom
from hmac import compare_digest
from random import choice
from string import ascii_lowercase

IV = urandom(16)
KEY = urandom(16)

admin_email = "".join(choice(ascii_lowercase) for i in range(4)) + "@example.com"
admin_password = b""

def menu():
    print("[1] register")
    print("[2] get flag")

def register(email):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    password = cipher.encrypt(pad(email.encode(), 16))
    print("thanks for registering")
    print(f"your password is: {password.hex()}")
    return password

def get_flag():
    email = input("email: ")
    password = bytes.fromhex(input("password: "))

    if compare_digest(password, admin_password) == False:
        print("must be admin to get flag")
        return

    print(open("flag.txt", "r").read().strip("\n"))
    
if __name__ == "__main__":
    admin_password = register(admin_email)

    menu()

    while True:
        choice = input(" > ")
        if choice == "1":
            register(input("email: "))
        elif choice == "2":
            get_flag()
        else:
            print("invalid choice")
            break
