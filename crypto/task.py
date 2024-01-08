import sys
import argon2

hash = "$argon2id$v=19$m=102400,t=2,p=8$ZmxhZ3tjb3JyZWN0IGhvcnNl$IGJhdHRlcnkgc3RhcGxlfQ=="
if argon2.PasswordHasher().verify(hash, sys.argv[1]):
	print("verified")
