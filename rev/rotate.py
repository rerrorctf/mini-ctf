import struct

flag = struct.unpack("<Q", b"flag{re}")[0]

for i in range(64):
    flag = (flag >> 1) | (flag << 63) & 0xffffffffffffffff
    print(f"{hex(flag)} {struct.pack('<Q', flag)}")
