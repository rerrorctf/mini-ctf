nasm -f elf64 ./task.S
ld -m elf_x86_64 task.o -o task
