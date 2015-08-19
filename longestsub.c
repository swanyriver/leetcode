#include <stdio.h>
#include <stdlib.h>
#include <strings.h>


int lengthOfLongestSubstring(char* s) {
    int pos[256];
    bzero(pos,sizeof(int)*256);
    int longest=0;
    char* begining = s;
    int length;
    
    while (*s){
        if(!pos[*s]){
            length = s-begining;
            if(length >= longest)longest = length + 1;
            pos[*s]=s;
        } else {
            while (begining < pos[*s]){
                pos[*begining]=0;
                ++begining;
            }
            begining = pos[*s]+1;
            char* point = pos[*s];
            if(*point==*s) pos[*s]=s;
            else pos[*s]=0;
        }
        ++s;
    }
    
    return longest;
}

int main(){
    printf("%d\n", lengthOfLongestSubstring("tmmzuxt") );
}