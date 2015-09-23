#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void reverseWords(char *s) {

    char* L;
    char* R;
    
    L=s;
    R=s;

    char temp;
    while(*R)++R;
    --R;
    while(*R == ' ') --R;

    ++R;
    --L;
    
    while(++L<R){
        temp = *L;
        *L = *--R;
        *R = temp;
    }

    //string is reversed

    L = s-2;
    R=s;
    char* endofword = s;

    while(*endofword){
        while(*R == ' ')++R;
        if (!*R) break;
        while(*R && *R != ' ') ++R;
        endofword = R;

        ++L;
        while(++L<R){
            temp = *L;
            *L = *--R;
            *R = temp;
        }

        L = endofword;
        while(*L==' ') --L;
        R = endofword+1;
    }
    while(*endofword == ' ') --endofword;
    *++endofword=0;

}

int main(int argc, char const *argv[])
{
    
    if(argc<2){
        printf("%s\n", "please include a string" );
        return 1;
    }

    char* copy = malloc(strlen(argv[1]));
    strcpy(copy,argv[1]);

    reverseWords(copy);

    printf("%s|\n", copy );


    return 0;
}