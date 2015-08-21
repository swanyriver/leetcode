#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    if(!*s || numRows == 1) return s;
    
    char* lenpoint = s;
    while(*lenpoint)++lenpoint;
    int len = lenpoint - s;
    
    if(numRows >= len) return s;
    
    
    char* answer = malloc(len+1);
    answer[len]=0;
    
    int set = numRows + numRows-2;

    int* cursors = malloc(sizeof(int*) * set);
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
        if(i<numRows) cursors[i]=i;
        else cursors[i] = numRows-2-(i%numRows);
        //printf("%d [%d]:%p,   ",cursors[i], lengthofRow[cursors[i]], rows[cursors[i]]);
    }
    //return "hello";

    while(*s){
        for(i=0;i<set && *s;++i){
            *(rows[cursors[i]])=*s;
            //printf("%c:%p",*(rows[cursors[i]]), rows[cursors[i]] );
            ++s;
            ++rows[cursors[i]];
            //printf(" --> %p\n",rows[cursors[i]] );
        }
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


