#include <stdio.h>
#include <stdlib.h>
#include <time.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode** generate( int numLists){

    struct ListNode** lists = malloc(sizeof(struct ListNode*)*numLists);

    for(int i=0; i<numLists; ++i){
        int lengthoflist = rand() % 20 + 1;

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

struct ListNode* reverseKGroup(struct ListNode* head, int k) {


    struct ListNode** first= &head;
    struct ListNode** nextFirst= &head;
    struct ListNode* kend = head;
    struct ListNode* tmp; 
    struct ListNode* butt;
    struct ListNode* read=head;
    int count;


    while(1){
        count =0;
        while(kend && count++<k){
            //printf("kend %p->%d  c:%d\n", kend, kend->val,count);
            kend = kend->next; 
        }
        if (count < k) return head;
        
        butt = kend;
        nextFirst = &read->next;

        while(read!=kend){
            tmp = read->next;
            read->next = butt;
            butt = read;
            //if (tmp == kend) break;
            read = tmp;
        }
        *first = butt;
        first = nextFirst;
        //printf("first:%p  head:%p\n", *first, head );

        //first = &(read->next);
        //if(read)read = read->next;
    }

    
}

int main(){

    srand (time(NULL));

    struct ListNode** myLists = generate( 1 );

    display(myLists,1);

    struct ListNode** mlist = malloc(sizeof(struct ListNode));
    *mlist = reverseKGroup(*myLists, 3);

    //struct ListNode* mlist = *mergedList;
    display(mlist,1);
   /* while(mlist){
        printf("%p --> %p, %d\n", mlist, mlist->next, mlist->val );
        mlist = mlist->next;
        getchar();
    }*/


}