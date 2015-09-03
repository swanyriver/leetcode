#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char** letterCombinations(char* digits, int* returnSize) {

    struct letter {
        char ch;
        struct letter* next;
    };

    struct number {
        int size;
        struct letter* letter;
    };
    
    struct number* numbers = malloc(sizeof(struct number)*8);
    struct letter* letters = malloc(sizeof(struct letter)*26);

    char nextletter = 'a';
    struct letter* let = letters;
    for(; let<letters+26; let+=1){
        let->ch = nextletter++;
        let->next = let+1;
    }
    letters['c'-'a'].next = letters;
    letters['f'-'a'].next = &letters['d'-'a'];

    letters['i'-'a'].next = &letters['g'-'a'];
    letters['l'-'a'].next = &letters['j'-'a'];
    letters['o'-'a'].next = &letters['m'-'a'];

    letters['s'-'a'].next = &letters['p'-'a'];
    letters['v'-'a'].next = &letters['t'-'a'];
    letters['z'-'a'].next = &letters['w'-'a'];
    

    numbers[0].size = 3; numbers[0].letter = letters;
    numbers[1].size = 3; numbers[1].letter = &letters['d'-'a'];

    numbers[2].size = 3; numbers[2].letter = &letters['g'-'a'];
    numbers[3].size = 3; numbers[3].letter = &letters['j'-'a'];
    numbers[4].size = 3; numbers[4].letter = &letters['m'-'a'];

    numbers[5].size = 4; numbers[5].letter = &letters['p'-'a'];
    numbers[6].size = 3; numbers[6].letter = &letters['t'-'a'];
    numbers[7].size = 4; numbers[7].letter = &letters['w'-'a'];
    


    int numcombos = 1;
    char* cursor = digits;

    while(*cursor){
        numcombos*= numbers[*cursor - '2'].size;
        ++cursor;
    }

    *returnSize = numcombos;

    int stringlength = (cursor-digits) +1;

    char* block = malloc(numcombos * stringlength );
    char* end = block + numcombos * stringlength;

    cursor = digits;

    struct number* mynumber;
    struct letter* myletter;
    int numcycles = numcombos;


    while(*cursor){
        mynumber = &numbers[*cursor - '2'];
        numcycles = numcycles/mynumber->size;
        myletter = mynumber->letter;

        for(char* write = block + ( cursor - digits ) ;write< end; ){
            for (int i = 0; i < numcycles; ++i)
            {
                *write = myletter->ch;
                write+=stringlength;
            }
            myletter = myletter->next;
        }

        ++cursor;
    }

    for(char* write = block + stringlength - 1;write< end; write+=stringlength){
        *write = 0;
    }

    char** answer = malloc(sizeof(char*) * numcombos);

    cursor = block;
    for (int i = 0; i < numcombos; ++i)
    {
       answer[i]=cursor;
       cursor+=stringlength;
    }

    return answer;

}

int main(int argc, char const *argv[])
{
    /* code */

    if(argc < 2){
        printf("more args:%d\n", argc);
        return 0;
    }

    int returnSize;

    char** combinations = letterCombinations(argv[1], &returnSize);

    for (int i = 0; i < returnSize; ++i)
    {
        printf("%s, ", combinations[i]);
    }

    return 0;
}