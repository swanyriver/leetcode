#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    
    char* mychars = malloc(sizeof(char)*10);

    int* myints = malloc(sizeof(int)*10);

    struct mystruct
    {
        char** cur;
        struct mystruct* next;
    };

    struct mystruct* starr = malloc(sizeof(struct mystruct)*10);

    putchar('\n');

    return 0;
}