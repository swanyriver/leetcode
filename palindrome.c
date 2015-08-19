#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* longestPalindrome(char* s) {
    char* middle = s;
    
    char *left, *right, *begining;
    int longest = 0;
    
    while (*middle){
        
        left = middle;
        right = middle;
        while(left>s && *right){
            if(*left == *right){
                if (right-left >= longest ) {
                    longest = (right-left)+1;
                    begining = left;
                }
                
                --left;
                ++right;
            } 
            else break;
        }
        
        ++middle;
    }
    
    *(begining+longest)=0; 
    return begining;
}

int main(){

    char* s = malloc(9);
    strcpy(s,"abcdedcz");

    printf("%s\n", longestPalindrome(s));

}
