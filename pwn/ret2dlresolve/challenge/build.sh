gcc -masm=intel -fno-stack-protector -Wl,-z,relro -no-pie -o task ./task.c
