#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
    char ch;
    struct letterlink* next;
    struct letterlink* prev;
}letterlink;

char* removeDuplicateLetters(char* s) {
    char* result = malloc(27);
    char* cursor = result;
    letterlink lettersinlist[26];
    letterlink* firstlink = lettersinlist;
    letterlink* lastlink = lettersinlist;
    int numlinks;
    letterlink* letters['z'+1];

    
    bzero(letters+'a',26 * sizeof(letterlink*));
    
    while(*s){
        printf("%c%d ",*s,*s);
        *s++;
        //letters[*s++]=true;
    }
    
    /*for(char i='a';i<='z';++i){
        if (letters[i]) *cursor++=i;
    }*/
    *cursor++='a';
    *cursor=0;
    return result;
    
}

int main(int argc, char const *argv[])
{
    /* code */

    //printf("%s\n", removeDuplicateLetters("abracadabra"));

    char* result = removeDuplicateLetters("abracadabra");
    free(result);

    return 0;
}
