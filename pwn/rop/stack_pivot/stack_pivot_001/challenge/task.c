#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

void win() {
    system("/bin/sh");
}

void free_bubblewrap() {
    __asm__ volatile("pop rbx\n pop rcx\n pop rdx\n ret\n");
}

void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int main() {
    int64_t buf[10];

    setup();

    for (int i = 0; i < 3; ++i){
        scanf("%ld", &buf[i]);
    }

    *(uintptr_t*)buf[2] = (uintptr_t)buf[1];

    puts("cya!");

    return 0;
}
