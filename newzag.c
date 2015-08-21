#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    if(!*s || numRows == 1) return s;
    
    char* endpoint = s;
    while(*endpoint)++endpoint;
    int len = endpoint - s;
    
    if(numRows >= len) return s;
    
    
    char* answer = malloc(len+1);
    answer[len]=0;
    char* realanswer = answer;
    
    int set = numRows + numRows-2;

    //firstrow
    char* cur = s;
    while(cur<endpoint){
        *answer=*cur;
        ++answer;
        cur+=set;
    }

    //middle rows
    int i=1;
    char* curB;
    int add=set; 
    for(;i<numRows-1;++i){
        cur = s+i;
        add -=2;
        curB = cur + add;
        while(cur<endpoint){
            *answer = *cur;
            ++answer;
            cur+=set;

            if(curB>endpoint) break;

            *answer = *curB;
            ++answer;
            curB+=set;
        }
    }

    //lastrow
    cur = s+numRows-1;
    while(cur<endpoint){
        *answer=*cur;
        ++answer;
        cur+=set;
    }


    return realanswer;
    
}

int main(int argc, char const *argv[])
{

    if(argc==3){
        printf("%s\n", convert(argv[1],atoi(argv[2])));
        return 0;
    }

    return 1;
}


