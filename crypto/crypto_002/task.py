import secrets
import math
import flag

def make_prime(bits):
    while True:
        p = 2**bits - (secrets.randbelow((0xFFFFFFFFFFFF+0x24)&((1<<32)-1))+1)
        if ((math.factorial(p - 1) % p) + 1) == p:
            return p

p = make_prime(414)
q = make_prime(414)
n = p * q
t = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, t)

m = int.from_bytes(flag.FLAG, byteorder="big")
c = pow(m, e, n)
print(c)
