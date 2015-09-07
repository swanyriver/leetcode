#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
    
    int* length = malloc(sizeof(int)*wordsSize);
    char* cursor;

    //get lengths;
    for (int i = 0; i < wordsSize; ++i)
    {
        cursor = words[i];
        while(*cursor) ++cursor;
        length[i]= cursor-words[i];
    }

    //maximum needed  //todo try mallocing each time
    char* output = malloc(maxWidth*wordsSize);
    char** lines = malloc(sizeof(char*)*(wordsSize+1));

    int linenum = 0;
    int firstword,lastword, wordslength, numwords;
    int spaceL,spaceS,numSpaceL;
    char** word;
    char* wordR;
    firstword=0;
    while(firstword < wordsSize){
        wordslength=length[firstword] +1;
        lastword=firstword;
        while(wordslength<maxWidth && ++lastword < wordsSize){
            wordslength+=length[lastword] + 1;
        }
        //lop off last word if it wasnt just the space
        if(wordslength > maxWidth+1){
            wordslength-=length[lastword]+1;
            --lastword;
        }
        

        //copy words to new spot
        lines[linenum]=output;
        numwords = lastword-firstword+1;
        word = &words[firstword];

        if(lastword == wordsSize || numwords == 1){
            if(lastword == wordsSize) --numwords;
            //left justified
            for (int i = 0; i < numwords-1; ++i)
            {
                //write word
                wordR = *word;
                while(*wordR) *output++ = *wordR++;
                *output++ = ' ';
                ++word;
            }
            wordR = *word;
            while(*wordR) *output++ = *wordR++;
            while(output-lines[linenum]<maxWidth) *output++ = ' ';
            *output++ = 0;

        }else {
            //justified
            
            wordslength -= numwords;
            spaceS = (maxWidth-wordslength) / (numwords-1);
            numSpaceL = (maxWidth-wordslength) % (numwords-1);
            
            for (int i = 0; i < numwords-1; ++i)
            {
                //write word
                wordR = *word;
                while(*wordR) *output++ = *wordR++;

                for (int v = 0; v < spaceS; ++v) *output++ = ' ';
                if(i<numSpaceL) *output++ = ' ';
                ++word;
            }
            wordR = *word;
            while(*wordR) *output++ = *wordR++;
            *output++ = 0;
        }

        //printf("%d :{%s}   firstword:%d  lastword:%d\n", linenum, lines[linenum] , firstword, lastword);
        //getchar();

        firstword = lastword+1;
        linenum++;
    }

    *returnSize = linenum;
    return lines;
}

int main(int argc, char const *argv[])
{
    
    char* words[] = {"well", "lets", "see", "if", "this",    "works", "im", "really", "not", "sure", 
                     "how", "well", "it", "will", "go",       "but", "it", "will", "probably", "have",
                      "a", "desirable", "effect", "nonetheless"};

    int returnsize;

    if(argc < 2) return 1;

    char** result = fullJustify(words,24,atoi(argv[1]),&returnsize);
    //display
    for (int i = 0; i < returnsize; ++i)
    {
        printf("%s\n", result[i]);
    }

    return 0;
}