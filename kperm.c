#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int factorial[10]={0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };

char* getPermutation(int n, int k) {
    int i,nextIndex,si;
    
    char* digits = malloc(sizeof(char)*n);
    strncpy(digits,"123456789",n);
    char* output = malloc(sizeof(char)*n);
    char* cursor = output;
    char* select;
    
    for(i=n-1;i>0;--i){
        nextIndex = (int) ceil( (float) k/factorial[i])-1;

        putchar(nextIndex + 3*16);
        
        /*si=0;
        select=digits;
        while(si<nextIndex){
            if(*select != 'Z') ++si;
            ++select;
        }
        *cursor=*select;
        cursor++;
        *select='Z';
        
        k = k%factorial[i];
        
        if(k==0){
            cursor = output + i-1;
            for (select = digits+8; select>=output; --select){
                if (*select!='Z') *cursor=*select;
                cursor++;
            }
        }*/
    }
    
    return output;
}

int main(){
    int i;
    for ( i = 1; i <= factorial[3]; ++i)
    {
        printf("%d-->%s\n",i,getPermutation(3,i) );
    }
}