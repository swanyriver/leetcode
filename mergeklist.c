#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){

    struct ListNode* head = 0;
    struct ListNode* current = malloc(sizeof (struct ListNode));
    struct ListNode** nextPoint;
    int min;


    for(struct ListNode** i = lists; i < lists+listsSize;){
        if(!*i){
            --listsSize;
            for(struct ListNode** v = i; v<lists+ listsSize; v+=1) *v = *(v+1);
        } else i += 1;
    }

    while(listsSize > 1){
        min = lists[0]->val;

        for(struct ListNode** i = lists; i < lists+listsSize; i+=1){
            if((*i)->val <= min ) {
                min = (*i)->val;
                nextPoint = i;
            }
        }

        if(!head)head = *nextPoint;
        current->next = *nextPoint;
        current = *nextPoint;
        *nextPoint = (*nextPoint)->next;
        if(!(*nextPoint)){
            --listsSize;
            for(struct ListNode** v = nextPoint; v<lists+ listsSize; v+=1) *v = *(v+1);
        } 
    }
    current->next = lists[0];

    if(!head) head = lists[0];

    return head;
}

struct ListNode** generate( int numLists){

    struct ListNode** lists = malloc(sizeof(struct ListNode*)*numLists);

    for(int i=0; i<numLists; ++i){
        int lengthoflist = rand() % 10 + 1;

        int val = rand()%10;

        if(rand()%2){
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
        } else lists[i] = NULL;
    }

    return lists;
}

void display(struct ListNode** lists, int numLists){
    struct ListNode* cursor;

    //printf("size:%d,  numLists:%d \n", sizeof(struct ListNode**), numLists);

    for(struct ListNode** i = lists; i < lists+numLists; i=i+1){
        cursor = *i;
        if(!cursor) printf("%s", "empty");
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

    struct ListNode* mergedList = mergeKLists(myLists, numLists);

    while(mergedList){
        printf("%d->", mergedList->val);
        mergedList=mergedList->next;
    }
    putchar('\n');

}