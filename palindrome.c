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
        while(left>=s && *right){
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

    //even numbered palindromes
    middle=s;
    while(*(middle+1)){

        left=middle;
        right=middle+1;

        while(left>=s && *right){
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

int main(int argc, char const *argv[])
{

    if(argc<2) return 1;

    char* s = malloc(40);
    strcpy(s,argv[1]);

    printf("%s\n", longestPalindrome(s));

}
