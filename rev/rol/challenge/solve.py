from itertools import product
import string
import subprocess

for combination in product(string.printable, repeat=2):
    flag = "flag{" + "".join(combination) + "}"
    command = "echo -n \"" + flag + "\" | ./task"
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if "correct :)" in result.stdout:
        print(flag)

# $ python3 ./solve.py
# flag{re}
