#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct ListNode {
    int val;
    struct ListNode *next;
};


struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){

}

struct ListNode** generate( int numLists){

    struct ListNode** lists = malloc(sizeof(struct ListNode*)*numLists);

    for(int i=0; i<numLists; ++i){
        int lengthoflist = rand() % 10 + 1;

        int val = rand()%10;

        lists[i] = malloc(sizeof(struct ListNode));

        lists[i]->val = val;

        struct ListNode* current = lists[i];

        for(int x=0; x<lengthoflist-1; ++x){
            val += rand()%10;
            current->next = malloc(sizeof(struct ListNode));
            current=current->next;
            current->val = val;
        }
        current->next = NULL;
    }

    return lists;
}

void display(struct ListNode** lists, int numLists){
    struct ListNode* cursor;

    printf("size:%d,  numLists:%d \n", sizeof(struct ListNode**), numLists);

    for(struct ListNode** i = lists; i < lists+numLists; i=i+1){
        cursor = *i;
        while(cursor){
            printf("%d->", cursor->val);
            cursor = cursor->next;
        }
        putchar('\n');
    }
}

int main(){

    srand (time(NULL));

    int numLists = rand() % 6 + 1;

    struct ListNode** myLists = generate( numLists );

    display(myLists,numLists);



}