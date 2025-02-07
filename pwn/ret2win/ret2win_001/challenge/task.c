#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void shell() {
    puts("[x] launching secret shell...");
    char* args[] = {"/bin/sh", 0};
    execve("/bin/sh", args, 0);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    puts("do you like to pwn? y/n");

    char answer[4];
    gets(answer);

    printf("you answered \"%c\"\n", answer[0]);

    return 0;
}
