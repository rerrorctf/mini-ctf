; $ echo -n "flag{re}" | xxd -p
; 666c61677b72657d
;
; >>> bin(0x666c61677b72657d)
; '0b110011001101100011000010110011101111011011100100110010101111101'
;
; echo -n "flag{re}" | ./task

section .data
    correct_str db "correct :)", 10, 0
    incorrect_str db "incorrect :<", 10, 0

section .text
    global _start

_start:
    xor edi, edi
    xor eax, eax
    mov rsi, rsp
    mov edx, 8
    syscall

    mov rax, [rsp]
    xor ebx, ebx
    xor ecx, ecx

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 2
    setc bl
    or rcx, rbx
    shl rcx, 1

    ror rax, 3
    setc bl
    or rcx, rbx
    shl rcx, 1

    rol rax, 1
    setc bl
    or rcx, rbx

    mov rax, 0x3de061f5d603e994
    cmp rax, rcx
    jnz incorrect

    mov eax, 1
    mov edi, 1
    mov rsi, correct_str
    mov rdx, 11
    syscall

    jmp exit

incorrect:
    mov eax, 1
    mov edi, 1
    mov rsi, incorrect_str
    mov rdx, 13
    syscall

exit:
    mov eax, 60
    xor edi, edi
    syscall
