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

    struct cursor{
        char** cur;
        struct cursor* next;
    };

    //struct cursor sizecur;

    int strucSize = sizeof(struct cursor);

    struct cursor* cursors = malloc(strucSize * set);
    char** rows = malloc(sizeof(char*) * numRows);
    int* lengthofRow = malloc(sizeof(int)*numRows);
  
    int addroffset = &cursors[1] - cursors;

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
    struct cursor* endloop = cursors + addroffset*numRows;
    struct cursor* mycursor = cursors;
    i=0;
    for(;mycursor<endloop;mycursor+=addroffset){

        mycursor->next=mycursor+addroffset;
        mycursor->cur= &rows[i];
        i++;
    }
    endloop = cursors + addroffset*set;
    for(;mycursor<endloop;mycursor+=addroffset){
        mycursor->next=mycursor+addroffset;
        mycursor->cur = &rows[numRows+2-i];
        i++;
    }

    mycursor-=addroffset;
    mycursor->next=cursors;

    mycursor = cursors;
    while(*s){
        **(mycursor->cur)=*s;
        ++s;
        ++*(mycursor->cur);
        mycursor=mycursor->next;
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


