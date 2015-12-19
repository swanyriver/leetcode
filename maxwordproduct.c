#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <math.h>

typedef struct 
{
  int length;
  int letters;
}parseword;

int maxProduct(char** words, int wordsSize) {
  parseword* pwords = malloc(sizeof(parseword)*wordsSize);
  bzero(pwords,sizeof(parseword)*wordsSize);

  int i=0;
  for(;i<wordsSize;++i){
    char* nextWord = words[i];
    while (*nextWord){
      pwords[i].letters |= 1 << (*nextWord++-'a'); 
    }
    pwords[i].length = nextWord-words[i];
  }

/*  for (i = 0; i < wordsSize; ++i)
  {
    printf("%s:%d(%d)\n",words[i], pwords[i].letters,pwords[i].length);
  }*/

  printf("%f\n", pow(2,wordsSize));

}

int main(int argc, char *argv[])
{
  /* code */

  maxProduct(argv,argc);

  return 0;
}