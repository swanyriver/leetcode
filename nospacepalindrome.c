#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

bool isPalindrome(int x) {
    
    if(x<0) return false;
    if(x<10) return true;
    
    //one less than length
    int length = (int) floor( log10 ((float) x) );

    while(length>=1){
        
        printf("%d%d\n",x%10, (int) x/(pow(10,length)));
        
        printf("%d:%d  [%d/%d], ",length,x, (int) x/(pow(10,length)),x%10);
    
        if(x%10 != (int) (x/(pow(10,length)))) return false;
        
        x=x%10*length;
        x=x%10;
        
        length-=2;
    }
    
    return true;
}

int main(int argc, char const *argv[])
{
    printf(isPalindrome(11) ? "true" : "false");
    return 0;
}