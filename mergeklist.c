#include <stdio.h>
#include <stdlib.h>
#include <time.h>


struct ListNode {
    int val;
    struct ListNode *next;
};

void printheap(struct ListNode** lists, int listsSize){
    //printf("heaped (%d)\n", listsSize );
    putchar('\n');

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
}

void heapify(struct ListNode** lists, int listsSize){
    int leftchild, rightchild, smallchild;
    struct ListNode* temp;
    for(int i = (listsSize >> 1) - 1; i>=0; --i ){
        leftchild = (i<<1) +1;
        rightchild = (i<<1) +2;

        //need to send down all the way to bottom
        int v=i;
        while(v<listsSize/2){
            leftchild = (v<<1) +1;
            rightchild = (v<<1) +2;

            if(rightchild >= listsSize){
                //only left child
                if(lists[v]->val < lists[leftchild]->val) break;
                temp = lists[v];
                lists[v]=lists[leftchild];
                lists[leftchild]=temp;
                break;
            } else {
                if(lists[v]->val < lists[leftchild]->val && lists[v]->val < lists[rightchild]->val) break;

                if(lists[leftchild]->val < lists[rightchild]->val) smallchild = leftchild;
                else smallchild = rightchild;

                temp = lists[v];
                lists[v]=lists[smallchild];
                lists[smallchild]=temp;
                v=smallchild;
            }

        }


        //end of percolate down



    }

    printheap(lists,listsSize);

}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    if(listsSize<=1) return *lists;

    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* current = head;

    
    for(int i = listsSize -1; i>=0; --i){
        if(!lists[i]){
            for(int v=i; v<listsSize; ++v) lists[v] = lists[v+1];
            --listsSize;
        }
    }
    
    //printf("lists:%d\n",listsSize);
    
    if(!listsSize) return *lists;


    heapify(lists,listsSize);

    int i, rightchild, leftchild, smallchild;
    struct ListNode* temp;


    while(listsSize){
        
        //printheap(lists,listsSize);
        
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