import base64

# we split the flag into two pieces and base64 encode them
# .. then we stuff them in the hash

hash = b"$argon2id$v=19$m=102400,t=2,p=8$"
hash += base64.b64encode(b"flag{correct horse")
hash += b"$"
hash += base64.b64encode(b" battery staple}")
print(hash)
