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
    char** rows = malloc(sizeof(char*) * numRows);
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

    //set row pointers
    rows[0]=answer;
    for(i=1;i<numRows;++i){
        rows[i]=rows[i-1]+lengthofRow[i-1];
    }

    //set cursors to point at appropriate row
    for(i=0;i<set;++i){
        if(i==set-1) cursors[i].next = cursors;
        else cursors[i].next = &cursors[i+1];

        if(i<numRows) cursors[i].cur=&rows[i];
        else cursors[i].cur = &rows[numRows-2-numRows%i];
    }

    struct cursor* curs = cursors;
    while(*s){
        curs->cur**=s*;
        curs->++cur**;
        curs = curs->next;
        ++s;
    }

    return answer;
    
}

int main(int argc, char const *argv[])
{
    if(argc==3){
        printf("%s\n", convert(argv[1],atoi(argv[2])));
        return 0;
    }

    return 1;
}


