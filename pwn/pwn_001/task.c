#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void shell() {
    puts("[x] launching secret shell...");
    char* args[] = {"/bin/sh", 0};
    execve("/bin/sh", args, 0);
}

int main() {
    puts("do you like to pwn? y/n");

    char answer[4];
    gets(answer);

    printf("you answered \"%c\"\n", answer[0]);

    return 0;
}
