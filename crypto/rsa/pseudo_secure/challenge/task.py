import secrets
import flag

def factorial(x):
    f = 1
    for i in range(x):
        f = f * (i + 1)
    return f

def make_prime(bits):
    while True:
        # generate a candidate pseudo-mersenne prime
        p = 2**bits - (secrets.randbelow((0xFFFFFFFFFFFF+0x24)&((1<<32)-1))+1)

        # check if the candidate is prime using wilson's theoreom
        if ((factorial(p - 1) % p) + 1) == p:
            return p

p = make_prime(414)
q = make_prime(414)
n = p * q
t = (p - 1) * (q - 1)
e = 65537

print(f"n = {n}")
print(f"e = {e}")

m = int.from_bytes(flag.FLAG, byteorder="big")
c = pow(m, e, n)

print(f"c = {c}")
