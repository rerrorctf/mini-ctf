# pwn

Task types listed roughly from easier => harder.

## shellcode

1) shellcode_mmap
2) shellcode_execstack
3) shellcode_execstack_gets_leak
4) shellcode_execstack_gets_no_leak
5) shellcode_execstack_gets_no_leak_pie
6) shellcode_mmap_bad_bytes

## ret2win

1) ret2win_gets
2) ret2win_gets_canary
3) ret2win_gets_pie
4) ret2win_gets_canary_pie
5) ret2win_read_1_byte
6) ret2win_read_1_byte_canary
7) ret2win_read_1_byte_pie
8) ret2win_read_1_byte_canary_pie

## ret2libc

1) ret2libc_gets
2) ret2libc_fgets
3) ret2libc_gets_canary
4) ret2libc_fgets_canary

## rop

1) rop_stack_pivot

## fmt_str

1) fmt_str_read_flag_from_stack
2) fmt_str_got_overwrite_read
3) fmt_str_got_overwrite_read_pie
4) fmt_str_got_overwrite_read_no_leak
5) fmt_str_got_overwrite_read_no_leak_pie
6) fmt_str_got_overwrite_fgets
7) fmt_str_got_overwrite_fgets_pie
8) fmt_str_got_overwrite_fgets_no_leak
9) fmt_str_got_overwrite_fgets_no_leak_pie
10) fmt_str_rop

## ret2plt

1) ret2plt_gets
2) ret2plt_gets_pie

## ret2dlresolve

1) ret2dlresolve
2) ret2dlresolve_canary
3) ret2dlresolve_pie
4) ret2dlresolve_canary_pie
