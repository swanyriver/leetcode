#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

int factorial[10]={0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 };

char* getPermutation(int n, int k) {

    if(n==1 && k==1) return "1";

    int i,nextIndex,si;
    
    char* digits = malloc(sizeof(char)*n);
    strncpy(digits,"123456789",n);
    char* output = malloc(sizeof(char)*n);
    char* cursor = output;
    char* select;
    
    for(i=n-1;i>0;--i){
        nextIndex = (int) ceil( (float) k/factorial[i])-1;
        
        si=0;
        select=digits;
        while(si<nextIndex){
            if(*select != 'Z') ++si;
            ++select;
        }
        while(*select=='Z') select++;
        *cursor=*select;
        cursor++;
        *select='Z';
        
        k = k%factorial[i];
        
        if(k==0){
            
            cursor=output + (n-i);
            for (select = digits+n -1; select>=digits; --select){
                if (*select!='Z'){
                    *cursor=*select;
                    ++cursor;
                }
                
            }
            return output;
        }
    }
    
    return output;
}

int main(){
    int i;
    for ( i = 1; i <= factorial[3]; ++i)
    {
        char* result = getPermutation(3,i);
        //printf("%d-->%d,%d,%d,%d,%d,%d,%d\n",i,result[0],result[1],result[2],result[3],result[4],result[5],result[6] );
        printf("%d --> %s\n",i,result);
    }

    printf("%d --> %s\n",1,getPermutation(1,1));

}