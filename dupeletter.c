#include <stdio.h>
#include <stdlib.h>
#include <strings.h>



struct letterlink{
    char ch;
    struct letterlink* next;
    struct letterlink* prev;
};

void printstuff(struct letterlink head, struct letterlink** array){
    struct letterlink* i = head.next;
    for (; i;i=i->next){
        printf("(%p)%c->",i,i->ch );
    }
    printf("%s","\n" );

    char c = 'a';
    for(;c<='z';++c){
        printf("%c:%p\n", c, array[c] );
    }
}

char* removeDuplicateLetters(char* s) {
    char* result = malloc(27);
    char* cursor = result;
    struct letterlink lettersinlist[26];
    struct letterlink head;
    struct letterlink* lastlink = lettersinlist;
    int numlinks;
    struct letterlink* letters['z'+1];

    if(!s || !*s){
        *result=0;
        return result;
    }

    
    bzero(letters+'a',26 * sizeof(struct letterlink*));

    numlinks=1;
    lettersinlist[0].ch=*s;
    lettersinlist[0].next=NULL;
    lettersinlist[0].prev=&head;
    head.next=lettersinlist;
    letters[*s]=lettersinlist;
    ++s;

    
    while(*s){

        //printstuff(head,letters);
        //getchar();

        //printf("%c%d ",*s,*s);
        
        if (!letters[*s])
        {
            //add letter to end of LL
            letters[*s]=lettersinlist+numlinks;
            lettersinlist[numlinks].ch=*s;
            lettersinlist[numlinks].next=NULL;
            lettersinlist[numlinks].prev=lastlink;
            lastlink->next = lettersinlist+numlinks;
            lastlink=&lettersinlist[numlinks]; 
            ++numlinks;
        }else if ( letters[*s]->next && letters[*s]->next->ch < *s ) {
            //reposition letter to the end
            letters[*s]->prev->next = letters[*s]->next;
            letters[*s]->next->prev = letters[*s]->prev;
            lastlink->next = letters[*s];
            letters[*s]->prev = lastlink;
            lastlink = letters[*s];
            letters[*s]->next = NULL;

        }
        ++s;
    }
    
    struct letterlink* i = head.next;
    for (; i;i=i->next){
        *cursor++=i->ch;
    }
    *cursor=0;
    return result;
    
}

int main(int argc, char const *argv[])
{
    /* code */

    //printf("%s\n", removeDuplicateLetters("abracadabra"));

    char* result = removeDuplicateLetters("abracadabra");
    printf("\n%s\n", result);
    free(result);

    return 0;
}
