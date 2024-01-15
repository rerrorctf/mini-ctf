from itertools import product
import string
import subprocess

for combination in product(string.printable, repeat=2):
    flag = "flag{" + "".join(combination) + "}"
    command = "echo -n " + flag + " | ./task"
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    if "correct :)" in result.stdout:
        print(f"potential: {flag}")

# $ python3 ./solve.py
# potential: flag{rd}
# potential: flag{re}
# potential: flag{vd}
# potential: flag{ve}
