#include <stdio.h>
#include <stdlib.h>
#include <time.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

void heapify(struct ListNode** lists, int listsSize){
    int leftchild, rightchild;
    struct ListNode* temp;
    for(int i = (listsSize >> 1) - 1; i>=0; --i ){
        leftchild = (i<<1) +1;
        rightchild = (i<<1) +2;

        if(lists[i]->val > lists[leftchild]->val){
            temp = lists[i];
            lists[i] = lists[leftchild];
            lists[leftchild]=temp;
        }

        if(rightchild < listsSize){
            //check both childs
            if(lists[i]->val > lists[rightchild]->val){
                temp = lists[i];
                lists[i] = lists[rightchild];
                lists[rightchild]=temp;

                if(lists[i]->val > lists[leftchild]->val){
                    temp = lists[i];
                    lists[i] = lists[leftchild];
                    lists[leftchild]=temp;
                }
            }
        }
    }


   /* printf("heaped (%d)\n", listsSize );

    //for testing
    int level = 1;
    int levelcount=0;
    for (int i = 0; i < listsSize; ++i)
    {
        if(levelcount==level){
            putchar('\n');
            level *= 2;
            levelcount=0;
        }
        printf(" %d ", lists[i]->val);
        ++levelcount;
    }
    putchar('\n');
    exit(0);*/

}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    if(listsSize<=1) return *lists;

    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* current = head;


    for(int i=0;i<listsSize;++i){
        if(!lists[i]){
            --listsSize;
            for (int v = i; v < listsSize; ++v) lists[v]=lists[v+1];
        }
    }


    heapify(lists,listsSize);

    int i, rightchild, leftchild, smallchild;
    struct ListNode* temp;


    while(listsSize){
        temp = lists[0]->next;
        current->next = lists[0];
        current = current->next;

        lists[0]=temp;
        if(!lists[0]){
           --listsSize;
           lists[0]=lists[listsSize];
        }

        if(listsSize){
            i=0;
            //percolate down
            while(i<listsSize/2){
                leftchild = (i<<1) +1;
                rightchild = (i<<1) +2;

                if(rightchild >= listsSize){
                    //only left child
                    if(lists[i]->val < lists[leftchild]->val) break;
                    temp = lists[i];
                    lists[i]=lists[leftchild];
                    lists[leftchild]=temp;
                    break;
                } else {
                    if(lists[i]->val < lists[leftchild]->val && lists[i]->val < lists[rightchild]->val) break;

                    if(lists[leftchild]->val < lists[rightchild]->val) smallchild = leftchild;
                    else smallchild = rightchild;

                    temp = lists[i];
                    lists[i]=lists[smallchild];
                    lists[smallchild]=temp;
                    i=smallchild;

                }

            }
        }
    }

    return head->next;


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

    int numLists = rand() % 20 + 1;

    struct ListNode** myLists = generate( numLists );

    display(myLists,numLists);

    struct ListNode* mergedList = mergeKLists(myLists, numLists);

    printf("merged bitches:\n");

    while(mergedList){
        printf("%d->", mergedList->val);
        mergedList=mergedList->next;
    }
    putchar('\n');

}