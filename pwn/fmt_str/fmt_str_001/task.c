#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd;
    char flag[16];
    char input[16];

    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    memset(flag, 0, sizeof(flag));

    fd = open("./flag.txt", O_RDONLY);
    
    read(fd, flag, sizeof(flag));
    
    close(fd);

    fd = -1;

    scanf("%16s", input);

    printf(input);

    puts("\nbye");

    return 0;
}
