#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    if(!*s || numRows == 1) return s;
    
    char* lenpoint = s;
    while(*lenpoint)++lenpoint;
    int len = lenpoint - s;
    
    if(numRows >= len) return s;
    
    struct cursor {
        char** cur;
        struct cursor* next;
    };
    
    char* answer = malloc(len+1);
    answer[len]=0;
    
    int set = numRows + numRows-2;

    struct cursor* cursors = malloc(sizeof(struct cursor) * set);
    char* rows = malloc(sizeof(char*) * numRows);
    int* lengthofRow = malloc(sizeof(int)*numRows);
  

    //set row lengths
    int firstlen = len/set;
    int middlelen = firstlen << 1;
    lengthofRow[0] = firstlen;
    lengthofRow[numRows-1] = firstlen;
    
    int i=1;
    for(;i<numRows-1;++i){
        lengthofRow[i]=middlelen;
    }
    int remain = len%set;
    i=0;
    while(remain && i<numRows){
        ++lengthofRow[i];
        ++i;
        --remain;
    }
    i=numRows-2;
    while(remain && i){
        ++lengthofRow[i];
        --i;
        --remain;
    }


    for(i=0;i<numRows;++i){
        printf("%d,",lengthofRow[i]);
    }
    putchar('\n');

    //set row pointers

    //set cursors to point at appropriate row
    return "hello";
    
}

int main(int argc, char const *argv[])
{
    if(argc==3){
        printf("%s\n", convert(argv[1],atoi(argv[2])));
        return 0;
    }

    return 1;
}


